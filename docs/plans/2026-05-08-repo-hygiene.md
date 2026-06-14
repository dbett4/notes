# Plan: Repo Hygiene and Agent Worktree Management
Date: 2026-05-08
Goal: Build a repeatable repo-management workflow that keeps canonical checkouts clean, routes agent work into isolated worktrees, and makes dirty states intentional and explainable.
Scope: In scope: a local `repo-lane` utility, repo registry, preflight/status classification, worktree creation, closeout flows, ignore-policy checks, and Workiva/ACFR live-session exceptions. Out of scope: rewriting existing repo histories, deleting current dirty files, force-pushing, or changing client delivery gates.
Dependencies: Local Git, existing repo folders under `/Users/davebettner/Documents`, mirror folders under `/Users/davebettner/Documents/Code/_mirrors`, planned worktree root `/Users/davebettner/Documents/Code/_worktrees`, and Dave approval before any destructive cleanup.

## Plan Inputs
Current working folder: `/Users/davebettner/Documents/Personal/notes`

Inspected:
- `/Users/davebettner/Documents/Personal/notes/README.md`
- `/Users/davebettner/Documents/Personal/notes/.gitignore`
- `git status --short --branch` in `/Users/davebettner/Documents/Personal/notes`
- `/Users/davebettner/.codex/memories/MEMORY.md`
- Public references checked during research: Git worktree docs, Git stash docs, GitHub ignore-file docs, pre-commit docs, Atlassian trunk-based development and gitignore guides

Evidence:
- The notes repo currently has no `docs/plans/` folder before this plan.
- The notes repo is dirty and ahead of `origin/main`; it includes many deleted `sports-gambling/` paths plus untracked `ai-x-follow-shortlist.md` and `research/`.
- Existing `.gitignore` only covers `.DS_Store`, Obsidian workspace files, and `.agent/`.
- Prior memory shows a successful safe pattern for D+Bet: agent work in a dedicated worktree to avoid collision with the active repo.
- Prior memory shows a Scottsdale exception: live ACFR repos can contain meaningful dirty evidence, so isolation must not blindly hide or clean current-session files.
- Prior memory shows Forge had a real-checkout mismatch; future tools must verify the actual repo root before editing or committing.

Assumptions:
- The first implementation should live in this notes repo until Dave chooses a permanent home such as `claude-config`, `lsl-forge`, or a dedicated local tools repo.
- The command name can be `repo-lane` unless Dave wants a different name.
- Worktrees should live under `/Users/davebettner/Documents/Code/_worktrees`.

Open questions:
- Permanent home for the utility remains open: this repo, `claude-config`, or a dedicated tools repo.
- Whether `repo-lane` should be shell-first or Python-first remains open until the current local scripting patterns are inspected.

## Task 1: Inventory Existing Repo Lanes
**Goal:** Create a current map of canonical repos, mirror repos, and likely agent worktree roots.
**Type:** Discovery/inspection
**Steps:**
1. Run `find /Users/davebettner/Documents -maxdepth 4 -name .git -type d -print` and save the reviewed repo roots into a draft registry file path chosen in Task 2.
2. Run `git -C <repo-root> status --short --branch` for each known active repo: `/Users/davebettner/Documents/Personal/notes`, `/Users/davebettner/Documents/Code/betting-bot`, `/Users/davebettner/Documents/Code/workiva-mcp`, `/Users/davebettner/Documents/Bradenton`, `/Users/davebettner/Documents/RCTC`, and mirror repos under `/Users/davebettner/Documents/Code/_mirrors`.
3. Classify each repo as `canonical`, `mirror`, `client-live`, `agent-worktree`, or `archive`.
**Verification:** The registry lists each inspected repo with absolute path, remote URL when present, current branch, dirty/clean state, and lane classification.
**Stop condition:** Stop if two paths point to the same remote and it is unclear which one is canonical.
**Rollback:** Delete the draft registry file if the inventory is wrong; no repo state should be changed.

