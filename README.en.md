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
- Starts a new substantial project with separate `SPEC.md`, `PLAN.md`, `TASKS.md`, `STATUS.md`, and `VALIDATION.md` files before implementation. Small scoped work can combine roles; existing projects retain their established structure. Each role has a [template](skills/ai-development-workflow/assets/).
- During ongoing work, updates established documents in place, keeps detailed requirements in one authoritative section, and avoids duplicate plans, handoffs, and iteration reports. See [documentation maintenance](skills/ai-development-workflow/references/documentation.md).
- Requires new tests to fail for the expected reason before implementing new behavior, with independently reviewed expectations.
- Delegates only useful independent work, with explicit model profiles and isolated parallel edits.
- Makes the coordinator inspect changes, rerun checks, and reconcile acceptance criteria.
- Keeps Git optional and preserves explicit authorization for external writes.

Use it for a substantial new application or complex feature. Small edits, explanations, diagnosis, and standalone reviews usually do not need the full workflow.

## Quick start

Ask Codex:

```text
$skill-installer Install skills/ai-development-workflow, skills/grilling,
and skills/domain-modeling from Lizard51/ai-development-workflow at tag v1.3.1.
```

Select GPT-6.1 Sol with High reasoning for coordination if available, then start a task:

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

Current release: [v1.3.1](https://github.com/Lizard51/ai-development-workflow/releases/tag/v1.3.1). [All releases](https://github.com/Lizard51/ai-development-workflow/releases).

Version 1.3.1 restores Sol 6.1 profiles and starts new substantial projects with five separate documents. Terra Medium and evidence-based escalation remain available. See the [changelog](CHANGELOG.md#131--2026-11-28).

## Model profiles and runtime requirements

| Model | Effort | When to choose it |
| --- | --- | --- |
| GPT-6.1 Sol | High | Coordination, architecture decisions, and final acceptance |
| GPT-6 Luna | Medium | Fact-finding and small edits with straightforward checks |
| GPT-6.1 Terra | Medium | Routine implementation with clear requirements and independent checks |
| GPT-6.1 Sol | Medium | Difficult implementation, test design, and escalation |

The coordinator can assign difficult work directly to Sol Medium. When Terra's work fails a check, the coordinator diagnoses the cause first. A local defect can get one bounded correction. A substantial or recurring defect can go to Sol Medium with the existing changes and check results.

Codex keeps the model selected for the chat. Subagent profiles depend on what the host supports. If a requested profile is unavailable, the coordinator discloses the substitute or works directly. See [the full routing policy](skills/ai-development-workflow/references/model-routing.md).

This is an instruction bundle. It does not provide an agent runtime, unlock tools, change global settings, or guarantee quality or cost savings. Package checks do not prove end-to-end delivery behavior. See [validation scope](docs/validation.md).

## Contributing and license

[Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md) · [Issues](https://github.com/Lizard51/ai-development-workflow/issues/new/choose)

[MIT](LICENSE). Bundled Matt Pocock skills retain their own copyright and MIT notices; see [third-party notices](THIRD_PARTY_NOTICES.md). This is an independent community project, not an official OpenAI product.
