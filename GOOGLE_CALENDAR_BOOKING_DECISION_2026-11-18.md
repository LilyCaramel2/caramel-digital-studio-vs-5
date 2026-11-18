# Google Calendar booking decision — 2026-11-18

## Decision

Google Calendar Appointment Schedules becomes the default booking layer for Caramel Digital Studio consultations.

Google Workspace provides the operating environment across business email, Drive, Calendar, Meet, Docs, and Gemini. This creates one connected foundation for client communication, appointment scheduling, project information, and approved business knowledge.

## Why this fits Caramel

Google Calendar connects naturally with the existing Caramel build approach:

- Google Workspace business email
- Google Drive as the central document space
- Google Calendar availability and appointments
- Google Meet consultation links
- Google Forms-style intake questions through appointment schedules
- Gmail confirmation and preparation messages
- Gemini assistance across approved Workspace information
- Google Analytics and Search Console for website measurement
- A clear route into lead-generation, CRM, dashboards, and intelligent systems

## Initial appointment setup

Create these Google Calendar Appointment Schedules:

1. **Free project-fit conversation** — 30 minutes
2. **Digital Marketing Consultation** — 60 minutes — R950
3. **Digital Marketing Strategy Session** — 90 minutes — R1,350
4. **Advisory Session** — 60 minutes — R900 per session within the R2,700 three-session block

Each schedule receives its own title, description, availability, time zone, buffer time, intake questions, meeting method, and confirmation message.

## Booking-page flow

1. Visitor selects an appointment type on the Caramel website.
2. The website opens the matching Google Calendar booking page.
3. The visitor selects an available time.
4. The visitor shares name, email, business, website, industry, priority, and relevant links.
5. Google Calendar creates the appointment and sends the calendar invitation.
6. Google Meet supplies the meeting link for online sessions.
7. The owner receives the booking in Google Calendar and Gmail.
8. The client receives preparation guidance and appointment details.

## Payments

Google’s current paid appointment flow connects Calendar to Stripe for payment at booking. The owner should confirm the preferred Workspace plan, Stripe account, currency, cancellation policy, and refund process before enabling paid appointment schedules.

The free project-fit appointment uses a direct Google Calendar booking page. The paid consultation and strategy schedules use payment collection after the Stripe connection is approved.

## Google Workspace tier decision

The initial build can begin with the available Google Calendar appointment-schedule features. A Workspace Business Standard plan provides the broader business layer for multiple professional booking pages, payment collection, automated reminders, email verification, multiple-calendar availability checks, business email, shared storage, Meet features, and Gemini access.

The owner selects the Workspace plan according to current account access, client volume, booking volume, storage, and Gemini requirements.

## Website implementation

The 05A Digital Marketing Guidance section keeps the existing Caramel styling. Each booking button receives the matching Google Calendar booking-page URL after the schedules are created.

Suggested button destinations:

- Free project-fit conversation → free Google Calendar booking page
- Digital Marketing Consultation → paid Google Calendar booking page
- Digital Marketing Strategy Session → paid Google Calendar booking page
- Advisory block → advisory booking page or a short intake route that schedules the three sessions

The website can use the approved `start.html#consultation-booking` route while the Google Calendar URLs are being prepared. The final review build replaces the route with the approved Google Calendar booking links.

## Setup checklist

- [ ] Confirm Google Workspace account and primary business email.
- [ ] Confirm the Calendar owner account.
- [ ] Set consultation availability and time zone.
- [ ] Set buffer time between appointments.
- [ ] Set maximum daily bookings.
- [ ] Add Google Meet as the meeting method.
- [ ] Add the booking-page descriptions.
- [ ] Add intake questions.
- [ ] Create the free appointment schedule.
- [ ] Create the paid consultation schedule.
- [ ] Create the paid strategy schedule.
- [ ] Create the advisory schedule.
- [ ] Connect Stripe for paid appointment collection.
- [ ] Confirm South African rand support and payment settings.
- [ ] Add cancellation and refund wording.
- [ ] Copy the approved booking-page URLs.
- [ ] Add the URLs to the 05A website buttons.
- [ ] Test the complete booking journey on desktop and mobile.
- [ ] Confirm Google Calendar, Gmail, Google Meet, and owner notifications.
- [ ] Record the final URLs in the agent handoff log and GitHub Issue #1.

## Official Google references

[Google Calendar appointment schedules](https://support.google.com/calendar/answer/10729749?hl=en)

[Google Calendar paid appointment schedules](https://support.google.com/calendar/answer/13762729?hl=en)

[Google Workspace appointment scheduling](https://workspace.google.com/resources/appointment-scheduling/)
