# CLAUDE.md

Free online book, "Building Scalable Kubernetes Infrastructure for Microservices", by Anji Keesari. Material for MkDocs, Markdown content, deployed to GitHub Pages (https://kubernetes.anjikeesari.com) by GitHub Actions. There is no application code; "not breaking it" means the site builds and links resolve.

Written by hand, before AI assistants. The voice is the author's. License: all rights reserved (see LICENSE); never add open-source headers or suggest relicensing.

## Commands

```powershell
py -m venv .venv; .venv\Scripts\activate    # plain `python` is the Store shim on this machine
pip install -r requirements.txt
mkdocs serve                                # http://127.0.0.1:8000/
mkdocs build --strict                       # must pass before every commit; CI runs `mkdocs build`
```

- Set `NO_MKDOCS_2_WARNING=1` to silence the Material end-of-life banner.
- Never run `mkdocs gh-deploy` by hand; CI deploys on push to `main`.

## Layout

| Path | Purpose |
|---|---|
| `docs/foundations/`, `azure/`, `kubernetes/`, `gettingstarted/` | Published chapters (Terraform and AKS labs) |
| `scripts/` | `check_sensitive.py` (CI + pre-commit guard), `strip_image_metadata.py` |
| `.pre-commit-config.yaml`, `.gitleaks.toml` | Local and CI secret scanning |
| `docs/<section>/images/` | Screenshots, referenced by relative path |
| `docs/overrides/` | Theme overrides (`home.html`, `404.html`, `main.html`) |
| `docs/CNAME` | Custom domain; keep it |
| `mkdocs.yml` | Config and `nav:` |

## Lab format and conventions

- Each lab follows `docs/gettingstarted/lab-format.md`: Introduction, Technical Scenario, Prerequisites, Objective (Task-N list), Architecture Diagram (optional), Implementation, Validation, References. Keep `## Task-N:` headings consistent with the Objective list.
- Images: `[![Alt text](images/x.png){:style="border: 1px solid black; border-radius: 10px;"}](images/x.png){:target="_blank"}`. Descriptive file names, real alt text.
- Admonitions: `!!! note|important|warning`. External links: `{:target="_blank"}`. Code fences always carry a language (`sh`, `ps1`, `tf`, `yaml`).
- Files are numbered by order (`7-log-analytics-workspace.md`).

## Operating principles

- **No silent assumptions.** If scope, a requirement or an acceptance criterion is ambiguous, ask before proceeding. Never present a guess as settled. In docs, an undecided point is a `TODO:`, not an invented default.
- **Stay in scope.** Don't touch unrelated files or do adjacent cleanup nobody asked for. Prefer the smallest change that solves the problem; add no dependency, plugin or script without a demonstrated need.
- **Work through to the end.** Treat the request as a goal and continue until it's done and verified, or a real blocker stops you (an action needing the user's go-ahead such as a push or deleting something you didn't create, information only the user has, or a failure you can't fix). Then state the blocker, what you tried and what's needed. Do what's clearly part of the task, such as fixing a failure you caused or updating affected docs, without asking, and report it.
- **Verify before claiming.** Never say the site builds or a check passes unless a run in this session showed it. Show real command output rather than a summary. Run the narrowest check first.

## Workflow rules

- Personal repo: commit directly to `main`, no branches or PRs from the owner. A push to `main` deploys the live site, so run `mkdocs build --strict` first. External contributors use PRs (see CONTRIBUTING.md); CI builds them and scans for secrets (gitleaks).
- Navigation is hand-curated. A new page is invisible until added under `nav:` (and to `docs/gettingstarted/toc.md` for published chapters). Several pages are deliberately unlisted; don't add or delete them without asking.
- Don't rename or move files without updating `mkdocs.yml`, `toc.md` and inbound links, then rebuild.
- Preserve the author's voice. Fix errors, outdated commands and structure; don't rewrite style or whole chapters.
- Don't commit large binaries (PDFs, videos) or `.DS_Store`.
- Don't add external scripts to `extra_javascript` without vetting (polyfill.io was removed for supply-chain reasons). Review `docs/overrides/` HTML changes for injected scripts.
- No secrets or private data in content, config or screenshots. Use `replaceme` for secrets and `00000000-0000-0000-0000-000000000000` for subscription/tenant/object IDs. No personal or work emails.
- Run `python scripts/check_sensitive.py` before every commit (it also runs in CI). It rejects non-zero GUIDs, unexpected emails, the employer name, key/secret shapes, literal passwords and image metadata. Add `sensitive-ok` on a line only for a deliberate false positive.
- New or edited screenshots: view them and confirm no IDs, keys, public IPs, employer or personal names, or profile photos are visible. Cover with opaque black boxes, then run `python scripts/strip_image_metadata.py`. Images stay in git history forever, so check before committing.
- Unpublished draft chapters (Azure DevOps, Argo CD, Helm) are deliberately NOT in this repo: they had unredacted screenshots. A copy is at `C:\Source\Repos\kubernetes-drafts` (local, outside git). Sanitize their screenshots before bringing any back.

## Keeping docs in sync

When behavior, structure or tooling changes, update every affected document in the same task and list them in the reply:

- `README.md` when usage, prerequisites or structure change.
- `CONTRIBUTING.md` when contributor rules or CI change.
- This file when layout, standards or workflow rules change.

## Commits

- One logical change per commit. Stage by path (`git add <paths>`), never `git add -A`. Never commit `.env` or other gitignored files.
- Message: `type: summary` (`feat`, `fix`, `docs`, `chore`, `ci`, ...), imperative, under about 70 characters, with a body when the why isn't obvious.
- Commit once the work is done and `mkdocs build --strict` passes. Push only when asked.

## Working alongside other sessions

Treat uncommitted changes you didn't make as another session's work. Don't revert or overwrite them, build on them when editing the same file, and ask before editing around something that looks unfinished.

## Writing style for docs

Applies to README, CONTRIBUTING, this file and commit messages (not to the book chapters, whose voice is preserved): condensed, each thing said once, tables and bullets over prose, current facts rather than edit history.

## Next steps

End every development response with a **Next steps** list of 2-4 numbered options that need the user's go-ahead, grounded in a real remaining gap (see Known gaps). Mark one **(Recommended)** and list it first. If nothing needs the user, say so in one line.

## Known gaps

- Remaining screenshots still show public IPs (5 azure, 8 kubernetes images), the author's name as the subscription display name and tags (~60 images), and the author's profile photo in some browser toolbars. Re-scan before relying on this.
- Labs not yet verified against current `azurerm` (pins range from `~>2.0` to `~>3.69`; current is 4.x) and AKS versions.
- Argo CD, Helm and DevOps chapters unpublished and outside the repo until their screenshots are sanitized.
- Link check runs weekly only (`checks.yml`); fix reported dead links.
- `requirements.txt` is a version range, not pinned.
- Material for MkDocs reaches end of life on 2027-05-05; a Zensical migration will be needed eventually.
