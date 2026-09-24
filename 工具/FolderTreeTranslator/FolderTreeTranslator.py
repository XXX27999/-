# -*- coding: utf-8 -*-
r"""
绿洲起源 · 文件夹结构整理工具（FolderTreeTranslator）

功能：
    1. 扫描指定地图项目的四个目录：
         - 表格文件夹：<项目根>\Asset\Data
         - UI 文件夹  ：<项目根>\Asset\Blueprint\Prefabs\UI
         - 物品文件夹：<项目根>\Asset\Blueprint\Prefabs\Items
         - 脚本文件夹：<项目根>\Script\Function（功能 Lua 脚本）
    2. 递归列出其中的全部子文件夹与文件（全量，不截断）。
    3. 为每个文件夹 / 文件标注翻译后的中文名：
         - 内置词典 + 驼峰/下划线分词规则
         - 型号 / 专有代号（M416、M16A4、UMP45、AKM、UIBP…）保留原文不硬拆
         - 拼音识别（音节切分 + 词级拼音表 + 单字兜底），命中段标注 [拼音]；
           严格合规校验（≥2 音节、禁用单字母音节），避免 orange/purple/blue
           这类英文词被误判成拼音
         - 同目录外置词典 translation_dict.json 可扩展/覆盖（首次运行自动生成）
    4. 以树状形式展示（总览 / 表格 / UI / 物品 / 脚本 五个页签），支持关键字筛选、
       展开折叠、导出 TXT、导出 HTML、复制到剪贴板。
    5. 表格蓝图数据（DataTable）MCP 读写：按资产路径 / 磁盘路径 / 表名定位表格，
       经 UGCAskQ MCP 读取行结构与行数据，编辑后按
       Resolve → Plan → Execute 回写，并做本地校验、写前备份与写后回读校验。

运行：python FolderTreeTranslator.py
命令行扫描：python FolderTreeTranslator.py --scan <项目根目录> [--txt a.txt] [--html a.html]
命令行读表：python FolderTreeTranslator.py --project <项目根目录> --table UIConfigTable
            [--table-json out.json]
打包：pyinstaller --noconfirm --onefile --windowed --name FolderTreeTranslator FolderTreeTranslator.py
"""

import os
import re
import sys
import json
import argparse
import datetime

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

APP_TITLE = "绿洲起源 · 文件夹结构整理工具"
APP_VERSION = "1.5.2"

# 表格蓝图数据（MCP）模块：缺失时功能降级，不影响原有扫描与导出
try:
    from oasis_mcp_client import McpError, UgcMcpClient
    from oasis_datatable import DataTableService, normalize_asset_path
    import oasis_table_ui
    MCP_AVAILABLE = True
    MCP_IMPORT_ERROR = ""
except Exception as _mcp_exc:                       # 模块缺失或依赖异常时仅关闭表格功能
    MCP_AVAILABLE = False
    MCP_IMPORT_ERROR = str(_mcp_exc)

# 默认工程集合根目录（用于快速探测可用项目）
DEFAULT_PROJECTS_ROOT = r"D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects"

# 待扫描目标：显示名、相对项目根的路径、中文说明
# 物品编辑器（物编）的 4 类资产各自落在 Prefabs 下的独立目录：
#   Items（物品） / Weapons（枪械） / Throwables（投掷物） / MeleeWeapons（近战武器）
# 需要追加时，照下面元组格式往列表里加一行即可，页签会自动生成。
SCAN_TARGETS = [
    ("表格文件夹", os.path.join("Asset", "Data"), "配置表 / DataTable 目录"),
    ("UI 文件夹", os.path.join("Asset", "Blueprint", "Prefabs", "UI"), "界面蓝图预制体目录"),
    ("物品文件夹", os.path.join("Asset", "Blueprint", "Prefabs", "Items"), "物品编辑器（物编）物品资产目录"),
    ("脚本文件夹", os.path.join("Script", "Function"), "功能 Lua 脚本目录（Script/Function）"),
]

DICT_FILENAME = "translation_dict.json"


# --------------------------------------------------------------------------
# 一、翻译词典（内置，可被外置 translation_dict.json 覆盖/扩展）
# --------------------------------------------------------------------------

# 1) 驼峰词表：把拆出来的英文单词映射为中文
WORD_DICT = {
    # --- 资产与目录通用 ---
    "Asset": "资产", "Assets": "资产", "Data": "数据", "DataTable": "数据表",
    "Table": "配置表", "Tables": "配置表", "Row": "行", "RowStruct": "行结构",
    "Struct": "结构", "Template": "模板", "Templates": "模板", "Customized": "自定义",
    "Custom": "自定义", "Blueprint": "蓝图", "Blueprints": "蓝图", "Prefab": "预制体",
    "Prefabs": "预制体", "UI": "界面", "UMG": "UMG", "Widget": "控件", "Widgets": "控件",
    "Particles": "粒子", "Particle": "粒子", "Effect": "特效", "Effects": "特效", "FX": "特效",
    "VFX": "视觉特效", "Audio": "音频", "Sound": "音效", "Sounds": "音效", "Music": "音乐",
    "Voice": "配音", "Wwise": "Wwise", "Texture": "贴图", "Textures": "贴图",
    "Image": "图片", "Images": "图片", "Icon": "图标", "Icons": "图标", "Pic": "图片",
    "Material": "材质", "Materials": "材质", "Mesh": "模型", "Model": "模型",
    "Mode": "模式", "GameMode": "游戏模式", "Control": "控制",
    "CodexItem": "图鉴条目", "GlobalConfig": "全局配置",
    "Anim": "动画", "Animation": "动画", "Animations": "动画", "Sequence": "序列", "Seq": "序列",
    "Font": "字体", "Style": "样式", "Theme": "主题", "Layout": "布局", "Panel": "面板",
    "Panels": "面板", "Frame": "框体", "Box": "框", "Border": "边框", "Canvas": "画布",
    "Overlay": "叠加层", "SizeBox": "尺寸框", "Spacer": "间隔", "Switcher": "切换器",
    "Grid": "网格", "ScrollBox": "滚动框", "ListView": "列表视图", "TileView": "平铺视图",
    "Button": "按钮", "Btn": "按钮", "Text": "文本", "Label": "标签", "Title": "标题",
    "Bar": "条", "Progress": "进度", "Slider": "滑块", "ComboBox": "下拉框",
    "CheckBox": "勾选框", "EditableText": "输入框", "RichText": "富文本",
    "Background": "背景", "Bg": "背景", "Popup": "弹窗", "Dialog": "对话框",
    "Page": "页面", "Screen": "屏幕", "View": "视图", "Window": "窗口",
    # --- 玩法与机制 ---
    "Game": "游戏", "GameMode": "游戏模式", "Gameplay": "玩法", "Play": "玩法",
    "Level": "关卡", "Map": "地图", "Scene": "场景", "World": "世界", "Match": "对局",
    "Lobby": "大厅", "Hall": "大厅", "Room": "房间",
    "Character": "角色", "Characters": "角色", "Char": "角色", "Player": "玩家",
    "Pawn": "角色载体", "Actor": "对象", "Component": "组件",
    "Skill": "技能", "Skills": "技能", "Buff": "增益", "Talent": "天赋",
    "Item": "物品", "Items": "物品", "Prop": "道具", "Props": "道具",
    "Weapon": "武器", "Weapons": "武器", "Attachment": "配件", "Attachments": "配件",
    "Battle": "战斗", "Combat": "战斗", "Damage": "伤害", "Health": "生命", "Hp": "生命",
    "Coin": "金币", "Gold": "金币", "Money": "货币", "Currency": "货币",
    "Price": "价格", "Cost": "成本", "Value": "数值", "Values": "数值",
    "Score": "分数", "Rank": "排名", "Round": "回合", "Rounds": "回合", "Turn": "轮次",
    "Phase": "阶段", "Stage": "阶段", "State": "状态", "Status": "状态",
    "Timer": "计时器", "Duration": "时长", "Time": "时间", "Count": "数量",
    "Num": "数量", "Number": "数量", "Amount": "数额", "Max": "最大", "Min": "最小",
    "Limit": "上限", "Capacity": "容量", "Size": "尺寸", "Width": "宽度",
    "Height": "高度", "Pos": "位置", "Position": "位置", "Offset": "偏移",
    "Rate": "比例", "Ratio": "比例", "Percent": "百分比", "Probability": "概率",
    "Weight": "权重", "Speed": "速度", "Delay": "延迟", "Interval": "间隔",
    "CoolDown": "冷却", "Quality": "品质", "Grade": "品质", "Rarity": "稀有度",
    "Star": "星级", "Level2": "等级", "Trigger": "触发", "Condition": "条件",
    "Conditions": "条件", "Require": "需求", "Requirement": "需求",
    # --- 竞拍玩法业务 ---
    "Auction": "竞拍", "Bid": "出价", "Bidding": "竞拍", "Bidder": "竞买者",
    "Lot": "拍品", "House": "场次", "Auctioneer": "拍卖师", "Settlement": "结算",
    "Settle": "结算", "Profit": "收益", "Loss": "亏损", "Compensation": "补偿",
    "Guarantee": "保底", "Collectible": "藏品", "Codex": "图鉴", "Catalog": "图鉴",
    "Warehouse": "仓库", "Storage": "仓库", "Inventory": "背包", "Bag": "背包",
    "Intel": "情报", "Intelligence": "情报", "Public": "公共", "Private": "私有",
    "Secret": "秘密", "Clue": "线索", "Hint": "提示",
    "Select": "选择", "Selection": "选择", "Choose": "选择", "Confirm": "确认",
    "Cancel": "取消", "Submit": "提交", "Dress": "装扮", "Skin": "皮肤",
    "Suit": "套装", "Cloth": "服装", "Hair": "发型", "Face": "面部",
    # --- 物品编辑器（物编）物品资产 ---
    "Items": "物品", "Consumable": "消耗品", "Medicine": "药品", "Potion": "药水",
    "Drug": "药品", "Bandage": "绷带", "FirstAid": "急救", "Painkiller": "止痛药",
    "Adrenaline": "肾上腺素", "EnergyDrink": "能量饮料", "MedKit": "医疗箱",
    "Armor": "护甲", "Vest": "防弹衣", "Helmet": "头盔", "Backpack": "背包",
    "Ring": "戒指", "KneePad": "护膝", "Grenade": "手雷", "Smoke": "烟雾",
    "Molotov": "燃烧瓶", "Flare": "信号弹", "Throwable": "投掷物", "Melee": "近战",
    "Gun": "枪械", "Pistol": "手枪", "Rifle": "步枪", "Sniper": "狙击枪",
    "Shotgun": "霰弹枪", "Smg": "冲锋枪", "Ammo": "弹药", "Bullet": "子弹",
    "Arrow": "箭矢", "Magazine": "弹匣", "Clip": "弹夹", "Grip": "握把",
    "Muzzle": "枪口", "Stock": "枪托", "Scope": "瞄准镜", "Suppressor": "消音器",
    "Compensator": "补偿器", "FlashHider": "消焰器", "Laser": "激光",
    "Key": "钥匙", "Token": "令牌", "Letter": "信件", "Chest": "箱子",
    "Gem": "宝石", "Jade": "玉石", "Painting": "画作", "Vase": "花瓶",
    "Antique": "古董", "Relic": "遗物", "Artifact": "器物", "Statue": "雕像",
    # --- 程序与工程 ---
    "Config": "配置", "Configs": "配置", "Setting": "设置", "Settings": "设置",
    "Option": "选项", "Options": "选项", "Local": "本地", "Server": "服务端",
    "Client": "客户端", "Sync": "同步", "Global": "全局", "General": "通用",
    "Common": "通用", "Main": "主", "Sub": "子", "Base": "基础", "Default": "默认",
    "New": "新建", "Create": "创建", "Init": "初始化", "Load": "加载", "Save": "保存",
    "Reset": "重置", "Refresh": "刷新", "Update": "更新", "Delete": "删除",
    "Add": "添加", "Remove": "移除", "Open": "打开", "Close": "关闭",
    "Show": "显示", "Hide": "隐藏", "Get": "获取", "Set": "设置",
    "Path": "路径", "PathSet": "路径集合", "Group": "分组", "Groups": "分组",
    "Category": "分类", "Type": "类型", "Kind": "种类", "List": "列表",
    "Entry": "条目", "Entries": "条目", "Card": "卡片", "Cards": "卡片",
    "Info": "信息", "Detail": "详情", "Details": "详情", "History": "历史",
    "Record": "记录", "Records": "记录", "Log": "日志", "Logs": "日志",
    "Manager": "管理器", "Service": "服务", "System": "系统", "Controller": "控制器",
    "Handler": "处理器", "Helper": "辅助", "Utils": "工具", "Util": "工具",
    "Tool": "工具", "Tools": "工具", "Module": "模块", "Function": "功能",
    "Test": "测试", "Debug": "调试", "Demo": "示例", "Sample": "示例", "Preview": "预览",
    "Temp": "临时", "Backup": "备份", "Old": "旧版", "Ex": "扩展",
    "Name": "名称", "Desc": "描述", "Description": "描述", "Note": "备注",
    "Notes": "备注", "Comment": "注释", "Tip": "提示", "Tips": "提示",
    "Enabled": "启用", "Disabled": "禁用", "Switch": "开关", "Toggle": "开关",
    "Loading": "加载", "Wait": "等待", "Waiting": "等待", "Ready": "准备",
    "Start": "开始", "End": "结束", "Finish": "完成", "Total": "总",
    # --- Lua 功能脚本高频词（Script/Function 目录）---
    "Feedback": "反馈", "Presentation": "展示", "Cell": "格子",
    "Continuous": "连续", "Loop": "循环", "Drag": "拖拽",
    "Estimated": "预估", "Filter": "筛选", "Grant": "发放",
    "Hub": "大厅", "Information": "信息", "Motion": "动效",
    "Navigation": "导航", "Pre": "赛前", "Rematch": "再战",
    "Replacement": "替换", "Usage": "使用",
    "Standard": "规范", "Standards": "规范", "Patch": "补丁", "Readme": "说明",
    # --- 通用业务扩展（覆盖宠物/沙盒/休闲等游戏项目高频词）---
    "Shop": "商店", "Pet": "宠物", "Pets": "宠物",
    "Drop": "掉落", "Gift": "礼包", "Pack": "包",
    "Object": "对象", "Mapping": "映射",
    "Ranking": "排行", "List": "列表",
    "Weapon": "武器", "Attachment": "配件",
    "Work": "工作", "Clean": "清洁", "Combat": "战斗",
    "Box": "框", "Entertainment": "娱乐", "Feed": "喂食",
    "Monthly": "月度", "Award": "奖励",
    "Task": "任务", "Line": "线", "Quality": "品质",
    "UAE": "UAE", "V2": "V2",
    "Exclusive": "专属", "Title": "称号",
    "Buy": "购买", "Month": "月", "Season": "赛季",
    "Card": "卡", "Adopt": "领养",
    "Tutorial": "教程", "Panel": "面板",
    "Percent": "百分比", "Power": "能量",
    "Tip": "提示", "Tips": "提示",
    "Choice": "选择", "Dining": "用餐",
    "Area": "区域", "Name": "名称",
    "Attribute": "属性", "Detail": "详情",
    "Player": "玩家", "Currency": "货币",
    "Advanced": "高级", "Body": "身体",
    "Upgrade": "升级", "Accelerator": "加速器",
    "Common": "通用", "Decoration": "装饰",
    "Food": "食物", "Growth": "成长",
    "Protection": "保护", "Snack": "零食",
    "Hosting": "托管", "Limited": "限定",
    "Edition": "版", "Rare": "稀有",
    "Double": "双", "Custody": "托管",
    "Normal": "普通", "Nomal": "普通",
    "Experience": "经验", "Exper": "经验", "Experince": "经验",
    "Level": "等级", "Forever": "永久",
    "Reward": "奖励", "Line": "线", "Clothes": "服饰",
    "Pad": "面板", "Base": "基础",
    "Use": "使用", "For": "为", "From": "从",
    "Coin": "金币", "Classic": "经典",
    "ID": "编号", "With": "含", "Pool": "池",
    "CardFragment": "卡片碎片", "DecorationFragment": "装饰碎片",
    "GM": "GM", "First": "首次",
    "Perfect": "完美", "Mult": "倍数",
    "LienCard": "链卡", "Health": "健康",
    "Aid": "急救", "Kit": "工具包",
    "BackPack": "背包", "Item": "物品",
    "Defence": "防御", "Defense": "防御",
    "Attack": "攻击", "Defense": "防御",
    "Honor": "荣誉", "Rank": "排名",
    "Equip": "装备", "EquipItem": "装备项",
    "GiftPack": "礼包", "DropItem": "掉落物品",
    "Battle": "战斗", "Combat": "战斗",
    "Stage": "关卡", "Node": "节点",
    "Always": "永久", "Adv": "高级",
    "Current": "当前", "Fragment": "碎片",
    "WorkPack": "工作包", "WorkItem": "工作物品",
    "Items": "物品集", "Item": "物品",
    "Exp": "经验", "GMPack": "GM 礼包",
    "Tag": "标签", "CardKit": "卡工具包",
    "PerfectCard": "完美卡", "MultCard": "倍数卡",
    "RewardCard": "奖励卡", "Lien": "链",
    "CustodyCard": "托管卡", "FirstAid": "急救",
    "FirstAidKit": "急救工具包", "AidKit": "急救工具包",
    "HealthCard": "健康卡", "AllHealth": "全健康",
    "GM": "GM", "GMPack": "GM 礼包",
    "Flower": "花",
    "Large": "大", "Mid": "中", "Small": "小",
    "ProMax": "顶级",
    # --- 颜色（关键：必须进英文词表，否则会被拼音引擎误判）---
    "Orange": "橙色", "Purple": "紫色", "Blue": "蓝色", "Green": "绿色",
    "Red": "红色", "Yellow": "黄色", "Black": "黑色", "White": "白色",
    "Gray": "灰色", "Grey": "灰色", "Pink": "粉色", "Brown": "棕色",
    "Cyan": "青色", "Gold": "金色", "Silver": "银色", "Color": "颜色",
    "Colour": "颜色", "Dark": "深色", "Light": "浅色", "Bright": "亮色",
    "Transparent": "透明", "Normal": "普通色",
    # --- 武器分类与装备（射击/生存类玩法高频）---
    "AssaultRifles": "突击步枪", "AssaultRifle": "突击步枪",
    "MachineGuns": "机枪", "MachineGun": "机枪",
    "MarksmanRifles": "精确射手步枪", "MarksmanRifle": "精确射手步枪",
    "SniperRifles": "狙击步枪", "SniperRifle": "狙击步枪",
    "SubmachineGuns": "冲锋枪", "SubmachineGun": "冲锋枪",
    "Shotguns": "霰弹枪", "Pistols": "手枪", "Rifles": "步枪",
    "TommyGun": "汤姆逊冲锋枪", "AidBag": "急救包",
    "Chest": "箱子", "ChestLoot": "箱子掉落", "Loot": "战利品",
    "DropGroup": "掉落组", "Collectible": "收藏品",
    "Collection": "收藏", "CollectionItem": "收藏品",
    "CustomBackpack": "自定义背包", "Custom": "自定义",
    "Avatar": "头像", "AvatarFrame": "头像框", "Frame": "边框",
    # --- 大厅 / 仓库 / 背包等界面面 ---
    "Lobby": "大厅", "LobbyMain": "大厅主界面",
    "BackpackMain": "背包主界面", "WarehouseMain": "仓库主界面",
    "Home": "主页", "MainMenu": "主菜单", "Menu": "菜单",
    "Sign": "签到", "SignIn": "签到", "Login": "登录",
}

