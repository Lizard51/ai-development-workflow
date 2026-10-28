# Package validation

The repository checks the distribution, not a generated application.

## Run locally

Python 3.9 or newer:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
git diff --check
```

GitHub Actions runs the same package validator on Linux and Windows with Python 3.11. Dependencies are needed only for repository maintenance; using the skills does not require Python or pip.

## Checked

- YAML frontmatter, skill names, descriptions, and UI metadata.
- Required workflow references, all five templates, and bundled dependency files/licenses.
- Relative Markdown links and fragment targets outside fenced code examples.
- UTF-8 readability, private workstation path patterns, and common credential patterns.

These scans are bounded checks, not a comprehensive security audit. Review changes before publishing.

## Not established by these checks

- Whether a model follows every instruction in a real conversation.
- Availability of named models, delegation, or particular tools in another account.
- Product correctness, browser acceptance, packaged installation, or deployment.
- Comparative quality, latency, token consumption, or subscription savings.

The initial public package is based on an existing local skill snapshot. No new end-to-end application build or clean-machine Codex installation was performed as part of packaging. Bundled supporting skills are local snapshots rather than a promise to track upstream `main`.
