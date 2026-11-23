# Next.js connected-systems handoff — 2026-11-18

## Build level

The next Caramel build level moves the static HTML, CSS, Tailwind, and JavaScript site into a component-based Next.js application. This level connects the public website to business data, CRM, project operations, and application services.

## Connected systems

### HubSpot — CRM and lead operations

HubSpot manages:

- Contact records
- Lead capture
- Lead-source tracking
- Consultation and project enquiry pipelines
- Follow-up activity
- Email sequences
- Forms and lifecycle stages
- Sales notes
- Client communication history

The website sends approved enquiry and consultation data into HubSpot through a secure server route or approved integration workflow.

### Supabase — application data layer

Supabase provides:

- PostgreSQL database
- Authentication
- Row-level security
- Storage
- Realtime features
- Edge Functions
- Structured business records
- Client portals
- Admin dashboards
- Form and booking data models

Supabase becomes the data foundation for client, project, booking, content, and operational records that require a structured application layer.

### Render — service and worker layer

Render provides a deployment home for selected services that support the Next.js application, such as:

- Background workers
- Scheduled jobs
- Webhook processors
- Data transformation services
- Long-running API services
- Queue and integration workers
- Internal automation services

The Render layer connects to Supabase, HubSpot, Linear, Google Workspace, and approved third-party services through secure environment variables and documented API routes.

### Linear — product and delivery operations

Linear manages:

- Product initiatives
- Engineering issues
- Feature requests
- Client build tasks
- Milestones
- Project cycles
- Agent handoff tasks
- Release tracking
- Build decisions

GitHub Issues remain the durable agent coordination board for repository work. Linear becomes the product and delivery operations layer for planned builds, client work, and connected system delivery.

## Architecture path

**Cloudflare → Vercel → Next.js application → Supabase and HubSpot**

**Next.js application → Render services and workers**

**Next.js application → Linear project and delivery records**

**All approved systems → Google Workspace, Drive, Calendar, Meet, Gemini, Analytics, and Search Console**

## Staged connection sequence

### Stage 1 — component foundation

Move the static pages into reusable Next.js components while preserving the locked Caramel visual system, copy, pricing structure, 05A consultation section, and responsive behaviour.

### Stage 2 — enquiry and consultation routes

Connect the project enquiry route, Google Calendar booking routes, Google Forms intake, Web3Forms workflow, and approved confirmation messages.

### Stage 3 — HubSpot CRM

Create the contact, lead, consultation, project, and lifecycle data model. Connect approved website submissions to HubSpot through secure server-side routes.

### Stage 4 — Supabase application data

Create the database schema, authentication, storage, permissions, and records required for dashboards, client portals, project operations, and approved intelligent workflows.

### Stage 5 — Render services

Deploy selected background jobs, webhook processors, scheduled workflows, and integration services to Render. Connect them to Supabase, HubSpot, Linear, and Google Workspace.

### Stage 6 — Linear operations

Create project templates, issue labels, delivery cycles, handoff tasks, agent tasks, release records, and client-work tracking in Linear.

### Stage 7 — measurement and intelligence

Connect Google Analytics, Search Console, Tag Manager, Looker Studio, Gemini, Workspace Studio, and approved AI services to the measured and documented application workflow.

## Environment and security

Store service keys in Vercel and Render environment settings. Keep Supabase keys, HubSpot tokens, Linear tokens, Google credentials, webhook secrets, and API keys outside committed source files.

Use separate development, preview, and production environments. Record the environment owner, deployment target, integration list, and verification result in Silo A and GitHub Issue #1.

## Agent handoff instruction

Read this file before changing the Next.js application, CRM, database, service deployment, project operations, or integration architecture. Preserve the static site as the visual reference and move through each build level with owner approval and a review build.
