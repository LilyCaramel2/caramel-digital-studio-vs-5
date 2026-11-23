# Caramel Digital Studio V5 — Audit, Repair Batch, and Next-Agent Handoff

**Date:** 2026-11-23  
**Repository:** `LilyCaramel2/caramel-digital-studio-vs-5`  
**Branch inspected:** `main`  
**Baseline HEAD:** `1ba2e2b docs: map Cloudflare and Vercel edge layer`  
**Public site:** https://www.carameldigitalstudio.com  
**Working clone:** `/tmp/cds-current-audit`

## Instruction to the next agent

This is a focused repair checkpoint, not permission to redesign the site or deploy it. Read this file, `AGENT_HANDOFF_LOG.md`, `AGENT_HANDOFF_2026-11-18_CARAMEL_VOICE.md`, and the current source before editing. Preserve the owner’s visual direction: near-black background, white type, pink emphasis, pale spring yellow, soft grassy green, thin borders, asymmetric editorial spacing, and glass treatment used with restraint.

Do not introduce Vite. The repository is a static HTML/CSS/JavaScript site using Tailwind CDN. The named exception elsewhere in the wider workspace is Marine Canvas Florida, which remains in its existing Vite implementation. Do not touch Gaia, Lily-code, Lotus OS, High Tide Tours, Learn AI to Earn, Cape Plaster & Pools, client sites, or any other silo in this batch.

## What was inspected

The audit inspected the current source for `index.html`, `pricing.html`, `start.html`, `work.html`, `capabilities.html`, `styles.css`, the handoff and voice documents, the consultation integration documents, the deployment architecture note, Git history, and the public claims/links relevant to the repair.

The repository is a static public site. It does not contain a `.github/workflows` directory or GitHub Actions workflow. The configured remote is:

`https://github.com/LilyCaramel2/caramel-digital-studio-vs-5.git`

The public deployment appears to run through Cloudflare in front of Vercel. The site source and deployment architecture documentation are separate from this content repair. No deployment was performed.

## Findings before this repair batch

### 1. The public Care Plan prices were stale

`pricing.html` still showed the earlier monthly care ladder:

- Essential Hosting & Care: **R190/month**
- Managed Website Care: **R370/month**
- Managed Care Plus: **R610/month**

Those numbers conflicted with the approved Issue #2 owner decision. The approved guided Care Plans are:

- **Essential Care:** R499/month + R1,500 once-off setup
- **Growth Care:** R699/month + R2,500 once-off setup
- **Pro Care:** R999/month + R4,500 once-off setup

The approved term is a **six-month initial term**, then month-to-month with **30 days’ notice**.

### 2. The Empowerment section duplicated the Care Plans

The previous public page showed a separate monthly Empowerment ladder at R399, R699, and R999 with a 12-month minimum. This made the page look as though two different products sold overlapping monthly website access. The user specifically corrected the starting figure and directed the public page toward the approved R499-based structure.

The repair keeps **Empowerment** as a positioning/access pathway, but removes the old competing price cards. It now explains that Empowerment is delivered through the approved Care Plans. It uses the same six-month initial term and 30-day notice rule. This is deliberately not a new product architecture.

### 3. Payment language was inconsistent across the public journey

The desired payment rules are:

- **Small sites:** 50% deposit to begin, 50% before launch or final file release.
- **Larger builds:** 40% to begin, 40% after design and core content approval, and 20% before launch or handover.
- A proper HTML visual demo may be shown before commitment.
- Final production publication and final file/source release remain subject to payment of the balance.

`start.html` previously described only the 40/40/20 path. The pricing page already had more complete wording, but its terms still referred to the old 12-month Empowerment minimum.

### 4. Public proof language was too broad and links were decorative

`work.html` previously stated “65+ five-star reviews since 2018” without a direct Fiverr link and described “LinkedIn B2B capability verified” without linking to the profile.

The owner approved the 65+ claim and supplied the Fiverr profile URL:

https://www.fiverr.com/lilly_caramel

During this audit, Fiverr returned a human-verification challenge in the available browser session, so the exact review count was **not independently read in this session**. The implementation therefore uses the owner-approved claim, links directly to the Fiverr profile, and does not falsely claim that this session independently verified the count.

The LinkedIn URL verified from Lily’s public GitHub profile is:

https://www.linkedin.com/in/lilygodden/

The repair links both the proof copy and the footer LinkedIn link to that profile. Placeholder `#` links for GitHub, Instagram, and X were removed rather than left as decorative dead links.

