---
title: RequestedPayer | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpayer/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpayer/index.md
---

A Requested Payer for the Invoice

## Fields

[`address` ](#field-address)· [`String` ](/reference/2026-01-01/scalars/string)· The address of the requested payer

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· The email of the requested payer

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the requested payer

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the requested payer

## Used By

[`BillingItem.requested_payer`](/reference/2026-01-01/objects/billingitem)

[`RequestedPayment.other_requested_payer`](/reference/2026-01-01/objects/requestedpayment)

[`RequestedPayment.requested_payer`](/reference/2026-01-01/objects/requestedpayment)

## Definition

```
"""
A Requested Payer for the Invoice
"""
type RequestedPayer {
  """
  The address of the requested payer
  """
  address: String


  """
  The email of the requested payer
  """
  email: String


  """
  The unique identifier of the requested payer
  """
  id: ID!


  """
  The name of the requested payer
  """
  name: String
}
```