# 2) 整段精确表：用于驼峰切分无法正确还原的拼音名、缩写、复合词
SEG_DICT = {
    "UGCTemplateRowStruct": "表格行结构模板",
    "ZhuJieMian": "主界面",
    "UGC": "UGC",
    "DA": "数据资产",
    "UI": "界面",
    "UMG": "UMG",
    "WwiseAudio": "Wwise 音频",
    "ExUIList": "扩展界面列表",
    # --- 业务整段（拼音+缩写混合）---
    "PetData": "宠物数据",
    "PetShop": "宠物商店",
    "PetTable": "宠物配置表",
    "PetPool": "宠物池",
    "CoinShop": "金币商店",
    "Help": "帮助",
    "TianFu": "天赋",
    "Shop": "商店",
    "Work": "工作",
    "Clean": "清洁",
    "Feed": "喂食",
    "CombatBox": "战斗框",
    "Entertainment": "娱乐",
    "MonthlyAward": "月度奖励",
    "NewUAEDataTable": "新版 UAE 数据表",
    "TaskLineConfigList": "任务线配置列表",
    "UGCBattleItem": "战斗物品",
    "UGCDrop": "掉落",
    "UGCGiftPack": "礼包",
    "UGCObject": "对象",
    "UGCObjectMapping": "对象映射",
    "UGCRankingList": "排行榜列表",
    "UGCShop": "商店",
    "UGCShopV2ItemQualty": "商店 V2 物品品质",
    "UGCWeaponAttachment": "武器配件",
    "ChenHaoLuJin": "称号录金",
    "ClassicIDWithPack": "经典编号配包",
    "MonthlyAward": "月度奖励",
    "BuyMonthCard": "购买月卡",
    "BuySeasonCard": "购买赛季卡",
    "ExclusiveTitle": "专属称号",
    "FirstAdoptPet": "首次领养宠物",
    "NewPlayerTutorialPanelMCP": "新玩家教程面板 MCP",
    "OpenShop": "打开商店",
    "PercentTestUI": "百分比测试界面",
    "PetPowerUI": "宠物能量界面",
    "StopWorkUI": "停止工作界面",
    "TimeItem": "时限物品",
    "UseItemForPet": "对宠物使用物品",
    "WorkPercent": "工作百分比",
    "WorkPercentUI": "工作百分比界面",
    "BackPackUI": "背包界面",
    "ItemPadUI": "物品面板界面",
    "UI3D": "三维界面",
    "DiningAreaUI": "用餐区域界面",
    "PetChoiceDining": "用餐选择宠物",
    "districtDisplay": "区域展示",
    "Clean": "清洁",
    "HelpDetailUI": "帮助详情界面",
    "MainHelpUI": "主帮助界面",
    "NamePet": "命名宠物",
    "NamePlayer": "命名玩家",
    "PlayerAttributeDetailUI": "玩家属性详情界面",
    "RenWuLan": "任务栏",
    "RenWuBuJian": "任务部件",
    "QueRen": "确认",
    "QueRenCWJB": "确认-宠物金币部",
    "QueRenCWLZB": "确认-宠物绿洲币部",
    "QueRenDJJB": "确认-道具金币部",
    "ChongWuChouQu": "宠物抽取",
    "ShanDian": "闪电",
    "ShanDianZhuUI": "闪电主界面",
    "ShanDianCWJB": "闪电-宠物金币部",
    "ShanDianCWLZB": "闪电-宠物绿洲币部",
    "ShanDianDJJB": "闪电-道具金币部",
    "ShanDianDJLZB": "闪电-道具绿洲币部",
    "ShanDianDJLZB2": "闪电-道具绿洲币部 2",
    "ShanDianFL": "闪电-分类",
    "YueKa": "月卡",
    "JiKaLQ": "季卡领取",
    "YueKaLQ": "月卡领取",
    "YueJiKaLQ": "月季卡领取",
    "LinQu": "领取",
    "GeRenXingXi": "个人信息",
    "GeRenXinXi": "个人信息",
    "ChenHao": "称号",
    "PaiHangBan": "排行榜",
    "BackPackV2Currency": "背包 V2 货币",
    "PetsCurrency": "宠物货币",
    "LevelGiftPack": "等级礼包",
    "ProMaxWorkPack": "顶级工作礼包",
    "ProMaxGMPack": "顶级 GM 礼包",
    "ForeverWorkRewardCard3": "永久工作奖励卡 3",
    "ForeverWorkRewardCard_3": "永久工作奖励卡 3",
    "LineClothes_2": "线条服饰 2",
    "LineClothes2": "线条服饰 2",
    "AdvancedDecorationFragment": "高级装饰碎片",
    "BodyUpgradeAcceleratorFragment": "身体升级加速碎片",
    "CommonCleaningItemFragment": "通用清洁物碎片",
    "CommonCleaningltemFragment": "通用清洁物碎片",
    "CommonDecorationFragment": "通用装饰碎片",
    "CommonFoodFragment": "通用食物碎片",
    "GrowthAcceleratorFragment": "成长加速碎片",
    "GrowthProtectionFragment": "成长保护碎片",
    "HappySnackFragment": "快乐零食碎片",
    "HostingCardFragment": "托管卡碎片",
    "LimitedEditionDecorationFragment": "限定装饰碎片",
    "RareDecorationFragment": "稀有装饰碎片",
    "WorkDoubleCardFragment": "工作双倍卡碎片",
    "SkillBase": "技能基础",
    "SkillItem": "技能物品",
    "AdvCustodyCard": "高级托管卡",
    "AdvCustodyCard": "高级托管卡",
    "AlwaysCustodyCard3": "永久托管卡 3",
    "AlwaysCustodyCard_3": "永久托管卡 3",
    "NomalCustodyCard": "普通托管卡",
    "LevelExperinceCardLarge": "等级经验卡 大",
    "LevelExperinceCardMid": "等级经验卡 中",
    "LevelExperinceCardSmall": "等级经验卡 小",
    "LevelExperinceCard_Large": "等级经验卡 大",
    "LevelExperinceCard_Mid": "等级经验卡 中",
    "LevelExperinceCard_Small": "等级经验卡 小",
    "AllHealthCard": "全健康卡",
    "PetFirstAidKit": "宠物急救包",
    "Pet_First_Aid_Kit": "宠物急救包",
    "NameCard": "名片",
    "WorkMult": "工作倍数",
    "WorkPerfectCard": "工作完美卡",
    "WorkRewardCard": "工作奖励卡",
    "HelpLienCard": "帮助链卡",
    "LevelOneHundredPack": "一百级礼包",
    "WorkRewardItem": "工作奖励物品",
    "WorkItem": "工作物品",
    "WorkItems": "工作物品集",
    "CustodyItems": "托管物品",
    "ExpCard": "经验卡",
    "TagItems": "标签物品",
    "TiShi": "提示",
    "HelpUI": "帮助界面",
    "ChonWuFuHua": "宠物孵化",
    "LineClothes": "线条服饰",
    "LineClothes2": "线条服饰 2",
    "LineClothes_2": "线条服饰 2",
    "ProMaxWorkPackItem": "顶级工作包物品",
    "AdvCustodyCard": "高级托管卡",
    "Adv_Custody_Card": "高级托管卡",
    "AlwaysCustodyCard3": "永久托管卡 3",
    "AlwaysCustodyCard_3": "永久托管卡 3",
    "NomalCustodyCard": "普通托管卡",
    "Nomal_Custody_Card": "普通托管卡",
    "PetFirstAidKit": "宠物急救包",
    "Pet_First_Aid_Kit": "宠物急救包",
    # --- 射击/生存类玩法整段（SearchInfectionZone 等）---
    "SouSUo": "搜索", "SouSuo": "搜索", "Sousuo": "搜索",
    "SearchInfectionZone": "搜索感染区",
    "CollectibleDataTable": "收藏品数据表",
    "CollectibleTable": "收藏品表",
    "UGCDropGroup": "掉落组",
    "CustomBackpck": "自定义背包",
    "LobbyMain": "大厅主界面",
    "BackpackMainUI": "背包主界面",
    "WarehouseMainUI": "仓库主界面",
    "PlayerAvatarFrameUI": "玩家头像框界面",
    "ChestLootUI": "箱子掉落界面",
    "ItemUI": "物品界面",
    "TestUI": "测试界面",
    "UIBP": "",          # UE「UI Blueprint」类型后缀，直接剥离，不占用中文名
    "BP": "",            # Blueprint 后缀
}

