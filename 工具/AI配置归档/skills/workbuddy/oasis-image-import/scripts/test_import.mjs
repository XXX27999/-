import { generateImportPlan } from './batch_import.mjs';

const sourceFolder = process.argv[2];
const targetPath = process.argv[3];
const textureGroup = parseInt(process.argv[4] || '16');

console.log(`Testing import plan generation...`);
console.log(`Source: ${sourceFolder}`);
console.log(`Target: ${targetPath}`);
console.log(`Texture Group: ${textureGroup}`);

try {
  const plan = generateImportPlan(sourceFolder, targetPath, textureGroup);
  console.log(`\n✓ Generated plan for ${plan.totalFiles} files`);
  console.log('\nSample mappings:');
  plan.mapping.slice(0, 5).forEach(m => {
    console.log(`  ${m.original} -> ${m.asset}`);
  });
  console.log('\nFull plan:');
  console.log(JSON.stringify(plan, null, 2));
} catch (error) {
  console.error('✗ Error:', error.message);
  process.exit(1);
}
