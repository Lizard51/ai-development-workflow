# Delivery workflow

Use the discovery and authorization rules in [the entry point](../SKILL.md). Scale the work to the change. Record a skipped or shortened step when the reason matters to scope, acceptance, or a future handoff.

## Agree on behavior and plan the work

Use [the documentation rules](documentation.md) to find the right home for requirements, plan, tasks, state, and evidence. State observable acceptance criteria, constraints, exclusions, assumptions, and open questions. Identify dependencies before assigning work. Record the expected result and validation, the owner, and the files or subsystem in scope. If delegating, apply the [routing policy](model-routing.md) and record the requested model and effort and any substitution. Preserve user edits when planning integration.

## Establish validation before production code

1. Discover the project's actual test, lint, typecheck, and build commands. Run the relevant baseline and record unrelated failures separately. For an empty project, record the absence of a suite and, after requirements are confirmed, bootstrap the minimal harness for acceptance checks before implementing the target behavior.
2. Add acceptance tests for the agreed behavior where feasible. Check expected results against the specification independently of the implementation. Run the new tests and verify that they fail because the promised behavior is missing. Fix or replace tests that pass without exercising it.
3. Freeze agreed acceptance tests for implementation workers. Only the coordinator may correct a demonstrated error in the expected result. Reconcile it with the unchanged specification, record the reason, and repeat red/green verification. Preserve existing passing behavior.

Test behavior through the entry point that reaches the promised outcome when it matters. For example, verify that saved data survives reopening, that an exported file works in its consuming application, or that loading reaches a usable screen or offers a retry. Add failure or conflict coverage where data loss or blocked work is plausible. For changes unsuited to executable tests, choose a repeatable build assertion, browser flow, visual comparison, or manual check before implementation and record the reason.

For concurrency or atomicity, have the coordinator review the expected result, deterministic schedule, fault point, recovery completion, and permitted outcome before freezing tests. Allow a correct lock to block a second request. A test must never require both requests to reach a barrier inside the same mutually exclusive section.

## Implement and integrate

The implementer runs the assigned failing tests, edits the owned scope, and reruns the checks after meaningful changes. For edits without a Git diff or equivalent versioned record, first preserve a bounded snapshot of the files in scope and frozen tests. Workers return a concise outcome, changed files, commands, results, and unresolved risks.

The coordinator inspects each change against the before-state and agreed scope, reruns the relevant checks, and verifies the test expectations and immutable tests. Recompute decision-relevant numbers and reconcile them with tables and conclusions. Integrate in dependency order and resolve conflicting changes deliberately. Use [the documentation rules](documentation.md) to update affected state, tasks, and evidence.

## Verify the integrated result

Run the complete set of relevant checks on the combined change, including required browser, visual, or manual checks. Review the combined diff against the contract, plan, and remaining tasks. For documentation-only changes, use proportional checks of the diff, links, and consistency. Run application checks when affected behavior or project rules require them.

For a replacement or removal, reconcile active callers, tests, links, and instructions. Run any changed documented command exactly as shown or report the impediment. Label retained historical material so it cannot be mistaken for active guidance.