# 3) 完整资产名精确表：仅收录通用规则无法准确翻译的少量条目
NAME_DICT = {
    "DressControlTable": "装扮方案表",
    "Pets_Currency": "宠物货币",
    "Pet_First_Aid_Kit": "宠物急救包",
    "LevelExperinceCard_Large": "等级经验卡 大",
    "LevelExperinceCard_Mid": "等级经验卡 中",
    "LevelExperinceCard_Small": "等级经验卡 小",
    "BackPackV2_Currency": "背包 V2 货币",
    "skill": "技能",
    "SkillBase": "技能基础",
    "Clean": "清洁",
    "Feed": "喂食",
    "Interact": "互动",
    "advanced": "进阶",
    "Work_2": "工作 2", "Work_3": "工作 3", "Work_4": "工作 4",
    "Work_5": "工作 5", "Work_6": "工作 6", "Work_7": "工作 7",
    "Work_8": "工作 8", "Work_9": "工作 9", "Work_10": "工作 10",
    "Work_11": "工作 11", "Work_12": "工作 12",
    "RenWu_1": "任务 1", "RenWu_2": "任务 2",
    "ChongWuChouQu": "宠物抽取",
    "TiShi": "提示",
    "mod": "模块",
    "shit": "测试",
    "sdf": "测试",
    "test1": "测试 1",
    "testuzi": "测试用字",
    "clean": "清洁",
    "clean2": "清洁 2",
    "feed": "喂食",
    "feed1": "喂食 1", "feed2": "喂食 2",
    "interact": "互动",
    "flower": "花",
    "A1": "工作 A1", "A2": "工作 A2", "A3": "工作 A3",
    "A4": "工作 A4", "A6": "工作 A6", "A7": "工作 A7",
    "A8": "工作 A8", "A9": "工作 A9", "A10": "工作 A10",
    "BHCWD": "宠物池-白虎宠蛋", "CSCWD": "宠物池-仓鼠宠蛋",
    "DJCWD": "宠物池-道具宠蛋", "GJCWD": "宠物池-高级宠蛋",
    "HLCWD": "宠物池-葫芦宠蛋", "NLCWD": "宠物池-NL 宠蛋",
    "QLCWD": "宠物池-青龙宠蛋", "ZJCWD": "宠物池-紫金宠蛋",
    "Works": "工作区",
    # IslandAuctionKing 功能脚本专名：Gold 在颜色表里是「金色」，这里按项目术语固定为「保底金」
    "AuctionGuaranteeGoldService": "竞拍保底金服务",
    "AuctionGuaranteeGoldUIService": "竞拍保底金界面服务",
}

# 4) 前缀表：命中后剥离前缀，产出「前缀中文：正文」
PREFIX_DICT = {
    "UGCTemplateRowStruct_": "表格行结构模板",
    "DA_": "数据资产",
    "AN_": "活动",
}

# 5) 扩展名中文说明
EXT_DICT = {
    ".uasset": "资产文件", ".umap": "地图资产", ".lua": "Lua 脚本",
    ".json": "JSON 数据", ".ini": "配置文件", ".txt": "文本文件",
    ".py": "Python 脚本", ".md": "Markdown 文档", ".png": "PNG 图片",
    ".jpg": "JPG 图片", ".tga": "TGA 图片", ".wav": "音频波形",
    ".csv": "CSV 表格", ".xlsx": "Excel 表格",
}


def load_dicts():
    """加载内置词典，并在存在外置词典时用其覆盖/扩展。"""
    dicts = {
        "words": dict(WORD_DICT),
        "segs": dict(SEG_DICT),
        "names": dict(NAME_DICT),
        "prefixes": dict(PREFIX_DICT),
        "exts": dict(EXT_DICT),
    }
    path = os.path.join(app_dir(), DICT_FILENAME)
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8") as fp:
                user = json.load(fp)
            for key in ("words", "segs", "names", "prefixes", "exts"):
                if isinstance(user.get(key), dict):
                    dicts[key].update({str(k): str(v) for k, v in user[key].items()})
        except Exception as exc:  # 外置词典损坏时退回内置词典，不中断工具
            print("[词典] 读取外置词典失败，已回退内置词典:", exc)
    return dicts


def app_dir():
    """返回程序所在目录（兼容 PyInstaller 单文件打包）。"""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------------------------------------
# 二、翻译引擎
# --------------------------------------------------------------------------

_CAMEL_RE = re.compile(r"[A-Z]+(?![a-z])|[A-Z][a-z0-9]*|[a-z0-9]+")
_SPLIT_RE = re.compile(r"[_\-\s]+")
_DUP_RE = re.compile(r"([\u4e00-\u9fa5]{2,4})\1")
_MAX_WINDOW = 4  # 词组窗口最大长度：命中「GameMode」这类连写词

# --------------------------------------------------------------------------
# 拼音识别：词级表 + 完整音节库 + 单字兜底
# --------------------------------------------------------------------------

