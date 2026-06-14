# Hermes Agent Masterclass 01 - Workiva Notes

Source video: https://www.youtube.com/watch?v=R3YOGfTBcQg
Title: Hermes Agent Masterclass: 1. Installation, Setup, Basic Commands
Channel: Onchain AI Garage
Duration: 28:31
Transcript: auto-generated English transcript fetched 2026-05-05.

## Core Takeaways

Hermes is presented as a terminal-first, provider-agnostic agent that can also run as a messaging gateway. The practical bet is compounding value: Hermes keeps sessions, skills, logs, config, and memory under `~/.hermes`, so repeated work can become reusable agent procedure instead of a one-off chat.

The video focuses on setup, model/provider choice, basic CLI commands, slash commands, skills discovery, config inspection, updates, and one first real task. The first task is competitor research, but the pattern is more important than the domain: give Hermes a repeatable research task, let it use tools, produce an artifact, and allow memory/skills to accumulate.

## Commands And Concepts From The Video

- `hermes` starts chat.
- `hermes model` opens model selection/configuration.
- `hermes gateway` starts messaging gateway for platforms such as Telegram, Discord, Slack, and others.
- `hermes skills browse` discovers installable skills.
- `hermes skills search <query>` searches for skills by topic.
- `hermes config show` shows active configuration.
- `hermes doctor` diagnoses setup issues.
- `hermes update` updates Hermes.
- `/new` starts a fresh session.
- `/model` changes model mid-session.
- `~/.hermes/config.yaml` holds main settings.
- `~/.hermes/.env` holds secrets.
- `~/.hermes/sessions`, `~/.hermes/skills`, `~/.hermes/logs`, and `~/.hermes/memory` are the important runtime folders.
- Do not hand-edit sessions or cron; ask Hermes to manage them.

## Fit For LSL Workiva Projects

Hermes should be used first as a read-only Workiva operating assistant. It is a good fit for tasks that need project context, repeatable procedure, and artifacts:

- ACFR tieout review from snapshots and exported spreadsheets.
- Wdata query inspection and result summarization.
- Chain/run status review.
- Document/spreadsheet export inventory.
- Daily watcher summaries.
- Open-items and client-status drafting from known project files.
- Skill creation from repeated diagnostic workflows.

Hermes should not be the first tool for direct Workiva writes. Direct writes should stay behind the Workiva playbook protocol: consult `memory/fixes_workiva.md` and `memory/errors_workiva.md` before API action, use tested recipes, and keep write authority explicit.

## Recommended Hermes Skill Targets

1. `workiva-readonly-diagnostic`
   - Load shared memory first.
   - Identify client/project.
   - Inspect available snapshots, exports, and read-only MCP tools.
   - Produce findings with source paths and unresolved questions.

2. `workiva-error-playbook-first`
   - Always scan `memory/errors_workiva.md`.
   - Then scan `memory/fixes_workiva.md`.
   - Only start fresh debugging after both fail to match.

3. `acfr-tieout-review`
   - Pull or inspect current snapshot.
   - Run available tieout/check scripts.
   - Compare current failures to known playbook issues.
   - Produce a short status artifact.

4. `wdata-query-inspection`
   - List relevant Wdata queries/tables through read-only tools.
   - Validate/describe queries.
   - Run read-only result checks where safe.
   - Summarize data gaps and stale mapping risks.

## Recommended Hermes Cron Targets

- Daily ACFR watcher digest.
- Daily failed-check summary per active client.
- Weekly Workiva open-items digest.
- Weekly memory/playbook drift review.

Cron output should be written as Markdown artifacts and optionally routed through a messaging gateway later. Start read-only only.

## Current Setup Implication

Your existing Hermes setup already has the right shape for this:

- Memory enabled.
- External skills include `/tmp/claude-config/skills` and `/Users/davebettner/.codex/skills`.
- Workiva read-only MCP server configured.
- Obsidian remains the human UI.
- Git-backed Markdown in `/tmp/claude-config/memory` remains canonical.

Next practical move: build one Hermes skill for `workiva-readonly-diagnostic`, test it against one LSL Workiva project, and only then add scheduled read-only digests.
