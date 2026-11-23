---
name: caramel-digital-studio
description: Build and maintain Caramel Digital Studio websites, pricing pages, consultation flows, agent handovers, and connected-system plans. Use for Caramel repository work, static HTML/CSS/Tailwind updates, 05A consultation integration, Google Workspace workflows, and staged Next.js planning.
---

# Caramel Digital Studio

Use this skill for Caramel Digital Studio repository work and client-facing digital-system planning.

Apply `AGENT_LANGUAGE_PROTOCOL.md` to every Caramel output: website copy, content, client replies, proposals, invoices, invoice packs, forms, chatbot responses, agent records, and future Next.js interfaces. The canonical protocol carries the shared language, negative-comparison, word-filter, and handover rules.

## Current repository mode

Treat `LilyCaramel2/caramel-digital-studio-vs-5` as a static HTML, CSS, Tailwind CDN, and JavaScript site until Melissa explicitly approves a framework migration.

Every Caramel site follows the same sequence: static HTML, CSS, Tailwind, and JavaScript first; review and owner approval next; a separate Next.js migration later. Keep Next.js, HubSpot, Supabase, Render, Linear, and chatbot systems out of the current static source until the later phase is approved.

Keep Next.js, HubSpot, Supabase, Render, Linear, and advanced application architecture in future-phase handovers. Prepare migration notes and component plans separately. Keep the current static build clean and coherent.

## Before editing

1. Read `AGENT_HANDOFF_LOG.md`.
2. Read `AGENT_HANDOFF_TEMPLATE.md`.
3. Read `AGENT_HANDOFF_2026-11-18_CARAMEL_VOICE.md`.
4. Inspect the live page and current source.
5. Check GitHub Issue #1 and the latest pricing decision Issue.
6. Identify locked copy, prices, layout, styling, provider choices, and open decisions.
7. Create a review checkpoint before source edits.

## Locked visual system

Preserve the approved deep-black and midnight visual direction, white type, pink emphasis, pale spring yellow, soft grassy green, fine borders, restrained glass surfaces, editorial spacing, and existing CTA treatment. Preserve source typography, layout rhythm, responsive behaviour, and interaction patterns.

Add new sections through existing classes and patterns. Keep additions native to the page.

## Current consultation implementation

The 05A Digital Marketing Guidance section belongs after Business Add-ons and before Brand Direction on the pricing page.

The current `pricing.html` uses Tailwind CDN utilities, the shared `styles.css` tokens, and inline section patterns. The existing enquiry route is in `start.html`: it contains the active Web3Forms access key and a form marked `data-enquiry-form`. The shared `script.js` submits every matching form to the Web3Forms API, so an integrated 05A form can use the same marker and field contract.

For the current static build:

- Use the existing `data-enquiry-form` Web3Forms handler.
- Add consultation type, name, email, business, website, priority, and message fields.
- Keep the Web3Forms access key in the existing secure project configuration pattern.
- Use positive button copy such as `Book a conversation`, `Send consultation enquiry`, and `Start your next step`.
- Keep Google Calendar booking URLs as a later provider connection after the owner creates the appointment schedules.
- Keep the free project-fit conversation and paid consultation options clearly separated in the copy.
- Reuse the current access key during the approved integration pass. Keep the key out of handover drafts and skill examples.
- Treat `PRICING_05A_WEB3FORMS_CONSULTATION_COMPONENT.html` as a review component. Replace its placeholder key with the existing project value only in the working site source after owner review.
- Use the existing pricing section classes and visual tokens rather than introducing a separate form language.

## Staged architecture

### Current static layer

HTML, CSS, Tailwind CDN, JavaScript, Web3Forms, Cloudflare, and Vercel.

### Next application layer

Next.js components, HubSpot CRM, Supabase data, Render services, Linear delivery operations, and connected Google Workspace workflows.

Move to the next layer through an approved review build. Keep the static source as the visual reference.

## Google Workspace layer

The primary account is `carameldigitalcontent@gmail.com`. Google Drive contains Silo A core-business records and Silo B demos and client builds. Google Calendar handles consultation schedules. Google Forms handles structured discovery. Google Meet handles sessions. Gmail, Sheets, Docs, Apps Script, Workspace Studio, Gemini, Analytics, Search Console, Tag Manager, YouTube, Flow, and Nano Banana support approved business and creative workflows.

## Language protocol

Use affirmative, specific, plain language. Describe the service, deliverable, process, business value, and next step.

Use UK English for UK and South African audiences. Use US English for US audiences. Choose the audience before writing.

Use commas, full stops, colons, and semicolons in place of long em dashes. Avoid generic AI language, vague agency language, inflated claims, competitor comparisons, and invented evidence.

Avoid the words `not`, `real`, `actual`, and `human` except when a precise technical or role-specific reference requires them. Prefer `agent`, `developer`, `orchestrator`, `owner`, `user`, or `person` for roles. Describe AI as a tool that extends capability. Keep Learn AI to Earn as the education pathway for learning how to wield, prompt, and secure AI tools.

## Handover protocol

Use `AGENT_HANDOFF_TEMPLATE.md` for each meaningful task. Record the repository, branch, source inspected, decisions, files changed, checks, open decisions, deployment state, owner approval, next action, commit, and GitHub Issue.

Start the handover at the beginning of the task. Add the baseline repository state and intended scope first, then update the same handover as work progresses. Finish with the exact next action so another agent can continue after a context limit or token interruption.

Use Markdown handovers, code drafts, checklists, and GitHub Issue updates for this solo-developer workflow. Prepare a presentation outline only as an internal planning note when useful. Produce a deck after Melissa explicitly requests one.

## Quality gate

Before delivery:

- Preserve locked copy, prices, terms, layout, and styling.
- Confirm current static source remains coherent.
- Run HTML parsing and link checks.
- Run the project’s available build or validation checks.
- Review desktop and mobile presentation.
- Scan new public copy for restricted vocabulary and long em dashes.
- Keep secrets in secure storage.
- Record the exact next action in the handover and GitHub Issue.
- Leave a complete handover before ending the task, even when the work remains in review.
- Request owner approval before merge or publication.
