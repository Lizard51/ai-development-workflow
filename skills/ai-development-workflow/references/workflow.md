# Delivery workflow

Use this sequence for substantial builds. Compress or omit a phase only when it has no decision or validation value; record the reason in `STATUS.md`.

## 1. Inspect and interview

- Read project instructions, manifests, repository status, tests, and relevant existing code.
- Find environmental facts yourself.
- Use `$grilling` for user decisions and wait for confirmation of shared understanding.
- Check runtime delegation capabilities and preserve the current coordinator. Read the routing reference before interview fact-finding agents; use Luna Medium for bounded read-only lookups. After confirmation, continue the authorized build rather than asking the user to launch each phase manually.

## 2. Specify

Create `.codex/SPEC.md` from [the specification template](../assets/SPEC.template.md). Make acceptance criteria observable. Separate requirements, constraints, exclusions, assumptions, and unresolved questions.

## 3. Plan and graph tasks

Create `.codex/PLAN.md` and `.codex/TASKS.md`. Identify dependencies before parallelizing. For each task record:

- objective and relevant acceptance criteria;
- prerequisites;
- owned files or subsystem;
- assigned model and reasoning effort from [the routing policy](model-routing.md), with any actual-profile substitution disclosed;
- writable isolation mode or read-only workspace;
- validation commands and expected evidence.

## 4. Establish validation before production code

1. Run the existing suite as a baseline. If the project is empty, record that no suite exists and, after requirements confirmation, create only the minimal test/build harness needed to exercise acceptance tests before implementing target behavior.
2. Record unrelated failures without claiming they were introduced by this work.
3. Write tests for the new behavior.
4. Check expected results against the specification independently of the implementation, then run tests before implementation and verify that the new assertions fail for the intended reason.
5. Keep old green tests green and new acceptance tests immutable to implementation workers.

Tests should express behavior, not mirror private implementation details. A test that passes before the behavior exists does not establish the requested red-green contract; fix or replace it.

For concurrency and atomicity requirements, have the coordinator, preferably the recommended High profile, review the oracle, fault point, recovery outcome, and deterministic schedule. Preserve and disclose the actual profile. Do not put a mandatory two-request barrier inside a section that a correct implementation serializes.

## 5. Delegate and optionally isolate

Delegate only independent tasks. A useful delegation costs less to describe and review than to perform directly. Read-only work can run in parallel without Git. Parallel editing requires non-overlapping file ownership plus distinct writable workspaces.

Use Luna Medium for narrow verifiable tasks and Sol Medium for standard implementation and substantive tests. Keep specification, critical decisions, and integration with the coordinator. Do not create an agent for every task merely to follow the routing table; record justified escalations and fallbacks.

Git is an optional isolation mechanism, not a required phase. When the repository uses Git and the task enables Git isolation, distinct worktrees are preferred for parallel editors; a branch in the same checkout is not isolation. When Git is unavailable or not enabled, keep editing sequential unless another safe isolated workspace mechanism already exists. Do not create repositories, branches, commits, worktrees, or remote operations merely for ceremony.

Before a non-Git editing task, preserve a lightweight before-state of its owned files and frozen acceptance tests, or an equivalent versioned change record. Use before/after comparison to verify scope and test immutability; do not create Git merely to obtain a diff. Coordinator writes in a shared workspace must be serialized with worker writes.

## 6. Implement through red-green loops

Each implementation worker:

1. runs its assigned failing tests;
2. changes only its owned scope;
3. reruns tests after meaningful changes;
4. diagnoses and fixes failures without asking the user for facts available in the repository;
5. returns a concise summary, changed files, commands run, exact results, and unresolved risks.

Workers must not modify acceptance criteria or skip validation to make a task appear complete.

## 7. Review and integrate

The coordinator verifies each result independently:

- inspect the Git diff or preserved before/after comparison for scope and correctness;
- run the task validation;
- confirm acceptance tests were not weakened;
- independently verify oracle correctness and consistency of decision-relevant numbers, tables, and conclusions;
- integrate in dependency order;
- resolve conflicts deliberately rather than taking either side wholesale;
- update `.codex/STATUS.md` after verified state changes.

When telemetry is available, record actual task usage and duration in `VALIDATION.md`; otherwise mark them unknown. Raw token counts, estimated credits, elapsed time, and subscription-limit use are different measures.

## 8. Final validation

Run the relevant full suite: tests, lint, typecheck, build, and any required browser or manual checks. Review the combined diff and reconcile every acceptance criterion and task.

All Git and GitHub operations are optional. Use local repositories, branches, commits, or worktrees only when the user requests them or the existing project workflow and authorized task make them useful. Push, pull-request, merge, or deployment actions always require an explicit user request.
