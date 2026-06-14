# HTML Artifacts and Completion Gates

**As of:** 2026-05-09

## Purpose

This is the two-part agent standard for Dave's Codex, Claude, and related local-agent work.

Agents should produce better review surfaces and stronger proof of completion. The standard has two parts:

1. **HTML artifact standard:** use standalone HTML when the output needs to be reviewed, decided on, presented, explored, or shared.
2. **Completion gate standard:** define "done means..." before meaningful work, then finish with evidence that proves the work is done.

This is an operating standard, not a one-off habit. Reusable procedures should become skills or playbooks once the route works end-to-end.

## Part 1: HTML Artifact Standard

### Rule

Use standalone HTML when the output is meant for review, decisions, presentation, dashboards, plans, exploration, or client-facing communication.

Keep Markdown for logs, recipes, memory, source-of-truth notes, handoff records, implementation plans, and durable playbooks.

### Use HTML For

- Client-ready review packets, status summaries, and decision briefs.
- Workiva or ACFR diagnostics where tables, visual grouping, or page-level review matters.
- Forge or app QA summaries that benefit from screenshots, state tables, or rendered flows.
- Research digests where the user needs to scan, filter, compare, or decide.
- Dashboards, scorecards, visual maps, diagrams, and executive summaries.
- Plans that need hierarchy, decision points, risks, and acceptance gates visible on one page.

### Use Markdown For

- Memory files and recurring recipes.
- Session logs and handoffs.
- Source-of-truth notes in Obsidian.
- Implementation plans that another agent will execute.
- Simple answers, command notes, and raw findings.
- Anything that should remain easy to diff, merge, quote, or sync through Git.

### Required HTML Structure

Every standalone HTML artifact should include:

- A clear title and date.
- An executive summary at the top.
- A "Decision Needed" or "Recommended Action" section when the artifact supports a choice.
- Status blocks for key outcomes, risks, blockers, and next actions.
- Source/evidence sections with links, file paths, screenshots, or command outputs as applicable.
- Tables for comparisons, checklists, mappings, or issue inventories.
- Diagrams when the workflow, architecture, data flow, or decision tree is non-trivial.
- A verification section that states what was checked and what remains unverified.

### HTML Quality Bar

Standalone HTML must be self-contained unless there is a deliberate reason to depend on app assets. It should open locally without a build step.

The artifact should be readable at desktop and laptop widths, use restrained styling, and avoid decorative filler. LSL-branded work should lean on teal and charcoal, with green used sparingly.

Do not use HTML as a prettier Markdown dump. Use it when layout, scanning, hierarchy, comparison, filtering, visual grouping, or presentation quality changes the usefulness of the output.

### File Placement

Store HTML artifacts near the work they support:

- Client or Workiva artifact: project folder under a dated review/export/artifacts directory.
- Forge or app artifact: repo-local `artifacts/`, `docs/reviews/`, or existing project convention.
- Personal research artifact: `~/Documents/Personal/notes/research/` or a topic-specific folder.
- Agent workflow artifact: `~/Documents/Personal/notes/agent-ops/artifacts/`.

Markdown standards and recipes stay in the notes vault or shared memory. HTML artifacts are review surfaces, not the canonical memory layer unless explicitly promoted.

## Part 2: Completion Gate Standard

### Rule

Every meaningful agent task must define completion before execution and finish with evidence.

The agent should not claim completion because the intended edits were made. It should claim completion only when the agreed checks pass or when the remaining gaps are named clearly.

### Required "Done Means..." Criteria

Before starting meaningful work, define:

- The intended outcome.
- Files, systems, or artifacts in scope.
- Explicit out-of-scope boundaries.
- Required verification evidence.
- Stop conditions: missing data, blocked credentials, destructive action, client approval, or ambiguous source of truth.

Use this format when the task is more than a small answer:

```markdown
Done means:
- [ ] Outcome achieved: ...
- [ ] In-scope files/systems touched: ...
- [ ] Verification evidence collected: ...
- [ ] Known gaps or blocked items named: ...
```

### Required Completion Evidence

Completion evidence depends on task type:

