# Caramel Digital Studio — Agent Handoff Log

This file is the durable coordination log for agents and instances working on the Caramel Digital Studio website. Add a dated entry after each meaningful inspection, implementation, review, or deployment task.

## Operating rules

1. Read this file before changing the website.
2. Inspect the live page and current source before editing.
3. Treat approved existing website copy, prices, layout, and styling as locked unless the owner explicitly approves a change.
4. Record what was inspected, what changed, what did not change, unresolved decisions, and the exact next step.
5. Keep the matching GitHub Issue updated so agents can coordinate outside a single Manus instance.
6. Never publish or deploy without a separate owner approval after the review build is checked.
7. Never expose internal hourly, weekly, quarterly, or effective-rate calculations on the public site.
8. Write in affirmative language. Describe what each service delivers, how it works, and who it helps. Remove negative comparisons and exclusion-led explanations from public copy. Prefer plain, direct sentences.
9. Read `AGENT_HANDOFF_2026-11-18_CARAMEL_VOICE.md` before writing public copy. Use Caramel’s agentic-age positioning, founder-led delivery, built-in lead generation, direct working relationship, and staged path into connected systems.
10. Use `AGENT_HANDOFF_TEMPLATE.md` for each meaningful agent handover. Record the task, repository, source inspected, decisions, files, checks, open decisions, deployment state, and next action.
11. Use UK English for UK and South African audiences. Use US English for US audiences. Choose the audience before writing public copy.
12. Use commas, full stops, colons, and semicolons in place of long em dashes. Keep language plain, direct, specific, and affirmative.
13. Use agents, developers, orchestrators, owners, and users for role-specific references. Present AI as a tool that extends capability. Learn AI to Earn is the education pathway for learning how to wield, prompt, and secure AI tools.
14. Use Markdown handovers, GitHub Issue updates, code drafts, and checklists for the solo-developer workflow. Presentation outlines remain planning notes unless Melissa explicitly requests a deck.

---

## 2026-11-18 — live baseline and coordination system established

### Agent

Manus, current sandbox session.

### User objective

Create a durable handoff process for multiple agents and instances. Use a Markdown log in the repository and GitHub Issues as the shared coordination board. Preserve the existing live pricing page and styling while preparing future additions safely.

### Inspected

- Live pricing page: https://www.carameldigitalstudio.com/pricing.html
- Live visual treatment: dark navy background, cream/white editorial type, coral/pink emphasis, restrained green and yellow details, thin borders, generous spacing, premium cards, existing CTA and navigation treatment.
- Repository: https://github.com/LilyCaramel2/caramel-digital-studio-vs-5
- Repository source: `pricing.html`, `styles.css`, `index.html`, `capabilities.html`, `start.html`, `work.html`, `script.js`, and existing assets.
- Existing pricing page source matches the live locked structure and includes website builds, payment structure, hosting/care, SEO/content, business add-ons, brand direction, empowerment access, and client terms.
- Fiverr profile URL: https://www.fiverr.com/lilly_caramel

### Important verification result

Fiverr returned a human-verification screen in the available browser session. The exact visible review count could not be independently read. Do not publish an independently verified exact review claim until the owner checks the profile in a normal browser session. The profile link may be added with wording such as “View Lily’s Fiverr profile and client reviews.”

### No website changes made in this entry

No pricing copy, styling, package, navigation, or live deployment was changed. This entry establishes the coordination system and records the locked baseline.

### Approved future direction recorded elsewhere

The working handoff specification is:

`/home/ubuntu/Caramel_Digital_Studio_Tiered_Pricing_and_Scaling_Ladder.md`

It contains the tiered pricing ladder, Stage 1–3 fixed prices, full SEO and long-form writing positioning, consultation products, advanced systems boundaries, Fiverr verification note, visual preservation rules, and pre-approval checklist.

### Next agent must do before editing

1. Read this log and the tiered pricing handoff.
2. Confirm the owner has approved which additions may be placed on the locked pricing page.
3. Create a Git branch or review checkpoint.
4. Add only non-destructive sections using the existing CSS classes and visual language.
5. Preserve every existing package, price, term, section, layout rhythm, and CTA unless an explicit written change is recorded.
6. Add full SEO, long-form writing, consultation/booking, and the staged scaling ladder only in approved new sections.
7. Add the Fiverr link, but use the exact review-count wording only after the owner verifies it.
8. Run desktop/mobile visual checks and leave a clear review note in the matching GitHub Issue.
9. Do not publish automatically.

