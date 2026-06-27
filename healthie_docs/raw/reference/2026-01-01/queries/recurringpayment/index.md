---
title: recurringPayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/recurringpayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/recurringpayment/index.md
---

Fetch a recurring payment by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`RecurringPayment`](/reference/2026-01-01/objects/recurringpayment)

## Example

```
query recurringPayment($id: ID) {
  recurringPayment(id: $id) {
    amount_paid
    amount_to_pay
    appointment_id
    billing_frequency
    billing_items_count
    canceled_at
    canceled_by
    created_at
    has_next_payment_date
    has_scheduled_billing_item
    id
    is_canceled
    is_paused
    last_billing_item
    next_payment_date
    next_restart_payment_date
    offering_coupon_id
    offering_id
    offering_name
    original_price
    paused_at
    paused_by
    payments_remaining
    recipient_id
    repeat_times
    sender_id
    start_at
    updated_at
  }
}
```