## Task 2: Choose the Utility Home and File Layout
**Goal:** Decide where the first `repo-lane` implementation belongs and create only the needed files.
**Type:** Discovery/inspection
**Steps:**
1. Inspect `/Users/davebettner/Documents/Personal/notes`, `/Users/davebettner/Documents/Code/_mirrors/claude-config`, and any existing local tools folders for scripts or command conventions.
2. Pick one home using this order: existing local tools repo if present, `claude-config` if the utility is cross-agent policy, or `/Users/davebettner/Documents/Personal/notes/tools/repo-lane/` if no better home exists.
3. Define files before editing: command entrypoint, registry file, README/usage note, and tests or smoke-check script.
**Verification:** A short implementation-location note exists in the plan execution log or README, with the selected root and the rejected alternatives.
**Stop condition:** Stop and ask Dave if the selected home would require pushing to a repo he does not want changed.
**Rollback:** Remove only newly created utility files and leave existing repo content untouched.

## Task 3: Implement `repo-lane status`
**Goal:** Provide a read-only status command that classifies repo dirt instead of treating every dirty tree as the same problem.
**Type:** Mutating work
**Steps:**
1. Add a `repo-lane status` command that accepts `--repo <absolute-path>` and defaults to the current directory.
2. Resolve the actual repo root with `git rev-parse --show-toplevel`.
3. Report branch, upstream, ahead/behind counts, tracked dirty files, untracked files, ignored artifact counts, and linked worktrees from `git worktree list --porcelain`.
4. Detect lane type from the registry and print one of: `clean`, `dirty-review-needed`, `dirty-evidence`, `dirty-generated`, or `blocked-unknown`.
**Verification:** Running `repo-lane status --repo /Users/davebettner/Documents/Personal/notes` reports the existing dirty notes repo without modifying files.
**Stop condition:** Stop if status detection cannot distinguish tracked deletions from untracked generated files.
**Rollback:** Remove the new command files or revert the implementation commit before use.

## Task 4: Implement `repo-lane start`
**Goal:** Create a named worktree and branch for agent tasks without dirtying the canonical checkout.
**Type:** Mutating work
**Steps:**
1. Add `repo-lane start <repo-key> <task-slug> --agent <codex|claude|hermes>`.
2. Resolve `<repo-key>` through the registry to an absolute canonical repo path.
3. Refuse to start from a dirty canonical checkout unless the lane policy allows it or `--from-current-dirty` is explicitly supplied.
4. Create the worktree under `/Users/davebettner/Documents/Code/_worktrees/<repo-key>/<agent>-<task-slug>/`.
5. Create the branch `codex/<task-slug>`, `claude/<task-slug>`, or `hermes/<task-slug>` from the configured base branch.
**Verification:** A test run creates a worktree for a non-client repo, `git worktree list` shows it, and the canonical checkout remains unchanged.
**Stop condition:** Stop if the target branch already exists or if the repo has submodules that make worktree behavior unsafe.
**Rollback:** Run `git worktree remove <created-worktree-path>` and delete the created branch only if no work was committed.

## Task 5: Add Workiva and ACFR Lane Rules
**Goal:** Prevent the utility from applying generic cleanup behavior to live client evidence.
**Type:** Mutating work
**Steps:**
1. Add registry fields for `client_live: true`, `requires_session_open: true`, and `allow_dirty_evidence: true`.
2. Mark Scottsdale, Bradenton, PGC, RCTC, and `lsl-acfr` according to their actual local paths after Task 1.
3. For `client_live` repos, make `repo-lane start` print the required session-open command before work begins.
4. For `allow_dirty_evidence` repos, make `repo-lane status` list dirty evidence separately and refuse `close --discard` without an explicit confirmation flag.
**Verification:** Running status against a client-live repo shows the stricter policy and does not suggest cleanup as the default next action.
**Stop condition:** Stop if the current client repo path is ambiguous or points to a stale mirror instead of the active working folder.
**Rollback:** Remove the client-specific registry entries and return to read-only generic status behavior.

## Task 6: Add Ignore-Policy Checks
**Goal:** Route generated files into known ignored artifact folders instead of letting them clutter `git status`.
**Type:** Mutating work
**Steps:**
1. Add an `ignore_check` routine that reports untracked files by pattern and directory.
2. Add approved artifact directories per repo, such as `.agent/`, `.forge-demo-studio/`, `.workiva-snapshots/`, and `.repo-lane/`, only after verifying each repo's existing conventions.
3. Make the tool recommend either a committed `.gitignore` update for shared artifacts or `.git/info/exclude` for local-only clutter.
4. Do not auto-edit `.gitignore` in client repos without a separate explicit approval step.
**Verification:** Running the check in the notes repo recognizes `.agent/` as ignored and flags `research/` or other untracked folders as review-needed instead of generated.
**Stop condition:** Stop if a proposed ignore rule could hide source data, client evidence, scripts, or Markdown notes.
**Rollback:** Revert any `.gitignore` changes and remove only the new ignore-check code.

