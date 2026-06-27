---
title: Payment Processing | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/billing/payment-processing/index
  md: https://docs.gethealthie.com/guides/billing/payment-processing/index.md
---

# Storing a Credit Card

```
mutation createStripeCustomerDetail(
  $token: String # e.g tok_1JjpBZ2eZvKYlo2CdI1Qwgf7
  $card_type_label: String # e.g 'personal'
  $user_id: ID # e.g "61"
  $is_default: Boolean # e.g true
) {
  createStripeCustomerDetail(
    input: {
      token: $token
      card_type_label: $card_type_label
      user_id: $user_id
      is_default: $is_default
    }
  ) {
    stripe_customer_detail {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Healthie (via our usage of Stripe) allows you to store a patient’s credit/debit cards on file. You can store multiple cards on file for the same patient. There are two main ways to store a card. The first way happens automatically when a patient makes a payment (see “Charging a Patient” below). The second is via the `createStripeCustomerDetail` mutation. That mutation takes in 4 input fields - `card_type_label`, `is_default`, `token`, and `user_id`. Let’s go over each one.

`user_id` is the ID of the patient that the card should be attached to. This is required.

`token` is the tokenized card information. You generate this via Stripe’s front-end libraries and can find info on how to do so [here](https://stripe.com/docs/js/tokens/create_token?type=cardElement). This is required. To generate the token, you’ll need Healthie’s Stripe publishable key for the appropriate environment:

Staging / sandbox: `pk_test_fAj7WlTrG0uc5Z9WHKQDdoTq` Production: `pk_live_WzFpsrfurxhcz0HJspt9nbnn`

`card_type_label` lets you store the type of card. Options are `personal`, `hsa`, and `fsa`. Defaults to `personal` if nothing is passed in. The `card_type_label` field is just for your own informational purposes, and does not affect how payments are processed.

`is_default` sets the default payment source for the patient. If the patient only has one stored payment source, that payment source is automatically the default, so this field only matters for patients with multiple payment sources.

# Charging a Patient

```
mutation createBillingItem(
  $amount_paid: String # e.g "567.53"
  $sender_id: ID # e.g "61"
  $requested_payment_id: ID # e.g 11
  $stripe_idempotency_key: String # Stripe reccommends using V4 UUIDs
  $stripe_customer_detail_id: ID # e.g 21
  $should_charge: Boolean # true
) {
  createBillingItem(
    input: {
      amount_paid: $amount_paid
      sender_id: $sender_id
      should_charge: $should_charge
      stripe_customer_detail_id: $stripe_customer_detail_id
      requested_payment_id: $requested_payment_id
      stripe_idempotency_key: $stripe_idempotency_key
    }
  ) {
    billingItem {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Patients make payments in two ways. You can charge a patient from a provider/staff account (via the `createBillingItem` mutation) or patients can make payments themselves (via `completeCheckout` mutation). In this example, we will cover how to charge a patient using `createBillingItem`. Only patients with a stored payment source can be charged using `createBillingItem`. Take a look at “Storing a Credit Card” above if you are not yet storing payment sources.

80: Check out [Creating a Billing Item](/guides/billing/billing-items/#creating-a-billing-item) or [Creating an Invoice](/guides/billing/invoices/#creating-an-invoice) for further reference.

## One-time vs. recurring payments

A client will automatically be billed on a recurring basis (a `RecurringPayment` will be created) given *all* of the following conditions:

* The `BillingItem` is associated with an `Offering` (also known as a “package” in Healthie) that has a `billing_frequency` value that is *not* “One-Time”
* You do *not* pass a `payment_due_date` parameter to the `createBillingItem` mutation

A client will be billed only once given *any* of the following conditions:

* The `BillingItem` is associated with an `Offering` that does *not have* a `billing_frequency` value, or if the `billing_frequency` value is “One-Time”
* The `BillingItem` is not associated with an `Offering` at all
* You pass a `payment_due_date` parameter to the `createBillingItem` mutation with the current day’s date

## How to halt a recurring payment

If you want to pause or stop a `RecurringPayment` via the API, you can use the `updateBillingItem` mutation. To *pause* the `RecurringPayment`, pass the parameter `is_paused: true`. To *stop* the `RecurringPayment`, pass the parameter `is_canceled: true`. You can pass the ID of *any* `BillingItem` that is part of the `RecurringPayment`.

# Insurance-Based Automatic Charging

Healthie’s insurance auto-billing integrates with existing payment processing to automatically charge patients their insurance responsibility amounts (copays, coinsurance, or deductibles) when appointments are marked as “Occurred”.

## How It Works

Insurance auto-billing extends existing auto-charge functionality:

1. **Calculates** patient responsibility based on insurance policy settings
2. **Integrates** with auto-charge infrastructure (2-day delay for cards)
3. **Creates** billing items automatically with calculated amounts
4. **Supports** both auto-charge and auto-invoice workflows

## Integration with Auto-Charge Settings

* **Auto-Charge Enabled**: Patients with stored payment methods are charged automatically
* **Auto-Invoice Enabled**: Patients without payment methods receive email invoices
* **Both Disabled**: Insurance amounts calculated but no automatic billing occurs

## Prerequisites

* **Plus plan** or above with insurance billing automation access
* **Auto-charge or auto-invoice** enabled in appointment settings
* **Patient primary insurance** with billing method configured
* **Appointment types** with `insurance_billing_enabled: true`

For complete setup instructions, configuration examples, error handling, and troubleshooting, see the **[Insurance Auto-Billing](/guides/billing/insurance-auto-billing/)** guide.