### 5. The visual treatment had drifted from deep black toward charcoal/glow

The shared CSS used a navy body background, translucent navy glass cards, a pink radial `.glow-hero`, and a yellow radial `.glow-yellow`. The homepage also added large inline pink and yellow blur fields. Together these made the UI read as charcoal with a visible glow rather than the intended deep-black Caramel treatment.

The repair changes the shared body and glass surfaces to a near-black base, removes the two shared radial glow backgrounds, reduces translucency, keeps the borders and accent colours, and lowers the homepage inline glow fields to near-invisible values. The known pink, pale spring yellow, and grassy green accent roles remain intact.

### 6. Homepage copy was too generic for the intended positioning

The previous copy described “clear, distinctive websites and digital systems” but did not explain the central idea strongly enough: AI has changed what websites can do. The owner wants visitors who know little about AI to understand that a site can support AI-search visibility, AEO, lead generation, repositioning, and later connected systems.

The repair adds concrete language about:

- AI-assisted search and answer-engine optimisation (AEO)
- Clear structure and useful content pathways
- Lead capture and enquiry routes
- Repositioning a person, career, business, or offer
- Landing pages for a CV or career repositioning
- Forms, bookings, CRM, commerce, and scoped AI workflows
- Learn AI to Earn as the education route
- Human judgement and creative direction staying with Lily

The copy does not promise rankings, leads, revenue, or AI outcomes.

## Changes made in this repair batch

### `pricing.html`

- Replaced the old R190 / R370 / R610 hosting-care cards with the approved R499 / R699 / R999 Care Plans.
- Added the approved R1,500 / R2,500 / R4,500 once-off setup fees.
- Added the six-month initial term and month-to-month continuation with 30 days’ notice.
- Removed the old R399 / R699 / R999 12-month Empowerment cards.
- Retained Empowerment as an access pathway tied to the Care Plans instead of a competing monthly ladder.
- Updated the client terms/payment summary to remove the old 12-month minimum and state the six-month Care Plan term.
- Preserved the existing website tiers, SEO/content packages, Google Business setup, social setup, ecommerce management, AI add-ons, and brand add-ons. Those were not re-priced in this batch.

### `start.html`

- Replaced the old three-step process copy with a demo-first explanation.
- Added explicit 50/50 wording for small sites.
- Retained explicit 40/40/20 wording for larger builds.
- Clarified that final payment precedes production launch or final file/source release.

### `work.html`

- Changed the proof heading to “65+ five-star Fiverr reviews since 2018.”
- Added a direct Fiverr profile link.
- Added a direct LinkedIn profile link and removed the vague “verified” wording.
- Kept the review claim owner-approved and transparent about the browser verification limitation in this handoff.

### `index.html`

- Rewrote the hero around “Your website can do more now.”
- Added AI-search/AEO, lead-generation, repositioning, connected-system, career landing-page, and Learn AI to Earn language.
- Replaced the generic technology section with concrete capability explanations.
- Reworked the intelligence section to describe human-led, AI-assisted work without inflated claims.
- Replaced the stale R999/12-month homepage preview with “Guided Care” starting at R499/month and a six-month initial term.
- Reduced the large inline glow fields.

### `styles.css` and public theme tokens

- Changed the shared body background to `#030508`.
- Changed glass surfaces to near-black, high-opacity surfaces.
- Removed the shared pink/yellow radial glow backgrounds.
- Updated public page `theme-color` and Tailwind `navy` tokens from `#0B1424` to `#030508`.
- Preserved the accent palette: pink `#F3B6C7`, green `#A9E59A`, and pale yellow `#FCE78B`.

### `capabilities.html`

- Updated the public near-black theme token and replaced the placeholder LinkedIn footer link with the verified profile URL. No capability content was rewritten in this batch.

### `AI_HANDOFF_CDS_AUDIT_AND_NEXT_BATCH_2026-11-23.md`

- This file records the full findings, exact conflicts, implemented state, evidence limitations, deployment facts, validation plan, and next execution batch.

## Implemented versus draft/unfinished state

Implemented in this repair batch:

- Public Care Plan replacement in `pricing.html`.
- Empowerment overlap resolution.
- Small-site and larger-build payment language.
- Fiverr and LinkedIn proof links.
- Near-black visual correction.
- Homepage AI/AEO/lead-generation/repositioning copy pass.
- Detailed handoff file.

Still draft or unfinished:

