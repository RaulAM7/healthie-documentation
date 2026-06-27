---
title: TransferType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/transfertype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/transfertype/index.md
---

A transfer

## Fields

[`amount` ](#field-amount)· [`String` ](/reference/2026-01-01/scalars/string)· The amount for the transfer

[`currency` ](#field-currency)· [`String` ](/reference/2026-01-01/scalars/string)· The currency of the transfer

[`displayed_amount` ](#field-displayed-amount)· [`String` ](/reference/2026-01-01/scalars/string)· The amount to display (formatted and with currency symbol)

[`displayed_expected_to_happen` ](#field-displayed-expected-to-happen)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The expected to happen date to display

[`displayed_initiated` ](#field-displayed-initiated)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The initiation date to display

[`expected_to_happen` ](#field-expected-to-happen)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date that the transfer is expected to complete

[`fees` ](#field-fees)· [`String` ](/reference/2026-01-01/scalars/string)· Total of all fees deducted from all transactions

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Stripe ID for this transfer

[`initiated` ](#field-initiated)· [`String` ](/reference/2026-01-01/scalars/string)· The initiation time of the transfer

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status for the transfer

[`transactions_count` ](#field-transactions-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Number of transactions

[`type` ](#field-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of transfer

## Used By

[`Query.transfers`](/reference/2026-01-01/queries/transfers)

## Definition

```
"""
A transfer
"""
type TransferType {
  """
  The amount for the transfer
  """
  amount: String


  """
  The currency of the transfer
  """
  currency: String


  """
  The amount to display (formatted and with currency symbol)
  """
  displayed_amount: String


  """
  The expected to happen date to display
  """
  displayed_expected_to_happen: ISO8601DateTime


  """
  The initiation date to display
  """
  displayed_initiated: ISO8601DateTime


  """
  The date that the transfer is expected to complete
  """
  expected_to_happen: ISO8601DateTime


  """
  Total of all fees deducted from all transactions
  """
  fees: String


  """
  Stripe ID for this transfer
  """
  id: String!


  """
  The initiation time of the transfer
  """
  initiated: String


  """
  The status for the transfer
  """
  status: String


  """
  Number of transactions
  """
  transactions_count: Int


  """
  The type of transfer
  """
  type: String
}
```