### Handoff status

**Status: coordination system created; website implementation pending owner-approved review build.**


## 2026-11-23 — public pricing, proof, copy, and visual repair batch

### Agent

Manus, current sandbox session.

### Inspected

Reviewed the current `main` checkout, `index.html`, `pricing.html`, `start.html`, `work.html`, `capabilities.html`, `styles.css`, the public Fiverr and LinkedIn profile URLs, the existing voice guidance, consultation integration records, and the Cloudflare/Vercel architecture note. Fiverr presented a human-verification challenge, so the exact review count was not independently read in this session.

### Changed

- Replaced the old R190/R370/R610 care cards with the approved R499/R699/R999 Care Plans and R1,500/R2,500/R4,500 setup fees.
- Added the six-month initial term and month-to-month continuation with 30 days’ notice.
- Removed the overlapping public Empowerment monthly cards and retained Empowerment as an access pathway delivered through the Care Plans.
- Updated `start.html` with demo-first wording, 50/50 small-site terms, and 40/40/20 larger-build terms.
- Corrected the work proof block with the owner-approved Fiverr claim, a direct Fiverr link, and a direct LinkedIn profile link.
- Replaced placeholder social links with only the verified LinkedIn destination.
- Restored the near-black visual system by reducing glass opacity and removing the shared radial glow treatment.
- Rewrote the most generic homepage positioning around AI search/AEO, lead generation, repositioning, career landing pages, Learn AI to Earn, and connected systems.
- Created `AI_HANDOFF_CDS_AUDIT_AND_NEXT_BATCH_2026-11-23.md` with the complete findings and next review batch.

### Deliberately not changed

No Gaia, Lily-code, Lotus OS, High Tide Tours, Learn AI to Earn, Cape Plaster & Pools, client site, Vite workflow, booking provider, payment integration, GitHub Actions workflow, Cloudflare configuration, Vercel configuration, deployment, commit, or push was performed.

### Review state

The repair is uncommitted and requires owner review. Run source, accessibility, link, and desktop/mobile visual checks before any commit or deployment.

### Next concrete action

Render and review the four changed public pages, then ask Lily to approve the named repository, branch, and phase before committing, pushing, or deploying.


## 2026-11-23 — repair committed and pushed

The pricing/style diff was reviewed again after the initial repair. The remaining pricing-page glow fields were reduced from `bg-pink/10` and `bg-yellow/10` to near-invisible values, the pricing cards moved from heavy `shadow-2xl`/`backdrop-blur-xl` treatment to restrained black `shadow-lg`/`backdrop-blur-md`, and the pink elevated-card hover shadow was replaced with a black depth shadow.

Source validation passed for HTML parsing, approved Care Plan prices, removal of the old Care Plan prices, six-month terms, 50/50 and 40/40/20 payment language, Fiverr and LinkedIn URLs, no placeholder links, near-black tokens, no guessed Learn AI to Earn domain, no residual pricing glow fields, and no pink hover shadow. `git diff --check` passed.

Commit `dc37624` — `repair CDS V5 pricing proof and visual system` — was pushed successfully to `origin/main` in `LilyCaramel2/caramel-digital-studio-vs-5`.

No Vercel deployment, Cloudflare change, booking integration, GitHub Actions workflow, or unrelated silo work was performed. The next concrete action is live/public deployment verification through the existing hosting path, not another content-planning pass.

## 2026-11-23 — live verification completed

After the push, the first raw public requests returned a 403 edge response. A retry with a standard browser user-agent returned HTTP 200 for `pricing.html`, `start.html`, and `work.html`.

The live HTML confirmed the corrected `#030508` near-black token, `R499` Care Plan pricing, `50% to begin` payment wording, and the direct Fiverr profile link. The live verification completed successfully through the existing Cloudflare/Vercel path. No further repair batch is pending from this audit.


## 2026-11-23 — 05A static integration and skill workflow prepared

### Agent

Manus, current sandbox session.

### Confirmed boundary

