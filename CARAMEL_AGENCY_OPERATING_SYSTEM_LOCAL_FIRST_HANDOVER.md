# Caramel agency operating system: local-first handover

**Source reviewed:** `caramel-agency-operating-system-handover-v1.0.1.zip`
**Use:** reusable template reference for future agency and client repositories
**Current repository mode:** static HTML, CSS, Tailwind CDN, JavaScript

## Owner operating decisions

Caramel Digital Studio is a solo developer studio supported by agents. The owner directs purpose, judgement, quality, security, approvals, and publication. Agents provide research, memory, drafting, analysis, testing, and implementation support.

The preferred resource model is local-first and free-first. Use open-source local models and deterministic local tools where they meet the task. Use free service tiers where they meet the task. Treat paid APIs and paid upgrades as optional owner-approved services with a written reason. Keep source, prompts, client records, research, and intellectual property in owner-controlled files and approved repositories.

Token conservation is an architecture requirement. Read existing Markdown and local files before requesting repeated context. Prefer bounded batches, concise handovers, local references, cached research, deterministic scripts, and file-based transfer between agents. Choose the smallest capable model or tool.

Use Markdown, YAML, JSON, and source files as the durable record. Use presentation slides only for an explicitly requested client pitch or presentation.

Google Workspace is the default low-cost coordination and file layer where a client already has Gmail or free Workspace access. Gemini and Gemma are preferred where the approved account and task support them. PDFs, media, research, and handovers live in the owner-approved C-drive silo or approved Google-backed storage. Linear, Render, Supabase, GitHub Issues, and similar systems may reference those files through controlled links. Each reference records ownership, access scope, privacy, retention, and link status.

## Reusable pack findings

The uploaded pack provides a strong reusable structure:

- agency core rules;
- specialist skills;
- industry packs;
- client and project context;
- platform adapters;
- evidence labels;
- client manifests and project briefs;
- task and handover contracts;
- QA and release reports;
- Chronodesk as a research case study rather than a universal template.

The pack separates capability from context. Preserve that separation when adapting it to another repository. Keep client facts, industry assumptions, research evidence, credentials, and universal rules in distinct files.

The Website Intelligence skill is valuable for source inventory, page extraction, evidence classification, original copy, conversion architecture, design-system analysis, HTML/Tailwind implementation, QA, and later Next.js migration. Reuse its method after a separate review; keep Chronodesk research as a case study and avoid reproducing its wording or identity.

## Framework version rule

Next.js 16.3 is a released version. The official Vercel documentation checked on 25 November 2026 identifies Next.js 16.4 as the current stable 16.x release. The repository therefore tracks the latest stable version available at the approved migration date rather than permanently naming 16.3 or 16.4.

The migration gate remains:

1. finish and approve the static site;
2. verify the current official Next.js and Vercel guidance;
3. record the selected version and Node, React, TypeScript, and browser requirements;
4. create a separate migration checkpoint;
5. migrate, test, review, and approve before connected-system work.

## Future decision layers

JEV, CLEF, and other decision models belong in the later application architecture. Define each model’s purpose, inputs, outputs, confidence, evidence, reviewer, escalation path, privacy boundary, and audit record before implementation. Keep decision layers separate from copy approval and from the current static site.

## Next agent batches

1. Review the uploaded pack against the repository’s current operating guide and writing standard.
2. Decide whether the Website Intelligence and Agency Skill Architect packages should be imported, adapted, or kept as external references.
3. Create or validate portable client-manifest, project-brief, task, and handover templates.
4. Add local-model and platform-adapter guidance only where a concrete repository workflow requires it.
5. Before any Next.js migration, verify the latest official release and record the version decision.
6. Run validators, the offline checker, and Issue #1 documentation updates after each meaningful batch.
