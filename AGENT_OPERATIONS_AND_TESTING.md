# Caramel Digital Studio agent operations and testing

**Repository:** `LilyCaramel2/caramel-digital-studio-vs-5`

**Active layer:** static HTML, CSS, Tailwind CDN, and JavaScript.

**Coordination board:** [GitHub Issue #1](https://github.com/LilyCaramel2/caramel-digital-studio-vs-5/issues/1).

## Where important work lives

Repository Markdown files are the durable handovers for future agents. Use clear dated names for substantial decisions, checklists, simulations, payment instructions, and next-agent tasks. Keep the working source in the repository and record each meaningful batch in Issue #1.

The agent handoff log is `AGENT_HANDOFF_LOG.md`. The reusable handoff structure is `AGENT_HANDOFF_TEMPLATE.md`. The deterministic checker is `scripts/check_caramel_repo.py`. The automated workflow is `.github/workflows/caramel-static-checks.yml`.

Payment documentation is split by purpose. Read `PAYMENT_METHODS_LAUNCH_GUIDELINES_2026-11-24.md` for the approved launch menu, `CLIENT_PAYMENT_INSTRUCTIONS_CAPITEC_MUKURU_WISE.md` for client-facing instructions, `GOOGLE_CALENDAR_05A_MANUAL_PAYMENT_TEMPLATES_2026-11-24.md` for private confirmation templates, `GOOGLE_CALENDAR_05A_BOOKING_FLOW_TEST_CHECKLIST_2026-11-24.md` for test steps, and `GOOGLE_CALENDAR_05A_BOOKING_AGENT_SIMULATION_2026-11-24.md` for generated-output examples. Read `WISE_AUTOMATED_PAYMENT_CONFIRMATION_NEXT_AGENT_TASK_2026-11-24.md` before planning Wise automation.

## Start of every agent batch

Read `AGENT_HANDOFF_LOG.md`, the relevant task handoff, and the latest Issue #1 comments. Run:

```bash
python3 scripts/check_caramel_repo.py --json
```

Record the current branch, commit, working-tree state, intended scope, and expected files before editing.

## End of every agent batch

Run the checker again. Review `git diff --check`. Record the changed files, checks, open decisions, and exact next action in `AGENT_HANDOFF_LOG.md`. Add a concise progress comment to Issue #1. Commit only the intended files, push when authorised, then verify:

```bash
git status --short --branch
git rev-parse HEAD origin/main
python3 scripts/check_caramel_repo.py --json
```

The expected release state is a clean working tree with local `HEAD` equal to `origin/main`.

## Offline checker scope

The checker uses Python’s standard library and local Git commands. It checks tracked text files for the retired payment-provider reference, confirms required agent files exist, checks the current branch, checks the upstream branch, verifies local and remote commit alignment, and reports uncommitted changes.

The checker does not send payments, contact clients, open Google Calendar, access Wise, access Capitec, access Mukuru, or verify live Web3Forms delivery. Those require owner-controlled testing and belong in the booking-flow checklist.

## Automated workflow

`.github/workflows/caramel-static-checks.yml` runs the checker on every push and pull request. It uses a read-only repository permission and installs no project dependencies.

## Interruption and resume protocol

If an agent stalls, stop the current process rather than waiting indefinitely. Inspect the terminal and repository state. Keep any completed file changes if they are valid. Run the checker and `git status` before resuming. Continue from the latest handoff-log entry and Issue #1 comment. Never assume that a stalled process completed a commit or push.

If a task ends early, record the partial result, current commit, changed files, checks completed, open decisions, and one next action. A later agent should be able to resume from the repository alone.

## Payment safety boundary

The client chooses a payment method from the owner-approved menu. The menu can include Capitec EFT, Mukuru where suitable, Wise methods, and other approved routes. Ask for country and preferred method, then send only the selected method’s private instructions. Keep PayPal outside the current launch phase.

Use the official bank spelling `Capitec`. Wise options can include payment links, requests, account details, approved email or Wisetag search, QR, card, or Google Pay where enabled in the owner’s account. Use `[OWNER_WISE_REFERRAL_LINK]` until Melissa supplies the final referral URL. Keep payment details, receiving identifiers, referral URLs, access keys, and private records outside public source and Issue #1.
