import path from 'node:path';
import process from 'node:process';
import { access, readdir, readFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';

const VALID_MODES = new Set(['verify-api', 'search']);
const VALID_SCOPES = new Set(['api', 'wiki', 'all']);
const API_ONLY_MODES = new Set(['verify-api']);
const LOCAL_DEFAULT_OASIS_REPO = process.env.OASIS_SKILL_PLUS_DEFAULT_ROOT || 'd:\\oasis-skill-plus';

function toPosixPath(filePath) {
  return filePath.replace(/\\/g, '/');
}

async function pathExists(filePath) {
  try {
    await access(filePath);
    return true;
  } catch {
    return false;
  }
}

function createCliError(code, message, details = {}) {
  const error = new Error(message);
  error.code = code;
  error.details = details;
  return error;
}

function printJson(payload, stream = process.stdout) {
  stream.write(`${JSON.stringify(payload, null, 2)}\n`);
}

function readTitle(content, fallbackTitle) {
  const match = String(content).match(/^#\s+(.+)$/m);
  return match?.[1]?.trim() || fallbackTitle;
}

function buildFallbackTitle(relativePath) {
  const baseName = path.posix.basename(relativePath, '.md');
  if (/^\d+_/.test(baseName)) {
    return baseName.replace(/^\d+_/, '');
  }

  return baseName;
}

function extractExcerpt(content, query) {
  const lines = String(content)
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean);
  const normalizedQuery = query.toLowerCase();
  const matchedLine = lines.find((line) => line.toLowerCase().includes(normalizedQuery));

  if (matchedLine) {
    return matchedLine;
  }

  return lines.find((line) => !line.startsWith('#')) || lines[0] || '';
}

async function collectMarkdownFiles(rootDir) {
  const results = [];

  async function walk(currentDir) {
    const entries = await readdir(currentDir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(currentDir, entry.name);
      if (entry.isDirectory()) {
        await walk(fullPath);
        continue;
      }

      if (!entry.isFile()) {
        continue;
      }

      if (!entry.name.endsWith('.md') || entry.name.startsWith('000_')) {
        continue;
      }

      results.push(fullPath);
    }
  }

  await walk(rootDir);
  return results.sort((left, right) => left.localeCompare(right, 'en'));
}

function normalizeProjectRoot(projectRoot) {
  if (!projectRoot) {
    throw createCliError('INVALID_ARGUMENTS', 'Missing required argument: --project-root or current working directory');
  }

  return path.resolve(projectRoot);
}

function uniquePaths(filePaths) {
  const seen = new Set();
  const unique = [];

  for (const filePath of filePaths) {
    const normalizedKey = path.normalize(filePath).toLowerCase();
    if (seen.has(normalizedKey)) {
      continue;
    }

    seen.add(normalizedKey);
    unique.push(filePath);
  }

  return unique;
}

function buildDefaultOasisRepoCandidates(projectRoot) {
  return uniquePaths([
    path.resolve(projectRoot, 'oasis-skill-plus'),
    path.resolve(LOCAL_DEFAULT_OASIS_REPO)
  ]);
}

export async function resolveOasisRepoRoot(projectRoot, customOasisRepo) {
  // 优先使用 --oasis-repo 指定的自定义路径
  if (customOasisRepo) {
    const resolved = path.resolve(customOasisRepo);
    if (await pathExists(path.join(resolved, 'docs'))) {
      return resolved;
    }
    throw createCliError(
      'OASIS_REPO_NOT_FOUND',
      `Custom --oasis-repo path does not contain a 'docs' directory: ${resolved}`,
      {
        customOasisRepo: resolved
      }
    );
  }

  const normalizedProjectRoot = normalizeProjectRoot(projectRoot);
  const defaultCandidates = buildDefaultOasisRepoCandidates(normalizedProjectRoot);

  for (const candidate of defaultCandidates) {
    if (await pathExists(path.join(candidate, 'docs'))) {
      return candidate;
    }
  }

  throw createCliError(
    'OASIS_REPO_NOT_FOUND',
    `Could not find an oasis-skill-plus repository at ${defaultCandidates.join(' or ')}. Use --oasis-repo to specify a custom path.`,
    {
      projectRoot: normalizedProjectRoot,
      checkedPaths: defaultCandidates
    }
  );
}

function validateArgs(args) {
  if (!VALID_MODES.has(args.mode)) {
    throw createCliError(
      'INVALID_ARGUMENTS',
      `Invalid --mode value "${args.mode}". Expected one of: ${Array.from(VALID_MODES).join(', ')}.`
    );
  }

  if (!VALID_SCOPES.has(args.scope)) {
    throw createCliError(
      'INVALID_ARGUMENTS',
      `Invalid --scope value "${args.scope}". Expected one of: ${Array.from(VALID_SCOPES).join(', ')}.`
    );
  }

  if (!args.query?.trim()) {
    throw createCliError('INVALID_ARGUMENTS', 'Missing required argument: --query');
  }

  if (API_ONLY_MODES.has(args.mode) && args.scope === 'wiki') {
    throw createCliError(
      'INVALID_ARGUMENTS',
      `Mode "${args.mode}" cannot be used with --scope wiki. Use --scope api or --scope all.`
    );
  }
}

function getRequestedScopes(scope) {
  return scope === 'all' ? ['api', 'wiki'] : [scope];
}

function getRequiredScopes(scope, mode) {
  if (mode === 'verify-api') {
    return ['api'];
  }

  return getRequestedScopes(scope);
}

async function resolveScopeDirectories(oasisRepoRoot, scope) {
  const requestedScopes = getRequestedScopes(scope);
  const directories = {};

  for (const requestedScope of requestedScopes) {
    const scopeDir = path.join(oasisRepoRoot, 'docs', requestedScope);
    if (!(await pathExists(scopeDir))) {
      throw createCliError(
        'DOCS_SCOPE_MISSING',
        `Expected ${toPosixPath(path.join('docs', requestedScope))} to exist under ${oasisRepoRoot}.`,
        {
          scope: requestedScope,
          expectedPath: scopeDir
        }
      );
    }

    directories[requestedScope] = scopeDir;
  }

  return directories;
}

async function loadDocuments(oasisRepoRoot, scopeDirectories) {
  const documents = [];

  for (const [scope, scopeDir] of Object.entries(scopeDirectories)) {
    const filePaths = await collectMarkdownFiles(scopeDir);

    for (const absolutePath of filePaths) {
      const content = await readFile(absolutePath, 'utf8');
      const relativePath = toPosixPath(path.relative(oasisRepoRoot, absolutePath));
      const title = readTitle(content, buildFallbackTitle(relativePath));
      const document = {
        type: scope,
        title,
        relativePath,
        absolutePath,
        content
      };

      if (scope === 'api') {
        const [, , family] = relativePath.split('/');
        document.family = family || null;
      }

      documents.push(document);
    }
  }

  return documents;
}

function toMatch(document, matchType, query) {
  const match = {
    type: document.type,
    matchType,
    title: document.title,
    relativePath: document.relativePath,
    absolutePath: document.absolutePath,
    excerpt: extractExcerpt(document.content, query)
  };

  if (document.family) {
    match.family = document.family;
  }

  return match;
}

function findVerifyApiMatches(documents, query) {
  const normalizedQuery = query.toLowerCase();
  const exactTitle = [];
  const exactFileName = [];
  const titleContains = [];
  const contentContains = [];

  for (const document of documents) {
    const title = document.title.trim();
    const normalizedTitle = title.toLowerCase();
    const fileName = path.posix.basename(document.relativePath, '.md');
    const normalizedFileName = fileName.toLowerCase();
    const normalizedContent = document.content.toLowerCase();

    if (title === query || normalizedTitle === normalizedQuery) {
      exactTitle.push(toMatch(document, 'exact-title', query));
      continue;
    }

    if (fileName === query || normalizedFileName === normalizedQuery) {
      exactFileName.push(toMatch(document, 'exact-filename', query));
      continue;
    }

    if (normalizedTitle.includes(normalizedQuery)) {
      titleContains.push(toMatch(document, 'title-contains', query));
      continue;
    }

    if (normalizedContent.includes(normalizedQuery)) {
      contentContains.push(toMatch(document, 'content', query));
    }
  }

  return [...exactTitle, ...exactFileName, ...titleContains, ...contentContains].slice(0, 20);
}

function findSearchMatches(documents, query) {
  const normalizedQuery = query.toLowerCase();
  const titleMatches = [];
  const contentMatches = [];

  for (const document of documents) {
    const normalizedTitle = document.title.toLowerCase();
    const normalizedContent = document.content.toLowerCase();

    if (normalizedTitle.includes(normalizedQuery)) {
      titleMatches.push(toMatch(document, 'title', query));
      continue;
    }

    if (normalizedContent.includes(normalizedQuery)) {
      contentMatches.push(toMatch(document, 'content', query));
    }
  }

  return [...titleMatches, ...contentMatches].slice(0, 20);
}

export async function runQuery({
  projectRoot = process.cwd(),
  scope = 'all',
  mode,
  query,
  oasisRepo
} = {}) {
  validateArgs({ mode, scope, query });

  const normalizedProjectRoot = normalizeProjectRoot(projectRoot);
  const oasisRepoRoot = await resolveOasisRepoRoot(normalizedProjectRoot, oasisRepo);
  const requiredScopes = getRequiredScopes(scope, mode);
  const scopeDirectories = await resolveScopeDirectories(
    oasisRepoRoot,
    requiredScopes.length === 1 ? requiredScopes[0] : scope
  );
  const documents = await loadDocuments(oasisRepoRoot, scopeDirectories);
  const filteredDocuments = mode === 'verify-api' ? documents.filter((document) => document.type === 'api') : documents;
  const matches =
    mode === 'verify-api'
      ? findVerifyApiMatches(filteredDocuments, query)
      : findSearchMatches(filteredDocuments, query);

  return {
    ok: true,
    projectRoot: normalizedProjectRoot,
    oasisRepoRoot,
    scope,
    mode,
    query,
    matches
  };
}

export function parseArgs(argv = process.argv.slice(2)) {
  const options = {
    projectRoot: process.cwd(),
    scope: 'all'
  };

  for (let index = 0; index < argv.length; index += 1) {
    const current = argv[index];
    const next = argv[index + 1];

    if (current === '--help') {
      options.help = true;
      continue;
    }

    if (!current.startsWith('--')) {
      throw createCliError('INVALID_ARGUMENTS', `Unexpected positional argument: ${current}`);
    }

    if (next == null || next.startsWith('--')) {
      throw createCliError('INVALID_ARGUMENTS', `Missing value for ${current}`);
    }

    switch (current) {
      case '--project-root':
        options.projectRoot = next;
        break;
      case '--oasis-repo':
        options.oasisRepo = next;
        break;
      case '--scope':
        options.scope = next;
        break;
      case '--mode':
        options.mode = next;
        break;
      case '--query':
        options.query = next;
        break;
      default:
        throw createCliError('INVALID_ARGUMENTS', `Unknown argument: ${current}`);
    }

    index += 1;
  }

  return options;
}

function createUsagePayload() {
  return {
    ok: false,
    error: {
      code: 'INVALID_ARGUMENTS',
      message: 'Usage: node query-oasis-docs.mjs --project-root <path> --scope api|wiki|all --mode verify-api|search --query <text>'
    }
  };
}

export async function runCli(argv = process.argv.slice(2)) {
  try {
    const options = parseArgs(argv);

    if (options.help) {
      printJson(createUsagePayload());
      return 0;
    }

    const payload = await runQuery(options);
    printJson(payload);
    return 0;
  } catch (error) {
    const payload = error.code
      ? {
          ok: false,
          error: {
            code: error.code,
            message: error.message,
            ...(error.details ? { details: error.details } : {})
          }
        }
      : {
          ok: false,
          error: {
            code: 'UNEXPECTED_ERROR',
            message: error.message
          }
        };

    printJson(payload);
    return 1;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const exitCode = await runCli();
  if (exitCode !== 0) {
    process.exitCode = exitCode;
  }
}
