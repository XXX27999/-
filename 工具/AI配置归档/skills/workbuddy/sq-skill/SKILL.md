---
name: sq-skill
description: Search the local Oasis community archive for practical answers, editor behavior, Lua and Blueprint usage, troubleshooting reports, and community workarounds. Use for Peace Elite Oasis editor questions when community experience can supplement official documentation.
agent_created: true
---

# Oasis Community Search

Use this skill as a read-only community-evidence source for Peace Elite Oasis editor work.

## Evidence Rules

- Treat `docs/community` as community material, not official API documentation.
- Keep official documentation authoritative for API existence, parameters, return values, lifecycle, authority, and client/server restrictions.
- Report the local archive snapshot date from `docs/community/manifest.json` when freshness matters.
- Cite the exact local Markdown paths used and distinguish confirmed text from community suggestions.

## Search Workflow

1. Identify the user's subsystem, error text, API name, editor operation, or symptom.
2. Search `docs/community/000_索引.md`, category files under `docs/community/lists`, and reply files under `docs/community/replies` with `rg`.
3. Read the matching post and its reply file when available. The index may contain historical `threads/...` links while this archive stores posts under category directories, so locate by numeric ID or title when a link path is absent.
4. Extract only evidence relevant to the question. Do not turn an unanswered post or anecdotal workaround into a guaranteed solution.
5. Combine the result with official documentation and project files, then state any remaining uncertainty.

## Sync Boundary

- The bundled `双击运行同步社区.cmd` is an optional maintenance helper, not a search requirement.
- Run it only when its referenced `oasis-community-mcp-skill` dependency is present and the user asks to refresh the archive.
- This installed package contains the captured archive and does not include that external sync dependency. Never claim that a sync completed from this package alone.