- The separate `PRICING_05A_DIGITAL_MARKETING_GUIDANCE.html` draft is not integrated into the public pricing page.
- The consultation prices and appointment types remain draft copy until Google Calendar appointment schedules, payment collection, confirmation emails, meeting links, cancellation rules, and tested booking destinations are connected.
- No booking URL has been invented.
- No GitHub Actions workflow has been created.
- No Vercel or Cloudflare configuration has been changed.
- No public deployment has been run.
- The Fiverr review count was not independently readable in this session because Fiverr presented a human-verification challenge.
- The page still uses Tailwind CDN and static HTML. This repair does not begin the separate Next.js 15 migration.

## Validation performed or required

Source-level checks performed after editing:

- Searched all public HTML pages for the old `#0B1424` token, old R399/R190/R370 markers, the old 12-month wording, and placeholder `href="#"` links.
- Confirmed the old Care Plan prices are no longer present in the public HTML.
- Confirmed the approved R499/R699/R999 prices and R1,500/R2,500/R4,500 setup fees appear in `pricing.html`.
- Confirmed `start.html` contains both `50%` and `40%/40%/20%` payment wording.
- Confirmed the public Fiverr and LinkedIn URLs are present.
- Confirmed the public pages use the near-black `#030508` theme token.
- Confirmed the repository remains static HTML/CSS/JavaScript and no Vite workflow was introduced.

Before owner approval, the next agent should additionally run:

1. An HTML parser check for all pages and a link-target scan for every local and external anchor.
2. A browser render at mobile and desktop widths for `index.html`, `pricing.html`, `start.html`, and `work.html`.
3. Keyboard navigation through the main navigation, pricing anchors, enquiry form, proof links, and footer links.
4. A Lighthouse or axe accessibility pass if live tools are available, with particular attention to contrast after moving to near-black, focus visibility, form labels, heading order, link names, and mobile target sizes.
5. A reduced-motion check for the existing animations and hover transforms.
6. A visual check that the deep-black background is restored without losing the pink, spring-yellow, and grassy-green accent rhythm.
7. A final factual scan for unsupported locations, credentials, reviews, partners, outcomes, prices, availability, or service-area claims.

## Exact next execution batch

Do not widen this batch into a migration, booking integration, or deployment. The next useful batch is a review-only pass on this repair:

1. Render the four changed public pages locally.
2. Compare desktop and mobile screenshots against the intended deep-black visual direction.
3. Confirm the Care Plan section is visually legible and that the setup fees and six-month term are not hidden below the fold or lost at mobile widths.
4. Confirm the proof links open the correct public profiles.
5. Confirm `start.html` uses “small sites: 50/50” and “larger builds: 40/40/20” consistently.
6. Confirm the new homepage copy remains direct and does not overstate AI, AEO, lead, search, or business outcomes.
7. Record any remaining issues in the matching GitHub Issue or `AGENT_HANDOFF_LOG.md`.
8. Present the review build to Lily for approval.

The current execution committed and pushed the named CDS repository and `main` branch as `dc37624` (`repair CDS V5 pricing proof and visual system`). It did not authorize or perform a Vercel/Cloudflare deployment, consultation/booking integration, or changes outside this repository.

## Repository state at handoff creation

The working clone began at `1ba2e2b` on `main`, matching `origin/main`. The current repair changes are in:

- `capabilities.html`
- `index.html`
- `pricing.html`
- `start.html`
- `styles.css`
- `work.html`
- `AI_HANDOFF_CDS_AUDIT_AND_NEXT_BATCH_2026-11-23.md`

Commit and push completed in this repair batch after the recorded validation checks. The resulting commit is `dc37624` on `main`.

## Source references

- Public site: https://www.carameldigitalstudio.com
- Repository: https://github.com/LilyCaramel2/caramel-digital-studio-vs-5
- Fiverr profile: https://www.fiverr.com/lilly_caramel
- LinkedIn profile: https://www.linkedin.com/in/lilygodden/
- Learn AI to Earn is named in the homepage copy, but its public URL is intentionally pending confirmation; no unverified domain was published.
- Deployment architecture note: `CLOUDFLARE_VERCEL_EDGE_ARCHITECTURE_2026-11-18.md`
- Existing coordination log: `AGENT_HANDOFF_LOG.md`
- Existing voice guidance: `AGENT_HANDOFF_2026-11-18_CARAMEL_VOICE.md`
- Consultation integration review: `CONSULTATION_PRICING_PAGE_INTEGRATION_REVIEW_2026-11-18.md`
