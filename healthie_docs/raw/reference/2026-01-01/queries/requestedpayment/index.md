---
title: requestedPayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/requestedpayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/requestedpayment/index.md
---

fetch a requested payment (invoice) by id

## Arguments

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the requested payment

[`invoice_id` ](#argument-invoice-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`preview` ](#argument-preview)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`uuid` ](#argument-uuid)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`RequestedPayment`](/reference/2026-01-01/objects/requestedpayment)

## Example

```
query requestedPayment(
  $id: ID
  $invoice_id: ID
  $preview: Boolean
  $uuid: String
) {
  requestedPayment(
    id: $id
    invoice_id: $invoice_id
    preview: $preview
    uuid: $uuid
  ) {
    appointment
    appointment_id
    balance_due
    billing_item_id
    billing_items
    cms1500_id
    cms1500_service_date
    created_at
    currency
    date_to_show
    debt_decimal
    details
    email_sent_at
    id
    invoice_id
    invoice_type
    is_manually_paid
    is_preview
    metadata
    notes
    offering
    offering_id
    offering_price_at_invoice_creation
    other_requested_payer
    paid_at
    paid_percent
    price
    recipient
    recipient_id
    requested_payer
    requested_payer_id
    requested_payment_template
    sender
    sender_id
    service_date
    services_provided
    status
    updated_at
    user_package_selection
    write_off_amount
    write_offs
  }
}
```
