# Plan: Agent Team Pilot
Date: 2026-05-18
Goal: Pilot the coordinator-led agent-team model on weekly LSL/internal shared-memory and agent-ops hygiene, proving the runtime loop rather than only the folder structure.
Scope: In scope is the first real pilot under `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/`. Out of scope is Workiva/API writes, client-visible changes, production pushes/deploys, credential changes, paid account changes, destructive git operations, or deleting source-of-truth files.
Dependencies: Existing operating model at `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/autonomous-agent-team-operating-model.md`; reusable template folder at `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/`.

## Pressure-Test Revision

The original plan proved the template against itself. The grill-me pressure test and independent agent review found that this is not enough. The pilot must prove the runtime loop:

```text
intake -> dispatch -> active lock -> proof review -> done/block/escalate -> memory update
```

Adopted answers are recorded at `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/agent-team-grill-answers.md`.

## Shortcut Trigger

Dave can trigger this pilot with:

```text
run team hygiene
```

This means: execute this plan, create or resume `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/`, start the coordinator loop, and move the next ready hygiene task forward.

The broader shortcut is:

```text
run the team
```

This means: start the coordinator loop for the current project. If no project-local `agent-team/` folder exists, use this LSL/internal hygiene plan as the default starting route.

## Plan Inputs

Current working folder: `/Users/davebettner/.codex/worktrees/d085/notes`

Inspected:
- `/Users/davebettner/.codex/skills/writing-plans/SKILL.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/autonomous-agent-team-operating-model.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/README.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/agent_registry.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/coordinator.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/task_board.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/task_packet_template.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/handoff_template.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/decision_log.md`
- `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/blockers.md`

Evidence:
- The canonical model exists outside the personal folder at `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/autonomous-agent-team-operating-model.md`.
- The model explicitly covers LSL work, client delivery, internal tooling, product work, automation, research, and personal systems.
- The template folder contains the files needed to initialize a project-local `agent-team/` workspace.
- No existing plan folder was present before this plan, so this file creates the required `docs/plans/` path.
- The pressure test identified weekly LSL/internal shared-memory and agent-ops hygiene as the recommended first real pilot.

Assumptions:
- The first pilot should prove coordination on real LSL/internal file-backed work before touching live client or Workiva systems.
- The pilot should live in the same non-personal notes worktree as the standard.
- Dave accepts the recommended grill answers without stopping after each question.

Open questions:
- Which live LSL/client/internal project should become the second pilot after the weekly hygiene loop completes one successful cycle?

## Runtime Transition Rules

| Transition | Owner | Trigger | File touched | Verification | Timeout |
|---|---|---|---|---|---|
| Intake | Coordinator | Weekly run starts | `task_board.md`, `blockers.md`, intake note | Hygiene candidates listed with source paths | Same session |
| Dispatch | Coordinator | Candidate is scoped | Task packet and `task_board.md` | One owner, priority, outcome, proof, stop condition | Same session |
| Active lock | Coordinator | Task moves to `active` | `task_board.md`, task packet | Owner and timestamp recorded | 48 hours |
| Proof review | Coordinator or QA Agent | Specialist returns work | `proof/`, `handoffs/`, `task_board.md` | Artifact-backed proof, not prose-only | 48 hours |
| Done/block/escalate | Coordinator | Proof passes or blocker appears | `task_board.md`, `blockers.md`, `decision_log.md` | Final state and next action clear | Same session |
| Memory update | Coordinator | Reusable route proven | memory/standard/proposed update note | `**As of:**` date and source proof present | Same session |

## Task 1: Create The LSL/Internal Hygiene Workspace

**Goal:** Create a project-local copy of the agent-team template for weekly LSL/internal shared-memory and agent-ops hygiene.
**Type:** Mutating work

**Steps:**
1. Create `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/`.
2. Copy the contents of `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/` into `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/`.
3. Update `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/README.md` so it says this pilot runs weekly LSL/internal shared-memory and agent-ops hygiene.

