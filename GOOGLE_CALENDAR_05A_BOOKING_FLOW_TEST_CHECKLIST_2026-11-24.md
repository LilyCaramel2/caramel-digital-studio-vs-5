# Google Calendar 05A booking-flow test checklist

**Repository:** `LilyCaramel2/caramel-digital-studio-vs-5`

**Purpose:** Give the next agent a repeatable test for the complete Caramel consultation journey using Web3Forms, Google Pay or Wise manual confirmation, Google Calendar, Gmail, and Google Meet.

**Payment model:** The client chooses from the owner-approved payment menu. The menu can include South African EFT to Capitec, Mukuru where suitable, Wise, card or Google Pay through Wise where enabled, and other approved methods.

**Privacy:** Use test identities and owner-approved payment instructions. Keep payment identifiers, account details, QR codes, access keys, and private links in the owner’s private records.

## Test preparation

- [ ] Confirm the owner-approved consultation options and prices.
- [ ] Confirm Option A: Advisory Session, 60 minutes, R900 per booking.
- [ ] Confirm the Google Calendar owner account: `carameldigitalcontent@gmail.com`.
- [ ] Confirm the test email address and a second email address for owner notifications.
- [ ] Confirm the approved Google Pay instructions through a private channel.
- [ ] Confirm the approved Wise instructions through a private channel.
- [ ] Confirm the approved South African EFT instructions through a private channel.
- [ ] Confirm the approved Mukuru instructions through a private channel where offered.
- [ ] Confirm the owner-approved payment-choice message.
- [ ] Prepare a test client identity, business name, website, priority, and preparation notes.
- [ ] Prepare a private test record for payment reference, timestamps, booking status, and results.
- [ ] Confirm a controlled test-payment amount or owner-approved simulated receipt process.
- [ ] Record the repository commit and Issue #1 URL before testing.

## A. Web3Forms enquiry test

- [ ] Open the approved consultation route on desktop.
- [ ] Open the same route on a mobile viewport.
- [ ] Submit the 05A consultation form with the test identity.
- [ ] Confirm required fields block an incomplete submission.
- [ ] Confirm the form shows its sending state.
- [ ] Confirm the submit button disables during the request.
- [ ] Confirm the enquiry reaches the owner’s configured Web3Forms destination.
- [ ] Confirm the success message appears after a successful response.
- [ ] Confirm the form resets after success.
- [ ] Confirm the form returns to an available state after completion.
- [ ] Record the Web3Forms delivery timestamp in the private test record.

## B. Payment-choice test

- [ ] Submit a test enquiry with a South African client profile.
- [ ] Present the approved payment menu.
- [ ] Select South African EFT to Capitec as the test method.
- [ ] Confirm the agent sends only the selected method’s private instructions.
- [ ] Repeat with Mukuru where the owner has an approved receiving process.
- [ ] Submit a test enquiry with an international client profile.
- [ ] Present the approved payment menu.
- [ ] Select Wise as the test method.
- [ ] Confirm the agent sends only the selected Wise method’s private instructions.
- [ ] Confirm the client can request another approved method before payment confirmation.

## C. Google Pay instruction test

- [ ] Reply to the test enquiry with the approved Google Pay email template.
- [ ] Confirm the email contains the consultation name, duration, ZAR amount, requested time, and time zone.
- [ ] Confirm the email contains the owner-approved Google Pay instructions.
- [ ] Confirm the email asks for a payment reference or covered confirmation screenshot.
- [ ] Confirm the email explains that Calendar and Meet details follow receipt confirmation.
- [ ] Complete the controlled Google Pay payment or run the owner-approved simulated receipt step.
- [ ] Check the payment in the owner’s Google Pay account or private test record.
- [ ] Record the payment reference and receipt time privately.
- [ ] Send the payment-received confirmation email.
- [ ] Confirm the client receives the Calendar and Meet details after receipt confirmation.

## D. Wise instruction test

- [ ] Run the same sequence with the Wise email template.
- [ ] Confirm the email contains the consultation name, duration, ZAR amount, requested time, and time zone.
- [ ] Confirm the email contains the owner-approved Wise instructions.
- [ ] Confirm the email asks for a Wise payment reference or covered confirmation screenshot.
- [ ] Complete the controlled Wise payment or run the owner-approved simulated receipt step.
- [ ] Check the payment in the owner’s Wise account or private test record.
- [ ] Record the payment reference and receipt time privately.
- [ ] Send the payment-received confirmation email.
- [ ] Confirm the client receives the Calendar and Meet details after receipt confirmation.

## E. Google Calendar and Meet test

- [ ] Open the approved Google Calendar appointment schedule.
- [ ] Confirm the title and consultation price match the approved wording.
- [ ] Confirm the duration and time zone.
- [ ] Confirm availability and buffer time.
- [ ] Confirm preparation questions.
- [ ] Select an available test time.
- [ ] Confirm the owner receives the Calendar event.
- [ ] Confirm the client receives the Calendar invitation.
- [ ] Confirm the Google Meet link appears in the event.
- [ ] Open the Meet link from the owner account.
- [ ] Open the Meet link from the client account.
- [ ] Confirm the reminder timing.
- [ ] Confirm the owner notification.
- [ ] Confirm the client confirmation wording.

## F. Advisory Session test

- [ ] Book one 60-minute Advisory Session at R900.
- [ ] Confirm the booking receives its own payment confirmation.
- [ ] Confirm the booking receives its own Calendar event.
- [ ] Confirm the three-session pathway wording remains separate from the individual booking.
- [ ] Repeat the test for a second session using a new time.
- [ ] Confirm each session has its own private payment record and Calendar event.

## G. Change, cancellation, and follow-up test

- [ ] Request a time change by email before the scheduled start.
- [ ] Confirm the owner replies with an available replacement time.
- [ ] Confirm the replacement event updates the Calendar and Meet details.
- [ ] Test the approved cancellation wording.
- [ ] Record the owner-approved refund, credit, or rescheduling outcome in the private test record.
- [ ] Send the relevant client follow-up email.
- [ ] Confirm the owner notification and client notification for the change.

## H. Failure-state test

- [ ] Test an incomplete Web3Forms submission.
- [ ] Test a controlled network failure if the environment supports it.
- [ ] Confirm the form displays a useful error state.
- [ ] Confirm the submit button becomes available after an error.
- [ ] Test a payment reference that requires owner review.
- [ ] Confirm the Calendar confirmation waits for owner receipt confirmation.
- [ ] Confirm private payment details remain outside public files, issue comments, and handovers.

## I. Evidence and handover

- [ ] Record desktop and mobile results.
- [ ] Record Web3Forms result.
- [ ] Record Google Pay result.
- [ ] Record Wise result.
- [ ] Record Google Calendar result.
- [ ] Record Google Meet result.
- [ ] Record Gmail confirmation and reminder result.
- [ ] Record change and cancellation results.
- [ ] Record every open decision.
- [ ] Add a concise result update to GitHub Issue #1.
- [ ] Add the final test result to `AGENT_HANDOFF_LOG.md`.
- [ ] Keep payment references and private account details in the owner’s private record.
- [ ] Request owner approval before public publication.
