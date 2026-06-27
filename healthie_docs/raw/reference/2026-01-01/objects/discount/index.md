---
title: Discount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/discount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/discount/index.md
---

A discount from stripe as object

## Fields

[`amount_off` ](#field-amount-off)· [`Int` ](/reference/2026-01-01/scalars/int)· Amount off in cents

[`annual_discount` ](#field-annual-discount)· [`String` ](/reference/2026-01-01/scalars/string)· Annual discount in cents

[`duration` ](#field-duration)· [`String` ](/reference/2026-01-01/scalars/string)· Duration of the discount

[`duration_in_months` ](#field-duration-in-months)· [`Int` ](/reference/2026-01-01/scalars/int)· Duration in months

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the discount

[`monthly_discount` ](#field-monthly-discount)· [`String` ](/reference/2026-01-01/scalars/string)· Monthly discount in cents

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the discount

[`percent_off` ](#field-percent-off)· [`Int` ](/reference/2026-01-01/scalars/int)· Percent off in cents

## Used By

[`StripeInvoice.discount`](/reference/2026-01-01/objects/stripeinvoice)

[`SubscriptionInstance.discounts`](/reference/2026-01-01/objects/subscriptioninstance)

[`SubscriptionInstance.discounts_if_switched`](/reference/2026-01-01/objects/subscriptioninstance)

## Definition

```
"""
A discount from stripe as object
"""
type Discount {
  """
  Amount off in cents
  """
  amount_off: Int


  """
  Annual discount in cents
  """
  annual_discount: String


  """
  Duration of the discount
  """
  duration: String


  """
  Duration in months
  """
  duration_in_months: Int


  """
  The unique identifier of the discount
  """
  id: String!


  """
  Monthly discount in cents
  """
  monthly_discount: String


  """
  The name of the discount
  """
  name: String


  """
  Percent off in cents
  """
  percent_off: Int
}
```
