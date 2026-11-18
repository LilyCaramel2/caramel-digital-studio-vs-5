# Consultation booking integration progress — 2026-11-18

## Status

**Copy and appointment specification complete. Calendar implementation ready for the next build stage.**

## Completed

- Drafted the Caramel consultation and booking section.
- Applied the affirmative-language rule.
- Completed the automated restricted-term scan with zero matches.
- Added the free 30-minute project-fit conversation.
- Added the R950 60-minute Digital Marketing Consultation.
- Added the R1,350 90-minute Digital Marketing Strategy Session.
- Added the R2,700 three-session advisory block.
- Defined appointment names, form fields, confirmation messages, preparation guidance, and booking steps.
- Defined the lead-generation, SEO, long-form writing, analytics, advertising, CRM, booking, and intelligent-system topics that clients can bring to a consultation.
- Saved the source copy in `CONSULTATION_BOOKING_COPY.md`.
- Saved the language review in `CONSULTATION_BOOKING_COPY_REVIEW_2026-11-18.md`.
- Logged the work in GitHub Issue #1.

## Appointment catalogue

### Free project-fit conversation

**Duration:** 30 minutes  
**Price:** Free  
**Purpose:** Discuss the business, goals, current digital presence, lead-generation opportunity, and suitable Caramel pathway.

### Digital Marketing Consultation

**Duration:** 60 minutes  
**Price:** R950  
**Purpose:** Give focused guidance for one priority such as SEO, content, website conversion, local visibility, social structure, lead generation, email, analytics, advertising, booking, or CRM planning.

### Digital Marketing Strategy Session

**Duration:** 90 minutes  
**Price:** R1,350  
**Purpose:** Create a broader direction across audience, offer, search demand, content, website flow, lead generation, channels, measurement, and staged systems growth.

### Advisory block

**Duration:** Three 60-minute sessions across three months  
**Price:** R2,700  
**Purpose:** Provide a continuing rhythm for planning, review, decisions, SEO, content, lead generation, campaigns, analytics, social, email, and system preparation.

## Recommended integration flow

1. Add the consultation section to the approved Caramel page structure.
2. Connect the “Book a conversation” calls to the selected calendar provider.
3. Create four appointment types using the catalogue above.
4. Add the consultation prices to the paid appointment types.
5. Add the form fields from `CONSULTATION_BOOKING_COPY.md`.
6. Connect payment before confirmation for paid appointments.
7. Connect calendar invitations and the meeting link.
8. Add the confirmation and thank-you messages.
9. Add email delivery for preparation guidance and appointment details.
10. Test desktop and mobile booking flows.
11. Test free booking, paid booking, payment confirmation, calendar invitation, rescheduling, and cancellation flows.
12. Create a review build for owner approval.

## Provider decision for the next agent

Select the calendar and payment tools after checking the owner’s preferred accounts and existing subscriptions. The implementation should support:

- Appointment types
- Availability rules
- Time-zone handling
- Payment collection
- Calendar invitations
- Meeting links
- Confirmation emails
- Rescheduling and cancellation rules
- Client intake fields
- Owner notifications

Keep the provider decision inside the review build stage so the owner can approve the flow before publication.

## Styling instruction

Use the locked Caramel visual system: dark navy, cream and white type, coral/pink emphasis, restrained green and yellow details, thin borders, editorial headlines, generous spacing, and the established card and CTA treatment. The booking section should feel native to the existing pricing and start-a-project pages.

## Source and deployment instruction

Work from the repository `LilyCaramel2/caramel-digital-studio-vs-5`. Read `AGENT_HANDOFF_LOG.md`, `AGENT_HANDOFF_2026-11-18_CARAMEL_VOICE.md`, and the tiered pricing handoff before editing. Create a review branch or checkpoint. Prepare a review build and desktop/mobile checks before publication.

## Next agent acceptance checklist

- [ ] Consultation section placed in the approved page location.
- [ ] Free project-fit conversation added.
- [ ] Paid consultation added at R950 for 60 minutes.
- [ ] Strategy session added at R1,350 for 90 minutes.
- [ ] Advisory block added at R2,700 for three sessions.
- [ ] Calendar provider selected with owner approval.
- [ ] Payment route connected for paid appointments.
- [ ] Calendar invitations and meeting links tested.
- [ ] Confirmation and preparation emails tested.
- [ ] Mobile and desktop booking views checked.
- [ ] Caramel styling preserved.
- [ ] Positive-language scan completed.
- [ ] Review build shared with the owner.
- [ ] GitHub Issue updated with the implementation result.

## Handoff state

**Copy specification complete. Calendar provider selection, payment connection, source implementation, QA, and owner review form the next work stage.**
