---
title: ReceiptLineItemInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/receiptlineiteminput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/receiptlineiteminput/index.md
---

Payload for a receipt line item

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time the receipt line item was created

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the receipt line item

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the receipt line item

[`previous_price` ](#field-previous-price)· [`String` ](/reference/2026-01-01/scalars/string)· The previous price of the receipt line item

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· The current price of the receipt line item

## Used By

[`createSuperBillInput.receipt_line_items`](/reference/2026-01-01/input-objects/createsuperbillinput)

[`updateSuperBillInput.receipt_line_items`](/reference/2026-01-01/input-objects/updatesuperbillinput)

## Definition

```
"""
Payload for a receipt line item
"""
input ReceiptLineItemInput {
  """
  The time the receipt line item was created
  """
  created_at: ISO8601DateTime


  """
  The description of the receipt line item
  """
  description: String


  """
  The ID of the receipt line item
  """
  id: ID


  """
  The previous price of the receipt line item
  """
  previous_price: String


  """
  The current price of the receipt line item
  """
  price: String
}
```
