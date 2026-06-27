---
title: ChargeBack | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chargeback/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chargeback/index.md
---

A Chargeback object, contains info on the dispute reason, status, and evidence submitted

## Fields

[`billing_item` ](#field-billing-item)· [`BillingItem` ](/reference/2026-01-01/objects/billingitem)· The payment in Healthie that was disputed

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time the chargeback was initiated

[`disputed_amount` ](#field-disputed-amount)· [`String` ](/reference/2026-01-01/scalars/string)· The amount that was disputed

[`evidence` ](#field-evidence)· [`ChargeBackEvidence` ](/reference/2026-01-01/objects/chargebackevidence)· Evidence to contest the chargeback

[`evidence_fields_to_submit` ](#field-evidence-fields-to-submit)· [`[String]` ](/reference/2026-01-01/scalars/string)· Fields that should be submitted for this chargeback

[`fee` ](#field-fee)· [`String` ](/reference/2026-01-01/scalars/string)· The dispute fee charged by the payment processor

[`formatted_reason` ](#field-formatted-reason)· [`String` ](/reference/2026-01-01/scalars/string)· A formatted version of the reason

[`formatted_status` ](#field-formatted-status)· [`String` ](/reference/2026-01-01/scalars/string)· A formatted version of the status

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the chargeback

[`reason` ](#field-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The reason for the chargeback. Matches Stripe's list of reasons at https\://stripe.com/docs/api/disputes/object?lang=ruby

[`response_required_by` ](#field-response-required-by)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date and time that evidence needs to be submitted by

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the chargeback

[`total_amount` ](#field-total-amount)· [`String` ](/reference/2026-01-01/scalars/string)· The total cost of the chargeback. Includes both the disputed amount and the fee

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time the chargeback was last updated

## Used By

[`BillingItem.charge_backs`](/reference/2026-01-01/objects/billingitem)

[`ChargeBackEdge.node`](/reference/2026-01-01/objects/chargebackedge)

[`ChargeBackPaginationConnection.nodes`](/reference/2026-01-01/objects/chargebackpaginationconnection)

[`updateChargeBackPayload.charge_back`](/reference/2026-01-01/objects/updatechargebackpayload)

[`Query.chargeBack`](/reference/2026-01-01/queries/chargeback)

## Definition

```
"""
A Chargeback object, contains info on the dispute reason, status, and evidence submitted
"""
type ChargeBack {
  """
  The payment in Healthie that was disputed
  """
  billing_item: BillingItem


  """
  The date and time the chargeback was initiated
  """
  created_at: ISO8601DateTime!


  """
  The amount that was disputed
  """
  disputed_amount: String


  """
  Evidence to contest the chargeback
  """
  evidence: ChargeBackEvidence


  """
  Fields that should be submitted for this chargeback
  """
  evidence_fields_to_submit: [String]


  """
  The dispute fee charged by the payment processor
  """
  fee: String


  """
  A formatted version of the reason
  """
  formatted_reason: String


  """
  A formatted version of the status
  """
  formatted_status: String


  """
  The unique identifier of the chargeback
  """
  id: ID!


  """
  The reason for the chargeback. Matches Stripe's list of reasons at https://stripe.com/docs/api/disputes/object?lang=ruby
  """
  reason: String


  """
  The date and time that evidence needs to be submitted by
  """
  response_required_by: ISO8601DateTime


  """
  The status of the chargeback
  """
  status: String


  """
  The total cost of the chargeback. Includes both the disputed amount and the fee
  """
  total_amount: String


  """
  The date and time the chargeback was last updated
  """
  updated_at: ISO8601DateTime!
}
```
