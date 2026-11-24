# Google Calendar 05A booking-agent simulation

**Mode:** Simulation only. No payment was moved, no client was contacted, and no Calendar event was created.

**Purpose:** Verify that an end booking agent can follow the checklist, offer payment choices, generate the correct messages, and hold confirmation until the owner verifies receipt.

## Simulated enquiry

Client: Amara Ndlovu

Country: South Africa

Business: Ndlovu Garden Projects

Consultation: Digital Marketing Consultation

Duration: 60 minutes

Fee: R950

Preferred time: 14:00 South Africa Standard Time

## Generated payment-choice message

**Subject:** Choose your preferred payment method for your Caramel Digital Studio consultation

Hello Amara,

Thank you for choosing a Digital Marketing Consultation with Caramel Digital Studio.

Your consultation details are:

- Duration: 60 minutes
- Fee: R950
- Preferred time: 14:00 South Africa Standard Time

You can choose the payment method that suits you:

1. South African EFT to Capitec.
2. Mukuru, where available for your payment route.
3. Wise, including the owner-approved payment link, account details, or available card or Google Pay option.
4. Another approved method confirmed privately by the owner.

Please reply with your preferred method. The owner will send the matching private payment instructions. Your Google Calendar and Google Meet confirmation follows payment receipt verification.

Kind regards,

Lily
Caramel Digital Studio

## Simulated client choice

Selected method: South African EFT to Capitec.

The agent output is the Capitec EFT template with private account placeholders. The agent keeps account number, branch details, payment reference, and proof of payment in the owner’s private record. The client made the choice, and the agent followed that choice.

## Simulated Mukuru branch

A second South African or African client profile chooses Mukuru instead of EFT. The agent confirms that the owner has an approved Mukuru receiving route, sends the matching private instructions, records the route label and payment reference privately, and waits for owner receipt confirmation before sending Calendar and Meet details.

## Generated Capitec EFT instruction

**Subject:** Capitec EFT instructions for your Caramel Digital Studio consultation

Hello Amara,

Your selected payment method is South African EFT.

Please pay R950 using the owner-approved Capitec instructions below:

[Private Capitec EFT instructions supplied at send time.]

Please reply with your payment reference or a payment confirmation screenshot with sensitive account details covered. The owner checks receipt and then sends your Google Calendar and Google Meet confirmation.

Kind regards,

Lily
Caramel Digital Studio

## Simulated international branch

A second test profile uses:

- Client: Daniel Brooks
- Country: United Kingdom
- Consultation: Digital Marketing Strategy Session
- Duration: 90 minutes
- Fee: R1,350

The agent presents the same payment-choice message. Daniel selects Wise. The agent sends the owner-approved Wise payment link, account-detail instructions, email request, card option, or Google Pay option available in the owner’s Wise account at send time.

The agent does not assume a Wise method. The selected method comes from the client and the owner’s current Wise setup.

## Generated Wise instruction

**Subject:** Wise payment instructions for your Caramel Digital Studio consultation

Hello Daniel,

Your selected payment method is Wise.

Please pay the listed R1,350 using the owner-approved Wise method below:

[Private Wise payment link, account details, email request, card option, or Google Pay option supplied at send time.]

Please reply with your Wise payment reference or payment confirmation. The owner checks receipt and then sends your Google Calendar and Google Meet confirmation.

Kind regards,

Lily
Caramel Digital Studio

## Receipt-confirmed output

**Subject:** Payment received, consultation confirmation to follow

Hello [Client name],

Your payment of R[Amount] for the [Consultation name] has been received.

Your consultation is scheduled for:

- Date: [Date]
- Time: [Time]
- Duration: [Duration]
- Time zone: [Time zone]

Google Calendar and Google Meet details:

[Approved Calendar invitation and Meet details.]

Preparation questions:

[Approved preparation questions or link.]

Kind regards,

Lily
Caramel Digital Studio

## Simulation result

The agent generated the correct outputs for a South African Capitec EFT choice and an international Wise choice. The agent kept payment instructions private, retained client choice, and held Calendar confirmation until owner receipt verification.

Live validation remains an owner-approved test task. The simulation does not verify account access, payment receipt, Wise webhook availability, Mukuru availability, or Calendar schedule URLs.