The current Version 5 website remains a static HTML, CSS, Tailwind CDN, and JavaScript build. The 05A Digital Marketing Guidance section belongs in the current pricing page and uses the existing Web3Forms enquiry handler. Next.js, HubSpot, Supabase, Render, and Linear remain a separate future connected-systems task.

### Created

- `AGENT_HANDOFF_TEMPLATE.md` with the latest audience, language, positive-copy, restricted-vocabulary, architecture, validation, and coordination rules.
- `PRICING_05A_WEB3FORMS_CONSULTATION_COMPONENT.html` with Web3Forms-compatible consultation fields and positive CTA copy.
- `NEXT_AGENT_TASK_05A_AND_CONNECTED_SYSTEMS.md` with the exact Issue #1 follow-on task.
- `/home/ubuntu/skills/caramel-digital-studio/SKILL.md` with Caramel-specific repository, visual, language, 05A, Google Workspace, and staged architecture rules.
- `/home/ubuntu/skills/agentic-studio-build/SKILL.md` with the transferable client-build workflow.

### Open decisions

The owner must supply or approve the live Google Calendar appointment URLs. The Web3Forms access key remains an owner-managed project value. The 05A section requires owner review before merge or publication.

### Next concrete action

The next agent should review Issue #1, integrate the 05A component into `pricing.html`, connect the approved booking URLs, run desktop/mobile/accessibility/link/language/form checks, and prepare the separate HubSpot/Supabase/Render/Linear architecture handoff.


## 2026-11-23 — 05A pre-integration inspection

### Repository state

The repository is on `main`, clean, and aligned with `origin/main` at commit `03051cd` before this inspection.

### Inspected

Reviewed `NEXT_AGENT_TASK_05A_AND_CONNECTED_SYSTEMS.md`, `pricing.html`, `start.html`, `script.js`, `styles.css`, `PRICING_05A_WEB3FORMS_CONSULTATION_COMPONENT.html`, and `GOOGLE_CALENDAR_05A_BOOKING_WIDGET.html`.

### Findings

`pricing.html` is a static Tailwind CDN page with inline section patterns and shared `styles.css` tokens. Business Add-ons is section 05 and Brand Direction is section 06, so 05A belongs between those sections. `start.html` already contains the active Web3Forms access-key field and the `data-enquiry-form` marker. `script.js` submits every matching form to the Web3Forms API and provides status, success, and error states. A Web3Forms link is unnecessary for the current integration. Dashboard access becomes useful for delivery settings, recipient changes, spam controls, or delivery review.

The current 05A draft uses a placeholder access key and a separate visual treatment, so the next implementation pass should copy its fields and positive wording into the pricing page while adopting the existing pricing section classes and project access-key pattern. Google Calendar URLs remain owner-supplied placeholders until appointment schedules exist.

### Changes in this inspection pass

Updated the active Caramel-specific and transferable client-build skills with the inspected pricing, form-marker, access-key, status-state, placeholder, and provider-reuse rules. No public pricing source was changed.

### Next action

Create a review build that integrates 05A into `pricing.html`, preserves the existing Web3Forms route, and replaces the draft-only styling with the pricing page’s established layout tokens. Keep Calendar URLs as placeholders and request owner review before merge or publication.


## 2026-11-23 — static-first architecture rule reaffirmed

Every site begins as a static HTML, CSS, Tailwind, and JavaScript build. The static version receives review and owner approval first. The approved site moves to Next.js later as a separate connected-systems phase. Next.js, HubSpot, Supabase, Render, Linear, and chatbot systems remain outside the current static source until that phase receives approval.


## 2026-11-23 — 05A review build integrated

### Scope completed

Integrated the 05A Digital Marketing Guidance section into `pricing.html` between Business Add-ons and Brand Direction. The section uses the existing dark pricing layout, shared visual tokens, `data-enquiry-form`, the project Web3Forms access-key pattern, and the shared deferred `script.js` handler.

### Exact fields

The form contains Name, Email, Business or project, Website, Guidance area, and Your priority. Guidance options are Digital marketing strategy, SEO and content, Social channel setup, AI tools and workflow, Connected systems planning, and Launch planning. Hidden provider fields include subject, sender name, and botcheck.

### Checks

