# Model routing and agent contracts

Documentation filenames below name roles in the default project layout. Use the existing equivalent sections on resumed projects; these recording requirements do not call for new files or duplicate reports. See [documentation maintenance](documentation.md) for upkeep.

Choose by required reasoning depth, risk, and verifiability, not by role name alone. These defaults are a cost-conscious starting point from bounded checks, not a guarantee of project-level quality, speed, raw-token savings, or subscription savings. Use models actually exposed by the current runtime.

## Default routing

| Task class | Default model | Effort | Typical work |
| --- | --- | --- | --- |
| Reconnaissance | `gpt-6-luna` | medium | Locate files, collect facts, summarize bounded code with references |
| Mechanical / narrow code | `gpt-6-luna` | medium | Repetitive edits, fixtures, small functions with clear independent checks |
| Ordinary bounded implementation | `gpt-6.1-terra` | medium | Isolated implementation and debugging with a clear contract and independent validation; implementing already specified checks |
| Substantive analysis and test design | `gpt-6.2-sol` | medium | Numerical analysis, non-trivial acceptance tests, ambiguous logic, or work whose correctness is difficult to check cheaply |
| Difficult implementation | `gpt-6.2-sol` | medium initially | Tightly coupled cross-file logic, non-trivial refactors, asynchronous ownership and lifecycle reasoning; coordinator review for critical decisions |
| Critical | coordinator; separate `gpt-6.2-sol` reviewer only if justified | high when the coordinator was selected as recommended | Architecture, concurrency/atomicity, authorization/security decisions, integration and final acceptance |

The recommended coordinator is `gpt-6.2-sol` / `high`. Keep the user-selected coordinator unchanged. Keep the interview, specification ownership, task graph, conflict resolution, and final acceptance with it. The coordinator owns both initial model assignment and any later escalation.

Choose Sol Medium directly when the task needs its reasoning or verification depth; Terra is not a required first attempt. Critical decisions can go directly to the coordinator. A separate Sol High worker is not needed for a review the coordinator can perform independently.

Four profiles are routing choices, not four persistent agents. Choose one suitable profile per task; do not run all profiles or create a standby Sol worker. Existing worker-capacity and isolation limits still apply.

## Runtime capability and fallback

Before the first spawn, inspect the available tool contract for model selection, reasoning settings, context forks, and capacity. Use explicit model/effort fields when supported. Custom-agent configuration can override requested settings, so verify the applied profile when metadata is available and record requested versus actual settings when they differ.

If a requested profile is unavailable, disclose and record a suitable available substitution in `TASKS.md`. For ordinary implementation, unavailable Terra can fall back to an available Sol Medium profile. For a small Luna task, prefer direct coordinator work or a justified available worker rather than creating many High workers. If heterogeneous model selection is unavailable, keep the work with the coordinator or use a disclosed supported agent profile when independent work still justifies it. Never claim a profile was applied without support or change global configuration to make this policy work.

## Spawn contract

When the collaboration tool supports these fields, pass `model` and `reasoning_effort` explicitly: `gpt-6-luna` / `medium`, `gpt-6.1-terra` / `medium`, `gpt-6.2-sol` / `medium`, or justified `gpt-6.2-sol` / `high`. Do not let workers inherit the coordinator's High effort unintentionally. With the current collaboration tool, use `fork_turns: "none"` when overriding model or effort and put all necessary context in the task message. Use other bounded-fork forms only when the actual tool schema supports them; never request an override with a full-history fork.

Every task message must include:

- one objective and a concrete deliverable;
- repository or workspace path, isolation mode, and whether writes are allowed;
- owned files or subsystem and forbidden overlap;
- relevant requirements and immutable acceptance tests;
- validation commands;
- expected report: concise summary, files changed, commands, results, and risks; include actual usage only when observable.

Record the assignment, any attempts, and the reason for substitution or escalation in the existing task record. A handoff includes the current change, reproducible failures, and relevant requirements; it does not require repeating completed discovery or copying the full chat.

## Verification by risk

- Luna results must be independently checkable. Recompute numbers that drive decisions; a correction in prose does not repair an inconsistent final table.
- Validate test expectations independently of the implementation under test, using a small worked example, specification-derived assertion, or simple reference oracle. Passing worker-authored tests alone is not acceptance evidence.
- Numerical analysis and non-trivial acceptance-test design start at Sol Medium. Terra may implement bounded checks whose expected behavior is already established. The coordinator verifies the final artifact, not only the explanation.
- For concurrency/atomicity, involve the coordinator, preferably the recommended High profile, in test design before freezing tests. Preserve and disclose the actual profile rather than silently changing it; if a required review capability is unavailable, report the limitation. Synchronization must allow a correct lock to block the second request; do not require both requests to reach a barrier inside one mutually exclusive section. Define the fault point, recovery completion, and allowed outcome from the agreed contract so that an overly broad assertion cannot mask failure.

## Escalation

The coordinator decides from inspected changes, reproducible checks, and the specification, not from the worker's claim of completion. A green test suite does not replace review of scope and required behavior.

First distinguish an implementation defect from an incorrect test oracle, environment failure, missing permission, or unresolved user decision. A failed check, slow answer, or request for a stronger model alone is not a sufficient reason to escalate. Fix the relevant prerequisite or clarify the decision instead of asking a stronger model to guess.

- The coordinator may move ordinary bounded work from Luna Medium to Terra Medium when it exceeds Luna's narrow remit. Route directly to Sol Medium when the evidence shows substantive reasoning, design, or verification needs; do not require a Luna-to-Terra-to-Sol ladder.
- For a simple, understood local Terra defect, allow at most one bounded correction per task with concrete feedback. If it still fails, use Sol Medium or have the coordinator finish a tiny correction directly. Escalate without that extra attempt when the reviewed evidence already shows substantial logical errors, a misunderstood contract, or reasoning needs beyond the ordinary bounded task.
- Escalate Sol Medium to the coordinator / Sol High when two well-scoped attempts fail, architecture must change, or critical high-confidence judgment is needed. Do not spend two retries when the evidence already identifies a critical task.

Stop the previous editing worker before handing its owned scope to another worker. Preserve its useful changes and evidence, then have the coordinator verify the corrected result under the same acceptance criteria. Do not weaken agreed tests to resolve a failure. When an oracle is demonstrably wrong, the coordinator corrects it against the unchanged specification, documents the reason in `VALIDATION.md`, and verifies the red/green evidence again; implementation workers cannot change it unilaterally.

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
