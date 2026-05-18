# Agent Team Grill Answers

**As of:** 2026-05-18

## Conclusion

Adopt the recommended answers from the grill. The first real pilot is weekly LSL/internal shared-memory and agent-ops hygiene. The agent-team model must prove a runtime control loop, not just a folder structure.

## Adopted Answers

### 1. What recurring workflow should run without Dave manually steering it?

Recommended answer adopted: weekly LSL/internal shared-memory and agent-ops hygiene.

Reason:

- It is real LSL work.
- It is low-risk and file-backed.
- It exercises multiple agent roles.
- Failure is inspectable.
- It does not mutate Workiva, client systems, credentials, or production surfaces.

### 2. What does hygiene mean?

Recommended answer adopted: hygiene covers stale tasks, broken handoffs, outdated memory, duplicate standards, missing proof, and unresolved blockers, but each needs a detection rule.

Detection rules:

- Stale task: `active` for more than 48 hours without a handoff, proof update, or blocker.
- Broken handoff: handoff lacks current state, next action, evidence, or blocker owner.
- Outdated memory: memory or standard has no `**As of:**` date, contradicts newer project docs, or points to moved/deleted paths.
- Duplicate standard: two files define competing canonical routes for the same recurring workflow.
- Missing proof: task is in `review` or `done` without command output, file diff, source link, screenshot, exported artifact, or explicit verification note.
- Unresolved blocker: blocker has no owner, needed input, or next action.

### 3. What is the coordinator allowed to do without Dave?

Recommended answer adopted: the coordinator can inspect, dispatch, lock, summarize, prepare, and move non-production file-backed work through review. It cannot mutate production/client systems or publish externally without approval or a project-specific authorization rule.

Allowed:

- Read repo docs, memory, standards, logs, task boards, handoffs, blockers, and queue files.
- Create and update task packets.
- Assign specialists based on role cards.
- Move tasks from `ready` to `active`, `review`, or `blocked`.
- Create proof packets and coordinator summaries.
- Propose memory, standards, and recipe updates.
- Mark low-risk internal hygiene tasks `done` when proof passes.

Not allowed:

- Workiva/API writes.
- Client-visible changes.
- Production pushes or deploys.
- Credential changes.
- Paid account changes.
- Destructive git operations.
- Deleting source-of-truth files.

### 4. What is the actual runtime loop?

Recommended answer adopted:

```text
intake -> dispatch -> active lock -> proof review -> done/block/escalate -> memory update
```

Each transition needs an owner, trigger, touched file, verification, and timeout.

### 5. How are tasks locked?

Recommended answer adopted: one active owner per task, recorded in the board and task packet. A task cannot have multiple owners unless the coordinator explicitly splits it into separate packets.

Lock rule:

- Moving a task to `active` records owner, timestamp, and expected return artifact.
- If the owner cannot finish, they write a handoff and move the task to `blocked` or `review`.
- No second agent edits the same packet while it is active unless the coordinator reassigns it.

### 6. How is stale work handled?

Recommended answer adopted: stale work is a coordinator responsibility, not Dave's problem.

Stall rule:

- Active task older than 48 hours: coordinator requests status from owner or moves to `blocked`.
- Review task older than 48 hours: coordinator reviews proof or escalates the missing review.
- Blocker older than 7 days: coordinator either closes it as parked, escalates it, or creates a smaller unblocked task.

### 7. What counts as proof?

Recommended answer adopted: proof must be artifact-backed, not prose-only.

Acceptable proof:

- Command output summary with exact command.
- File path and diff summary.
- Browser screenshot or visual-state note.
- Source link checked on a date.
- Exported artifact.
- Passing test/build/lint output.
- Read-only state verification.
- Explicit blocked-state evidence.

### 8. Who judges proof?

Recommended answer adopted: the coordinator reviews ordinary proof; QA Agent reviews proof for higher-risk or recurring-route changes.

Rules:

- Low-risk file hygiene: coordinator can mark done.
- Standards/memory changes: coordinator reviews and may request QA.
- LSL/client delivery, Workiva, production, or external-facing work: coordinator cannot mark final done unless the project rule allows it or Dave approves.

### 9. What should specialists receive?

Recommended answer adopted: specialists receive a role card reference and one task packet. They should not receive broad project goals unless assigned as coordinator.

Dispatch format:

```text
You are <role>. Use your standing role card.
Task packet: <absolute path>
Return: result, changed files, proof, blockers, handoff path if needed.
```

### 10. What makes the first pilot successful?

Recommended answer adopted: the first pilot succeeds only if the team completes one weekly hygiene cycle without Dave interpreting priorities during execution.

Success criteria:

- Intake finds real hygiene candidates.
- Coordinator creates scoped task packets.
- At least two specialist roles can work from packets.
- Active locks prevent duplicate/conflicting work.
- Proof review catches at least one weak or missing proof item, or explicitly confirms none.
- Board ends with clear `done`, `blocked`, and next-cycle state.
- Memory or standards update is proposed only when supported by proof.

## Decision

Do not execute the original self-referential pilot as the main test. Keep it only as a template sanity check if needed.

The execution plan should be revised around weekly LSL/internal shared-memory and agent-ops hygiene.
