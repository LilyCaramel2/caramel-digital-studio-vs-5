# Version five audit and merge recommendation — 2026-11-23

## Repository confirmed

Working repository:

`LilyCaramel2/caramel-digital-studio-vs-5`

Current branch: `main`

The repository contains the locked website source, pricing records, agent handoff log, GitHub coordination notes, consultation copy, Google Calendar drafts, Google Workspace workflow, Cloudflare/Vercel architecture, and the new Next.js connected-systems handoff.

## GitHub coordination

- Issue #1: Agent coordination, locked pricing page, staged service additions, consultation, Google Calendar, Google Workspace, Cloudflare, and Vercel.
- Issue #2: Approved pricing correction for guided monthly website plans.

Issue #1 remains the main agent board. Issue #2 remains the pricing decision record.

## Current implementation state

The following items are documented and ready for an approved review build:

- Consultation booking copy
- Affirmative-language review
- Consultation pricing-page integration review
- 05A Digital Marketing Guidance HTML section
- Google Calendar booking decision
- Google Calendar 05A widget draft
- Google Workspace and Web3Forms workflow
- Cloudflare and Vercel edge architecture
- Next.js connected-systems handoff for HubSpot, Supabase, Render, and Linear

The static pricing page source remains the production reference. The 05A section is a drop-in draft. The Google Calendar widget uses replaceable booking-page URLs. The approved Google Calendar appointment URLs and live booking provider setup form the next implementation step.

## Recommended merge order

1. Resolve the approved pricing values from Issue #2 against `pricing.html` and `CDS-V5-PRICING-AND-TERMS.md`.
2. Create a review branch or checkpoint from `main`.
3. Add the 05A section after Business Add-ons and before Brand Direction.
4. Preserve every existing package, price, term, card, navigation item, and CTA.
5. Add the Google Calendar URLs after the four appointment schedules are created.
6. Keep Web3Forms for the concise project enquiry route.
7. Add Google Forms as the structured discovery layer.
8. Test the review build on desktop and mobile.
9. Run the affirmative-language scan across every new public-copy file.
10. Record the review result in Issue #1.

## Suggested upgrades

### Agent handoff template

Create one reusable Markdown template for every future agent. It should include task, repository, branch, source inspected, decisions, files changed, files created, owner approvals, open decisions, tests, deployment state, and next action.

### Copy lint

Add a lightweight copy-lint command for new public-facing Markdown, HTML, and text files. The lint should flag restricted vocabulary, exclusion-led wording, comparison-led agency language, long em dashes, and unapproved review claims.

### Language profile

Use UK English for UK and South African audiences. Use US English for US audiences. Choose the audience before writing public copy. Use commas, full stops, colons, or semicolons in place of long em dashes.

### Caramel voice

Write about services through their deliverables, process, business value, and next action. Use agents, developers, orchestrators, owners, and users where those roles apply. Present AI as a tool that extends capability and helps a business work with greater intelligence. Keep Learn AI to Earn as the education pathway for learning how to wield, prompt, and secure AI tools.

### Presentation handling

Use Markdown handovers, issue updates, code drafts, and implementation checklists for this solo-developer workflow. Presentation outlines remain optional planning notes for an agent and receive no deck production unless Melissa explicitly requests a deck.

## Merge decision

The work is ready to merge as documentation and review-build material. The live pricing page remains unchanged until the owner approves the 05A review build and the Google Calendar appointment URLs are available.