The static parser found no local-link errors or duplicate IDs. The 05A form marker and shared script are present. All four required user fields are present and labelled. The draft Web3Forms key placeholder and Calendar URL placeholder are absent from the integrated pricing page. The 05A block contains no long em dash. HTTP served `pricing.html` with status 200, and the Web3Forms handler was served from `script.js`.

Chromium renders were captured at 1440px, 768px, 390px, and 320px widths. Desktop, tablet, mobile, and narrow layouts rendered successfully. The mobile navigation toggle is active through the shared script. The review build remains owner-review material.

### Language and skill governance

Created `AGENT_LANGUAGE_PROTOCOL.md` as the shared language, word-filter, negative-comparison, static-first, and handover source for every build. Updated the Caramel skill, generic client-build skill, handover template, and current log. Created the separate Lotus OS Gaia skill and kept its mission and architecture guidance isolated from Caramel.

### Pricing and seasonal note

No summer-launch, Christmas, January, FOMO, or future pricing increase copy was added. Those commercial decisions remain open for a separate pricing-content approval pass. Existing locked pricing remains unchanged.

### Next action

Review the 05A section in the live review build, approve the consultation wording and prices, create the Google Calendar appointment schedules, then replace the Calendar placeholders in a separate approved pass. Keep Next.js and connected systems in the later migration phase.


## 2026-11-23 — January pricing draft and migration hold

Created `JANUARY_PRICING_AND_CHRISTMAS_PROMO_GUIDELINES_DRAFT.md` and `NEXT_AGENT_TODO_AND_HANDOVER_2026-11-23.md`. The current priority is the static website, 05A consultation, Google Calendar setup, seasonal approval, pricing QA, and agent handovers. The Next.js migration and connected systems remain on hold.


## 2026-11-24 — Issue #1 and Web3Forms status clarification

### Scope

Reviewed GitHub Issue #1, the Google Calendar 05A handoff, `pricing.html`, `start.html`, and `script.js` after the owner queried the proposed four appointment schedules and Web3Forms error handling.

### Exact Issue #1 state

- Issue: `#1`, `Agent coordination: locked pricing page and staged service additions`.
- State: open.
- Repository: `LilyCaramel2/caramel-digital-studio-vs-5`.
- Branch: `main`.
- Working tree: clean before this documentation entry.
- Latest commit at review: `3ce9a03`, `document approved MIT license`.
- Existing issue records 05A as a review build and records Google Calendar schedules as open owner decisions.

### Google Calendar clarification

The phrase “four schedules” comes from `GOOGLE_CALENDAR_05A_INTEGRATION_HANDOFF_2026-11-18.md`. It describes four proposed appointment types:

1. Free project-fit conversation, 30 minutes.
2. Digital Marketing Consultation, 60 minutes, R950.
3. Digital Marketing Strategy Session, 90 minutes, R1,350.
4. Advisory Session, 60 minutes at R900 per session within the R2,700 block.

These are proposed options in the handoff. They are not confirmed schedules, live URLs, or completed Google Calendar configuration. Owner approval is required before creation.

### Web3Forms verification

- `start.html` and `pricing.html` load the shared deferred `script.js`.
- Both forms use `data-enquiry-form`.
- Both forms contain the configured Web3Forms access-key field without exposing the value in this log.
- Both forms contain a `[data-form-status]` live status element and a submit button.
- `script.js` prevents the native submit, sends `FormData` to `https://api.web3forms.com/submit`, checks both HTTP status and the Web3Forms `success` value, resets the form after success, writes status text, catches network, JSON, and API errors, and re-enables the submit button in `finally`.
- The missing-key path gives a direct-email fallback and leaves the button available.
- Current edge cases for a later hardening pass: missing form controls would raise a JavaScript error, non-JSON responses use the generic fallback after JSON parsing fails, and requests have no timeout or abort controller. The current HTML supplies the required controls, so the existing flow is structurally connected.

### Files changed

This review changes documentation only. No public HTML, CSS, JavaScript, pricing, or booking URL was changed.

### Next action

Melissa decides which consultation options to offer. After approval, create only the approved Google Calendar Appointment Schedules under `carameldigitalcontent@gmail.com`, configure the agreed availability, Meet, payment, reminders, and notifications, then add the resulting URLs to the approved 05A booking location and test the flow.


