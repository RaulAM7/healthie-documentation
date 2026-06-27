---
title: RefundItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/refunditem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/refunditem/index.md
---

A refunding item of a related billing item

## Fields

[`billing_item_id` ](#field-billing-item-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the billing\_item

[`currency` ](#field-currency)· [`String` ](/reference/2026-01-01/scalars/string)· The currency

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the refund

[`refund_amount` ](#field-refund-amount)· [`String` ](/reference/2026-01-01/scalars/string)· The refund amount

[`refund_date` ](#field-refund-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The refund date

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of refunding

## Used By

[`BillingItem.refund_items`](/reference/2026-01-01/objects/billingitem)

## Definition

```
"""
A refunding item of a related billing item
"""
type RefundItem {
  """
  The ID of the billing_item
  """
  billing_item_id: String


  """
  The currency
  """
  currency: String


  """
  The unique identifier of the refund
  """
  id: ID!


  """
  The refund amount
  """
  refund_amount: String


  """
  The refund date
  """
  refund_date: ISO8601DateTime


  """
  The status of refunding
  """
  status: String
}
```
