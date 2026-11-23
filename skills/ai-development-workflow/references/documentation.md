# Documentation maintenance

Read project instructions and an existing entry point or current-state section. Then locate only the requirements, plan, task records, source, and evidence relevant to the work. Use history for specific questions.

## Choose the minimum set of records

Reuse the project's existing files and sections. For a new project, use as many files as the work actually needs, including one combined file when sufficient. The templates below define roles and can be combined or used selectively. Use `.codex/` when a new project needs a dedicated home and has no established convention.

| Role | What belongs there |
| --- | --- |
| [Specification](../assets/SPEC.template.md) | Requirements, behavior, acceptance criteria, constraints, open decisions |
| [Plan](../assets/PLAN.template.md) | Approach, sequence, dependencies, risks, and recovery |
| [Tasks](../assets/TASKS.template.md) | Actionable work, ownership, scope, assignment, and validation |
| [Status](../assets/STATUS.template.md) | Current phase, blockers, latest outcomes, temporary scope |
| [Validation](../assets/VALIDATION.template.md) | Baseline, red/green checks, corrected expectations, and acceptance evidence |

Create a separate document when a distinct, lasting purpose has no suitable existing home. Link it from existing navigation. Keep detailed requirements in their authoritative section. Use links and brief summaries in other records. Link a reliable code registry of values or assets when maintaining a second list would add drift.

## Maintain records by change

- Requirements changed: replace the outdated requirement and reconcile affected references, plan, and tasks. Preserve conditions, exceptions, and rationale that still matter.
- Work progressed: update the affected task and current state. Remove completed items from the active queue once their outcome and evidence are retained. Preserve unresolved questions and evidence needed to reproduce failures.
- Checks ran: record actual scope or revision, command, result, and limitations. Distinguish proposed, agreed, implemented, and verified behavior. Preserve prior evidence that explains a regression or acceptance decision. Unit checks alone do not establish real-use acceptance.
- An explanation produced no decision or material change: leave project records as they are.

Reconcile current claims with code and evidence as needed. Treat the spec as intended behavior and code as observed behavior. Surface mismatches while preserving confirmed requirements. Keep durable rules in project instructions and temporary chat limits in the task state. Keep one owner for shared records and preserve intervening edits. Workers report findings in their result unless an assigned document is the deliverable.

Use committed history when sufficient. Before substantial consolidation, preserve unprotected original material. Archive superseded guidance with its status and keep historical `AGENTS.md` copies outside active instruction paths. Limit maintenance to the affected material and its dependent summaries or links.
