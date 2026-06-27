---
title: ReceiptLineItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receiptlineitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receiptlineitem/index.md
---

receipt line item

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date of service (as a date)

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· description of line item

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the line item

[`previous_price` ](#field-previous-price)· [`String` ](/reference/2026-01-01/scalars/string)· previous price

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· price of line item

[`super_bill_id` ](#field-super-bill-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of super bill

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

## Used By

[`ReceiptLineItemEdge.node`](/reference/2026-01-01/objects/receiptlineitemedge)

[`ReceiptLineItemPaginationConnection.nodes`](/reference/2026-01-01/objects/receiptlineitempaginationconnection)

[`SuperBill.receipt_line_items`](/reference/2026-01-01/objects/superbill)

## Definition

```
"""
receipt line item
"""
type ReceiptLineItem {
  """
  Date of service (as a date)
  """
  created_at: ISO8601DateTime!


  """
  description of line item
  """
  description: String


  """
  The unique identifier of the line item
  """
  id: ID!


  """
  previous price
  """
  previous_price: String


  """
  price of line item
  """
  price: String


  """
  id of super bill
  """
  super_bill_id: ID


  """
  updated at
  """
  updated_at: ISO8601DateTime!
}
```
