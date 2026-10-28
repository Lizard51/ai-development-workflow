# AI Development Workflow

**From an idea to a verified result.** A Codex skill that connects requirements discovery, planning, tests, implementation, and acceptance.

[Русский](README.md) · [Installation](docs/installation.md) · [Examples](docs/examples.md) · [Workflow reference](skills/ai-development-workflow/references/workflow.md)

[![Validate](https://github.com/Lizard51/ai-development-workflow/actions/workflows/validate.yml/badge.svg)](https://github.com/Lizard51/ai-development-workflow/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

```text
Discover → Specify → Plan → Verify failing acceptance tests
                                      ↓
               Verify ← Integrate ← Implement
```

## What it does

- Inspects the project and interviews you about unresolved decisions before implementation.
- Records the contract in five short files under `.codex/`: `SPEC.md`, `PLAN.md`, `TASKS.md`, `STATUS.md`, and `VALIDATION.md`.
- Requires new tests to fail for the expected reason before implementing new behavior, with independently reviewed expectations.
- Delegates only useful independent work, with explicit model profiles and isolated parallel edits.
- Makes the coordinator inspect changes, rerun checks, and reconcile acceptance criteria.
- Keeps Git optional and preserves explicit authorization for external writes.

Use it for a substantial new application or complex feature. Small edits, explanations, diagnosis, and standalone reviews usually do not need the full workflow.

## Quick start

Ask Codex:

```text
$skill-installer Install skills/ai-development-workflow, skills/grilling,
and skills/domain-modeling from Lizard51/ai-development-workflow.
```

Then start a task:

```text
$ai-development-workflow
Build an order tracker for a small workshop. Inspect the existing project,
clarify the requirements with me, then implement and verify the agreed scope.
```

If the skills do not appear, restart Codex. See [manual and project-local installation](docs/installation.md).

## Included skills

| Skill | Role | Author |
| --- | --- | --- |
| [`ai-development-workflow`](skills/ai-development-workflow/SKILL.md) | Delivery process, routing policy, document templates | Lizard51 |
| [`grilling`](skills/grilling/SKILL.md) | Required requirements interview | Matt Pocock |
| [`domain-modeling`](skills/domain-modeling/SKILL.md) | Conditional domain glossary and ADR guidance | Matt Pocock |

## Runtime requirements

The bundled routing recommends `gpt-6.1-sol` / `high` as coordinator, `gpt-6-luna` / `medium` for narrow work, and `gpt-6.1-sol` / `medium` for substantive implementation. These are skill preferences, not availability guarantees. The current coordinator is preserved. Unsupported profiles or delegation capabilities must be disclosed; coordinator-only work is a supported fallback. See [model routing](skills/ai-development-workflow/references/model-routing.md).

This is an instruction bundle. It does not provide an agent runtime, unlock tools, change global settings, or guarantee quality or cost savings. Package checks do not prove end-to-end delivery behavior. See [validation scope](docs/validation.md).

## Contributing and license

[Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md) · [Issues](https://github.com/Lizard51/ai-development-workflow/issues/new/choose)

[MIT](LICENSE). Bundled Matt Pocock skills retain their own copyright and MIT notices; see [third-party notices](THIRD_PARTY_NOTICES.md). This is an independent community project, not an official OpenAI product.
