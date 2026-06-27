---
title: RequestedPayerInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/requestedpayerinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/requestedpayerinput/index.md
---

Payload for a requested payer

## Fields

[`address` ](#field-address)· [`String` ](/reference/2026-01-01/scalars/string)· The address of the requested payer

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· The email of the requested payer

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the requested payer

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the requested payer

## Used By

[`createRequestedPaymentInput.requested_payer`](/reference/2026-01-01/input-objects/createrequestedpaymentinput)

[`updateRequestedPaymentInput.requested_payer`](/reference/2026-01-01/input-objects/updaterequestedpaymentinput)

## Definition

```
"""
Payload for a requested payer
"""
input RequestedPayerInput {
  """
  The address of the requested payer
  """
  address: String


  """
  The email of the requested payer
  """
  email: String


  """
  The ID of the requested payer
  """
  id: ID


  """
  The graphql_name of the requested payer
  """
  name: String
}
```
