# Consultation package integration review — 2026-11-18

## Result

**The consultation package integrates cleanly with the live pricing page through a new 05A section.**

## Live page baseline

Reviewed: https://www.carameldigitalstudio.com/pricing.html

The page presents a clear sequence:

1. Website builds
2. Payment structure
3. Hosting and website care
4. SEO and content
5. Business add-ons
6. Brand direction
7. Empowerment access
8. Client terms

The visual system uses the established Caramel treatment: dark navy, cream and white type, coral/pink emphasis, green and yellow accents, editorial headings, compact mono labels, thin borders, rounded cards, generous spacing, and direct CTA links.

## Recommended placement

Add a new section after Business Add-ons and before Brand Direction:

**05A · DIGITAL MARKETING GUIDANCE**

# Build the next move with clarity.

This position gives consultations a natural connection to the existing add-ons and creates a direct bridge into brand, systems, and project work.

The existing section labels, prices, package names, cards, terms, and navigation remain intact. The new section receives its own anchor ID such as `consultation-packages`.

## Recommended content structure

### Free project-fit conversation

30 minutes · free

A relaxed introduction to the business, current goals, lead-generation opportunity, and suitable Caramel pathway.

### Digital Marketing Consultation

R950 · 60 minutes

Focused guidance for one priority across SEO, long-form content, website conversion, local visibility, social structure, lead generation, email, analytics, advertising, booking, or CRM planning.

### Digital Marketing Strategy Session

R1,350 · 90 minutes

A deeper direction across audience, offer, search demand, content, website flow, lead generation, channels, measurement, and staged systems growth.

### Advisory block

R2,700 · three 60-minute sessions

A three-month rhythm for planning, review, decisions, SEO, content, lead generation, campaigns, analytics, social, email, and system preparation.

## Styling integration

Build the new cards with the current pricing-page classes and visual tokens:

- `border-t border-pink/10 px-6 py-24` for the section shell
- `mx-auto max-w-7xl` for the content width
- `font-mono text-xs uppercase tracking-[0.28em]` for the section label
- `text-4xl font-thin tracking-[-0.03em] md:text-6xl` for the heading
- `pricing-card rounded-2xl border ... bg-white/[0.045] p-7` for appointment cards
- Existing pink, yellow, and green accent patterns for price hierarchy
- Existing `start.html` CTA styling for enquiry and booking actions

The section should feel native to the locked page through the same spacing, typography, card treatment, colour rhythm, and interaction details.

## CTA route

Use two clear actions:

- **Book a conversation** — opens the calendar route for the free project-fit appointment.
- **Start a project** — links to `start.html` for broader project enquiries.

Paid consultation buttons connect to the selected booking provider after the owner confirms the calendar and payment accounts.

## Booking implementation handoff

The next build stage connects:

- Four appointment types
- Availability rules
- Time-zone handling
- Payment collection for paid appointments
- Calendar invitations
- Meeting links
- Confirmation emails
- Preparation guidance
- Owner notifications
- Rescheduling and cancellation flows

The provider choice remains a review decision. The page can receive the approved section structure while the booking destination awaits the selected calendar account.

## Integration review outcome

The consultation package adds a natural expert-guidance pathway between the existing business add-ons and the visual-foundation services. It reinforces the current Caramel promise of scalable digital growth and gives visitors a clear route into founder-led strategy, lead generation, SEO, content, and connected systems.

## Next agent acceptance checklist

- [ ] Add the 05A Digital Marketing Guidance section after Business Add-ons.
- [ ] Preserve every existing section, price, package name, term, card, and CTA.
- [ ] Apply the existing Caramel visual tokens and responsive classes.
- [ ] Add the free 30-minute appointment.
- [ ] Add the R950 60-minute consultation.
- [ ] Add the R1,350 90-minute strategy session.
- [ ] Add the R2,700 three-session advisory block.
- [ ] Connect the project-fit CTA to the calendar route.
- [ ] Connect the project CTA to `start.html`.
- [ ] Confirm the calendar and payment provider with the owner.
- [ ] Test desktop and mobile presentation.
- [ ] Test link destinations and keyboard access.
- [ ] Complete the affirmative-language scan.
- [ ] Create a review build for owner approval.
- [ ] Update GitHub Issue #1 with the implementation result.
