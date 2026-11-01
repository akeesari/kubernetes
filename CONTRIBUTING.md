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
- Follow the [lab format](docs/gettingstarted/lab-format.md).
- Add new pages to the `nav:` section of `mkdocs.yml`.
- Preview locally with `mkdocs serve` before opening a PR.
