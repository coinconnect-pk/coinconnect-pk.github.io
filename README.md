# CoinConnect Intelligence

Complete, primary-source analysis of Pakistan's virtual asset regulatory framework.

Live at **https://blog.coinconnect.site**

A standalone Jekyll site on GitHub Pages. The main CoinConnect site stays on Odoo at coinconnect.site and is not touched by anything here.

The writing brief lives in `CONTENT-PROMPT.md`.

## What is here

| Path | What it is |
|---|---|
| `index.html` | Homepage and article listing |
| `topics.md` | Articles grouped by category |
| `about.md` `editorial-policy.md` `privacy.md` | Static pages |
| `_posts/` | Published articles |
| `_queue/` | Finished articles waiting their turn — see `_queue/README.md` |
| `overrides/` | Publish your own article on any day — see `overrides/README.md` |
| `_data/published-log.csv` | Running record of what published, when, from where |
| `_layouts/` `_includes/` | Templates |
| `assets/css/style.css` | All styling |
| `.github/workflows/auto-publish.yml` | 06:00 and 18:00 PKT jobs |
| `.github/scripts/publish.py` | The publisher |

## How publishing works

**This is a queue publisher, not a generator.** Nothing here calls a model API.

Articles are written in advance in batched sessions, committed into `_queue/`, and released **two per day** via two runs — 06:00 and 18:00 PKT. Each run:

1. Stops if today's limit of two has been reached.
2. Checks `overrides/<today>/article.md` for a manual article not already used today. **Present** → publishes it and **leaves the queue untouched**, so the queued article keeps its place.
3. **No manual article** → takes the lowest-numbered file from `_queue/`, validates it, stamps today's date, publishes it, and removes it from the queue.

The queue never loses a slot.

Publish on demand from **Actions → Publish article → Run workflow**, with a `dry_run` option that validates without publishing and a `force` option that publishes past the daily limit.

## Content rules

Enforced by `publish.py`. An article that breaks any of these will not publish, and the Actions log names the rule.

- 1200–2100 words
- At least four `##` headings
- Must end with `## About this analysis`
- Title under 75 characters; description 120–165 characters
- Category is one of: `Licensing`, `Compliance`, `Tax & Banking`, `Corporate Setup`, `Sandbox`, `Enforcement`, `Market Entry`
- At most one link to coinconnect.site
- Outbound links restricted to an allowlist of official and primary sources
- Author byline: Malik Abbas

### Source discipline

Every specific in an article — section number, threshold, deadline, defined term, penalty —
must trace to a published primary source named in the text. Nothing is reconstructed from
memory. Where general knowledge conflicts with the published document, the document governs.

Statement of a provision is fact; its cost, difficulty or likely application is analysis,
and the two are always separated in the text.

Outbound links are restricted by an allowlist in `publish.py` to regulators, legislation
and official statistics.

## Setup checklist

- [ ] Repository created under the CoinConnect GitHub account, **public**
- [ ] Settings → Pages → source `main` / root
- [ ] Settings → Pages → Custom domain → `blog.coinconnect.site`, then **Enforce HTTPS** once the certificate issues
- [ ] Settings → Actions → General → Workflow permissions → **Read and write**
- [ ] DNS: one `CNAME` record only — `blog` → `<account>.github.io`
- [ ] Google Search Console verified, code pasted into `google_site_verification` in `_config.yml`
- [ ] Sitemap `https://blog.coinconnect.site/sitemap.xml` submitted to Search Console
- [ ] `about.md` biography filled in
- [ ] `_config.yml` → `author.linkedin` filled in

## Local preview

Requires Ruby.

```bash
bundle install
bundle exec jekyll serve
```
