# Contributing

Issues and pull requests are welcome in Russian or English.

For a workflow change, explain the concrete request that currently fails, the observed behavior, and what should happen instead. Remove private project data and credentials from examples.

Keep the main entrypoint focused. Put conditional detail in references and reusable output files in assets. Preserve user scope, optional Git, explicit authorization for external actions, capability fallbacks, and independent verification of worker results.

Before opening a pull request:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
git diff --check
```

For behavior changes, include a realistic anonymized before/after example and describe what was actually tested. A package check is not evidence that an agent followed the workflow. Do not add quality or savings claims without reproducible measurements.

Update the relevant documentation and `CHANGELOG.md`. Treat the bundled Matt Pocock skills as third-party snapshots: keep their notices, document modifications, and explain any upstream refresh separately from workflow changes.
