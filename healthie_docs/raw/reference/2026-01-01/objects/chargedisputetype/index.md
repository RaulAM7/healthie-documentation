---
title: ChargeDisputeType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chargedisputetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chargedisputetype/index.md
---

An object containing information on a Stripe charge dispute

## Fields

[`amount` ](#field-amount)· [`Int` ](/reference/2026-01-01/scalars/int)· The amount that was disputed, in cents

[`billing_item_id` ](#field-billing-item-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the billing item being disputed

[`client` ](#field-client)· [`User!` ](/reference/2026-01-01/objects/user)· required · The client associated with the billing item

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID for the charge dispute at Healthie

[`invoice_id` ](#field-invoice-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the invoice associated with this dispute

[`provider` ](#field-provider)· [`User!` ](/reference/2026-01-01/objects/user)· required · The provider associated with the billing item

[`reason` ](#field-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The reason for the charge dispute

[`requested_payment_id` ](#field-requested-payment-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the requested payment associated with the billing item attached to this dispute

[`status` ](#field-status)· [`ChargeDisputeStatus` ](/reference/2026-01-01/enums/chargedisputestatus)· The status of the charge dispute

[`stripe_dispute_id` ](#field-stripe-dispute-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The ID for the charge dispute object at Stripe

## Used By

[`ChargeDisputeTypeConnection.nodes`](/reference/2026-01-01/objects/chargedisputetypeconnection)

[`ChargeDisputeTypeEdge.node`](/reference/2026-01-01/objects/chargedisputetypeedge)

## Definition

```
"""
An object containing information on a Stripe charge dispute
"""
type ChargeDisputeType {
  """
  The amount that was disputed, in cents
  """
  amount: Int


  """
  The ID of the billing item being disputed
  """
  billing_item_id: ID!


  """
  The client associated with the billing item
  """
  client: User!


  """
  The ID for the charge dispute at Healthie
  """
  id: ID!


  """
  The ID of the invoice associated with this dispute
  """
  invoice_id: ID


  """
  The provider associated with the billing item
  """
  provider: User!


  """
  The reason for the charge dispute
  """
  reason: String


  """
  The ID of the requested payment associated with the billing item attached to this dispute
  """
  requested_payment_id: ID


  """
  The status of the charge dispute
  """
  status: ChargeDisputeStatus


  """
  The ID for the charge dispute object at Stripe
  """
  stripe_dispute_id: String!
}
```
