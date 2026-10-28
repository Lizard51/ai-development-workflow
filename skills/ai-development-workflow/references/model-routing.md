# Model routing and agent contracts

Choose by required reasoning depth, risk, and verifiability, not by role name alone. This policy favors selective routing. It does not establish universal quality, speed, token, or subscription-savings guarantees. Use models actually exposed by the current runtime.

## Default routing

| Task class | Default model | Effort | Typical work |
| --- | --- | --- | --- |
| Reconnaissance | `gpt-6-luna` | medium | Locate files, collect facts, summarize bounded code with references |
| Mechanical / narrow code | `gpt-6-luna` | medium | Repetitive edits, fixtures, small functions with clear independent checks |
| Standard | `gpt-6.1-sol` | medium | Substantial isolated implementation, test design, ordinary debugging, numerical analysis |
| Difficult but bounded | `gpt-6.1-sol` | medium initially | Cross-file logic or non-trivial refactors with explicit contracts and meaningful validation; escalate on demonstrated need |
| Critical | coordinator; separate `gpt-6.1-sol` reviewer only if justified | high when the coordinator was selected as recommended | Architecture, concurrency/atomicity, authorization/security decisions, integration and final acceptance |

The recommended coordinator is `gpt-6.1-sol` / `high`. Keep the user-selected coordinator unchanged. Keep the interview, specification ownership, task graph, conflict resolution, and final acceptance with it. Critical work can go directly to this tier; escalation is not a mandatory sequence for every task. A separate Sol High worker is not needed for a review the coordinator can perform independently.

## Runtime capability and fallback

Before the first spawn, inspect the available tool contract for model selection, reasoning settings, context forks, and capacity. Use explicit model/effort fields when supported. Custom-agent configuration can override requested settings, so verify the applied profile when metadata is available and record requested versus actual settings when they differ.

If a requested model is unavailable, disclose and record a suitable available substitution in `TASKS.md`. `gpt-5.6-terra` / `medium` may be used as an optional middle-tier fallback, not as the default or a mandatory escalation step. If heterogeneous model selection is unavailable, keep the work with the coordinator or use a disclosed supported agent profile when independent work still justifies it. Never silently spawn all workers on High, claim a profile was applied without support, or change global configuration to make the policy work.

## Spawn contract

When the collaboration tool supports these fields, pass `model` and `reasoning_effort` explicitly: `gpt-6-luna` / `medium`, `gpt-6.1-sol` / `medium`, or justified `gpt-6.1-sol` / `high`. A model/effort override requires a bounded context fork with the current collaboration tool; use `fork_turns: "none"` when that value is supported, and put all required context in the task message. Do not use a full-history fork while requesting an override. Adapt field names to the actual runtime rather than inventing unsupported arguments.

Every task message must include:

- one objective and a concrete deliverable;
- repository or workspace path, isolation mode, and whether writes are allowed;
- owned files or subsystem and forbidden overlap;
- relevant requirements and immutable acceptance tests;
- validation commands;
- expected report: concise summary, files changed, commands, results, and risks; include actual usage only when observable.

## Verification by risk

- Luna results must be independently checkable. Recompute numbers that drive decisions; a correction in prose does not repair an inconsistent final table.
- Validate test expectations independently of the implementation under test, using a small worked example, specification-derived assertion, or simple reference oracle. Passing worker-authored tests alone is not acceptance evidence.
- Numerical analysis and non-trivial acceptance-test design start at Sol Medium. The coordinator verifies the final artifact, not only the explanation.
- For concurrency/atomicity, involve the coordinator, preferably the recommended High profile, in test design before freezing tests. Preserve and disclose the actual profile rather than silently changing it; if a required review capability is unavailable, report the limitation. Synchronization must allow a correct lock to block the second request; do not require both requests to reach a barrier inside one mutually exclusive section. Define the fault point, recovery completion, and allowed outcome from the agreed contract so that an overly broad assertion cannot mask failure.

## Escalation

Do not escalate merely because the worker asks, a check fails, or an answer is slow. Review the evidence first: distinguish an implementation error from an incorrect test oracle, environment failure, missing permission, or unresolved user decision.

Escalate Luna Medium to Sol Medium when the work requires non-local reasoning or a design choice, cannot be independently verified cheaply, or a reviewed correction still leaves defects. Escalate Sol Medium to the coordinator / Sol High when two well-scoped attempts fail, architecture must change, subsystems are tightly coupled, or critical high-confidence judgment is needed. Do not spend two retries when the evidence already identifies a critical task; route it directly. Missing user decisions require clarification, not a stronger model guessing them.

Do not weaken agreed acceptance tests to resolve a failure. When an oracle is demonstrably wrong, the coordinator corrects it against the unchanged specification, documents the reason in `VALIDATION.md`, and verifies the red/green evidence again; implementation workers cannot change it unilaterally.

## Context and usage discipline

Optimize the total cost of a correct result: briefing, worker execution, corrections, coordinator review, and integration. Keep task contracts compact, point to relevant files or document sections, and do not copy full chat history, whole repositories, or unrelated tool output into each worker. This does not remove the runtime's unavoidable system context.

When reliable telemetry is available, record per-task elapsed time, actual model/effort, input tokens, cached-input tokens, output tokens, and reasoning tokens in `VALIDATION.md`. Cached input is a subset of input; reasoning output is a subset of output, so do not add either twice. Keep interrupted attempts separate. Without telemetry, mark usage unknown; do not ask a model to estimate its own hidden usage or infer tokens from elapsed time or answer length. Separate observed counts from tariff-based estimates and subscription-limit consumption. Different context size, caching, and speed modes are comparison confounders.

## Concurrency and isolation

- Default maximum: three active workers, further limited by the runtime's available capacity.
- Outside `$grilling` fact lookup, do not delegate a task whose briefing and review cost exceeds direct execution. During that interview, follow its required read-only subagent lookup rule for unresolved environmental facts.
- Do not parallelize a dependency chain.
- Do not let parallel editing workers share a writable workspace or file ownership. If safe isolation is unavailable, serialize editing work.
- In a shared workspace, coordinator writes must also wait for the active editing worker to finish. Without Git, preserve a bounded before/after record of owned files and acceptance tests for scope and immutability review.
- A worker's passing local checks are evidence, not final acceptance; the coordinator reruns them after integration.