**Verification:** `find /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team -maxdepth 2 -type f | sort` shows the copied template files.
**Stop condition:** Stop if the template source folder is missing or the target folder already contains unrelated work.
**Rollback:** Delete only `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/` if the copy is wrong and recreate it from the template.

## Task 2: Customize The Coordinator Charter For The Runtime Loop

**Goal:** Make coordinator authority and runtime transitions concrete enough to run without Dave steering.
**Type:** Mutating work

**Steps:**
1. Edit `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/coordinator.md`.
2. Set the coordinator objective to: `Run weekly LSL/internal shared-memory and agent-ops hygiene through intake, dispatch, active lock, proof review, done/block/escalate, and memory update.`
3. Add allowed actions: read files, create/update task packets, move tasks through queues, create proof packets, propose memory/standards updates, and mark low-risk internal hygiene tasks `done` when proof passes.
4. Add forbidden actions: Workiva/API writes, client-visible changes, production pushes/deploys, credential changes, paid account changes, destructive git operations, and deleting source-of-truth files.
5. Add stale-work rules: active over 48 hours requires status/block; review over 48 hours requires review/escalation; blockers over 7 days require close/escalate/split.

**Verification:** `rg -n "weekly LSL/internal|active over 48 hours|forbidden actions|mark low-risk internal hygiene tasks" /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/coordinator.md` returns matches.
**Stop condition:** Stop if the coordinator charter starts assigning live client work.
**Rollback:** Restore `coordinator.md` from `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/coordinator.md`.

## Task 3: Define Hygiene-Specific Agent Roles

**Goal:** Tune the agent registry so specialists receive role-card references and scoped task packets, not broad goals.
**Type:** Mutating work

**Steps:**
1. Edit `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/agent_registry.md`.
2. Keep the roles `Coordinator`, `Codex`, `Claude`, `Hermes`, `Browser Agent`, and `QA Agent`.
3. Add a boundary to each role: work only from assigned task packets, write proof, and return blockers instead of expanding scope.
4. Assign Codex to repo/file inspection and exact path checks.
5. Assign Claude to standards/memory consistency review and wording.
6. Assign QA Agent to proof gate review.
7. Assign Hermes only to background watch/research drafts until provider reliability is proven.

**Verification:** `rg -n "assigned task packets|repo/file inspection|standards/memory consistency|proof gate review" /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/agent_registry.md` returns matches.
**Stop condition:** Stop if any role is given authority to self-assign broad work.
**Rollback:** Restore `agent_registry.md` from `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/agent_registry.md`.

## Task 4: Write Initial Hygiene Task Packets

**Goal:** Create enough work items to exercise the coordinator loop end to end.
**Type:** Mutating work

**Steps:**
1. Create `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/tasks/`.
2. Create `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/tasks/HYGIENE-001-stale-agent-ops-scan.md` assigned to `Codex`.
3. Create `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/tasks/HYGIENE-002-standards-memory-consistency.md` assigned to `Claude`.
4. Create `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/tasks/HYGIENE-003-proof-gate-review.md` assigned to `QA Agent`.
5. In each task packet, include outcome, context, scope, exact steps, `Done Means`, required proof, stop conditions, and handoff requirement.

**Verification:** `rg -n "Task ID: HYGIENE-00|Done Means|Required Proof|Stop Conditions" /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/tasks` returns matches for all three files.
**Stop condition:** Stop if any task requires live external system access, Workiva writes, client delivery, or broad judgment beyond the hygiene scope.
**Rollback:** Delete only the three `HYGIENE-00*.md` task packet files and recreate them from the task packet template.

## Task 5: Populate The Task Board

**Goal:** Make the pilot board runnable by listing the three scoped tasks in `ready`.
**Type:** Mutating work

**Steps:**
1. Edit `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/task_board.md`.
2. Set `**As of:** 2026-05-18`.
3. Add `HYGIENE-001`, `HYGIENE-002`, and `HYGIENE-003` to the `Ready` table with priorities, owners, task names, and packet paths.
4. Leave `Active`, `Review`, `Blocked`, and `Done` empty except for their headers.