# 1) 拼音词级表（驼峰切分后整段命中优先于英文词典）
PY_WORDS = {
    # --- 业务核心词（覆盖宠物/沙盒/休闲项目高频拼音命名）---
    "JiaGe": "价格", "JingBi": "金币", "LvZhouBi": "绿洲币", "LvZhou": "绿洲",
    "RenWu": "任务", "RenWuLan": "任务栏", "BuJian": "部件",
    "ChongWu": "宠物", "ChouQu": "抽取", "FuHua": "孵化",
    "ShanDian": "闪电", "ZhuUI": "主界面",
    "TianFu": "天赋",
    "JieMian": "界面", "ZhuJieMian": "主界面",
    "TiShi": "提示",
    "GeRen": "个人", "XinXi": "信息", "XingXi": "信息",
    "ChenHao": "称号", "LuJin": "录金", "ChenHaoLuJin": "称号录金",
    "PaiHang": "排行", "PaiHangBan": "排行榜",
    "YueKa": "月卡", "JiKa": "季卡", "LinQu": "领取", "LQ": "领取",
    "YueJiKa": "月季卡",
    "BianYi": "便捷", "ChongWuChouQu": "宠物抽取",
    "QueRen": "确认", "ShanDianZhu": "闪电主",
    "CWJB": "宠物金币部", "CWLZB": "宠物绿洲币部",
    "DJJB": "道具金币部", "DJLZB": "道具绿洲币部",
    "FL": "分类", "CW": "宠物", "DJ": "道具",
    # --- 数字 + 量词 ---
    "Yi": "一", "Er": "二", "San": "三", "Si": "四", "Wu": "五",
    "Liu": "六", "Qi": "七", "Ba": "八", "Jiu": "九", "Shi": "十",
    # --- 方位与属性 ---
    "Da": "大", "Xiao": "小", "Zhong": "中",
    "Shang": "上", "Xia": "下", "Zuo": "左", "You": "右",
    "Qian": "前", "Hou": "后", "ZhongXin": "中心",
    "Xin": "新", "Jiu": "旧", "Lao": "老",
    "Gao": "高", "Di": "低", "Chang": "长", "Duan": "短",
    "Kuan": "宽", "Zhai": "窄", "Yuan": "远", "Jin": "近",
    "Duo": "多", "Shao": "少", "Man": "满", "Kong": "空",
    "Zui": "最", "Zong": "总", "PingJun": "平均",
    "ZuiGao": "最高", "ZuiDi": "最低", "ZuiDa": "最大", "ZuiXiao": "最小",
    "ZuiXin": "最新", "ZuiJin": "最近", "ZuiKuai": "最快", "ZuiMan": "最慢",
    # --- 时间 ---
    "Nian": "年", "Yue": "月", "Ri": "日", "Tian": "天",
    "XiaoShi": "小时", "FenZhong": "分钟", "Miao": "秒",
    "JinTian": "今天", "MingTian": "明天", "Zuotian": "昨天",
    "XianZai": "现在", "CongQian": "从前", "YiHou": "以后",
    # --- 状态/动作 ---
    "Kai": "开", "Guan": "关", "QieHuan": "切换",
    "XianShi": "显示", "YinCang": "隐藏",
    "KaiQi": "开启", "GuanBi": "关闭", "JinYong": "禁用", "QiYong": "启用",
    "ShuaXin": "刷新", "ZhongZhi": "重置",
    "KaiShi": "开始", "JieShu": "结束", "TuiChu": "退出",
    "XuanZe": "选择", "ShanChu": "删除", "TianJia": "添加",
    "XiuGai": "修改", "GengXin": "更新", "ChuangJian": "创建",
    "BaoCun": "保存", "QuXiao": "取消", "QueDing": "确定",
    "HuiFu": "恢复", "ZanTing": "暂停", "JiXu": "继续",
    "ShangChuan": "上传", "XiaZai": "下载",
    "FaSong": "发送", "JieShou": "接收",
    "ChuFa": "触发", "JieDian": "节点",
    "ShuJu": "数据", "ShuJuBiao": "数据表", "ShuJuKu": "数据库",
    "Biao": "表", "BiaoGe": "表格", "WenJian": "文件",
    "MuLu": "目录", "LuJing": "路径", "WenDang": "文档",
    "BianJi": "编辑", "BianJiQi": "编辑器",
    "MingCheng": "名称", "MiaoShu": "描述", "BeiZhu": "备注",
    "TuPian": "图片", "TuBiao": "图标", "BeiJing": "背景",
    "YinYue": "音乐", "ShengYin": "声音", "ShiPin": "视频",
    "WenZi": "文字", "ZiTi": "字体", "YanSe": "颜色",
    "DongHua": "动画", "TeXiao": "特效",
    "YongHu": "用户", "MiMa": "密码", "ZhangHao": "账号",
    "DengLu": "登录", "ZhuCe": "注册", "YanZheng": "验证",
    "SheZhi": "设置", "PeiZhi": "配置", "CanShu": "参数",
    "MoKuai": "模块", "GongNeng": "功能", "ZuJian": "组件",
    "CeShi": "测试", "TiaoShi": "调试", "YuLan": "预览",
    "BanBen": "版本", "FaBu": "发布", "ShengJi": "升级",
    "YouXi": "游戏", "WanJia": "玩家", "DuiYou": "队友",
    "ShengLi": "胜利", "ShiBai": "失败", "MVP": "MVP",
    "WuQi": "武器", "DaoJu": "道具", "WuPin": "物品",
    "ZhuangBei": "装备", "BeiBao": "背包", "KouDai": "口袋",
    "JinBi": "金币", "YuanBao": "元宝", "ZuanShi": "钻石",
    "YaoPin": "药品", "YaoShui": "药水", "DaoJu": "道具",
    "YuanJia": "原价", "XianJia": "现价", "ZheKou": "折扣",
    "DingDan": "订单", "GouWuChe": "购物车", "ShangPin": "商品",
    "CuoWu": "错误", "ChengGong": "成功", "JingGao": "警告",
    "TongZhi": "通知", "XiaoXi": "消息", "BangZhu": "帮助",
    "WenTi": "问题", "JieJue": "解决", "BanFa": "办法",
    "FangFa": "方法", "FangAn": "方案", "BuZhou": "步骤",
    "LiuCheng": "流程", "JieDuan": "阶段", "HuanJie": "环节",
    "MingLing": "命令", "CaoZuo": "操作", "BianHao": "编号",
    "XuHao": "序号", "BiaoJi": "标记", "BiaoQian": "标签",
    "FenLei": "分类", "LeiBie": "类别", "LeiXing": "类型",
    "LieBiao": "列表", "XiangMu": "项目", "ChanPin": "产品",
    "QuanXian": "权限", "JueSe": "角色", "JiaoSe": "角色",
    "ChengHao": "称号", "ChengJi": "成绩", "ChengJiu": "成就",
    "JiFen": "积分", "PaiMing": "排名", "BangDan": "榜单",
    "BaiMing": "百名", "QianMing": "前名", "HouMing": "后名",
    "YiDong": "移动", "DianNao": "电脑", "PingMu": "屏幕",
    "ShouJi": "手机", "YouXiang": "邮箱",
    "WangLuo": "网络", "LianJie": "连接", "DuanKai": "断开",
    "JiaZai": "加载", "XiaZai": "下载", "ShangChuan": "上传",
    "JieTu": "截图", "JianQie": "剪切", "FuZhi": "复制", "ZhanTie": "粘贴",
    "ShiBai": "失败", "ChengGong": "成功",
    "TiaoJian": "条件", "PanDuan": "判断", "XunHuan": "循环",
    "BianLiang": "变量", "ChangLiang": "常量", "HanShu": "函数",
    "ShuZu": "数组", "DuiXiang": "对象", "JieGou": "结构",
    "Lei": "类", "JieKou": "接口", "JiCheng": "继承",
    "ShiLi": "实例", "FangWen": "访问",
    "BaoLiu": "保留", "BaoCun": "保存",
    "ChongFu": "重复", "ShanChu": "删除",
    "MingDan": "名单", "MingXi": "明细",
    "YiXiang": "意象", "XiangXiang": "想象",
    "BianHao": "编号", "MingZi": "名字", "ChaoHao": "潮号",
    "NiCheng": "昵称", "HaoCheng": "号称",
    "ZongHe": "综合", "ZongLan": "总览",
    "GongGao": "公告", "XinWen": "新闻",
    "TongZhi": "通知", "CuoWu": "错误",
    "MingLing": "命令", "ShouCe": "手册",
    "FenXiang": "分享", "ShouCang": "收藏",
    "DianZan": "点赞", "PingLun": "评论",
    "HuiFu": "回复", "TiWen": "提问",
    "YiJian": "意见", "JianYi": "建议",
    "TuPian": "图片", "ZhaoPian": "照片",
    "YinPin": "音频", "ShiPin": "视频",
    "LuXiang": "录像", "BaoLiu": "保留",
    "RuJin": "如今", "CongLai": "从来",
    "WeiLai": "未来", "GuoQu": "过去",
    "YiBan": "一般", "TeBie": "特别",
    "FeiChang": "非常", "JiQi": "极其",
    "ChaoJi": "超级", "ZhiJi": "至极",
    "WuBi": "无比", "ChaoFan": "超凡",
    "MingYan": "名言", "YongHeng": "永恒",
    "FeiShi": "飞逝", "YiShun": "一瞬",
    "WanMei": "完美", "YouQue": "有缺",
    "HuLian": "互联", "HuLianWang": "互联网",
    "JiQi": "机器", "DianNao": "电脑",
    "ShouBiao": "鼠标", "JianPan": "键盘",
    "DaBao": "打包", "JieBao": "解包",
    "BianMa": "编码", "JieMa": "解码",
    "JiaMi": "加密", "JieMi": "解密",
    "KaiFa": "开发", "SheJi": "设计",
    "YunWei": "运维", "WeiHu": "维护",
    "ShangXian": "上线", "XiaXian": "下线",
    "ShengJi": "升级", "JiangJi": "降级",
    "BanBenHao": "版本号", "FaBanBen": "发版本",
    "ZhuanYe": "专业", "MenPai": "门派",
    "ShiMen": "师门", "ShiTu": "视图",
    "YaoQing": "邀请", "YaoQingMa": "邀请码",
    "TuTeng": "图腾", "XunZhang": "勋章",
    "JiNian": "纪念", "JiNianPin": "纪念品",
    "HuoDong": "活动", "HuoDongChang": "活动场",
    "MiaoSha": "秒杀", "TuanGou": "团购",
    "YouHui": "优惠", "YouHuiQuan": "优惠券",
    "DaiJin": "代金", "DaiJinQuan": "代金券",
    "HongBao": "红包", "LiJin": "礼金",
    "ZhiFu": "支付", "ZhiFuBao": "支付宝",
    "WeiXin": "微信", "WeiXinZhiFu": "微信支付",
    "BaiFen": "百分", "BaiFenBai": "百分百",
    "YiTao": "一套", "LiangTao": "两套",
    "YiZu": "一组", "YiPai": "一排",
    "YiGe": "一个", "YiShi": "一时",
    "YiHui": "一回", "YiFan": "一番",
    "YiDun": "一顿", "YiCan": "一餐",
    "YiPian": "一片", "YiKuai": "一块",
    "YiDai": "一代", "YiWang": "以往",
    "YiZhang": "一张", "YiBen": "一本",
    "YiJian": "一件", "YiTao": "一套",
    "YiJu": "一句", "YiHua": "一句",
    "YiShu": "一束", "YiDuo": "一朵",
    "YiKe": "一颗", "YiLi": "一粒",
    "YiWei": "一位", "YiMing": "一名",
    "YiYuan": "一元", "YiJiao": "一角",
    "YiFen": "一分", "YiLi": "一里",
    "YiMi": "一米", "YiChi": "一尺",
    "YiCun": "一寸", "YiDian": "一点",
    "YiXie": "一些", "YiDui": "一对",
    "YiShuang": "一双", "YiXie": "一些",
    "ErShi": "二十", "ErShiYi": "二十一",
    "SanShi": "三十", "SiShi": "四十",
    "WuShi": "五十", "LiuShi": "六十",
    "QiShi": "七十", "BaShi": "八十",
    "JiuShi": "九十", "YiBai": "一百",
    "YiQian": "一千", "YiWan": "一万",
    "ShiWan": "十万", "BaiWan": "百万",
    "QianWan": "千万", "YiYi": "一亿",
}

# 2) 完整拼音音节库（无声调，~400 段）
_PY_SYLLABLES = set([
    "a", "ai", "an", "ang", "ao",
    "ba", "bai", "ban", "bang", "bao", "bei", "ben", "beng", "bi", "bian", "biao", "bie", "bin", "bing", "bo", "bu",
    "ca", "cai", "can", "cang", "cao", "ce", "cen", "ceng", "cha", "chai", "chan", "chang", "chao", "che",
    "chen", "cheng", "chi", "chong", "chou", "chu", "chua", "chuai", "chuan", "chuang", "chui", "chun", "chuo",
    "ci", "cong", "cou", "cu", "cuan", "cui", "cun", "cuo",
    "da", "dai", "dan", "dang", "dao", "de", "dei", "den", "deng", "di", "dia", "dian", "diao", "die",
    "ding", "diu", "dong", "dou", "du", "duan", "dui", "dun", "duo",
    "e", "ei", "en", "eng", "er",
    "fa", "fan", "fang", "fei", "fen", "feng", "fo", "fou", "fu",
    "ga", "gai", "gan", "gang", "gao", "ge", "gei", "gen", "geng", "gong", "gou", "gu", "gua", "guai",
    "guan", "guang", "gui", "gun", "guo",
    "ha", "hai", "han", "hang", "hao", "he", "hei", "hen", "heng", "hong", "hou", "hu", "hua", "huai",
    "huan", "huang", "hui", "hun", "huo",
    "ji", "jia", "jian", "jiang", "jiao", "jie", "jin", "jing", "jiong", "jiu", "ju", "juan", "jue", "jun",
    "ka", "kai", "kan", "kao", "ke", "kei", "ken", "keng", "kong", "kou", "ku", "kua", "kuai", "kuan",
    "kuang", "kui", "kun", "kuo",
    "la", "lai", "lan", "lang", "lao", "le", "lei", "leng", "li", "lia", "lian", "liang", "liao", "lie",
    "lin", "ling", "liu", "lo", "long", "lou", "lu", "luan", "lue", "lun", "luo", "lv", "lve",
    "ma", "mai", "man", "mang", "mao", "me", "mei", "men", "meng", "mi", "mian", "miao", "mie", "min",
    "ming", "miu", "mo", "mou", "mu",
    "na", "nai", "nan", "nao", "ne", "nei", "nen", "neng", "ni", "nian", "niang", "niao", "nie", "nin",
    "ning", "niu", "nong", "nou", "nu", "nuan", "nue", "nun", "nuo", "nv", "nve",
    "o", "ou",
    "pa", "pai", "pan", "pang", "pao", "pei", "pen", "peng", "pi", "pian", "piao", "pie", "pin", "ping",
    "po", "pou", "pu",
    "qi", "qia", "qian", "qiang", "qiao", "qie", "qin", "qing", "qiong", "qiu", "qu", "quan", "que", "qun",
    "ran", "rang", "rao", "re", "ren", "reng", "ri", "rong", "rou", "ru", "ruan", "rui", "run", "ruo",
    "sa", "sai", "san", "sang", "sao", "se", "sen", "seng", "sha", "shai", "shan", "shang", "shao", "she",
    "shei", "shen", "sheng", "shi", "shou", "shu", "shua", "shuai", "shuan", "shuang", "shui", "shun", "shuo",
    "si", "song", "sou", "su", "suan", "sui", "sun", "suo",
    "ta", "tai", "tan", "tang", "tao", "te", "teng", "ti", "tian", "tiao", "tie", "ting", "tong", "tou",
    "tu", "tuan", "tui", "tun", "tuo",
    "wa", "wai", "wan", "wang", "wei", "wen", "weng", "wo", "wu",
    "xi", "xia", "xian", "xiang", "xiao", "xie", "xin", "xing", "xiong", "xiu", "xu", "xuan", "xue", "xun",
    "ya", "yan", "yang", "yao", "ye", "yi", "yin", "ying", "yo", "yong", "you", "yu", "yuan", "yue", "yun",
    "za", "zai", "zan", "zang", "zao", "ze", "zei", "zen", "zeng", "zha", "zhai", "zhan", "zhang", "zhao",
    "zhe", "zhei", "zhen", "zheng", "zhi", "zhong", "zhou", "zhu", "zhua", "zhuai", "zhuan", "zhuang",
    "zhui", "zhun", "zhuo", "zi", "zong", "zou", "zu", "zuan", "zui", "zun", "zuo",
])