## 2026-11-24 — Google Pay and Wise payment-route cleanup

### Scope

Reviewed the Google Calendar handoff, booking decision, advisory decision, manual-payment templates, and every comment on GitHub Issue #1 for obsolete payment-provider wording.

### Decisions

- Google Pay and Wise are the documented manual payment routes.
- The owner checks payment receipt before confirming a paid appointment.
- The owner sends the Google Calendar and Google Meet details after receipt confirmation.
- Private payment identifiers remain outside the repository and GitHub Issues.
- Option A remains the recommended public advisory structure: one 60-minute R900 session per booking.

### Documentation work

- Updated the Google Calendar integration handoff.
- Updated the older Google Calendar booking decision.
- Added `GOOGLE_CALENDAR_05A_MANUAL_PAYMENT_TEMPLATES_2026-11-24.md` with the manual process, Google Pay email, Wise email, payment-received email, pending-confirmation email, and advisory wording.
- Removed the obsolete presentation outline because agent handovers use Markdown files and GitHub Issues.
- Updated all four Issue #1 comments that contained the retired payment-provider wording.

### Verification

Repository and Issue #1 scans show zero residual matches for the retired payment-provider reference. No public website HTML, CSS, JavaScript, pricing, or booking URL changed.

### Next action

The owner approves the final payment wording and supplies private Google Pay or Wise instructions through a secure channel. An agent then configures only the approved Google Calendar appointment options and completes the manual confirmation test.


## 2026-11-24 — manual booking-flow test checklist and skill update

### Scope

Added a repeatable agent checklist for the complete consultation journey using Web3Forms, Google Pay or Wise manual confirmation, Google Calendar, Gmail, and Google Meet.

### Files added or updated

- Added `GOOGLE_CALENDAR_05A_BOOKING_FLOW_TEST_CHECKLIST_2026-11-24.md`.
- Updated `.agent-skills/caramel-digital-studio/SKILL.md` with the approved manual payment route, Option A advisory structure, private-data boundary, and checklist references.
- Updated `.agent-skills/agentic-studio-build/SKILL.md` with a provider-neutral manual payment and booking-flow test pattern.

### Validation scope

The checklist covers preparation, Web3Forms enquiry, Google Pay instructions, Wise instructions, payment receipt, Calendar and Meet confirmation, advisory sessions, changes, cancellations, failure states, evidence, and Issue #1 handover.

### Next action

An agent runs the checklist with owner-approved test instructions, records results privately, updates Issue #1, and requests owner approval before publication.


## 2026-11-24 — client-choice payment menu and launch guidelines

### Owner correction

Payment selection belongs to the client. Country and location guide the available menu, while the client chooses the method that suits their account, currency, access, and preference.

The approved menu can include South African EFT to Capitec, Mukuru where suitable, Wise payment links or requests, Wise account details, Wise email or Wisetag search, card or Google Pay through Wise where enabled, and other owner-approved methods. The official bank spelling is `Capitec`.

PayPal sits outside the current launch phase. A separate owner decision and demand check can review it later.

### Documentation

- Added `PAYMENT_METHODS_LAUNCH_GUIDELINES_2026-11-24.md`.
- Added `CLIENT_PAYMENT_INSTRUCTIONS_CAPITEC_MUKURU_WISE.md`.
- Updated `GOOGLE_CALENDAR_05A_MANUAL_PAYMENT_TEMPLATES_2026-11-24.md` with client-choice routing.
- Updated `GOOGLE_CALENDAR_05A_PAYMENT_AND_ADVISORY_DECISION_2026-11-24.md`.
- Updated the booking-agent simulation with Capitec, Mukuru, and Wise client-choice branches.
- Updated the Caramel and generic build skills.

### Wise referral boundary

Use `[OWNER_WISE_REFERRAL_LINK]` until Melissa supplies the final Wise referral URL. Never invent or publish a referral URL. Use the referral link when a client chooses to open or use Wise through an onboarding route and the owner’s approved link is available.

### Research record

Official Wise guidance reviewed for payment links, account details, USD receiving options, Wisetag, and Wise-supported Google Pay scenarios. Wise capabilities depend on account type, country, currency, and current product availability. The next agent must verify the owner’s account before selecting a client method or building automated confirmation.