**Verification:** `rg -n "HYGIENE-001|HYGIENE-002|HYGIENE-003|Ready|Active|Review|Blocked|Done" /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/task_board.md` returns matches.
**Stop condition:** Stop if any task appears in more than one queue.
**Rollback:** Restore `task_board.md` from `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/task_board.md`.

## Task 6: Record The Initial Decision And Blocker State

**Goal:** Make the pilot state auditable before execution starts.
**Type:** Mutating work

**Steps:**
1. Edit `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/decision_log.md`.
2. Add a decision dated `2026-05-18`: first pilot is weekly LSL/internal shared-memory and agent-ops hygiene.
3. Add a decision dated `2026-05-18`: coordinator can mark low-risk internal hygiene tasks done when proof passes.
4. Edit `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/blockers.md`.
5. Add one open question blocker: second pilot target for live LSL/client/internal work is not chosen yet.

**Verification:** `rg -n "weekly LSL/internal|low-risk internal hygiene|second pilot target" /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/decision_log.md /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/blockers.md` returns matches.
**Stop condition:** Stop if the blocker is phrased as blocking this first pilot; it should block only the second pilot.
**Rollback:** Restore `decision_log.md` and `blockers.md` from `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/templates/agent-team/`.

## Task 7: Verify The Pilot Folder

**Goal:** Confirm the hygiene pilot can be executed by a coordinator without missing files.
**Type:** Verification

**Steps:**
1. Run `find /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team -maxdepth 3 -type f | sort`.
2. Run `rg -n "HYGIENE-001|HYGIENE-002|HYGIENE-003" /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team`.
3. Run `rg -n "TBD|TODO|as needed|etc\\." /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team` and review any matches manually.
4. Confirm no file path under `/Users/davebettner/Documents/Personal/notes/` remains in the pilot folder.

**Verification:** The commands show all required files, all three task IDs, no unresolved placeholders that affect execution, and no personal-folder path references.
**Stop condition:** Stop if required files are missing, task IDs do not match the board, or personal-folder paths remain.
**Rollback:** Fix the specific file from the template or delete and recreate the pilot folder from the template.

## Task 8: Write The Execution Handoff

**Goal:** Give the next agent or coordinator a clean start point.
**Type:** Handoff

**Steps:**
1. Create `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/handoffs/2026-05-18-initial-coordinator-handoff.md`.
2. State that the first action is to move `HYGIENE-001` from `Ready` to `Active`.
3. Include the exact path to the task board and the three task packets.
4. Name the stop condition: Dave must choose the second pilot target before applying this to a live LSL/client/internal project.

**Verification:** `rg -n "HYGIENE-001|Ready|Active|second pilot target" /Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/handoffs/2026-05-18-initial-coordinator-handoff.md` returns matches.
**Stop condition:** Stop if the handoff instructs execution against a live project.
**Rollback:** Delete only `/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/lsl-internal-hygiene-team/handoffs/2026-05-18-initial-coordinator-handoff.md` and rewrite it from the handoff template.

## Self-Review Checklist

- [x] Discovery was performed before the task list was written.
- [x] Current working folder is recorded.
- [x] Inspected files/scripts/docs are listed.
- [x] Evidence, assumptions, and open questions are separated.
- [x] Every task has a concrete verification step.
- [x] Every task has a stop condition.
- [x] No task contains placeholder language that an executor must invent.
- [x] File paths are exact.
- [x] The plan addresses the full first-pilot scope.
- [x] Rollback is noted for mutating tasks.

## Execution Paths

1. Review first: Dave reviews the revised runtime-loop plan.
2. Execute now: create the LSL/internal hygiene team folder and task packets exactly as described above.

Parallel dispatch candidates after the pilot folder exists:

- `HYGIENE-001` can be handled by Codex.
- `HYGIENE-002` can be handled by Claude.
- `HYGIENE-003` can be handled by QA Agent after `HYGIENE-001` and `HYGIENE-002` return proof.
