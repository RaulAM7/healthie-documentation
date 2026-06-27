---
title: StripeInvoice | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/stripeinvoice/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/stripeinvoice/index.md
---

An invoice from stripe as object

## Fields

[`add_ons` ](#field-add-ons)· [`[StripePlan!]` ](/reference/2026-01-01/objects/stripeplan)· The list of add-ons applied to the invoice.

[`applied_balance` ](#field-applied-balance)· [`StripePlan` ](/reference/2026-01-01/objects/stripeplan)· The amount of the invoice, as a positive or negative integer in the smallest currency unit (e.g., 100 cents to charge $1.00 or -100 to credit $1.00). The value is multiplied by the quantity to get the full amount. If the total is zero, this field will be absent.

[`base_plan` ](#field-base-plan)· [`StripePlan` ](/reference/2026-01-01/objects/stripeplan)· The base amount of the invoice, not including any discounts, in cents.

[`credits` ](#field-credits)· [`[StripePlan!]` ](/reference/2026-01-01/objects/stripeplan)· The list of credits applied to the invoice.

[`discount` ](#field-discount)· [`Discount` ](/reference/2026-01-01/objects/discount)· The discount applied to the invoice.

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the invoice

[`period_end` ](#field-period-end)· [`String` ](/reference/2026-01-01/scalars/string)· The end of the period the invoice covers.

[`period_start` ](#field-period-start)· [`String` ](/reference/2026-01-01/scalars/string)· The start of the period the invoice covers.

[`total` ](#field-total)· [`String` ](/reference/2026-01-01/scalars/string)· The total amount of the invoice, including all discounts and add-ons.

## Used By

[`SubscriptionInstance.invoice_if_switched`](/reference/2026-01-01/objects/subscriptioninstance)

[`SubscriptionInstance.last_invoice`](/reference/2026-01-01/objects/subscriptioninstance)

[`SubscriptionInstance.upcoming_invoice`](/reference/2026-01-01/objects/subscriptioninstance)

## Definition

```
"""
An invoice from stripe as object
"""
type StripeInvoice {
  """
  The list of add-ons applied to the invoice.
  """
  add_ons: [StripePlan!]


  """
  The amount of the invoice, as a positive or negative integer in the smallest currency unit (e.g., 100 cents to charge $1.00 or -100 to credit $1.00). The value is multiplied by the quantity to get the full amount. If the total is zero, this field will be absent.
  """
  applied_balance: StripePlan


  """
  The base amount of the invoice, not including any discounts, in cents.
  """
  base_plan: StripePlan


  """
  The list of credits applied to the invoice.
  """
  credits: [StripePlan!]


  """
  The discount applied to the invoice.
  """
  discount: Discount


  """
  The unique identifier of the invoice
  """
  id: String!


  """
  The end of the period the invoice covers.
  """
  period_end: String


  """
  The start of the period the invoice covers.
  """
  period_start: String


  """
  The total amount of the invoice, including all discounts and add-ons.
  """
  total: String
}
```
