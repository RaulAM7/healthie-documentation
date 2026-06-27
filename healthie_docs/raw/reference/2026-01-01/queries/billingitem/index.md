---
title: billingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/billingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/billingitem/index.md
---

fetch a billing item by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`BillingItem`](/reference/2026-01-01/objects/billingitem)

## Example

```
query billingItem($id: ID) {
  billingItem(id: $id) {
    amount_paid
    amount_paid_string
    application_fee_amount
    card_brand
    card_last4
    card_source
    charge_backs
    coupon_code
    cpt_codes_super_bills_id
    created_at
    currency
    deleted_at
    failure_reason
    gifted_by
    gifted_to
    id
    is_canceled
    is_outside_payment
    is_recurring
    item_position_number
    net_payment
    next_scheduled_payment_amount
    note
    offering
    offering_coupon
    offering_coupon_id
    offering_id
    original_price
    payment_medium
    provider
    receipt_last_sent_at
    recipient
    recipient_id
    recurring_payment
    refund_amount
    refund_date
    refund_items
    requested_payer
    requested_payment
    requested_payment_id
    sender
    sender_id
    shown_description
    shown_note
    state
    stripe_charge_id
    stripe_error
    successful_retried_payment
    updated_at
    user_package_selection
  }
}
```
