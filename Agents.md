# Agent guide

This is Ganesh Raman’s public Jekyll blog. Read README.md for the exact build and checks. Ruby, the Minimal Mistakes theme, gems and Node packages are pinned. Keep the primary checkout and unrelated repositories intact; do substantial work in an isolated worktree.

- Preserve article prose, original publication dates, corrected content, URLs and full-URL Giscus associations. The unusual historical cgroups filename is part of a published URL: do not rename it as cleanup.
- Categories are URL-bearing. Keep `blog` and `/:categories/:title/`; topics and series belong in `_data/discovery.json` and `_data/series.json`.
- Add new articles to discovery metadata and the tag directory. Keep legacy tag fragments as aliases when normalizing labels.
- Use focused local theme overrides. Keep a readable article measure, native no-JavaScript navigation/contents, visible focus, horizontal table/code regions and meaningful search snippets. Pagefind is the only active article search engine.
- Keep project tools on their existing URLs. Research descriptions and dates must come from verified project evidence.
- Run `bundle exec jekyll build`, `pnpm index`, `pnpm check` and `pnpm test`. Review screenshots as well as automated results. Existing baseline fixtures may be updated only for an intentional content or routing change; do not weaken them to pass a presentation regression.
- PR previews are downloadable artifacts. Never deploy unreviewed PRs to production. The master workflow publishes to the existing public GitHub Pages destination; verify its exact revision after deployment.
- Keep plans, private evidence, credentials, generated caches and local runtime paths out of commits and published output. Maintenance docs/tests remain technical repository files and are excluded by `_config.yml`.

No extra `.agents/skills` exist in the current source. Comments use the existing local Giscus include once; do not add a second theme embed or change mappings without reading the public discussion associations.