# 3) 音节 → 单字兜底（每个拼音音节给最高频汉字）
_PY_SYLLABLE_CHAR = {
    "a": "啊", "ai": "爱", "an": "安", "ang": "昂", "ao": "奥",
    "ba": "把", "bai": "白", "ban": "半", "bang": "帮", "bao": "包",
    "bei": "被", "ben": "本", "beng": "蹦", "bi": "比", "bian": "边",
    "biao": "表", "bie": "别", "bin": "宾", "bing": "并", "bo": "不",
    "bu": "不",
    "ca": "擦", "cai": "才", "can": "参", "cang": "仓", "cao": "草",
    "ce": "侧", "cen": "岑", "ceng": "层", "cha": "查", "chai": "拆",
    "chan": "产", "chang": "长", "chao": "超", "che": "车", "chen": "陈",
    "cheng": "成", "chi": "吃", "chong": "冲", "chou": "抽", "chu": "出",
    "chua": "揣", "chuai": "揣", "chuan": "川", "chuang": "创", "chui": "吹",
    "chun": "春", "chuo": "戳", "ci": "次", "cong": "从", "cou": "凑",
    "cu": "粗", "cuan": "窜", "cui": "催", "cun": "村", "cuo": "错",
    "da": "打", "dai": "代", "dan": "但", "dang": "当", "dao": "到",
    "de": "的", "dei": "得", "den": "扽", "deng": "等", "di": "地",
    "dia": "嗲", "dian": "点", "diao": "掉", "die": "跌", "ding": "定",
    "diu": "丢", "dong": "东", "dou": "都", "du": "读", "duan": "段",
    "dui": "对", "dun": "顿", "duo": "多",
    "e": "鹅", "ei": "诶", "en": "恩", "eng": "鞥", "er": "儿",
    "fa": "发", "fan": "反", "fang": "方", "fei": "非", "fen": "分",
    "feng": "风", "fo": "佛", "fou": "否", "fu": "服",
    "ga": "嘎", "gai": "改", "gan": "干", "gang": "刚", "gao": "高",
    "ge": "个", "gei": "给", "gen": "根", "geng": "更", "gong": "工",
    "gou": "够", "gu": "古", "gua": "挂", "guai": "怪", "guan": "关",
    "guang": "光", "gui": "规", "gun": "滚", "guo": "国",
    "ha": "哈", "hai": "海", "han": "汉", "hang": "行", "hao": "好",
    "he": "和", "hei": "黑", "hen": "很", "heng": "横", "hong": "红",
    "hou": "后", "hu": "呼", "hua": "花", "huai": "坏", "huan": "换",
    "huang": "黄", "hui": "回", "hun": "混", "huo": "或",
    "ji": "及", "jia": "家", "jian": "见", "jiang": "将", "jiao": "叫",
    "jie": "接", "jin": "进", "jing": "经", "jiong": "窘", "jiu": "就",
    "ju": "局", "juan": "卷", "jue": "决", "jun": "军",
    "ka": "卡", "kai": "开", "kan": "看", "kao": "考", "ke": "可",
    "kei": "可", "ken": "肯", "keng": "坑", "kong": "空", "kou": "口",
    "ku": "苦", "kua": "夸", "kuai": "快", "kuan": "宽", "kuang": "狂",
    "kui": "亏", "kun": "困", "kuo": "阔",
    "la": "拉", "lai": "来", "lan": "蓝", "lang": "浪", "lao": "老",
    "le": "了", "lei": "类", "leng": "冷", "li": "里", "lia": "俩",
    "lian": "连", "liang": "量", "liao": "了", "lie": "列", "lin": "林",
    "ling": "令", "liu": "流", "lo": "咯", "long": "龙", "lou": "楼",
    "lu": "路", "luan": "乱", "lue": "掠", "lun": "论", "luo": "落",
    "lv": "绿", "lve": "掠",
    "ma": "妈", "mai": "买", "man": "满", "mang": "忙", "mao": "毛",
    "me": "么", "mei": "没", "men": "门", "meng": "梦", "mi": "米",
    "mian": "面", "miao": "秒", "mie": "灭", "min": "民", "ming": "名",
    "miu": "谬", "mo": "摸", "mou": "某", "mu": "木",
    "na": "那", "nai": "奶", "nan": "男", "nao": "脑", "ne": "呢",
    "nei": "内", "nen": "嫩", "neng": "能", "ni": "你", "nian": "年",
    "niang": "娘", "niao": "鸟", "nie": "捏", "nin": "您", "ning": "宁",
    "niu": "牛", "nong": "农", "nou": "耨", "nu": "努", "nuan": "暖",
    "nue": "虐", "nun": "嫩", "nuo": "诺", "nv": "女", "nve": "虐",
    "o": "哦", "ou": "偶",
    "pa": "怕", "pai": "排", "pan": "盘", "pang": "胖", "pao": "跑",
    "pei": "配", "pen": "盆", "peng": "朋", "pi": "皮", "pian": "片",
    "piao": "飘", "pie": "撇", "pin": "品", "ping": "平", "po": "破",
    "pou": "剖", "pu": "普",
    "qi": "起", "qia": "卡", "qian": "前", "qiang": "强", "qiao": "桥",
    "qie": "切", "qin": "亲", "qing": "请", "qiong": "穷", "qiu": "球",
    "qu": "去", "quan": "全", "que": "确", "qun": "群",
    "ran": "然", "rang": "让", "rao": "绕", "re": "热", "ren": "人",
    "reng": "仍", "ri": "日", "rong": "容", "rou": "肉", "ru": "如",
    "ruan": "软", "rui": "锐", "run": "润", "ruo": "若",
    "sa": "撒", "sai": "塞", "san": "三", "sang": "桑", "sao": "扫",
    "se": "色", "sen": "森", "seng": "僧", "sha": "沙", "shai": "晒",
    "shan": "山", "shang": "上", "shao": "少", "she": "设", "shei": "谁",
    "shen": "深", "sheng": "生", "shi": "是", "shou": "收", "shu": "书",
    "shua": "刷", "shuai": "帅", "shuan": "拴", "shuang": "双", "shui": "水",
    "shun": "顺", "shuo": "说", "si": "四", "song": "送", "sou": "搜",
    "su": "速", "suan": "算", "sui": "随", "sun": "孙", "suo": "所",
    "ta": "他", "tai": "太", "tan": "谈", "tang": "唐", "tao": "套",
    "te": "特", "teng": "疼", "ti": "提", "tian": "天", "tiao": "条",
    "tie": "铁", "ting": "听", "tong": "同", "tou": "头", "tu": "土",
    "tuan": "团", "tui": "推", "tun": "吞", "tuo": "托",
    "wa": "瓦", "wai": "外", "wan": "完", "wang": "王", "wei": "为",
    "wen": "问", "weng": "翁", "wo": "我", "wu": "无",
    "xi": "西", "xia": "下", "xian": "先", "xiang": "想", "xiao": "小",
    "xie": "写", "xin": "新", "xing": "行", "xiong": "兄", "xiu": "修",
    "xu": "许", "xuan": "选", "xue": "学", "xun": "寻",
    "ya": "压", "yan": "眼", "yang": "样", "yao": "要", "ye": "也",
    "yi": "一", "yin": "因", "ying": "应", "yo": "哟", "yong": "用",
    "you": "有", "yu": "与", "yuan": "元", "yue": "月", "yun": "云",
    "za": "杂", "zai": "在", "zan": "赞", "zang": "脏", "zao": "早",
    "ze": "则", "zei": "贼", "zen": "怎", "zeng": "增", "zha": "炸",
    "zhai": "宅", "zhan": "战", "zhang": "张", "zhao": "找", "zhe": "这",
    "zhei": "这", "zhen": "真", "zheng": "正", "zhi": "之", "zhong": "中",
    "zhou": "周", "zhu": "主", "zhua": "抓", "zhuai": "拽", "zhuan": "转",
    "zhuang": "装", "zhui": "追", "zhun": "准", "zhuo": "桌", "zi": "字",
    "zong": "总", "zou": "走", "zu": "组", "zuan": "钻", "zui": "最",
    "zun": "尊", "zuo": "做",
}

# 4) 拼音音节切分（贪婪最长匹配 + 严格合规校验）
def _split_pinyin(low):
    """对纯拼音小写串做音节切分，返回音节列表；切不出或不合规返回 None。

    合规要求（用于防止英文单词被误判为拼音，如 orange→o+ran+ge、
    purple→pu+rp+le、blue→bl+ue 这类"看起来能切"的英文词）：
        1. 原串长度 >= 4（排除过短串）
        2. 音节数 >= 2（单音节交给词级表处理）
        3. 每个音节长度 >= 2 —— 禁用单字母音节 a/o/e，它们在英文里极常见、
           但在拼音里只出现在极少数词（另见 PY_WORDS 词级表兜底）
    """
    if not low or len(low) < 4 or not all(c.isalpha() for c in low):
        return None
    parts = []
    i = 0
    while i < len(low):
        matched = None
        for j in range(min(6, len(low) - i), 1, -1):   # 下限 2：不接受单字母音节
            cand = low[i:i + j]
            if cand in _PY_SYLLABLES:
                matched = cand
                break
        if matched is None:
            return None
        parts.append(matched)
        i += len(matched)
    if len(parts) < 2:
        return None
    return parts


# 5) 型号 / 专有名词：形如「字母+数字」（M416 / M16A4 / UMP45 / QBZ95）或
#    短全大写代号（AKM / SKS）——这类是枪械、装备型号，翻译反而看不清，保留原文。
_MODEL_RE = re.compile(r"^(?:[A-Za-z]+[0-9]+[A-Za-z0-9]*|[0-9]+[A-Za-z]+[A-Za-z0-9]*)$")
_UPPER_TOKEN_RE = re.compile(r"^[A-Z]{3,6}$")


def is_model_name(key):
    """判断是否为型号 / 专有代号：含数字的字母数字混排，或 2~6 位全大写缩写。"""
    if _MODEL_RE.match(key):
        return True
    if _UPPER_TOKEN_RE.match(key):
        return True
    return False


def _dedupe(text):
    """合并因逐词翻译产生的叠词（如「配置配置表」→「配置表」）。"""
    prev = None
    while prev != text:
        prev = text
        text = _DUP_RE.sub(r"\1", text)
    return text


def _is_ascii(ch):
    """判断字符是否为 ASCII（含数字），用于决定拼接时是否补空格。"""
    return ord(ch) < 128


def _join_parts(parts):
    """拼接中文片段：中文与中文直连，出现英文/数字时补空格。"""
    out = ""
    for part in parts:
        if not part:
            continue
        if not out:
            out = part
            continue
        if _is_ascii(out[-1]) or _is_ascii(part[0]):
            out += " " + part
        else:
            out += part
    return out.strip()


