# Agent Team Folder

**As of:** 2026-05-18

This folder is the project-local operating layer for coordinator-led agent work.

Use this when an LSL, client, internal tooling, product, automation, research, or personal project needs multiple agents, autonomous continuation, scoped handoffs, or durable queues.

The template is domain-neutral. Put a copy inside the relevant Git-backed project folder so the execution record travels with the work.

For LSL work, use this for client delivery, Workiva/ACFR work, Forge/internal tooling, client prep, marketing/business development, reusable standards, and automation. For LSL-branded artifacts, teal and charcoal should dominate; green is secondary.

## Files

- `coordinator.md` - coordinator role, loop, and project rules.
- `agent_registry.md` - standing role cards for specialist agents.
- `task_board.md` - current ready, active, review, blocked, and done queues.
- `decision_log.md` - durable project decisions.
- `blockers.md` - blockers separated from ordinary work.
- `task_packet_template.md` - copy for each new task.
- `handoff_template.md` - copy when an agent returns work or transfers ownership.
- `handoffs/` - completed handoff notes.
- `proof/` - verification artifacts.
- `queues/` - optional split queue files for larger projects.

## Startup

1. Coordinator reads `task_board.md`, `blockers.md`, `decision_log.md`, and latest files in `handoffs/`.
2. Coordinator selects one ready task or writes a new task packet.
3. Coordinator dispatches the packet to the specialist agent named as owner.
4. Specialist returns proof and, when needed, writes a handoff file.
5. Coordinator reviews proof and moves the task to `done`, `blocked`, or back to `ready`.
