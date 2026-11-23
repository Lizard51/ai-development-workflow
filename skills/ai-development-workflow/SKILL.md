---
name: ai-development-workflow
description: Turn a substantial software idea or complex feature into a specified, test-first, delegation-capable implementation. Use for end-to-end builds with planning, validation, selective agents, and integration; do not use for small edits, explanation-only, diagnosis-only, or review-only requests.
---

# AI Development Workflow

The coordinator owns requirements, critical decisions, integration, and final acceptance. Recommend GPT-6.2 Sol High before starting and keep the model the user selected. Git is optional. Pushes, pull requests, merges, deployments, and other external writes require explicit user authorization.

## Discover and confirm

Inspect project instructions, current state, and relevant code before asking the user. Use `$grilling` for new products, large features, and materially ambiguous work. Its decision rounds cover unresolved product choices and material trade-offs that need the user. Resolve routine implementation choices from the repository and confirmed requirements. Wait for confirmation of shared understanding before implementing. Explicit confirmation in the last round counts. Reuse confirmed decisions on resumed work and reopen the interview for newly ambiguous requirements. Use `$domain-modeling` when unclear domain terms or a consequential domain trade-off need it.

When composing this workflow with `$grilling`, use this fact-finding rule in place of its default dispatch rule. Look up quick facts directly. Delegate a bounded read-only investigation if it can resolve an independent prerequisite while other questions move forward, or if delegation materially improves the result. Use the [routing policy](references/model-routing.md) before assigning an agent, including during the interview.

## Plan and deliver

After confirmation continue the authorized work through acceptance. Ask again for unresolved user decisions, material scope changes, permissions, or external actions.

1. Capture requirements, plan, task ownership, current state, and evidence where they fit. Read [documentation maintenance](references/documentation.md) when choosing or updating records. The five templates are available for these roles. Combine roles in one file or use existing sections when that covers the work.
2. Follow [the delivery workflow](references/workflow.md) to plan and build. For new behavior, establish the baseline and independently check that acceptance tests fail for the intended reason before implementation. Keep agreed tests fixed during implementation. Use a repeatable alternative when an executable test is unsuitable.
3. Delegate independent work selectively when its benefit exceeds the briefing and review cost. Use the [routing policy](references/model-routing.md) for assignments, isolation, or escalation. Keep tiny and tightly coupled edits with the coordinator.
4. Independently review worker results, integrate in dependency order, and verify the affected behavior against the confirmed contract. Apply the delivery workflow's final checks to user-visible outcomes and replacements or removals.

Report the delivered result, checks and outcomes, material failures or unverified areas, and any remaining work. Close the task when the required evidence supports acceptance. Unchanged pre-existing failures may remain if disclosed and they do not prevent verifying the requested behavior.
