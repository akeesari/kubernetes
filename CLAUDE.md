# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

A free online book, "Building Scalable Kubernetes Infrastructure for Microservices", by Anji Keesari. It is a MkDocs Material site published to GitHub Pages at https://kubernetes.anjikeesari.com. The content was written by hand, before AI assistants existed. The voice is the author's, so keep edits light and preserve it.

License: all rights reserved (see LICENSE). Do not add open-source license headers or suggest relicensing.

## Layout

- `docs/` - Markdown content, one folder per section: `foundations/`, `azure/` (Terraform labs), `kubernetes/` (AKS labs), `gettingstarted/`. Also `argocd/`, `helmchart/` and `devops/`, which are drafts currently commented out of the nav.
- `docs/<section>/images/` - screenshots referenced by relative path.
- `docs/overrides/` - theme overrides (`home.html`, `404.html`, `main.html`).
- `docs/CNAME` - custom domain. Keep it.
- `mkdocs.yml` - config and the `nav:` that decides which pages are published.
- `.github/workflows/ci.yml` - builds on PRs, runs `mkdocs gh-deploy` on push to `main`.

## Commands

```sh
pip install -r requirements.txt
mkdocs serve        # preview at http://127.0.0.1:8000
mkdocs build        # must succeed before committing
```

## Lab format

Every lab page follows `docs/gettingstarted/lab-format.md`: Introduction, Technical Scenario, Prerequisites, Objective (Task-N list), Architecture Diagram (optional), Implementation, Validation, References. Keep `## Task-N: ...` headings consistent with the Objective list.

## Conventions

- Images: `[![Alt text](images/x.png){:style="border: 1px solid black; border-radius: 10px;"}](images/x.png){:target="_blank"}`. Give new images descriptive names and real alt text.
- Admonitions use `!!! note|important|warning`; external links use `{:target="_blank"}`.
- Code fences carry a language (`sh`, `ps1`, `tf`, `yaml`).
- Page files are numbered by order (`7-log-analytics-workspace.md`). New pages must be added to `nav:` and to `docs/gettingstarted/toc.md`.

## Do not

- Commit real secrets, keys, tokens, subscription/tenant/object IDs or personal/work emails. Use `replaceme` for secrets and `00000000-0000-0000-0000-000000000000` for IDs. Screenshots may still contain real IDs: flag them rather than ignoring them.
- Rename or move files without updating `mkdocs.yml`, `toc.md` and inbound links, then check with `mkdocs build`.
- Rewrite chapters wholesale. Prefer targeted fixes: typos, outdated provider versions, deprecated settings, broken commands.
- Change the canonical URL (`docs/CNAME`, `site_url`) unless asked.

## Open work

- Verify each lab against current `azurerm` provider and AKS versions.
- Decide whether to publish the Argo CD, Helm and DevOps sections.
- Blur real IDs in screenshots.
