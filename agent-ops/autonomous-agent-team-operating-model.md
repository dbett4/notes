# Autonomous Agent Team Operating Model

**As of:** 2026-05-18

## Conclusion

Use a coordinator-led task board, not ad hoc chat handoffs. The coordinator owns intake, decomposition, dispatch, queue hygiene, verification, and escalation. Specialist agents own execution inside pre-defined role boundaries, using standing role cards instead of receiving full instructions every time.

This is the operating model for keeping work moving across Codex, Claude, Hermes, Browser Use, and future specialist agents without Dave repeatedly restating context.

It applies to LSL work, client delivery, internal tooling, product work, automation, research, and personal systems. The file may live in the notes vault, but the scope is not personal-only.

## Core Rule

One coordinator keeps the project running. Agents do not self-assign broad work, rewrite the plan, or invent priorities. They pull scoped task packets, produce proof, write handoffs, and return status.

## Shortcut Phrases

Dave can trigger the coordinator with short phrases:

| Phrase | Meaning |
|---|---|
| `run the team` | Start the coordinator loop for the current project. Read the local `agent-team/` folder or nearest relevant team plan, then continue from the board. |
| `run team hygiene` | Start the weekly LSL/internal shared-memory and agent-ops hygiene loop. Use `/Users/davebettner/.codex/worktrees/d085/notes/docs/plans/2026-05-18-agent-team-pilot.md` until the runnable team folder exists. |
| `team status` | Read the current team board, blockers, latest handoffs, and proof state; summarize what is active, blocked, ready, and next. |
| `team handoff` | Write or refresh the coordinator handoff so another agent can continue without chat history. |

Default interpretation: if Dave says `run the team` with no project named, use the current working project. If no project-local `agent-team/` folder exists, use the LSL/internal hygiene pilot plan as the starting point and create the missing team folder before dispatching work.

## Scope

Use this model for any project where one of these is true:

- Multiple agents or tools contribute work.
- Work spans more than one session.
- A coordinator needs to keep tasks moving without Dave re-explaining priorities.
- LSL, client, internal, product, or operational work needs durable proof.
- Specialists have standing expertise and should receive task packets, not full re-instructions.

Do not limit this to personal projects. The same pattern should work for LSL work broadly: ACFR/Workiva delivery, client prep, LSL tooling, Forge, marketing/business development, reusable standards, automation, betting systems, and home infrastructure.

## LSL Work

LSL work is a first-class use case for this model.

Use the coordinator pattern for:

- Client ACFR/Workiva delivery.
- Client prep, status packets, decision briefs, and follow-up.
- Internal LSL tools, Forge, Workiva MCP/API work, and reusable scripts.
- LSL-branded marketing, training, sales, and enablement artifacts.
- Cross-client standards, reusable playbooks, skills, and templates.
- Research that may change LSL service delivery or internal operations.

For LSL-branded artifacts, follow the LSL visual preference: teal and charcoal should dominate; green is secondary and used sparingly.

For Workiva or ACFR work, the coordinator must enforce the existing Workiva playbook rules before any API/write action.

## Source of Truth

Git-backed Markdown is the authority.

Use Obsidian as a human UI when convenient. Use chat as a transient control surface. Use local files as the shared memory and handoff layer.

## Folder Pattern

Each substantial project should have an `agent-team/` folder:

```text
agent-team/
  README.md
  coordinator.md
  agent_registry.md
  task_board.md
  decision_log.md
  blockers.md
  handoffs/
  proof/
  queues/
    ready.md
    active.md
    review.md
    blocked.md
    done.md
```

For cross-project standards, keep canonical guidance in:

```text
/Users/davebettner/.codex/worktrees/d085/notes/agent-ops/
```

If this model is being used for LSL or client delivery, mirror or promote the project-local `agent-team/` folder into the relevant Git-backed project repo or shared memory repo. The vault copy is the standard; the project folder is the execution record.

## Coordinator Responsibilities

The coordinator is the only role that owns the whole project state.

Coordinator duties:

- Maintain the task board.
- Convert vague goals into scoped task packets.
- Assign the right specialist based on role, evidence, and risk.
- Keep one active owner per task.
- Prevent duplicate work.
- Track blockers separately from work in progress.
- Review proof before marking work done.
- Promote repeated routes into memory, recipes, or skills.
- Escalate only when a decision, credential, source file, or approval is actually missing.

The coordinator should not do deep specialist work unless it is the shortest safe path.

## Specialist Agent Registry

Each agent gets a standing role card. The coordinator references the role card and sends only the task packet plus any project-specific context.

Minimum role card:

```markdown
# Agent Role: <name>

Purpose:
- ...

Best at:
- ...

Do not do:
- ...

Required first reads:
- ...

Default output:
- ...

Proof required:
- ...

Escalate when:
- ...
```

## Default Team Roles

### Coordinator

Purpose: keep the project moving, not produce every artifact personally.

Best at:

- Intake and scoping.
- Breaking work into task packets.
- Assigning owners.
- Checking completion evidence.
- Keeping `task_board.md`, `blockers.md`, and `decision_log.md` current.

Do not do:

- Let specialists drift into open-ended research.
- Mark tasks done without proof.
- Ask Dave for context that exists in files.

### Codex

Purpose: implementation, tests, repo work, automation, local apps, UI work, code review.

Best at:

- Editing files.
- Running tests.
- Building scripts.
- Verifying local systems.
- Producing exact diffs and proof.

Default output:

- Changed files.
- Verification commands.
- Remaining risks.
- Handoff note when work continues elsewhere.

### Claude

Purpose: Workiva-heavy work, ACFR reasoning, long-form synthesis, client-ready wording, standards, and memory maintenance.

Best at:

