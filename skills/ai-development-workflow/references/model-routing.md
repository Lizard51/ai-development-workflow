# Model routing and agent contracts

## Choose the profile

| Profile | Task |
| --- | --- |
| `gpt-6-luna` / `medium` | Read-only fact-finding, fixtures, mechanical edits, and small functions with independent checks |
| `gpt-6.1-terra` / `medium` | Ordinary bounded implementation and debugging with a clear contract, including implementing checks whose expectations are settled |
| `gpt-6.2-sol` / `medium` | Difficult bounded implementation, substantive numerical analysis, or non-trivial test design |
| Coordinator, preferably `gpt-6.2-sol` / `high` | Requirements, architecture, consequential security or concurrency decisions, and acceptance. Use a separate Sol High reviewer when independent review justifies the overhead. |

Assign Sol Medium directly when reasoning or verification requires it. Start with the lightest profile suited to the task and choose one per assignment.

## Assign and isolate

Check whether the host supports delegation, explicit model and effort, context forks, and available worker slots. Set both model and effort explicitly where supported. For the collaboration tool, use `fork_turns: "none"` with overrides if supported and pass the needed context. Respect the actual schema and avoid full-history forks with overrides. Verify the applied profile when metadata is available.

If Terra is unavailable for ordinary implementation, use a supported Sol Medium profile where appropriate. If Luna is unavailable for a quick lookup or assignment, prefer direct work or a justified supported worker. If differentiated profiles are unavailable, keep the task with the coordinator or justify a supported worker. Disclose and record substitutions and limitations in the task record. Keep the chat's selected model and global settings intact.

- Use at most three active workers within host limits by default. Wider parallelism requires explicit user authorization and host support.
- Delegate independent tasks. Parallel editors need non-overlapping ownership and separate writable workspaces. If using Git for isolation, use distinct worktrees. Where safe isolation is unavailable, serialize edits by workers and coordinator. Read-only workers can still run in parallel.
- Give each worker a concrete deliverable, necessary context, workspace and rights, owned files, relevant requirements and frozen tests, commands to validate, and the expected report. Keep context bounded to the task and link relevant material.

## Review failures and escalate

The coordinator reviews the change, reproducible checks, and the specification. Distinguish implementation defects from incorrect test expectations, environment failures, missing permissions, and unresolved decisions. Resolve the actual cause before changing profiles.

- Move work beyond Luna's remit to Terra when bounded, or directly to Sol Medium when reasoning and verification warrant it.
- Allow at most one bounded Terra correction for a simple local defect. Hand off persistent or substantive defects to Sol Medium. The coordinator can finish a tiny correction directly.
- Bring in the coordinator immediately for critical judgment or architecture changes, or after two failed scoped attempts with Sol Medium.

Stop the previous editor before transferring ownership. Pass the current changes, reproducible evidence, and relevant contract. Record assignments, attempts, and escalation reasons in the existing task record.

Bring proposals that change architecture, the agreed contract, or observable behavior to the coordinator before proceeding.

## Measure the whole task

Include briefing, execution, correction, review, and integration when judging delegation costs. Record observed model and effort, time, input and output counts, and cached input and reasoning subsets in the existing validation record. Keep interrupted runs separate and mark unobservable values unknown. Avoid double counting subsets or estimating hidden usage from time or answer length. Distinguish observed tokens, estimated costs, and subscription limits. Account for differences in context, cache, and speed mode when comparing.
