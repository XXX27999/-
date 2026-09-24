# -*- coding: utf-8 -*-
"""
绿洲编辑器图片批量导入 - Python 执行脚本
基于导入计划执行实际的资产导入和配置
"""
import unreal_engine as ue
import json
import os
import shutil
import tempfile

def execute_import_plan(plan_json):
    """
    执行导入计划
    
    参数：
        plan_json (dict): 由 batch_import.mjs 生成的导入计划
    
    返回：
        dict: 导入结果统计
    """
    source_folder = plan_json['sourceFolder']
    target_path = plan_json['targetPath']
    texture_group = plan_json['textureGroup']
    files = plan_json['files']
    
    ue.log(f"【OasisImageImport+执行导入】入口 totalFiles={len(files)}, targetPath={target_path}, textureGroup={texture_group}")
    
    imported_files = []
    skipped_files = []
    
    temp_dir = tempfile.mkdtemp(prefix="oasis_img_import_")
    
    try:
        for file_info in files:
            original_path = file_info['originalPath']
            original_name = file_info['originalName']
            asset_name = file_info['assetName']
            sub_dir = file_info.get('subDirectory', '')
            ext = file_info.get('extension', '')
            if not ext:
                _, ext = os.path.splitext(original_path)
            
            # 计算目标 UE 文件夹路径。import_asset 的第二参数必须是目录，绝不能拼接资产名。
            if sub_dir:
                ue_import_path = f"{target_path}/{sub_dir}".replace('\\', '/')
            else:
                ue_import_path = target_path
            
            ue.log(f"【OasisImageImport+执行导入】关键数据 导入: {original_name} -> {asset_name} at {ue_import_path}")
            
            # 将源文件以规范化资产名复制到临时路径，确保 ue.import_asset 直接生成正确的英文资产且不创建多余目录
            temp_file_path = os.path.join(temp_dir, f"{asset_name}{ext}")
            
            try:
                shutil.copy2(original_path, temp_file_path)
                
                # 临时文件已使用英文 asset_name 命名，导入到纯目录路径后会直接得到目标英文资产。
                # 严禁传入 target_path/asset_name，否则编辑器会将 asset_name 视为子目录。
                imported_asset = ue.import_asset(temp_file_path, ue_import_path)
                
                if imported_asset:
                    # 配置纹理属性
                    # TC_Default = 0, TEXTUREGROUP_UI = 16, TMGS_NoMipmaps = 13。
                    imported_asset.CompressionSettings = 0
                    imported_asset.LODGroup = texture_group
                    imported_asset.MipGenSettings = 13  # UI贴图不需要Mipmap
                    imported_asset.SRGB = True
                    
                    # 保存
                    imported_asset.save_package()
                    
                    imported_files.append({
                        "original": original_name,
                        "asset": asset_name,
                        "path": imported_asset.get_path_name()
                    })
                    ue.log(f"【OasisImageImport+执行导入】关键数据 成功: {original_name} -> {imported_asset.get_path_name()}")
                else:
                    skipped_files.append({"file": original_name, "reason": "import_asset返回None"})
                    ue.log(f"【OasisImageImport+错误】失败: {original_name}")
                    
            except Exception as e:
                skipped_files.append({"file": original_name, "reason": str(e)})
                ue.log(f"【OasisImageImport+错误】异常: {original_name}, error={str(e)}")
            finally:
                if os.path.exists(temp_file_path):
                    try:
                        os.remove(temp_file_path)
                    except Exception:
                        pass
    finally:
        if os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir, ignore_errors=True)
            except Exception:
                pass
    
    ue.log(f"【OasisImageImport+执行导入】出口 成功={len(imported_files)}, 失败={len(skipped_files)}")
    
    return {
        "success": True,
        "imported_count": len(imported_files),
        "skipped_count": len(skipped_files),
        "imported_files": imported_files,
        "skipped_files": skipped_files,
        "mapping": plan_json['mapping']
    }


# 模板：待替换为实际的 plan JSON
PLAN_TEMPLATE = """{{PLAN_JSON}}"""

if __name__ == "__main__":
    plan = json.loads(PLAN_TEMPLATE)
    result = execute_import_plan(plan)
    print(json.dumps(result, ensure_ascii=False, indent=2))