def _translate_segment(seg, dicts, miss=None):
    """翻译单个英文段（下划线/连字符之间的一段）。

    采用「最长词组窗口优先」策略：先尝试 4~2 个连续驼峰词的整体译法，
    未命中再退化为单词翻译，未命中单词继续走拼音识别。
    拼音整段（PY_WORDS）也按最长窗口匹配；单词级查表；最后兜底
    按合法拼音音节切分，未识别保留英文原文。

    miss：可选 dict（形如 {"n": 0}），用于回填"未识别 token 数"，
    供调用方统计中文名完整率；型号/缩写等有意保留原文的段不计入。
    """
    if seg in dicts["segs"]:
        return dicts["segs"][seg]
    # 整段直接命中英文词表（含大小写变体）——必须排在型号判断之前，
    # 否则 FX / GM / ID 这类 2 字母缩写会被当成型号而丢掉中文译名。
    _w = dicts["words"]
    for _cand in (seg, seg.upper(), seg.capitalize(), seg.lower()):
        if _cand in _w:
            return _w[_cand]
    # 拼音词级表整段命中：CWJB（宠物金币部）这类业务缩写在类型号判断之前，
    # 否则 3~6 位全大写缩写会被当型号而丢掉中文译名。
    if seg in PY_WORDS:
        return PY_WORDS[seg]
    if seg.lower() in PY_WORDS:
        return PY_WORDS[seg.lower()]
    # 型号 / 专有代号（M416 / M16A4 / UMP45 / AKM / SKS / QBZ / UIBP …）保留原文：
    # 枪械与装备型号在中英文里写法一致，硬拆硬译只会更难看懂。
    if is_model_name(seg):
        return seg
    tokens = _CAMEL_RE.findall(seg)
    if not tokens:
        return seg

    words = dicts["words"]
    parts = []
    idx = 0
    total = len(tokens)
    while idx < total:
        hit_width = 0
        hit_cn = None

        # 1) 英文最长窗口优先
        for width in range(min(_MAX_WINDOW, total - idx), 1, -1):
            key = "".join(tokens[idx:idx + width])
            if key in words:
                hit_width, hit_cn = width, words[key]
                break
        if hit_cn is None:
            # 2) 拼音整段窗口（驼峰切分后仍可整段命中的业务词）
            for width in range(min(3, total - idx), 1, -1):
                key = "".join(tokens[idx:idx + width])
                if key in PY_WORDS:
                    hit_width, hit_cn = width, PY_WORDS[key]
                    break
        if hit_cn is not None:
            parts.append(hit_cn)
            idx += hit_width
            continue

        tok = tokens[idx]
        # 3) 英文单词命中（含大小写变体）
        cn = words.get(tok)
        if cn is None and tok.isalpha():
            for variant in (tok.upper(), tok.capitalize(), tok.lower()):
                if variant in words:
                    cn = words[variant]
                    break
        if cn is not None:
            parts.append(cn)
            idx += 1
            continue

        # 4) 拼音识别（仅对 >=2 字母的 token；单字母 A/M/O 一律不动，避免
        #    「M16A4」里的 A 被译成「啊」这类误判）
        if tok.isalpha() and len(tok) >= 2:
            # 先按原大小写查词级表（适配 CWJB 类全大写缩写）
            if tok in PY_WORDS:
                parts.append(PY_WORDS[tok])
                idx += 1
                continue
            low = tok.lower()
            if low in PY_WORDS:
                parts.append(PY_WORDS[low])
                idx += 1
                continue
            # 5) 音节切分兜底：整串是合法拼音音节才翻译（严格合规校验）
            syllables = _split_pinyin(low)
            if syllables is not None:
                cn_chars = "".join(_PY_SYLLABLE_CHAR[s] for s in syllables)
                parts.append(cn_chars + " [拼音]")
                idx += 1
                continue

        parts.append(tok)
        if miss is not None:
            miss["n"] += 1          # 未识别 token：保留原文，计入完整率缺口
        idx += 1
    return _join_parts(parts)


def translate_name(raw_name, dicts, miss=None):
    """把文件夹名 / 文件名翻译为中文名；未命中部分保留英文原文。

    miss：可选 dict（{"n": 0}），回填未识别 token 数，用于统计中文名完整率。
    """
    base, _ext = os.path.splitext(raw_name)
    key = base if base else raw_name

    if key in dicts["names"]:
        return dicts["names"][key]

    prefix_cn = None
    work = key
    for prefix, cn in dicts["prefixes"].items():
        if work.startswith(prefix) and len(work) > len(prefix):
            prefix_cn = cn
            work = work[len(prefix):]
            break

    if work in dicts["names"]:
        body = dicts["names"][work]
    else:
        segs = [s for s in _SPLIT_RE.split(work) if s]
        body = _dedupe(_join_parts([_translate_segment(seg, dicts, miss) for seg in segs]))

    if prefix_cn:
        return "%s：%s" % (prefix_cn, body) if body else prefix_cn
    return body if body else key


def has_untranslated(cn_text):
    """判断中文名里是否仍残留未翻译的拉丁字母（用于覆盖率统计）。"""
    return any("a" <= ch.lower() <= "z" for ch in cn_text)


def ext_desc(raw_name, dicts):
    """返回扩展名对应的中文类型说明，文件夹传空字符串。"""
    ext = os.path.splitext(raw_name)[1].lower()
    if not ext:
        return ""
    return dicts["exts"].get(ext, "%s 文件" % ext.lstrip(".").upper())


# --------------------------------------------------------------------------
# 三、目录扫描
# --------------------------------------------------------------------------

class FsNode(object):
    """文件系统树节点。"""

    __slots__ = ("name", "path", "is_dir", "size", "cn", "children")

    def __init__(self, name, path, is_dir, size=0, cn=""):
        self.name = name
        self.path = path
        self.is_dir = is_dir
        self.size = size
        self.cn = cn
        self.children = []


def scan_directory(path, dicts, counter):
    """递归扫描目录，返回 FsNode 树。"""
    name = os.path.basename(os.path.normpath(path)) or path
    node = FsNode(name, path, True, 0, translate_name(name, dicts))
    counter["dirs"] += 1
    try:
        entries = sorted(
            os.scandir(path),
            key=lambda e: (not e.is_dir(follow_symlinks=False), e.name.lower()),
        )
    except OSError as exc:
        print("[扫描] 无法读取目录 %s: %s" % (path, exc))
        return node

    for entry in entries:
        try:
            if entry.is_dir(follow_symlinks=False):
                node.children.append(scan_directory(entry.path, dicts, counter))
            else:
                size = entry.stat(follow_symlinks=False).st_size
                counter["files"] += 1
                counter["bytes"] += size
                miss = {"n": 0}
                cn = translate_name(entry.name, dicts, miss)
                if miss["n"] > 0:
                    # 有 token 未被任何规则识别（型号等有意保留的不计入）
                    counter["untranslated"] += 1
                node.children.append(
                    FsNode(entry.name, entry.path, False, size, cn)
                )
        except OSError as exc:
            print("[扫描] 跳过错项 %s: %s" % (entry.path, exc))
    return node


def count_nodes(node, acc=None):
    """统计子树内的文件夹数 / 文件数。"""
    if acc is None:
        acc = {"dirs": 0, "files": 0}
    for child in node.children:
        if child.is_dir:
            acc["dirs"] += 1
            count_nodes(child, acc)
        else:
            acc["files"] += 1
    return acc


def collect_trees(root_path, dicts):
    """扫描两个目标目录，返回 (trees, missing, total)。

    trees   : [(显示名, 说明, FsNode)]
    missing : 不存在的目标目录描述列表
    total   : {"dirs","files","bytes","untranslated"} 汇总
    """
    trees = []
    missing = []
    total = {"dirs": 0, "files": 0, "bytes": 0, "untranslated": 0}
    for title, rel, desc in SCAN_TARGETS:
        target = os.path.join(root_path, rel)
        if not os.path.isdir(target):
            missing.append("%s  →  %s" % (title, target))
            continue
        counter = {"dirs": 0, "files": 0, "bytes": 0, "untranslated": 0}
        node = scan_directory(target, dicts, counter)
        node.name = "%s  (%s)" % (title, rel.replace("\\", "/"))
        node.cn = desc
        trees.append((title, desc, node))
        for key in total:
            total[key] += counter[key]
    return trees, missing, total


def build_status(project_root, trees, missing, total):
    """拼装状态栏 / 统计说明文本。"""
    if not trees:
        return "未找到可扫描目录。缺失项：" + "；".join(missing)
    rate = 0.0
    if total["files"]:
        rate = (total["files"] - total["untranslated"]) * 100.0 / total["files"]
    status = ("扫描完成：%d 个文件夹 · %d 个文件 · 合计 %s · 中文名完整率 %.1f%%"
              % (total["dirs"], total["files"], human_size(total["bytes"]), rate))
    if missing:
        status += " · 缺失目录 %d 个" % len(missing)
    return status


