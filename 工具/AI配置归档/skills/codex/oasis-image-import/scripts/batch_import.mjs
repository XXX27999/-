// batch_import.mjs - 图片批量导入预处理脚本
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/**
 * 简易拼音转换（首字母）
 * 仅支持常用汉字，复杂字符使用通用前缀
 */
const pinyinMap = {
  '金': 'jin', '币': 'bi', '帮': 'bang', '助': 'zhu', '按': 'an', '钮': 'niu',
  '大': 'da', '厅': 'ting', '右': 'you', '侧': 'ce', '头': 'tou', '像': 'xiang', '框': 'kuang',
  '展': 'zhan', '示': 'shi', '价': 'jia', '值': 'zhi', '每': 'mei', '日': 'ri', '任': 'ren', '务': 'wu',
  '顶': 'ding', '部': 'bu', '领': 'ling', '取': 'qu', '保': 'bao', '底': 'di',
  '主': 'zhu', '界': 'jie', '面': 'mian', '参': 'can', '考': 'kao', '上': 'shang', '半': 'ban', '名': 'ming', '称': 'cheng',
  '技': 'ji', '能': 'neng', '选': 'xuan', '择': 'ze', '勾': 'gou', '空': 'kong', '槽': 'cao', '位': 'wei', '栏': 'lan',
  '背': 'bei', '景': 'jing', '图': 'tu', '标': 'biao', '题': 'ti', '文': 'wen', '字': 'zi',
  '按': 'an', '钮': 'niu', '键': 'jian', '盘': 'pan', '鼠': 'shu', '标': 'biao',
  '人': 'ren', '物': 'wu', '道': 'dao', '具': 'ju', '装': 'zhuang', '备': 'bei',
  '特': 'te', '效': 'xiao', '光': 'guang', '影': 'ying', '粒': 'li', '子': 'zi'
};

/**
 * 将中文字符转换为拼音
 */
function chineseToPinyin(text) {
  return text.split('').map(char => pinyinMap[char] || char).join('');
}

/**
 * 将文件名转换为合法的 UE 资产名称
 * 规则：
 * 1. 只能包含英文字母、数字、下划线
 * 2. 必须以英文字母开头
 * 3. 中文转换为拼音
 */
function sanitizeAssetName(filename, usedNames = new Set()) {
  // 去掉扩展名
  const nameWithoutExt = path.parse(filename).name;
  
  let sanitized = nameWithoutExt
    // 先尝试转换中文为拼音
    .split('').map(char => {
      if (/[\u4e00-\u9fa5]/.test(char)) {
        return pinyinMap[char] || 'x';
      }
      return char;
    }).join('')
    // 将空格、短横线等转为下划线
    .replace(/[\s\-]+/g, '_')
    // 移除所有非法字符（保留字母、数字、下划线）
    .replace(/[^a-zA-Z0-9_]/g, '')
    // 多个下划线合并为一个
    .replace(/_+/g, '_')
    // 去除首尾下划线
    .replace(/^_+|_+$/g, '');
  
  // 如果为空或不以字母开头，添加前缀
  if (!sanitized || !/^[a-zA-Z]/.test(sanitized)) {
    sanitized = 'Image_' + sanitized;
  }
  
  // 处理重名
  let finalName = sanitized;
  let counter = 1;
  while (usedNames.has(finalName)) {
    finalName = `${sanitized}_${counter}`;
    counter++;
  }
  
  usedNames.add(finalName);
  return finalName;
}

/**
 * 扫描源文件夹，生成导入计划
 */
function scanFolder(sourceFolder) {
  const files = [];
  const usedNames = new Set();
  const mapping = [];
  
  function scan(dir, relPath = '') {
    const items = fs.readdirSync(dir, { withFileTypes: true });
    
    for (const item of items) {
      const fullPath = path.join(dir, item.name);
      const itemRelPath = relPath ? path.join(relPath, item.name) : item.name;
      
      if (item.isDirectory()) {
        scan(fullPath, itemRelPath);
      } else if (item.isFile()) {
        const ext = path.extname(item.name).toLowerCase();
        if (['.png', '.jpg', '.jpeg', '.tga'].includes(ext)) {
          const assetName = sanitizeAssetName(item.name, usedNames);
          const subDir = relPath ? relPath.replace(/\\/g, '/') : '';
          
          files.push({
            originalPath: fullPath,
            originalName: item.name,
            assetName: assetName,
            subDirectory: subDir,
            extension: ext
          });
          
          mapping.push({
            original: item.name,
            asset: assetName,
            path: itemRelPath
          });
        }
      }
    }
  }
  
  scan(sourceFolder);
  
  return { files, mapping };
}

/**
 * 生成导入计划 JSON
 */
export function generateImportPlan(sourceFolder, targetPath, textureGroup = 16) {
  if (!fs.existsSync(sourceFolder)) {
    throw new Error(`源文件夹不存在: ${sourceFolder}`);
  }
  
  console.log(`扫描文件夹: ${sourceFolder}`);
  const { files, mapping } = scanFolder(sourceFolder);
  
  const plan = {
    sourceFolder,
    targetPath,
    textureGroup,
    totalFiles: files.length,
    files,
    mapping,
    timestamp: new Date().toISOString()
  };
  
  return plan;
}

/**
 * 主函数 - 命令行调用
 */
// Windows 下 file:// URL 与 argv 的盘符和斜杠形式不稳定，使用解析后的本地路径判断直接运行。
if (process.argv[1] && path.resolve(process.argv[1]) === __filename) {
  const args = process.argv.slice(2);
  
  if (args.length < 2) {
    console.error('用法: node batch_import.mjs <源文件夹> <目标UE路径> [贴图组]');
    console.error('示例: node batch_import.mjs "C:\\素材\\UI" "/IslandAuctionKing/Asset/TuPian/UI" 16');
    process.exit(1);
  }
  
  const [sourceFolder, targetPath, textureGroup = '16'] = args;
  
  try {
    const plan = generateImportPlan(sourceFolder, targetPath, parseInt(textureGroup));
    
    // 输出 JSON 格式的计划
    console.log(JSON.stringify(plan, null, 2));
    
    // 保存到文件
    const outputFile = path.join(__dirname, `import_plan_${Date.now()}.json`);
    fs.writeFileSync(outputFile, JSON.stringify(plan, null, 2), 'utf8');
    console.error(`\n导入计划已保存到: ${outputFile}`);
    console.error(`共扫描到 ${plan.totalFiles} 个图片文件`);
    
  } catch (error) {
    console.error('错误:', error.message);
    process.exit(1);
  }
}