| Task type | Required evidence |
|---|---|
| Code change | File diff summary, tests/build/lint where relevant, and a note if tests could not run. |
| Frontend/UI change | Browser check, screenshot or visual inspection summary, responsive check when relevant, and console/error check. |
| Local app or Forge change | Local or public-surface verification, endpoint/browser check, and logs/errors reviewed. |
| Workiva/API action | Playbook consulted, target/workspace verified, dry-run or read-only inspection when possible, API result checked against expected state. |
| ACFR/financial work | Tieout, source path, control totals, exception list, and any client-blocked items separated from agent-blocked items. |
| Research | Current sources, date checked, source quality, recommendation, and unresolved uncertainty. |
| Writing/client prep | Intended speaker/audience, concise conclusion, source facts verified, and tone matched to Dave or the actual speaker. |
| Memory or standards update | `**As of:** YYYY-MM-DD`, canonical file path, stale recipe replaced when applicable, and sync status if shared memory changed. |

### Browser Verification Gate

Browser verification is mandatory when a task changes:

- UI layout, styling, or interaction.
- A local web app or public web surface.
- Screenshots, charts, dashboards, reports, or embedded visual assets.
- Authentication, routing, upload, download, or form flows.

Minimum browser evidence:

- Page or route opened.
- Primary interaction exercised.
- No obvious render breakage.
- Console/network errors checked when available.
- Screenshot captured or visual state described.

For public Forge work, verify the public/tunneled surface when the user reported the issue there.

### Workiva Gate

Before any Workiva write, format, row insert, structural edit, Wdata connection, or direct API action:

- Consult `memory/fixes_workiva.md`.
- Consult `memory/errors_workiva.md`.
- Verify the target workspace/project/folder/file.
- Prefer read-only inspection before mutation.
- Use proven recipes when one matches.
- Stop at approval gates when the task is client-facing or delivery-sensitive.

For new ACFR diagnostic or write scripts, start from the shared ACFR script template rather than a blank file.

### Evidence Language

Final responses should say what was proven, not just what was attempted.

Good:

```text
Done. I updated the standard, opened the local HTML report in-browser, and verified the decision table renders without console errors.
```

Bad:

```text
Done. This should work now.
```

If verification is incomplete, say that directly:

```text
Implemented, but not fully verified. The local build passed; I could not verify the public Workiva state because credentials were unavailable.
```

## Examples

### Workiva Diagnostic

Use Markdown for the source-of-truth recipe. Use HTML for the review packet if Dave or a client needs to inspect exceptions, tieouts, screenshots, status, or decision points.

Done means:

- Target workspace and file verified.
- Relevant Workiva playbook entries checked.
- Read-only snapshot or API state inspected before any mutation.
- Tieout or exception report produced.
- Any client-blocked items separated from agent-blocked items.

### Forge/Public App QA

Use HTML when summarizing a bug investigation or QA pass with screenshots, reproduction steps, status blocks, and endpoint results.

Done means:

- Real serving checkout confirmed.
- Local and public surface checked as applicable.
- Browser route opened and interaction exercised.
- Console/network errors reviewed.
- Fix verified against the original reported surface.

### Client Prep

Use HTML for meeting packets, stakeholder-ready dashboards, and decision briefs. Use Markdown for the durable prep note or follow-up email draft.

Done means:

- Intended speaker and audience identified.
- Status, blockers, and asks are visible at the top.
- Claims trace to source notes, emails, files, or current system state.
- Tone matches Dave or the named speaker.

### Personal Research

Use HTML when the research needs comparison, ranking, filters, or a decision surface. Use Markdown for evergreen notes and recipes.

Done means:

- Current sources checked when the topic can drift.
- Recommendation stated directly.
- Uncertainty and source limits named.
- Useful findings promoted into the relevant note or recipe.

## Adoption Path

1. Use this Markdown standard as the source of truth.
2. Create a reusable skill/playbook that enforces the two gates.
3. Add lightweight templates for common HTML artifacts.
4. Add task-type checklists for Workiva, Forge, client prep, and research.
5. Promote proven routes into the appropriate memory recipe once they work end-to-end.

## Source Basis

- Anthropic Claude Code guidance: verification is the highest-impact agent workflow improvement.
- Claude skills documentation: reusable procedures belong in skills/playbooks rather than bloated global instructions.
- Agent workflow examples: rich standalone HTML improves review, presentation, and decision-making when Markdown becomes too flat.
- Local operating preference: Git-backed Markdown remains the source of truth; Obsidian is the human UI; HTML is the review surface.
