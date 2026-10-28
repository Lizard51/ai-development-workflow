---
name: ai-development-workflow
description: Turn a substantial software idea or complex feature into a specified, test-first, delegation-capable implementation. Use for end-to-end builds with planning, validation, selective agents, and integration; do not use for small edits, explanation-only, diagnosis-only, or review-only requests.
---

# AI Development Workflow

Apply an adaptive, test-first delivery workflow. Preserve the user's requested product and authorization boundaries; this skill does not authorize publishing, pushing, opening pull requests, merging, deploying, or other external writes.

## Execution profile

The recommended coordinator is `gpt-6.1-sol` with `high` reasoning, selected by the user before starting. Keep the current coordinator model; a skill does not change the chat's model or enable unavailable tools.

Use `gpt-6-luna` / `medium` for narrow, independently checkable work and `gpt-6.1-sol` / `medium` for substantial implementation, tests, and analysis. Keep critical decisions and final acceptance with the coordinator; use a separate Sol High reviewer only when independent review is worth its overhead. Read [references/model-routing.md](references/model-routing.md) before the first delegation, including read-only interview fact-finding.

Check that the runtime exposes delegation and model/effort selection. Select both explicitly rather than letting workers inherit the coordinator's High profile. If those capabilities or a requested model are unavailable, disclose the limitation and use the routing reference's fallback; do not pretend that differentiated agents ran or modify global settings automatically.

## Start with discovery

1. Inspect the repository and existing project instructions for facts that can be learned without asking the user.
2. Load and follow `$grilling` for unresolved product and design decisions. This skill explicitly requires the interview for a new product, a large feature, or materially ambiguous work.
3. Do not implement during the interview. Continue until the decision frontier is empty and the user confirms shared understanding.
4. For a mature domain with ambiguous terminology or consequential architectural trade-offs, also load `$domain-modeling`; otherwise keep domain glossary and ADR work out of the critical path.

During the `$grilling` interview, its environmental fact-finding rule takes priority over the later delegation cost heuristic: if a frontier decision needs a repository fact that was not found during initial inspection, use a Luna Medium read-only subagent and continue with the rest of the available frontier. Interview lookups also obey the routing reference's capability/profile fallback: if delegation or the requested profile cannot be selected, disclose the limitation and inspect directly or use a justified supported profile. Outside the interview, apply the normal delegation threshold below.

After the user confirms shared understanding, continue through the authorized build without requesting approval for each routine phase. Ask again only for unresolved decisions, material scope changes, missing permissions, or external actions. On resumed work, reuse confirmed decisions and project artifacts; reopen the interview only for newly ambiguous requirements.

## Establish the contract

Read [references/workflow.md](references/workflow.md) before executing the build.

Create the relevant project-local artifacts under `.codex/` from the templates in `assets/`:

- `SPEC.md`: required behavior, constraints, exclusions, and acceptance criteria.
- `PLAN.md`: architecture, sequence, risks, and affected areas.
- `TASKS.md`: dependency graph, ownership, model assignment, optional isolation, and validation per task.
- `STATUS.md`: current phase, completed work, blockers, and verified commands.
- `VALIDATION.md`: baseline, new failing tests, final commands, and evidence.

Keep these files concise and update them when decisions or verified state change. Do not replace repository-native documentation that already serves the same purpose.

## Require tests before implementation

Before changing production code for new behavior:

1. Discover the project's real test, lint, typecheck, and build commands.
2. Run the existing validation baseline and record pre-existing failures separately. For an empty project, record that no suite exists and bootstrap only the minimal test/build harness after requirements confirmation; do not implement the target behavior during setup.
3. Add executable tests for the new acceptance criteria where feasible.
4. Independently check test expectations against the specification, then run the new tests and confirm that they fail for the expected missing behavior, not because the test or its expected result is broken.
5. Freeze the agreed acceptance tests. Implementation workers may not weaken, delete, skip, or rewrite them merely to obtain a green result.

When an executable automated test is genuinely unsuitable, define the strongest repeatable alternative before implementation, such as a build assertion, browser flow, screenshot comparison, or explicit manual verification. Document the reason instead of creating a meaningless test.

## Delegate selectively

This skill explicitly authorizes subagents when independent workstreams would materially improve speed or quality. Read [references/model-routing.md](references/model-routing.md) before spawning them.

- Keep dependent, tiny, or tightly coupled work with the coordinator.
- Use at most three active workers and never exceed the runtime's available worker capacity. Wider parallelism requires both an explicit user request and runtime support.
- Assign the lightest profile that meets the task's reasoning and verification needs, with an explicit model and reasoning effort. Do not force difficult work through Luna first or treat fewer raw tokens as proof of lower cost.
- Give each worker a bounded task, necessary context, permitted files, immutable tests, validation commands, and a required result format.
- Parallel editing workers must have non-overlapping ownership and isolated writable workspaces. Git is optional: use distinct Git worktrees only when the repository uses Git and Git isolation is enabled for the task. Without safe isolation, keep code editing sequential; serialize coordinator edits with worker edits in the same workspace. Read-only workers may still run in parallel.
- Never let multiple workers edit the same checkout or the same files concurrently.
- Escalate a failed task only after reviewing the evidence: Luna Medium to Sol Medium, then to the coordinator / Sol High. Terra is an optional disclosed fallback, not a required stage.

## Integrate and verify

Treat worker claims as untrusted until verified. The coordinator must inspect each change using a Git diff or a preserved before/after file comparison, run the assigned checks, reject scope drift or weakened tests, and integrate in dependency order. Verify test oracles as well as code: a failing assertion may have an incorrect expectation. Recompute decision-relevant numbers and ensure tables and conclusions agree. For concurrency tests, check that the synchronization cannot deadlock a correct implementation. After integration, run the complete relevant validation suite and compare the result with `SPEC.md`, `PLAN.md`, and unfinished tasks.

Report:

- what was implemented;
- which checks ran and their exact outcomes;
- any pre-existing failures or unverified areas;
- remaining work or deviations from the specification.

Do not call the work complete while checks for the requested or affected behavior are failing or required evidence is missing. A verified pre-existing failure outside the task scope may remain only when it is unchanged, clearly disclosed, and does not prevent validating the requested work.
