# Agents Guide for `ganesh47.github.io`

This repository powers Ganesh Raman's public blog using GitHub Pages and the Minimal Mistakes Jekyll theme. Use this guide as the control room for any agents automating content, configuration, or maintenance work in the project.

## 1. Mission Overview
- **Tech stack**: Jekyll (remote theme `mmistakes/minimal-mistakes`) served via GitHub Pages.
- **Primary goal**: Publish long-form posts on distributed systems, data engineering, and related topics (2015–2019 archive currently tracked).
- **Site features**: Pagination, category/tag/year archives, estimated read time, sharing controls, and Giscus-powered comments.
- **Key dependencies**: `github-pages` gem bundle plus explicit plugins (`jekyll-paginate`, `jekyll-sitemap`, `jekyll-gist`, `jekyll-feed`, `jemoji`, `jekyll-include-cache`, `jekyll-algolia`).

## 2. Repository Map
- `_config.yml`: Central site configuration (metadata, plugin list, pagination, defaults for posts/pages, comment provider settings).
- `_posts/`: Markdown posts named `YYYY-MM-DD-title.md` with front matter fields (`title`, `date`, `categories`, `tags`, optional `author`). Content uses standard Markdown with Minimal Mistakes shortcodes and supports code fences.
- `_pages/`: Custom pages for 404, archives (`/posts/`, `/tags/`, `/categories/`). Each page uses `layout: single`, `layout: posts`, or built-in archive layouts.
- `_data/navigation.yml`: Defines the top navigation links. Update this file to expose new pages.
- `_includes/giscus.html`: Injects the Giscus widget. Adjust attributes here to change comment behavior.
- `assets/images/`: Houses author avatar (`bio-photo.jpg`) and any static imagery referenced in posts/pages.
- `index.html`: Empty content file referencing the theme’s `home` layout and enabling the author profile on the landing page.
- `Gemfile`: Declares Ruby dependencies; Bundler manages the lockfile on the user’s machine (not checked in).

## 3. Local Development Workflow
1. Install Ruby (>= 2.7 recommended) and Bundler.
2. From the repo root run `bundle install` to resolve gems (GitHub Pages bundle will pin compatible versions).
3. Serve locally with `bundle exec jekyll serve` (add `--livereload` if desired). The site will be available at `http://localhost:4000`.
4. Use `bundle exec jekyll build` for production builds; artifacts generate under `_site/` (ignored by default).

## 4. Content Operations
- **New Post**:
  1. Create `_posts/YYYY-MM-DD-descriptive-title.md`.
  2. Include front matter: `title`, ISO8601 `date`, `categories` (array, e.g. `blog`), `tags` list, optional `excerpt`.
  3. Write Markdown content; Minimal Mistakes supports `{: .something }` classes, callouts, and `toc: true` if desired.
  4. Preview locally, validate links, then commit.
- **New Static Page**: Drop a Markdown file in `_pages/` with appropriate `layout` (`single`, `page`, or archive). Add the page to `_data/navigation.yml` if it should surface in the menu.
- **Images/Assets**: Store under `assets/images`. Reference via `/assets/images/<file>` in Markdown.
- **Comments**: Giscus uses `data-mapping="url"`; ensure published URLs are stable when renaming or moving posts.

## 5. Configuration Touchpoints
- **Site metadata**: Update title/description/author information in `_config.yml`.
- **Pagination**: `paginate: 5` controls posts-on-home; adjust `paginate_path` as needed.
- **Search**: `search: true` is enabled; `jekyll-algolia` is available if Algolia crawler credentials are configured.
- **Theme skin**: `minimal_mistakes_skin: default`; switch skins via `_config.yml` or override SCSS in assets if added later.
- **Author profile**: Defaults are set to show the profile block on posts and pages (`author_profile: true`).
- **Footer/links**: Maintained within `_config.yml` and `_data/navigation.yml`.

## 6. Observations & Follow-Up Tasks
- The post file `2017-02-10-Understanding Linux cgroups: The Foundation of Resource Isolation in LXC" date: 2017-02-10 author: Ganesh Raman tags: [linux, containers, lxc, cgroups, system internals, kernel, process-isolation] categories.md` has an embedded front-matter fragment in the filename. Rename to a clean `YYYY-MM-DD-title.md` and move the metadata into the front matter to avoid build issues.
- Consider checking in a `Gemfile.lock` to lock plugin versions for deterministic local builds (optional for GitHub Pages but helpful for agents).
- No CI workflows are present. If automated builds or link checks are desired, integrate GitHub Actions (`jekyll build`, `htmlproofer`, etc.).
- `_config.yml` sets both `remote_theme` and `theme`; ensure no conflict when upgrading (GitHub Pages will prioritize `remote_theme`).

## 7. Agent Playbook
- **Generate content**: Draft new technical posts, ensuring metadata accuracy and internal links between related articles.
- **Refine archives**: Extend `_pages/` with topic-specific landing pages or update navigation to highlight new series.
- **Maintain comments/search**: Update Giscus IDs or Algolia credentials if repository ownership changes.
- **Quality passes**: Run `bundle exec jekyll doctor` or `bundle exec jekyll build` before merging to spot configuration or Markdown errors.

Treat this document as the canonical briefing—update it whenever new features, workflows, or automation hooks are introduced.
