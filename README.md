# Ganesh Raman’s notebook

Jekyll 4.4.1 and a pinned Minimal Mistakes revision publish to <https://ganesh47.github.io/> through the existing master GitHub Pages workflow.

Use Ruby 3.3.11, Node 24.14.0 and pnpm 12.8.1. `Gemfile.lock` and `pnpm-lock.yaml` are checked in.

```sh
bundle install
pnpm install --frozen-lockfile
JEKYLL_ENV=production bundle exec jekyll build
pnpm index
pnpm check
pnpm exec playwright install chromium
pnpm test
python3 -m http.server 4315 --directory _site
```

The `index` step builds one Pagefind index from article bodies. It excludes navigation, comments and repeated series maps. Search queries and topic filters are reflected in the URL; browser back/forward restores them. Reading, the menu, contents and archive links work without JavaScript. Search has a browsing fallback.

`_data/discovery.json` assigns topics independently of categories. `_data/series.json` holds ordered reading paths; `_data/tags.json` consolidates display labels and preserves old fragment aliases. New posts need discovery metadata and relevant tag/series entries. Preserve `categories: [blog]`, existing permalinks and the `/:categories/:title/` scheme. Existing article files and category/tag/archive/pagination routes are protected by the deployed baseline fixture.

Presentation overrides live in `_layouts/`, `_includes/` and `assets/`. The article layout demotes body h1 elements to h2 at render time, preserving text and IDs. The original `_includes/giscus.html` supplies one full-URL-mapped embed with the existing repository/category IDs. There were no public discussion threads at the 3 October 2026 migration check.

Pull requests run a locked build, route/canonical/feed/sitemap/prose/link checks, Chromium layouts at 320/390/768/1280 pixels, axe checks, search/history, keyboard, reduced-motion and no-JavaScript reading tests. A 640 CSS-pixel viewport tests reflow equivalent to a 1280px viewport at 200% zoom. This is not a complete assistive-technology or cross-browser conformance audit. CI retains downloadable site and browser artifacts; it does not deploy PRs to production.

Production uses only `.github/workflows/jekyll.yml` on master, with Pages configured to GitHub Actions. `_site/build-revision.json` identifies the exact source and theme revisions. Planning, credentials, test fixtures and maintenance files are excluded from the public site. Before publishing, compare the candidate SHA, checks and screenshots; after deployment, verify the revision marker and representative live routes. Revert the merged presentation change for rollback; keep the prior content release `630945dc98e599ffbd02b62b714b3ea74c3a1cbc` available.
