# Cloudflare and Vercel edge architecture — 2026-11-18

## Architecture decision

Cloudflare provides the public edge and DNS layer for Caramel Digital Studio. Vercel provides the deployment and application layer behind Cloudflare.

The public request path is:

**Visitor → Cloudflare DNS and edge → Cloudflare geotargeting and edge services → Vercel deployment → website or application**

## Cloudflare responsibilities

Cloudflare manages the public domain routing and edge layer, including:

- DNS records
- Domain routing
- Proxy and edge delivery
- TLS and secure transport
- Geotargeting rules
- Regional routing decisions
- Caching and performance controls
- Redirects and hostname rules
- Security settings
- Edge analytics
- Future Workers and serverless edge logic

The Cloudflare layer sits in front of Vercel and gives the Caramel ecosystem a consistent domain, routing, security, and geotargeting foundation.

## Vercel responsibilities

Vercel manages:

- Static website deployment
- Next.js deployment
- Preview environments
- Production builds
- Domain targets behind Cloudflare
- Serverless and edge functions where selected
- Future application routes and connected experiences

## Current Caramel site

The current Caramel Digital Studio site is a static HTML, CSS, Tailwind, and JavaScript build. Cloudflare provides its domain and edge routing. Vercel provides the deployment destination.

## Future Next.js migration

When the site moves into Next.js:

1. Preserve the public domain in Cloudflare.
2. Create the approved Next.js project in the Lily-Lotus2 GitHub account.
3. Connect the repository to Vercel.
4. Add the Vercel target to the Cloudflare DNS configuration.
5. Confirm proxy, TLS, redirects, canonical URLs, and preview routing.
6. Reconnect Google Analytics, Search Console, Tag Manager, Calendar, Forms, and lead-generation routes.
7. Test geotargeting, booking, forms, image assets, SEO metadata, structured data, and mobile presentation.
8. Record the production configuration in Silo A and GitHub Issue #1.

## Google ecosystem connection

Cloudflare and Vercel form the delivery layer. Google Workspace, Calendar, Drive, Forms, Meet, Gemini, Analytics, Search Console, Tag Manager, YouTube, Flow, and Nano Banana form the business, measurement, booking, and creative layers.

The combined path is:

**Cloudflare → Vercel → Caramel website → Google booking, enquiry, measurement, content, and intelligent-system workflows**

## Agent handoff requirements

Before changing DNS, domain routing, deployment targets, or production configuration, read this file and the repository handoff log. Record each change with the domain, environment, destination, date, owner approval, and verification result.

## Suggested Silo A folder

`Caramel Business Systems/05 Shared Brand and Operations/Cloudflare and Vercel`

Store DNS records, routing notes, deployment notes, geotargeting rules, and production checklists in this folder.
