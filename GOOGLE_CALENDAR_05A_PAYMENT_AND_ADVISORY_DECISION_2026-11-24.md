# Google Calendar 05A payment and advisory decision

**Repository:** `LilyCaramel2/caramel-digital-studio-vs-5`

**Scope:** Caramel Digital Studio static 05A consultation flow.

**Decision status:** Google Pay and Wise manual confirmation are the approved payment routes for this integration.

## Recommended advisory structure

Use **Option A: separate advisory sessions**.

- Appointment name: Advisory Session
- Duration: 60 minutes
- Price: R900 per session
- Booking model: each session is booked separately
- Payment route: Google Pay or Wise, using owner-approved payment instructions
- Delivery: Google Meet
- Follow-up: the owner confirms the paid booking and sends the Calendar/Meet confirmation

### Reason for the recommendation

Separate sessions match the manual payment route, keep the offer clear, and let the owner schedule one session at a time. The client can book a second or third session when useful. This structure keeps the R2,700 advisory value visible as three R900 sessions without requiring a package checkout system.

## Option B recorded for reference

Option B would sell one R2,700 advisory block containing three 60-minute sessions. It requires a separate method for payment confirmation, session scheduling, package tracking, rescheduling, unused-session records, and completion records. Google Calendar Appointment Schedules do not provide the required package workflow through the current setup. Option B remains available as a manually managed service after a direct enquiry, while Option A is the recommended public booking structure.

## Payment terms draft

### Paid consultations

Payment confirms the consultation booking.

The owner sends the approved Google Pay or Wise payment instructions after receiving the consultation enquiry or booking request. The client pays the listed South African rand amount and sends payment confirmation to the owner. The owner confirms receipt, schedules the Google Meet appointment, and sends the calendar confirmation.

The consultation price covers the agreed session duration and preparation stated on the consultation page. Additional work receives a separate written quote before work begins.

### Advisory sessions

Each Advisory Session costs R900 for 60 minutes. Three sessions represent a R2,700 advisory pathway. Each session is paid and scheduled separately through the approved Google Pay or Wise process.

### Changes and cancellations

A client may request a change by email before the scheduled start time. The owner confirms the available replacement time. A missed session or late cancellation receives owner review according to the circumstances and the written booking confirmation.

The owner confirms any refund, credit, or rescheduling outcome directly with the client before making a change. The final cancellation and refund wording requires owner approval before public publication.

## Provider boundary

- Google Pay: use only with the owner-approved receiving account or payment instructions.
- Wise: use only with the owner-approved receiving account or payment instructions.
- Google Calendar: use for appointment availability, confirmations, reminders, and Google Meet links.
- Web3Forms: use for consultation enquiries and preparation details.

Do not place bank details, Wise account details, Google Pay identifiers, passwords, access keys, or other private payment information in the repository or GitHub Issues.

## Agent next steps

1. Keep Google Pay and Wise as the only documented payment routes for Calendar consultations.
2. Confirm the owner-approved Google Pay and Wise instructions through a secure channel.
3. Create the public Advisory Session schedule as a 60-minute R900 option only after owner approval.
4. Treat the R2,700 three-session pathway as a service description, with each session booked separately.
5. Test the enquiry, manual payment confirmation, Google Meet, Calendar confirmation, and reminder workflow.
6. Record final owner-approved wording and test results in Issue #1.
