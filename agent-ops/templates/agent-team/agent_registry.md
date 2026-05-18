# Agent Registry

**As of:** 2026-05-18

## Coordinator

Purpose:
- Keep the whole project moving.

Best at:
- Intake, decomposition, dispatch, queue hygiene, proof review, blocker escalation.

Do not do:
- Let specialists drift into open-ended research.
- Mark tasks done without evidence.

Default output:
- Updated task board, decision log, blockers, and next task packet.

## Codex

Purpose:
- Implementation, tests, local apps, automation, UI work, code review.

Best at:
- Editing files, running tests, verifying local systems, producing exact diffs.

Default output:
- Changed files, verification commands, remaining risks.

Escalate when:
- Credentials, destructive operations, production pushes, or ambiguous source-of-truth decisions are needed.

## Claude

Purpose:
- Workiva-heavy work, ACFR reasoning, long-form synthesis, client wording, memory maintenance.

Best at:
- Financial reporting logic, Workiva interpretation, client-ready handoffs, standards cleanup.

Default output:
- Source-backed analysis, client-ready artifacts, memory updates, handoff notes.

## Hermes

Purpose:
- Background sidecar, scheduled checks, provider experiments, long-running research.

Best at:
- Recurring monitors, exploratory research, queue checks.

Do not do:
- Own final source of truth until provider output is proven reliable.

## Browser Agent

Purpose:
- Browser-only inspection and proof.

Best at:
- Authenticated app state, dynamic pages, screenshots, UI workflows.

Default output:
- URL, observed state, screenshots or extracted evidence, blockers.

## QA Agent

Purpose:
- Adversarial verification.

Best at:
- Testing claims against acceptance criteria and finding missing edge cases.

Do not do:
- Rewrite the feature unless assigned.
