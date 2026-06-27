---
title: TransactionType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/transactiontype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/transactiontype/index.md
---

A transaction

## Fields

[`currency` ](#field-currency)· [`String` ](/reference/2026-01-01/scalars/string)· The currency of the transaction

[`displayed_amount` ](#field-displayed-amount)· [`String` ](/reference/2026-01-01/scalars/string)· The amount for the transaction after fees

[`source_name` ](#field-source-name)· [`String` ](/reference/2026-01-01/scalars/string)· Charge ID associated to transaction. Can be matched with billing\_item.stripe\_charge\_id

## Used By

[`Query.transactions`](/reference/2026-01-01/queries/transactions)

## Definition

```
"""
A transaction
"""
type TransactionType {
  """
  The currency of the transaction
  """
  currency: String


  """
  The amount for the transaction after fees
  """
  displayed_amount: String


  """
  Charge ID associated to transaction. Can be matched with billing_item.stripe_charge_id
  """
  source_name: String
}
```
