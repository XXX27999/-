// Token estimation (approximate, for previews) + cost computation from the
// exact usage numbers Anthropic returns on every response.
//
// Calibrated 2026-09-24 against real captured Codex traffic under
// %USERPROFILE%\.ccglass\codex-desktop: counting the full request JSON (system,
// input items including function_call / function_call_output / reasoning, tools)
// plus the response content, CJK characters bill at about 1.12 tokens each and
// other characters at about 1/4.6 tokens. Across the measured requests that
// keeps the summed estimate within about +/-1% of the summed input_tokens +
// output_tokens (median per-request error ~3%), which is what the dashboard
// shows side by side.
//
// The constants were fitted by grid search over (CJK weight, ASCII chars per
// token) on captured traffic, preferring the pair with the smallest summed
// deviation while keeping the per-request error low. Re-run the search and
// update these two numbers if the capture mix changes a lot (new model,
// different language ratio, much longer contexts).
export const ESTIMATE_CJK_WEIGHT = 1.12;
export const ESTIMATE_ASCII_CHARS_PER_TOKEN = 4.6;

// Rough token estimate: CJK chars count heavier than Latin text. Labelled "≈"
// everywhere in the UI — the real numbers come from response.usage.
export function estimateTokens(text) {
  if (!text) return 0;
  const cjk = (text.match(/[㐀-鿿豈-﫿぀-ヿ]/g) || []).length;
  const rest = text.length - cjk;
  return Math.ceil(cjk * ESTIMATE_CJK_WEIGHT + rest / ESTIMATE_ASCII_CHARS_PER_TOKEN);
}

export function estimateRequestTokens(body) {
  if (!body || typeof body !== "object") return 0;
  try {
    return estimateTokens(JSON.stringify(body));
  } catch {
    return 0;
  }
}

// Estimate a reassembled response: assistant text, reasoning summaries, and
// tool-call arguments. Paired with estimateRequestTokens it approximates the
// full input + output bill of one HTTP round-trip.
export function estimateResponseTokens(response) {
  if (!response || typeof response !== "object") return 0;
  let text = "";
  for (const block of response.content || []) {
    if (block == null) continue;
    if (typeof block === "string") { text += block; continue; }
    if (block.text) text += block.text;
    if (block.input != null) text += JSON.stringify(block.input);
  }
  return estimateTokens(text);
}

// USD per 1M tokens. Approximate public Claude pricing; edit as needed.
// Cache columns follow Anthropic's multipliers: 5m write = 1.25x input,
// read = 0.1x input. Opus and Haiku are split by generation: Opus 4.5 (2025-11)
// cut the rate to $5/$25 and 4.6+ kept it, while Opus 3/4/4.1 stay at $15/$75;
// the three Haiku generations live at $0.25 / $0.80 / $1.00 input.
const PRICES = {
  opus: { input: 5, output: 25, cacheWrite: 6.25, cacheRead: 0.5 },
  opusLegacy: { input: 15, output: 75, cacheWrite: 18.75, cacheRead: 1.5 },
  sonnet: { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.3 },
  haiku45: { input: 1, output: 5, cacheWrite: 1.25, cacheRead: 0.1 },
  haiku35: { input: 0.8, output: 4, cacheWrite: 1.0, cacheRead: 0.08 },
  haiku3: { input: 0.25, output: 1.25, cacheWrite: 0.3125, cacheRead: 0.025 },
};

function priceFor(model = "") {
  const m = model.toLowerCase();
  if (m.includes("opus")) {
    // Opus 4.5 (2025-11) cut pricing to $5/$25 and Opus 4.6+ kept it; only the
    // dated legacy ids — Opus 3 (`3-opus`), 4.0 (`opus-4-2025…`), 4.1
    // (`opus-4-1`) — bill at the old $15/$75. Default current/newer Opus to the
    // cut rate.
    if (m.includes("3-opus") || m.includes("opus-4-1") || /opus-4-20\d\d/.test(m)) {
      return PRICES.opusLegacy;
    }
    return PRICES.opus;
  }
  if (m.includes("haiku")) {
    // Generation appears as `3-5-haiku` / `3-haiku` (older) or `haiku-4-5`
    // (newer). Check the dated 3.x ids first; a bare/newer "haiku" is 4.x.
    if (m.includes("3-5-haiku")) return PRICES.haiku35;
    if (m.includes("3-haiku")) return PRICES.haiku3;
    return PRICES.haiku45;
  }
  return PRICES.sonnet;
}

export function costFromUsage(model, usage = {}) {
  const p = priceFor(model);
  const input = usage.input_tokens || 0;
  const output = usage.output_tokens || 0;
  const cacheWrite = usage.cache_creation_input_tokens || 0;
  const cacheRead = usage.cache_read_input_tokens || 0;
  const usd =
    (input * p.input +
      output * p.output +
      cacheWrite * p.cacheWrite +
      cacheRead * p.cacheRead) /
    1e6;
  const totalInput = input + cacheWrite + cacheRead;
  const cacheHitRate = totalInput ? cacheRead / totalInput : 0;
  return {
    input,
    output,
    cacheWrite,
    cacheRead,
    totalInput,
    cacheHitRate,
    usd,
  };
}