## 2026-11-24 — offline checker and automated static workflow

### Scope

Added a dependency-free repository checker, GitHub Actions workflow, and durable agent operations guide. No public website source or payment configuration changed.

### Files added

- `scripts/check_caramel_repo.py` checks tracked text files, retired-provider references, required agent files, branch state, upstream alignment, and uncommitted changes.
- `.github/workflows/caramel-static-checks.yml` runs the checker on pushes and pull requests with read-only repository permission.
- `AGENT_OPERATIONS_AND_TESTING.md` explains where handovers live, how agents start and finish batches, how to recover from stalls, and what the offline checker can and cannot verify.

### Validation

The checker uses only Python’s standard library and local Git commands. It installs no dependencies and does not contact payment providers. GitHub Actions handles detached pull-request checkouts by validating repository content while local release checks remain strict about upstream alignment.

### Next action

Run the checker after commit and push. Review the first GitHub Actions result. Continue with owner-controlled payment and Calendar testing only after the repository checks pass.


## 2026-11-24 — incoming-agent payment documentation review

### Scope

Reviewed `AGENT_OPERATIONS_AND_TESTING.md`, the launch guidelines, client instructions, manual templates, booking-flow checklist, booking-agent simulation, Wise automation task, repository-managed skills, and the latest Issue #1 status comments.

### Confirmed coverage

Incoming agents now have a direct file map for Capitec EFT, Mukuru, Wise payment links and requests, Wise account details, approved email or Wisetag search, QR, card, Google Pay where enabled, Wise referral handling, client-choice flow, manual confirmation, simulations, and future automation discovery.

The official bank spelling is `Capitec`. The Wise referral placeholder is `[OWNER_WISE_REFERRAL_LINK]`. PayPal remains outside the current launch phase. Private receiving details remain outside source control and Issue #1.

### Verification

The offline checker passed manually at commit `95663d9`. It found zero retired-provider matches, zero missing required agent files, a clean working tree, and local `HEAD` aligned with `origin/main`. The latest Issue #1 comments include the automated workflow status and tested results.

### Files changed

Updated `AGENT_OPERATIONS_AND_TESTING.md`, `.agent-skills/caramel-digital-studio/SKILL.md`, and `.agent-skills/agentic-studio-build/SKILL.md`. No public website source or payment configuration changed.

### Next action

Commit and push this documentation-only update, rerun the checker, validate both repository-managed skills, and add the final status to Issue #1.

## 2026-11-25 — verification and next-agent batches

### Verification

Reviewed the payment document map and launch boundary. `Capitec` spelling, Mukuru routing, Wise options, `[OWNER_WISE_REFERRAL_LINK]`, client choice, privacy boundary, and PayPal launch exclusion are present. Both repository skills remain valid. The offline checker passed: 45 files checked, zero retired-provider matches, zero missing agent files, clean tree, and `HEAD` aligned with `origin/main` at `5ec05e2`.

### Next-agent batch plan

1. **Read and orient:** read this log, Issue #1, operations/testing guidance, and the payment file map; run the checker.
2. **Owner-controlled payment tests:** use the booking checklist to test selected Capitec, Mukuru, or Wise paths with private details supplied only by the owner.
3. **Wise automation discovery:** review the Wise automation task; document webhook and confirmation decisions without adding credentials.
4. **Booking-flow verification:** test Calendar, Web3Forms, confirmation email, reminder, reschedule, and cancellation states.
5. **Close the batch:** run both skill validators and the checker, update this log and Issue #1, then commit and push only intended files.

Keep batches short, visible, and bounded. Leave connected-system work separate from the active static site until owner approval.

## 2026-11-25 — modern agentic writing standard

### Scope

Reworked the supplied Caramel writing audit into `CARAMEL_WRITING_AUDIT_AGENTIC.md` and consolidated the operating rules in `AGENT_LANGUAGE_PROTOCOL.md`.

### Decisions

Caramel writing uses a solo-studio voice: `I` for Melissa’s work, `Caramel Digital Studio` for the studio, and `we` only for a named collaboration or approved quotation. The audit adds five review passes covering purpose, meaning, voice, language, and delivery.

