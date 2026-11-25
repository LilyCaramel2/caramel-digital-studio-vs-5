# Agent language and handover protocol

**Version:** Living document
**Scope:** Caramel Digital Studio builds, client work, agent responses, content, invoices, proposals, forms, chatbots, translations, applications, and handovers.

## Source of truth

Read `CARAMEL_WRITING_AUDIT_AGENTIC.md` before writing Caramel copy or agent-facing client communication. This protocol provides the short operating rules. The audit provides the full review method.

## Ownership and voice

Caramel Digital Studio is a solo developer studio supported by agents.

- Use **I** for Melissa’s work, judgement, availability, delivery, and decisions.
- Use **Caramel Digital Studio** for the studio, services, website, and systems.
- Use **agent**, **developer**, **orchestrator**, **owner**, **client**, or **person** for roles.
- Use **we** only for a named collaboration or an approved quotation.
- Keep authorship, judgement, ethics, approval, and responsibility with the owner.

## Build sequence

Every site starts as a static HTML, CSS, Tailwind, and JavaScript build. Review and approve the static site first. Move the approved site to Next.js later as a separate connected-systems phase. Keep CRM, database, hosting, project operations, chatbot, and decision-layer work in future handovers until the owner approves that phase. At migration time, check the current official Vercel and Next.js release, then select the latest stable version supported by the project. Current repository guidance tracks Next.js 16.x and avoids hard-coding an older minor release.

## Local-first and resource-aware operation

Prefer open-source local models and local deterministic tools for Lotus, Gaia, and reusable agency workflows. Treat paid APIs as optional owner-approved services. Use free tiers where they meet the task, keep each repository’s services and accounts separated as required, and preserve the owner’s control of source, prompts, research, client data, and intellectual property.

Conserve tokens and compute. Read existing Markdown, handovers, skills, and local files before asking for repeated context. Use bounded batches, concise handovers, deterministic scripts, cached local research, and file-based transfer between agents. Choose the smallest capable model or tool. Record when a remote service is required and why a local or free route cannot complete the task.

Use Google Workspace as the default low-cost coordination and file layer where the client already has Gmail and free Workspace access. Use Gemini or Gemma where the approved account and task support them. Keep durable PDFs, media, research, and handovers in the owner-approved C-drive silo or its approved Google-backed file store. Linear, Render, Supabase, GitHub Issues, and similar systems may point to those files through controlled references; they do not become the sole source of truth. Record file ownership, access scope, link stability, privacy, and retention for every reference.

For model routing and Render call paths, read `MODEL_ROUTING_AND_RENDER_INTEGRATION_HANDOVER.md`. Keep local models, Google Workspace permissions, public web-service ingress, Render webhooks, private services, workers, payment actions, and decision layers in separate control boundaries.

Read `CARAMEL_OPERATING_SYSTEM_MODEL_ROUTING_SUMMARY_2026-11-25.md` for the current verified and pending configuration state, content-production process, and next-agent build batches.

Use Markdown, YAML, JSON, and source files as the durable working record. Use presentations only when Melissa explicitly requests a client pitch or presentation. Agent summaries, plans, checklists, architecture notes, and handovers stay in Markdown.

## Direct writing

Name the present service, scope, structure, capability, behaviour, opportunity, constraint, price, route, decision, or next action. Use short sentences, common words, concrete nouns, direct verbs, and calm professional language. Give each paragraph one job.

Use UK English for UK and South African audiences. Use US English for US audiences. Record the audience and language variant before drafting. Use commas, full stops, colons, and semicolons. Use an em dash zero times in new copy, handovers, client messages, and agent outputs.

## Positive language and evidence

Write the approved offer directly. Keep competitor framing, fear framing, exclusion-led copy, inflated claims, invented evidence, stock AI language, repeated filler, and artificial urgency out of new writing. State material constraints once as clear rules, then return to the useful path.

Rewrite sentences to avoid `not`, `real`, `actual`, and `human` wherever a precise alternative exists. Record a justified exception for a quotation, technical term, role reference, review reference, or ethical discussion. Ground claims in approved sources, verified results, named files, owner decisions, or observed behaviour.

## Translation

Translate from approved source copy. Record language, regional variant, source version, reviewer, and approval state. Keep names, prices, URLs, placeholders, provider names, and technical identifiers stable. Use focused language coverage supported by audience evidence and qualified review. Route Afrikaans, isiXhosa, isiZulu, and later African-language work through the approved language reviewer or African-language model, followed by owner review.

## Review and handover

Apply the five passes in `CARAMEL_WRITING_AUDIT_AGENTIC.md`: purpose, meaning, voice, language, and delivery. Review headings, links, calls to action, accessibility, terminology, grammar, repeated phrases, and long em dashes.

Start a Markdown handover at task start. Record baseline state, branch, scope, audience, language, owner decision state, files, checks, open items, deployment state, issue, commit, and exact next action. Use GitHub Issues as the coordination board. Leave a complete handover after every batch, including partial and token-limited work.
