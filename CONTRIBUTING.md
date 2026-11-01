# Contributing

Thanks for helping improve this book.

## Reporting problems

Open a GitHub issue with:

- the page or chapter,
- what you expected and what happened,
- tool versions (Terraform, azurerm provider, Azure CLI, kubectl) and any error output, with secrets removed.

## Pull requests

Small fixes (typos, broken links, outdated commands) are welcome. For anything larger, open an issue first so we can agree on the change.

By submitting a pull request you confirm that you wrote the change and grant the author (Anji Keesari) a perpetual, irrevocable right to use, modify and publish it as part of this book. The repository itself stays under the [LICENSE](LICENSE) (all rights reserved).

## Rules for content

- Never commit real passwords, keys, tokens, subscription or tenant IDs, or personal emails. Use `replaceme` for secrets and `00000000-0000-0000-0000-000000000000` for IDs. Blur them in screenshots.
- Screenshots: before capturing, use a clean browser profile (no personal photo or extensions) and fake or throwaway resources. Before committing, cover with opaque black boxes (never blur or pixelate): subscription, tenant, client and object IDs, keys, passwords, SAS tokens, connection strings, public IPs, personal and employer names, and email addresses. Then run `python scripts/strip_image_metadata.py`.
- Run the checks before every commit: `python scripts/check_sensitive.py`. To run them automatically, `pip install pre-commit && pre-commit install`. CI runs the same checks plus gitleaks and fails the PR on a hit.
- Follow the [lab format](docs/gettingstarted/lab-format.md).
- Add new pages to the `nav:` section of `mkdocs.yml`.
- Preview locally with `mkdocs serve` before opening a PR.