The standard adds source-grounded claims, freshness checks, translation controls, focused African-language localisation, and separate handling for Caramel, Gaia, and future JEV or CLEF decision layers. Decision models remain future architecture work and stay outside the current static site.

### Changed files

- `CARAMEL_WRITING_AUDIT_AGENTIC.md`
- `AGENT_LANGUAGE_PROTOCOL.md`
- `.agent-skills/caramel-digital-studio/SKILL.md`
- `.agent-skills/agentic-studio-build/SKILL.md`
- `AGENT_HANDOFF_LOG.md`

### Checks

Run both skill validators, `git diff --check`, a long-em-dash scan, and the offline repository checker before delivery. Add the final commit and Issue #1 reference here.

## 2026-11-25 — local-first agency operating system review

### Scope

Reviewed `caramel-agency-operating-system-handover-v1.0.1.zip`, including its agency specification, handover, website-intelligence skill, skill-architect package, context templates, and Chronodesk research reference.

### Decisions

The reusable model is layered: agency core, specialist skills, industry packs, client/project context, and platform adapters. Caramel adds a local-first and free-first policy: prefer open-source local models and deterministic tools, use free tiers where suitable, require owner approval for paid APIs, protect source and intellectual property, and conserve tokens through bounded batches, local references, cached research, Markdown handovers, and file-based transfer.

Markdown, YAML, JSON, and source files remain the durable record. Presentation slides belong to explicitly requested client pitches or presentations.

Next.js 16.3 is released. Official Vercel documentation checked on 2026-11-25 identifies 16.4 as the current stable 16.x line. Future migration work must verify the latest stable release at approval time rather than permanently locking an older minor version.

JEV, CLEF, and other decision models remain future application architecture. Define purpose, inputs, outputs, confidence, evidence, review, escalation, privacy, and audit records before implementation.

### Changed files

- `AGENT_LANGUAGE_PROTOCOL.md`
- `.agent-skills/caramel-digital-studio/SKILL.md`
- `.agent-skills/agentic-studio-build/SKILL.md`
- `CARAMEL_AGENCY_OPERATING_SYSTEM_LOCAL_FIRST_HANDOVER.md`
- `AGENT_HANDOFF_LOG.md`

### Sources

- https://nextjs.org/blog/next-16-3
- https://nextjs.org/blog/next-16-4
- https://nextjs.org/docs/app/guides/upgrading/version-16

### Next action

Review whether to import or adapt the uploaded Website Intelligence and Agency Skill Architect packages in a separate bounded batch. Keep the current static site unchanged until that review is approved.

## 2026-11-25 — Google-first file and coordination layer

### Decision

Use Google Workspace as the default low-cost coordination and file layer where a client has Gmail or free Workspace access. Use Gemini or Gemma where the approved account and task support them. Keep PDFs, media, research, and handovers in the owner-approved C-drive silo or approved Google-backed storage.

Linear, Render, Supabase, GitHub Issues, and similar systems may reference those files through controlled links. The approved file store remains the durable source. Record ownership, access scope, privacy, retention, and link status for each reference.

### Validation note

The previous validation stopped because the em-dash scan included older historical handoff entries. New-line scanning is now scoped to the changed additions, while historical records remain preserved.

## 2026-11-25 — model routing and Render call paths

### Research result

Created `MODEL_ROUTING_AND_RENDER_INTEGRATION_HANDOVER.md` after reviewing official Gemma, Google Workspace, Qwen Code, GLM, OpenManus, and Render documentation.

Recommended roles: Gemma for local Google-adjacent document and Workspace preparation; Gemini for approved Workspace actions; Qwen Code for local repository and coding work; GLM for tested local or approved hosted coding and tool use; OpenManus for isolated local orchestration experiments.

Gemma or Gemini may prepare payment explanations or classify receipts. Payment authorisation, account access, receipt verification, and client confirmation remain owner-controlled through the approved payment workflow.

Render web services receive inbound HTTPS on a public URL when bound to `0.0.0.0` and `PORT`. Render webhooks require a Pro-or-higher workspace. A free-tier design can use a secured web-service endpoint that validates input and queues work for a worker when required.

### Next action

Keep the model and Render architecture separate from the current static site. Test one local model route and one secured Render endpoint in a future approved batch.