## Task 7: Implement `repo-lane close`
**Goal:** End an agent lane with a clear result: commit, park, preserve evidence, or discard with approval.
**Type:** Mutating work
**Steps:**
1. Add `repo-lane close --commit`, `repo-lane close --park`, `repo-lane close --evidence`, and `repo-lane close --discard`.
2. For `--commit`, require clean verification commands to be recorded in the closeout summary.
3. For `--park`, write a local handoff note under `.repo-lane/parked/<branch>.md` and leave the worktree intact.
4. For `--evidence`, require a destination evidence folder and write a summary of why the dirty files remain.
5. For `--discard`, require an explicit flag and print the exact files that would be lost before any destructive command.
**Verification:** Each close mode can be run against a disposable test repo and leaves an auditable summary.
**Stop condition:** Stop if a close operation would remove untracked files not created by the current lane.
**Rollback:** For committed work, use `git revert` or branch deletion only after review; for parked work, keep the worktree and remove only the closeout note if incorrect.

## Task 8: Add Smoke Tests with a Disposable Repo
**Goal:** Prove the workflow without risking real client or product repos.
**Type:** Verification
**Steps:**
1. Create a disposable repo under `/tmp/repo-lane-smoke` or another clearly temporary path.
2. Initialize commits, dirty tracked files, untracked files, ignored files, and one linked worktree.
3. Run `repo-lane status`, `repo-lane start`, and each non-destructive close path.
4. Record expected and actual output in a smoke-test transcript.
**Verification:** Smoke tests pass and demonstrate no destructive action occurs without an explicit discard mode.
**Stop condition:** Stop if any command changes files outside the disposable repo.
**Rollback:** Delete the disposable repo after saving only the relevant test transcript if needed.

## Task 9: Document the Operating Rule
**Goal:** Make the workflow usable by Dave, Codex, Claude, and Hermes without re-explaining it in chat.
**Type:** Handoff
**Steps:**
1. Write a concise README or memory note with the canonical rule: clean checkout for review, worktree per agent task, generated artifacts in approved ignored folders, client-live exceptions preserved.
2. Include command examples for `status`, `start`, and `close`.
3. Include a warning that `stash` is temporary parking, not the default workflow.
4. If the final home is shared memory, sync the note according to the shared memory process.
**Verification:** A new session can read the note and run the first command without asking where repos live.
**Stop condition:** Stop before syncing shared memory if the implementation has not passed smoke tests.
**Rollback:** Remove or supersede the note if the utility interface changes before adoption.

## Task 10: Pilot on One Non-Client Repo
**Goal:** Validate the workflow on a real repo with low delivery risk.
**Type:** Verification
**Steps:**
1. Choose one non-client repo from the registry, preferably Forge or betting-bot if currently available and not in a high-risk delivery state.
2. Run `repo-lane status` and save the output.
3. Create a no-op or documentation-only worktree with `repo-lane start`.
4. Close it using `repo-lane close --park` or `repo-lane close --discard` depending on whether any useful artifact was created.
**Verification:** The canonical checkout remains in its original state and the worktree lifecycle is visible through `git worktree list`.
**Stop condition:** Stop if the selected repo is already dirty with unrelated changes that need human review.
**Rollback:** Remove the pilot worktree and branch if no committed work should remain.

## Self-Review Checklist
- [x] Discovery was performed before the task list was written
- [x] Current working folder is recorded
- [x] Inspected files/scripts/docs are listed
- [x] Evidence, assumptions, and open questions are separated
- [x] Every task has a concrete verification step
- [x] Every task has a stop condition
- [x] No task contains placeholder language
- [x] File paths are exact where discovered; unresolved locations are marked as open questions
- [x] The plan addresses the full scope and does not assume cleanup happens automatically
- [x] Rollback is noted for mutating or destructive tasks
