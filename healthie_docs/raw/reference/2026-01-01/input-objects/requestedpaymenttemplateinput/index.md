---
title: RequestedPaymentTemplateInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/requestedpaymenttemplateinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/requestedpaymenttemplateinput/index.md
---

Payload for a requested payment template

## Fields

[`active_template` ](#field-active-template)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not the requested payment template is active

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the requested payment template

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the requested payment template

## Used By

[`createRequestedPaymentInput.requested_payment_template`](/reference/2026-01-01/input-objects/createrequestedpaymentinput)

[`updateRequestedPaymentInput.requested_payment_template`](/reference/2026-01-01/input-objects/updaterequestedpaymentinput)

## Definition

```
"""
Payload for a requested payment template
"""
input RequestedPaymentTemplateInput {
  """
  Whether or not the requested payment template is active
  """
  active_template: Boolean


  """
  The ID of the requested payment template
  """
  id: ID


  """
  The graphql_name of the requested payment template
  """
  name: String
}
```