def build_report_text(project_root, trees, status):
    """生成树状纯文本报告。"""
    if not trees:
        return ""
    lines = ["=" * 78,
             "地图项目：%s" % project_root,
             "生成时间：%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             "=" * 78, ""]
    for title, desc, node in trees:
        lines.append("【%s】%s" % (title, desc))
        lines.append("-" * 78)
        lines.extend(render_text(node))
        lines.append("")
    lines.append(status)
    return "\n".join(lines)


def human_size(size):
    """字节数格式化为可读文本。"""
    value = float(size)
    for unit in ("B", "KB", "MB", "GB"):
        if value < 1024.0 or unit == "GB":
            if unit == "B":
                return "%d B" % int(value)
            return "%.1f %s" % (value, unit)
        value /= 1024.0
    return "%.1f GB" % value


# --------------------------------------------------------------------------
# 四、文本 / HTML 导出
# --------------------------------------------------------------------------

def render_text(node, prefix="", is_last=True, is_root=True, lines=None):
    """把 FsNode 树渲染为树状文本行列表。"""
    if lines is None:
        lines = []
    if is_root:
        lines.append("%s  [%s]" % (node.name, node.cn))
    else:
        connector = "└── " if is_last else "├── "
        suffix = "/" if node.is_dir else ""
        lines.append("%s%s%s%s  ->  %s" % (prefix, connector, node.name, suffix, node.cn))
    if node.children:
        new_prefix = "" if is_root else prefix + ("    " if is_last else "│   ")
        for idx, child in enumerate(node.children):
            render_text(child, new_prefix, idx == len(node.children) - 1,
                        False, lines)
    return lines


def render_html(title, nodes, stats_text):
    """生成可直接在浏览器打开的可折叠 HTML 树。"""
    esc = lambda s: (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

    def build(node, is_root):
        if is_root:
            head = "<div class='root'>%s <span class='cn'>%s</span></div>" % (
                esc(node.name), esc(node.cn))
        elif node.is_dir:
            cnt = count_nodes(node)
            head = ("<summary><span class='dir'>%s/</span>"
                    "<span class='cn'>%s</span>"
                    "<span class='meta'>%d 文件夹 / %d 文件</span></summary>"
                    % (esc(node.name), esc(node.cn), cnt["dirs"], cnt["files"]))
        else:
            head = ("<div class='file'><span class='fname'>%s</span>"
                    "<span class='cn'>%s</span>"
                    "<span class='meta'>%s · %s</span></div>"
                    % (esc(node.name), esc(node.cn), esc(ext_desc(node.name, DICTS)),
                       human_size(node.size)))
        if node.is_dir and node.children:
            inner = "".join(build(c, False) for c in node.children)
            if is_root:
                return head + "<div class='children'>%s</div>" % inner
            return "<details open>%s<div class='children'>%s</div></details>" % (head, inner)
        if node.is_dir:
            if is_root:
                return head + "<div class='children'><span class='empty'>（空文件夹）</span></div>"
            return "<details>%s<div class='children'><span class='empty'>（空文件夹）</span></div></details>" % head
        return head

    body = "".join(build(n, True) for n in nodes)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>%s</title>
<style>
  body{margin:0;padding:24px;background:#f7f8fa;color:#1f2328;
       font:14px/1.7 "Microsoft YaHei UI","Microsoft YaHei",sans-serif;}
  h1{font-size:20px;margin:0 0 6px;}
  .stats{color:#656d76;font-size:13px;margin-bottom:18px;}
  .card{background:#fff;border:1px solid #e3e6ea;border-radius:10px;padding:16px 20px;
        margin-bottom:18px;box-shadow:0 1px 2px rgba(0,0,0,.04);}
  .root{font-weight:700;color:#1f6feb;font-size:15px;margin-bottom:8px;
        border-bottom:1px solid #e3e6ea;padding-bottom:6px;}
  details{margin-left:2px;}
  summary{cursor:pointer;padding:2px 4px;border-radius:4px;list-style:none;}
  summary::-webkit-details-marker{display:none;}
  summary:before{content:"▸ ";color:#8b949e;}
  details[open]>summary:before{content:"▾ ";}
  summary:hover{background:#eef2f7;}
  .dir{font-weight:600;color:#1f2328;}
  .cn{color:#0a7d55;margin-left:10px;}
  .file{padding:2px 4px;}
  .fname{color:#1f2328;}
  .meta{color:#8b949e;font-size:12px;margin-left:10px;}
  .children{margin-left:16px;border-left:1px dashed #dfe3e8;padding-left:10px;}
  .empty{color:#8b949e;font-style:italic;}
</style></head><body>
<h1>%s</h1>
<div class="stats">%s<br>生成时间：%s · 工具版本 %s</div>
%s
</body></html>""" % (esc(title), esc(title), esc(stats_text), stamp, APP_VERSION, body)


# --------------------------------------------------------------------------
# 五、图形界面
# --------------------------------------------------------------------------

DICTS = load_dicts()


class App(object):
    """主窗口。"""

    def __init__(self, root):
        self.root = root
        self.project_root = tk.StringVar()
        self.filter_text = tk.StringVar()
        self.status_text = tk.StringVar(value="就绪：请选择地图项目目录后点击「开始扫描」。")
        self.trees = []          # [(显示名, 说明, FsNode)]
        self.tab_trees = {}      # 页签名 -> ttk.Treeview
        self.node_seq = 0
        self.table_window = None # 表格蓝图数据窗口（单例）
        self.node_by_iid = {}    # 页签名 -> {Treeview iid: FsNode}

        self._build_ui()
        self._auto_detect_projects()

    # ---------------- 界面搭建 ----------------
    def _build_ui(self):
        self.root.title("%s  v%s" % (APP_TITLE, APP_VERSION))
        self.root.geometry("1200x780")
        self.root.minsize(940, 600)

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Treeview", rowheight=24, font=("Microsoft YaHei UI", 10))
        style.configure("Treeview.Heading", font=("Microsoft YaHei UI", 10, "bold"))
        style.configure("TLabel", font=("Microsoft YaHei UI", 10))
        style.configure("TButton", font=("Microsoft YaHei UI", 10), padding=(10, 4))
        style.configure("TCheckbutton", font=("Microsoft YaHei UI", 10))

        # —— 顶部：路径选择 ——
        top = ttk.Frame(self.root, padding=(14, 12, 14, 6))
        top.pack(fill="x")

        ttk.Label(top, text="地图项目根目录：").grid(row=0, column=0, sticky="w")
        entry = ttk.Entry(top, textvariable=self.project_root,
                          font=("Consolas", 10))
        entry.grid(row=0, column=1, sticky="ew", padx=(0, 8))
        ttk.Button(top, text="浏览…", command=self.on_browse).grid(row=0, column=2)
        ttk.Button(top, text="开始扫描", command=self.on_scan).grid(row=0, column=3, padx=(8, 0))

        ttk.Label(top, text="快速选择：").grid(row=1, column=0, sticky="w", pady=(8, 0))
        self.combo = ttk.Combobox(top, values=[], state="readonly",
                                  font=("Microsoft YaHei UI", 10))
        self.combo.grid(row=1, column=1, sticky="ew", padx=(0, 8), pady=(8, 0))
        self.combo.bind("<<ComboboxSelected>>", self.on_combo_selected)
        ttk.Button(top, text="刷新列表", command=self._auto_detect_projects).grid(
            row=1, column=2, pady=(8, 0))
        ttk.Button(top, text="打开工程目录", command=self.on_open_project).grid(
            row=1, column=3, padx=(8, 0), pady=(8, 0))
        top.columnconfigure(1, weight=1)

        ttk.Separator(self.root).pack(fill="x", pady=(8, 0))

        # —— 中部：页签 + 树 ——
        self.nb = ttk.Notebook(self.root)
        self.nb.pack(fill="both", expand=True, padx=14, pady=(10, 6))

        columns = ("cn", "type", "size")
        for tab_name in ["总览"] + [t[0] for t in SCAN_TARGETS]:
            frame = ttk.Frame(self.nb)
            self.nb.add(frame, text=tab_name)

            tree = ttk.Treeview(frame, columns=columns, show="tree headings",
                                selectmode="browse")
            tree.heading("#0", text="名称（英文原文）", anchor="w")
            tree.heading("cn", text="中文名称（翻译）", anchor="w")
            tree.heading("type", text="类型", anchor="w")
            tree.heading("size", text="大小", anchor="e")
            tree.column("#0", width=390, minwidth=220, stretch=False)
            tree.column("cn", width=360, minwidth=180, stretch=True)
            tree.column("type", width=110, minwidth=90, stretch=False, anchor="w")
            tree.column("size", width=90, minwidth=70, stretch=False, anchor="e")
            tree.tag_configure("dir", background="#eef4fb")
            tree.tag_configure("root", background="#dce9f8",
                               font=("Microsoft YaHei UI", 10, "bold"))
            tree.tag_configure("file", background="#ffffff")

            vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

            tree.grid(row=0, column=0, sticky="nsew")
            vsb.grid(row=0, column=1, sticky="ns")
            hsb.grid(row=1, column=0, sticky="ew")
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)

            self.tab_trees[tab_name] = tree
            tree.bind("<Double-1>", self.on_tree_double_click)

        # —— 底部：筛选与操作 ——
        bottom = ttk.Frame(self.root, padding=(14, 4, 14, 12))
        bottom.pack(fill="x")

        ttk.Label(bottom, text="筛选：").pack(side="left")
        filt = ttk.Entry(bottom, textvariable=self.filter_text, width=26,
                         font=("Microsoft YaHei UI", 10))
        filt.pack(side="left", padx=(0, 8))
        filt.bind("<KeyRelease>", lambda _e: self.render_all())

        for text, cmd in (("展开全部", self.on_expand_all),
                          ("折叠全部", self.on_collapse_all),
                          ("导出 TXT", self.on_export_txt),
                          ("导出 HTML", self.on_export_html),
                          ("复制树文本", self.on_copy),
                          ("打开词典", self.on_open_dict),
                          ("表格数据(MCP)", self.on_open_table)):
            ttk.Button(bottom, text=text, command=cmd).pack(side="left", padx=3)

        if not MCP_AVAILABLE:
            self.status_text.set("表格数据(MCP) 不可用：%s" % (MCP_IMPORT_ERROR or "模块缺失"))

        ttk.Label(self.root, textvariable=self.status_text,
                  font=("Microsoft YaHei UI", 9), foreground="#4a5560",
                  anchor="w", padding=(14, 0, 14, 8)).pack(fill="x")

    # ---------------- 项目探测 ----------------
    def _auto_detect_projects(self):
        """扫描工程集合根目录，列出可用地图项目。"""
        projects = []
        if os.path.isdir(DEFAULT_PROJECTS_ROOT):
            try:
                for name in sorted(os.listdir(DEFAULT_PROJECTS_ROOT)):
                    full = os.path.join(DEFAULT_PROJECTS_ROOT, name)
                    if os.path.isdir(full) and os.path.isdir(os.path.join(full, "Asset")):
                        projects.append(full)
            except OSError:
                pass
        self.combo["values"] = projects
        if projects:
            if not self.project_root.get():
                self.project_root.set(projects[0])
            self.combo.current(0)
            self.status_text.set("已探测到 %d 个地图项目，双击快速选择后点击「开始扫描」。"
                                 % len(projects))
        else:
            self.status_text.set("未在默认集合目录探测到项目，请手动浏览选择项目根目录。")

    def on_combo_selected(self, _event=None):
        idx = self.combo.current()
        values = self.combo["values"]
        if 0 <= idx < len(values):
            self.project_root.set(values[idx])

    def on_browse(self):
        init = self.project_root.get() or DEFAULT_PROJECTS_ROOT
        chosen = filedialog.askdirectory(title="选择地图项目根目录（含 Asset 文件夹）",
                                         initialdir=init if os.path.isdir(init) else "D:\\")
        if chosen:
            self.project_root.set(os.path.normpath(chosen))

    def on_open_project(self):
        path = self.project_root.get()
        if path and os.path.isdir(path):
            os.startfile(path)
        else:
            messagebox.showwarning("路径无效", "当前项目根目录不存在，请重新选择。")

    # ---------------- 扫描 ----------------
    def on_scan(self):
        raw = self.project_root.get().strip().strip('"')
        if not raw:
            messagebox.showwarning("未指定目录", "请先选择地图项目根目录。")
            return
        root_path = self._resolve_project_root(raw)
        if root_path is None:
            messagebox.showerror(
                "目录无效",
                "未找到有效的项目目录：\n%s\n\n请选择 UGCProjects 下的地图项目目录"
                "（其中应包含 Asset 文件夹）。" % raw)
            return

        self.project_root.set(root_path)
        self.trees, missing, total = collect_trees(root_path, DICTS)
        self.render_all()

        if not self.trees:
            self.status_text.set(build_status(root_path, self.trees, missing, total))
            messagebox.showwarning("未找到扫描目录", "以下目录不存在：\n\n" + "\n".join(missing))
            return

        self.status_text.set(build_status(root_path, self.trees, missing, total))

    @staticmethod
    def _resolve_project_root(raw):
        """把用户输入解析为项目根目录。

        接受：项目根目录、项目下的 Asset 目录、Asset/Data 目录；
        若传入 UGCProjects 集合根且其中只有一个项目，则自动进入该项目。
        """
        path = os.path.normpath(os.path.abspath(raw))
        if not os.path.isdir(path):
            return None

        # 1) 向上回溯最多 4 层，找出同时含 Asset 且至少含一个目标目录的层级
        probe = path
        for _ in range(4):
            if os.path.isdir(os.path.join(probe, "Asset")) and \
                    any(os.path.isdir(os.path.join(probe, rel)) for _t, rel, _d in SCAN_TARGETS):
                return probe
            parent = os.path.dirname(probe)
            if parent == probe:
                break
            probe = parent

        # 2) 退一步：只要含有 Asset 目录即视为项目根
        probe = path
        for _ in range(4):
            if os.path.isdir(os.path.join(probe, "Asset")):
                return probe
            parent = os.path.dirname(probe)
            if parent == probe:
                break
            probe = parent

        # 3) 输入是 UGCProjects 集合根：其中只有一个项目时自动选取
        try:
            subs = [os.path.join(path, n) for n in sorted(os.listdir(path))]
        except OSError:
            return None
        sub_projects = [s for s in subs
                        if os.path.isdir(s) and os.path.isdir(os.path.join(s, "Asset"))]
        if len(sub_projects) == 1:
            return sub_projects[0]
        return None

    # ---------------- 表格蓝图数据（MCP） ----------------
    def project_name(self):
        root = (self.project_root.get() or "").strip().strip('"')
        return os.path.basename(os.path.normpath(root)) if root else ""

    def _selected_asset_path(self):
        """取得当前选中节点的资产路径（仅表格目录下的 .uasset 有效）。"""
        tab = self.nb.tab(self.nb.select(), "text")
        if tab not in ("总览", "表格文件夹"):
            return ""
        tree = self._current_tree()
        if not tree:
            return ""
        sel = tree.selection()
        if not sel:
            return ""
        node = self._find_node(sel[0])
        if node is None or node.is_dir or not node.path.lower().endswith(".uasset"):
            return ""
        return normalize_asset_path(node.path, self.project_name())

    def _find_node(self, iid):
        """按 Treeview iid 反查 FsNode（插入时已建立 iid → 节点映射）。"""
        tab = self.nb.tab(self.nb.select(), "text")
        return self.node_by_iid.get(tab, {}).get(iid)

    def on_tree_double_click(self, event):
        """双击表格 .uasset 直接打开表格数据窗口；其余节点保持原有展开行为。"""
        path = self._selected_asset_path()
        if path:
            self.open_table_window(path)

    def on_open_table(self):
        self.open_table_window(self._selected_asset_path())

    def open_table_window(self, initial_path=""):
        if not MCP_AVAILABLE:
            messagebox.showerror("功能不可用",
                                 "表格数据(MCP) 模块未加载：%s" % (MCP_IMPORT_ERROR or "未知原因"))
            return
        root = (self.project_root.get() or "").strip().strip('"')
        if not root or not os.path.isdir(root):
            messagebox.showwarning("未选择项目", "请先在上方选择地图项目根目录。")
            return
        # 单例：已开着就复用（可能只是最小化，先还原再置顶）；换表时直接重新读取。
        # winfo_exists() 对已销毁句柄返回 0，但个别情况下会抛异常，这里单独兜住，
        # 不能让它掉进下面的 except 变成「打开失败」却又没开新窗口。
        existing = getattr(self, "table_window", None)
        if existing is not None:
            try:
                alive = bool(existing.winfo_exists())
            except Exception:
                alive = False
            if alive:
                try:
                    if initial_path:
                        existing.path_var.set(initial_path)
                    existing.deiconify()
                    existing.lift()
                    try:
                        existing.focus_force()
                    except Exception:
                        pass
                    if initial_path:
                        existing.on_read()
                    return
                except Exception:
                    # 复用失败就关掉重建，宁可重建也不能同时开两个
                    try:
                        existing.destroy()
                    except Exception:
                        pass
                    self.table_window = None
            else:
                self.table_window = None
        try:
            self.table_window = oasis_table_ui.TableEditorWindow(
                self.root, project_root=root, project_name=self.project_name(),
                initial_path=initial_path, logger=lambda m: print("[表格MCP]", m))
            self.table_window.bind("<Destroy>", self._on_table_window_closed)
        except Exception as exc:
            messagebox.showerror("打开失败", "无法打开表格数据窗口：%s" % exc)

    def _on_table_window_closed(self, event=None):
        """表格窗口关闭后清引用，避免下次打开撞上已销毁的句柄。"""
        try:
            if event is not None and self.table_window is not None \
                    and event.widget is not self.table_window:
                return
        except Exception:
            pass
        self.table_window = None

    # ---------------- 渲染 ----------------
    def render_all(self):
        """按当前数据与筛选条件刷新三个页签的树。"""
        for tab_name, tree in self.tab_trees.items():
            self._render_one(tab_name, tree)

    def _render_one(self, tab_name, tree):
        tree.delete(*tree.get_children())
        self.node_seq = 0
        self.node_by_iid[tab_name] = {}
        keyword = self.filter_text.get().strip().lower()

        if not self.trees:
            return

        if tab_name == "总览":
            targets = self.trees
        else:
            targets = [t for t in self.trees if t[0] == tab_name]

        for title, _desc, node in targets:
            if keyword and not self._subtree_match(node, keyword):
                continue
            self._insert(tree, "", node, "root", keyword, is_root=True, tab_name=tab_name)

        if keyword:
            tree.item(tree.get_children()[0] if tree.get_children() else "", open=True)
        else:
            for iid in tree.get_children():
                tree.item(iid, open=True)

    def _subtree_match(self, node, keyword):
        """判断子树内是否存在命中关键字的节点。"""
        if keyword in node.name.lower() or keyword in (node.cn or "").lower():
            return True
        return any(self._subtree_match(c, keyword) for c in node.children)

    def _insert(self, tree, parent, node, tag, keyword, is_root=False, tab_name=""):
        """递归插入树节点。"""
        self.node_seq += 1
        iid = "n%d" % self.node_seq
        label = node.name
        if node.is_dir and not is_root:
            label = node.name + "/"
        type_text = "文件夹" if node.is_dir else (ext_desc(node.name, DICTS) or "文件")
        size_text = "" if node.is_dir else human_size(node.size)

        tree.insert(parent, "end", iid=iid, text=label, values=(node.cn, type_text, size_text),
                    tags=(tag,), open=True)
        if tab_name:
            self.node_by_iid.setdefault(tab_name, {})[iid] = node

        for child in node.children:
            if keyword and not self._subtree_match(child, keyword):
                continue
            self._insert(tree, iid, child, "dir" if child.is_dir else "file", keyword,
                         tab_name=tab_name)

    # ---------------- 交互操作 ----------------
    def _current_tree(self):
        return self.tab_trees.get(self.nb.tab(self.nb.select(), "text"))

    def on_expand_all(self):
        tree = self._current_tree()
        if tree:
            for iid in self._all_iids(tree):
                tree.item(iid, open=True)

    def on_collapse_all(self):
        tree = self._current_tree()
        if tree:
            for iid in self._all_iids(tree):
                tree.item(iid, open=False)

    @staticmethod
    def _all_iids(tree, parent=""):
        out = []
        for iid in tree.get_children(parent):
            out.append(iid)
            out.extend(App._all_iids(tree, iid))
        return out

    def _current_targets(self):
        tab = self.nb.tab(self.nb.select(), "text")
        if tab == "总览":
            return self.trees
        return [t for t in self.trees if t[0] == tab]

    def _plain_text(self):
        targets = self._current_targets()
        if not targets:
            return ""
        tab = self.nb.tab(self.nb.select(), "text")
        if tab == "总览":
            return build_report_text(self.project_root.get(), targets, self.status_text.get())
        lines = ["=" * 78,
                 "地图项目：%s" % self.project_root.get(),
                 "生成时间：%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 "=" * 78, ""]
        for title, desc, node in targets:
            lines.append("【%s】%s" % (title, desc))
            lines.append("-" * 78)
            lines.extend(render_text(node))
            lines.append("")
        lines.append(self.status_text.get())
        return "\n".join(lines)

    def on_export_txt(self):
        text = self._plain_text()
        if not text:
            messagebox.showinfo("无内容", "请先执行扫描。")
            return
        path = filedialog.asksaveasfilename(
            title="导出树状文本", defaultextension=".txt",
            initialfile="文件夹结构_%s.txt" % datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(text)
        except OSError as exc:
            messagebox.showerror("导出失败", str(exc))
            return
        self.status_text.set("已导出文本：%s" % path)
        messagebox.showinfo("导出成功", "已导出：\n%s" % path)

    def on_export_html(self):
        targets = self._current_targets()
        if not targets:
            messagebox.showinfo("无内容", "请先执行扫描。")
            return
        path = filedialog.asksaveasfilename(
            title="导出树状网页", defaultextension=".html",
            initialfile="文件夹结构_%s.html" % datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),
            filetypes=[("网页文件", "*.html"), ("所有文件", "*.*")])
        if not path:
            return
        tab = self.nb.tab(self.nb.select(), "text")
        title = "%s — %s" % (os.path.basename(self.project_root.get()), tab)
        try:
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(render_html(title, [t[2] for t in targets], self.status_text.get()))
        except OSError as exc:
            messagebox.showerror("导出失败", str(exc))
            return
        self.status_text.set("已导出网页：%s" % path)
        if messagebox.askyesno("导出成功", "已导出：\n%s\n\n是否立即打开？" % path):
            os.startfile(path)

    def on_copy(self):
        text = self._plain_text()
        if not text:
            messagebox.showinfo("无内容", "请先执行扫描。")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.status_text.set("树状文本已复制到剪贴板（%d 行）。" % text.count("\n"))

    def on_open_dict(self):
        """生成（若不存在）并打开外置翻译词典，便于用户自行扩充。"""
        path = os.path.join(app_dir(), DICT_FILENAME)
        if not os.path.isfile(path):
            template = {
                "_说明": "按需扩充翻译词典；words=单词表，segs=整段表，names=完整名表，"
                         "prefixes=前缀表，exts=扩展名表。修改后重新扫描即可生效。",
                "words": {},
                "segs": {},
                "names": {},
                "prefixes": {},
                "exts": {},
            }
            try:
                with open(path, "w", encoding="utf-8") as fp:
                    json.dump(template, fp, ensure_ascii=False, indent=2)
            except OSError as exc:
                messagebox.showerror("写入词典失败", str(exc))
                return
        os.startfile(path)
        self.status_text.set("已打开翻译词典：%s（修改后点击「开始扫描」重新加载）" % path)


def parse_args(argv=None):
    """解析命令行参数；不带 --scan 时进入图形界面。"""
    parser = argparse.ArgumentParser(
        prog="FolderTreeTranslator",
        description="绿洲起源 · 文件夹结构整理工具"
                    "（表格目录 Asset/Data + UI 目录 Asset/Blueprint/Prefabs/UI，"
                    "树状展示并标注中文名）")
    parser.add_argument("--scan", metavar="项目根目录",
                        help="命令行扫描模式：扫描该地图项目并输出树状结果")
    parser.add_argument("--txt", metavar="输出文件",
                        help="把树状文本写入指定 .txt 文件（建议命令行模式使用）")
    parser.add_argument("--html", metavar="输出文件",
                        help="把可折叠树状网页写入指定 .html 文件")
    parser.add_argument("--project", metavar="项目根目录",
                        help="表格模式的项目根目录（配合 --table 使用）")
    parser.add_argument("--table", metavar="表格路径或表名",
                        help="表格模式：经 MCP 读取 DataTable（如 UIConfigTable 或 /项目名/Asset/...）")
    parser.add_argument("--table-json", metavar="输出文件",
                        help="表格模式：把读取结果写入 JSON 文件")
    return parser.parse_args(argv)


def run_cli(args):
    """命令行扫描模式：不启动界面，直接产出文本 / 网页报告。"""
    raw = (args.scan or "").strip().strip('"')
    root_path = App._resolve_project_root(raw)
    if root_path is None:
        sys.stderr.write("未找到有效的项目目录：%s\n" % raw)
        return 2

    trees, missing, total = collect_trees(root_path, DICTS)
    status = build_status(root_path, trees, missing, total)
    text = build_report_text(root_path, trees, status)
    if text:
        sys.stdout.write(text + "\n")
    for line in missing:
        sys.stdout.write("[缺失] %s\n" % line)

    if args.txt and text:
        with open(args.txt, "w", encoding="utf-8") as fp:
            fp.write(text)
        sys.stdout.write("[已写出] %s\n" % args.txt)
    if args.html and trees:
        with open(args.html, "w", encoding="utf-8") as fp:
            fp.write(render_html("%s — 文件夹结构" % os.path.basename(root_path),
                                 [t[2] for t in trees], status))
        sys.stdout.write("[已写出] %s\n" % args.html)
    return 0 if trees else 1


def run_table_cli(args):
    """表格模式：经 UGCAskQ MCP 读取 DataTable 并输出（可选导出 JSON）。"""
    if not MCP_AVAILABLE:
        sys.stderr.write("表格功能不可用：%s\n" % (MCP_IMPORT_ERROR or "模块缺失"))
        return 2
    root_raw = (args.project or "").strip().strip('"')
    root_path = App._resolve_project_root(root_raw) if root_raw else None
    if root_path is None:
        sys.stderr.write("未找到有效的项目目录：%s（请用 --project 指定）\n" % root_raw)
        return 2

    project_name = os.path.basename(os.path.normpath(root_path))
    service = DataTableService(project_name=project_name, project_root=root_path,
                               logger=lambda m: sys.stderr.write("[MCP] %s\n" % m))
    try:
        service.ensure_connected()
        resolved = service.resolve(args.table)
        data = service.read_table(resolved["path"], limit=0)
    except McpError as exc:
        sys.stderr.write("读取失败：%s\n" % exc)
        return 3

    fields = [f["name"] for f in (data.get("fields") or [])]
    sys.stdout.write("表格：%s（定位方式：%s）\n" % (resolved["path"], resolved.get("source", "?")))
    sys.stdout.write("字段：%s\n" % "、".join(fields))
    sys.stdout.write("行数：%d\n%s\n" % (len(data.get("rows") or {}), "-" * 78))
    for row_name in sorted((data.get("rows") or {}).keys()):
        values = data["rows"][row_name]
        sys.stdout.write("%s  ->  %s\n" % (
            row_name, " | ".join("%s=%s" % (f, values.get(f)) for f in fields)))

    if args.table_json:
        with open(args.table_json, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
        sys.stdout.write("[已写出] %s\n" % args.table_json)
    return 0


def main():
    # 打包为 --windowed 时没有控制台，stdout/stderr 为 None，先兜底避免写入报错
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")

    args = parse_args()
    if args.scan:
        return run_cli(args)
    if args.table:
        return run_table_cli(args)

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    root = tk.Tk()
    App(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
