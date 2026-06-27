---
title: RequestedPaymentTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymenttemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymenttemplate/index.md
---

Requested payment template

## Fields

[`active_template` ](#field-active-template)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the template is active or not

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the template

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the template

[`requested_payment` ](#field-requested-payment)· [`RequestedPayment` ](/reference/2026-01-01/objects/requestedpayment)· The requested payment of the template

## Used By

[`RequestedPayment.requested_payment_template`](/reference/2026-01-01/objects/requestedpayment)

[`RequestedPaymentTemplateEdge.node`](/reference/2026-01-01/objects/requestedpaymenttemplateedge)

[`RequestedPaymentTemplatePaginationConnection.nodes`](/reference/2026-01-01/objects/requestedpaymenttemplatepaginationconnection)

## Definition

```
"""
Requested payment template
"""
type RequestedPaymentTemplate {
  """
  Whether the template is active or not
  """
  active_template: Boolean!


  """
  The unique identifier of the template
  """
  id: ID!


  """
  The name of the template
  """
  name: String


  """
  The requested payment of the template
  """
  requested_payment: RequestedPayment
}
```
