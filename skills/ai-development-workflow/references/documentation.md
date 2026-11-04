# Documentation maintenance

Use this reference when continuing development or updating project records. It governs documentation upkeep, not the interview, initial new-project contract, model routing, or test-first implementation process.

## Find the existing home

Read applicable project instructions, the existing README or navigation, and a concise current-state section. Then locate only the requirements, plan, queue, source, and evidence relevant to the task. Use targeted searches when the location is unclear; read archives only to answer a specific question. Do not repeat a full documentation audit for each message or small edit.

Keep the established structure. For example, README, TODO, and an architecture document may already cover the default specification, tasks, and plan roles. Reuse those locations rather than adding a parallel `.codex/` set. A resumed chat uses the same records. Broader reorganization requires a concrete task need; it is not routine maintenance.

The default new-project SPEC, PLAN, TASKS, STATUS, and VALIDATION remain available. Additional roles such as design, protocol, or platform requirements need separate files only when their subject warrants one; roles are not a checklist of new documents.

## One authoritative place per fact

Keep the full requirement in its primary requirements section. State and queue entries carry short outcomes or remaining actions and a link to that section. Plans describe approach and dependencies; validation records describe observed checks and their limits. Do not copy the detailed contract into all of them. Brief reminders of critical constraints are useful when they do not become competing specifications.

If code already provides a reliable registry of values or assets, link to it rather than maintaining a second complete list. Preserve readable sentences, units, conditions, exceptions, and useful rationale; brevity must not change meaning.

Before creating a file, identify a lasting purpose, its intended reader or future task, why no current section fits, and its place in existing navigation. Make that judgment yourself rather than asking the user a file-creation questionnaire. A distinct design effort or protocol may qualify; another recap of the current task normally does not. Link a justified new file from existing navigation, without creating a second index.

## Update by meaning, not by chronology

| What changed | What to maintain |
| --- | --- |
| An agreed requirement | Replace its authoritative wording and reconcile affected links, state, and tasks. |
| Implementation progress | Update current state and the affected task; link to the requirement. |
| Validation evidence | Record actual scope, command, result, and limitations in the existing evidence location. |
| An unresolved issue | Keep the remaining question and useful reproduction evidence visible. |
| An explanation with no new decision | No documentation update is needed. |

Do not append dated amendments that leave superseded rules looking active. Keep status as a current snapshot with open work and the latest material outcome, not a transcript. Move completed work out of the active queue once its necessary outcome or evidence is retained. Keep earlier evidence when it explains a baseline, regression, acceptance decision, or unresolved problem; do not erase it merely to shorten a file.

Use clear language to distinguish proposals, user choices, requirements, implementation, automatic checks, real-use checks, assumptions, confirmed defects, unreproduced reports, and deferred work. Labels on every sentence are unnecessary. An approved mockup is still unimplemented until built. Passing unit tests does not establish real-use acceptance. One successful retry does not close an intermittent defect. A task on a plan is not authorization to implement it now.

Documentation is a claim about implementation, not proof. Compare relevant claims with code and checks in proportion to the task. A new direct user instruction takes precedence; requirements describe intended behavior, code existing behavior, and history past behavior. Identify a mismatch rather than automatically rewriting an approved requirement to match faulty code.

## Keep instructions and history useful

Put durable working rules in project instructions and temporary assignments or chat-specific limits in the existing task-state location. Do not leave a temporary instruction such as “this chat only covers design” as a permanent project-wide rule. Preserve the user's actual scope; generalize a temporary instruction into a conditional permanent rule only when that lasting rule is intended.

Separate meaningful history from active instructions and leave a discoverable path to it. Use committed Git history when sufficient; uncommitted user content is not protected merely because Git exists. Before substantial consolidation or relocation, preserve any otherwise unprotected original content with a bounded before-state. Do not delete existing history, mirror all documentation after every task, or create an endless series of handoffs. Archived instruction copies must not become active `AGENTS.md` files in new directories.

During routine development, touch only the affected sections and known dependent summaries or links. Do not launch a project-wide cleanup, migration, or archive-reading pass without a concrete need. Use no fixed line cap that forces requirements or open questions to disappear.

## Shared records

Use the workflow's existing ownership and writable-isolation rules for documents too. One designated owner updates shared records from concise worker results; an agent does not create its own general plan or permanent report outside its assigned scope. Read the latest version before editing, preserve parallel changes, and serialize writes when safe isolation is unavailable. Small documentation edits do not require delegation.