- Workiva/ACFR task interpretation.
- Financial reporting logic.
- Client communication drafts.
- Handoff and memory grooming.

Required first reads:

- Relevant project handoff.
- Workiva playbooks when Workiva is involved.
- Recent session logs.

### Hermes

Purpose: background sidecar, scheduled research, provider experiments, long-running watch tasks.

Best at:

- Recurring checks.
- Research sidecars.
- Queue monitoring.
- Producing draft artifacts for coordinator review.

Do not do:

- Own final source of truth until provider output is proven reliable.
- Make unreviewed local mutations.

### Browser Agent

Purpose: authenticated browser inspection and UI-state proof.

Best at:

- Dynamic pages.
- Logged-in app state.
- Screenshots.
- Browser-only workflows.

Default output:

- URL inspected.
- State observed.
- Screenshots or extracted evidence.
- Blockers such as auth, rate limits, or empty page state.

### QA Agent

Purpose: adversarial verification.

Best at:

- Finding missing edge cases.
- Testing claims against acceptance criteria.
- Checking that proof matches done criteria.

Do not do:

- Rewrite the feature unless explicitly assigned.

## Task Packet

Every delegated task should be a file-backed packet. Chat can point to the packet, but the packet is the work order.

```markdown
# Task: <short title>

**As of:** YYYY-MM-DD
**Task ID:** <project>-<number>
**Owner:** <agent role or name>
**Status:** ready | active | review | blocked | done
**Priority:** P0 | P1 | P2 | P3

## Outcome

One sentence describing what must be true when the task is done.

## Context

- Project:
- Relevant files:
- Prior decisions:
- Constraints:

## Scope

In scope:
- ...

Out of scope:
- ...

## Steps

1. ...
2. ...
3. ...

## Done Means

- [ ] Output artifact exists.
- [ ] Verification evidence collected.
- [ ] Relevant queue/status file updated.
- [ ] Blockers or gaps named.

## Required Proof

- Commands run:
- Files changed:
- Browser/API/source evidence:
- Tests/checks:

## Stop Conditions

- ...

## Handoff Required

Write a handoff under `agent-team/handoffs/` if the task is blocked, partially complete, or needs another specialist.
```

## Handoff Packet

Specialists do not hand off by saying “continue from here.” They write a short handoff file.

```markdown
# Handoff: <task title>

**As of:** YYYY-MM-DD
**From:** <agent>
**To:** <agent/coordinator>
**Task ID:** <id>
**Status:** blocked | review | needs-specialist | done

## What Changed

- ...

## Evidence

- ...

## Current State

- ...

## Next Action

1. ...

## Do Not Repeat

- ...

## Blockers

- None, or exact blocker and owner.
```

## Coordinator Loop

Run this loop whenever the project wakes up:

1. Read `task_board.md`, `blockers.md`, `decision_log.md`, and the latest handoffs.
2. Move blocked tasks out of active work.
3. Pick the highest-priority ready task with a clear owner.
4. Dispatch one scoped packet to the specialist.
5. While specialists work, update board state and prepare the next non-conflicting packet.
6. Review returned proof against `Done Means`.
7. Mark done, return for correction, or escalate.
8. Promote reusable routes into memory, recipes, or skills.

## Status Rules

Use these statuses only:

| Status | Meaning |
|---|---|
| `ready` | Scoped and assignable. |
| `active` | One owner is working it now. |
| `review` | Work returned; coordinator must verify proof. |
| `blocked` | Cannot move without source, credential, approval, or decision. |
| `done` | Proof passed and source-of-truth files are updated. |

No task stays `active` without an owner and a timestamp.

## Autonomy Bands

### Green: Agent Can Proceed

- Read files.
- Create or update Markdown handoffs, plans, logs, and proof packets.
- Run non-destructive verification.
- Edit files inside assigned scope.
- Add tests for assigned code.

### Yellow: Coordinator Review First

- Broad refactors.
- New dependencies.
- Workflow changes that affect other agents.
- Browser actions that change external account state.
- Workiva/API writes.
- Client-facing wording or delivery artifacts.

### Red: Dave Approval Required

- Destructive git operations.
- Production pushes/deploys.
- Client-visible Workiva mutations unless already authorized.
- Paid account changes.
- Credential changes.
- Deleting source-of-truth files.

## Dispatch Format

Coordinator sends specialists this:

```text
You are <role>. Use your standing role card.

Task packet:
<absolute path>

Return:
- concise result
- changed files
- proof
- blockers
- handoff path if follow-up is needed
```

The coordinator should not restate global instructions unless the role card or task packet is missing something specific.

## Review Gate

A task is done only when:

- The output exists where expected.
- The proof matches the task's `Done Means`.
- Related queue/status files are updated.
- Any memory-worthy route is recorded.
- The next task is clear or the project is explicitly parked.

## Recommended First Implementation

Build this first as Markdown infrastructure before adding software:

1. Add `agent-team/` to one active project, preferably a real client/internal/product project rather than a toy example.
2. Create `agent_registry.md` with Codex, Claude, Hermes, Browser Agent, QA Agent, and Coordinator role cards.
3. Create `task_board.md` with five queues: ready, active, review, blocked, done.
4. Convert the next real project goal into three task packets.
5. Have the coordinator dispatch one task and require a handoff file before switching agents.

Only automate after the Markdown loop works end-to-end.

## What Not To Build Yet

Do not start with a complex app, dashboard, or autonomous process manager. The failure mode is another tool that must be maintained.

Start with Git-backed Markdown. Add scripts later for:

- Task ID creation.
- Board validation.
- Stale active-task detection.
- Handoff linting.
- Summary generation.

## Adoption Decision

Adopt this operating model now for multi-agent work.

The next concrete step is to pilot it on one project with a real coordinator-owned `agent-team/` folder and three scoped task packets.
