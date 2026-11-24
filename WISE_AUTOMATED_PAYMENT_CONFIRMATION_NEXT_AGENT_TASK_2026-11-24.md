# Next agent task: Wise automated payment confirmation

**Repository:** `LilyCaramel2/caramel-digital-studio-vs-5`

**Phase:** Discovery and architecture handoff. Keep the current website static. Keep payment automation separate until the owner approves the connected-systems phase.

## Owner decisions already recorded

The client chooses the payment method from the approved menu. The menu can include South African EFT to Capitec, Mukuru where suitable, Wise, card or Google Pay through Wise where enabled, and another method approved by the owner.

The agent asks for the client’s country and preferred method. The agent sends only the selected method’s private instructions. The owner verifies receipt before Calendar and Google Meet confirmation.

Capitec is the receiving bank name. Keep all account details private.

## Task outcome

Produce a discovery report and implementation plan for automated confirmation of Wise payments. The plan must cover account eligibility, payment-link options, email or request flows, card and Google Pay availability within the owner’s Wise setup, Wise API access, webhook subscriptions, event handling, security, idempotency, private records, and Calendar confirmation.

## Required discovery

1. Confirm whether the owner uses Wise Personal or Wise Business for client payments.
2. Confirm the owner’s eligible currencies, account details, payment links, request-money features, and available payment methods.
3. Confirm whether a single-use or reusable Wise payment link suits each consultation type.
4. Confirm whether Wise payment links support the required ZAR price presentation or whether the payment request uses another currency.
5. Confirm the Wise account’s card and Google Pay payment availability for international clients.
6. Confirm Wise API access through the owner’s Developer Hub account.
7. Confirm access to Wise webhook subscriptions and the profile or application scope required.
8. Confirm the receiving events available for the owner’s Wise account. Review transfer state changes, balance updates, and incoming-payment events where available.
9. Confirm whether Wise provides a sandbox or test event path for this account and workflow.
10. Confirm the owner’s preferred record store for payment status, consultation ID, client email, selected method, amount, currency, payment reference, receipt time, and booking status.

## Proposed event flow

1. Web3Forms receives the consultation enquiry.
2. The agent asks for the client’s country and preferred payment method.
3. The system creates or selects a payment request reference for the chosen Wise method when Wise is selected.
4. The client completes the Wise payment using the owner-approved method.
5. Wise sends a webhook event to a secure HTTPS endpoint when the relevant payment or balance event occurs.
6. The endpoint verifies the webhook, records the delivery ID, and applies idempotency.
7. The workflow matches the payment to the consultation reference and amount.
8. The workflow marks the payment as receipt-confirmed after the approved event and reconciliation checks.
9. The owner receives a notification for review.
10. Google Calendar and Google Meet confirmation follows the owner-approved confirmation rule.
11. Gmail sends the payment-received and appointment confirmation templates.

The owner retains final control over paid appointment confirmation until the workflow has passed testing and received explicit approval.

## Wise-specific implementation checks

Wise’s official developer documentation describes webhooks for event-driven workflows, HTTP POST delivery, a required 2xx response, retry delivery, and `X-Delivery-Id` as an idempotency key. The agent must verify the current event and payload available to the owner’s account before implementation.

Wise’s official help documentation describes payment links for Wise Business, including single-use and reusable links, amount and currency selection, descriptions, and payment methods. The agent must verify availability in the owner’s account before placing a link in client communication.

Wise also documents account details, payment requests, email-based receiving options, and other receiving methods. The agent must present these as owner-approved choices and keep private details outside source control.

## Security requirements

- Keep Wise API credentials in approved secrets storage.
- Keep webhook signing material and private tokens out of the repository.
- Use HTTPS and a valid public domain for the webhook endpoint.
- Verify webhook authenticity according to the current Wise documentation.
- Use `X-Delivery-Id` for idempotency and duplicate-event protection.
- Store the minimum client and payment data required for reconciliation.
- Never mark a payment confirmed from a client screenshot alone.
- Keep payment details out of Issue #1, public forms, public URLs, and Markdown templates.
- Log failed, delayed, duplicate, and unmatched events for owner review.

## Test plan

Run the manual checklist first:

`GOOGLE_CALENDAR_05A_BOOKING_FLOW_TEST_CHECKLIST_2026-11-24.md`

Then test Wise automation with owner-approved test data:

- payment request created;
- client payment completed;
- webhook received;
- webhook authenticated;
- duplicate webhook ignored safely;
- unmatched payment held for owner review;
- amount or currency mismatch held for owner review;
- delayed payment handled safely;
- owner notification generated;
- Calendar confirmation generated only after approved receipt status;
- Gmail confirmation generated;
- failure and retry path recorded.

## Deliverables

- Wise account and capability discovery report.
- Data and status model.
- Webhook endpoint architecture.
- Secret and privacy plan.
- Payment-choice and routing logic.
- Test evidence.
- Owner approval request.
- GitHub Issue #1 update.
- Markdown handover with one next action.

## References

[1]: https://docs.wise.com/guides/developer/webhooks "Wise webhooks and notifications"
[2]: https://wise.com/help/articles/4qr3kkvIQlHNiD8BegEB4u/getting-paid-to-your-wise-business-by-payment-link "Wise Business payment links"
[3]: https://wise.com/help/articles/2898124/how-do-i-receive-money-to-my-wise-account-details "Wise receiving methods and account details"
