---
title: InsurancePayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/insurancepayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/insurancepayment/index.md
---

An insurance payment object

## Fields

[`ach_check_number` ](#field-ach-check-number)· [`String` ](/reference/2026-01-01/scalars/string)· The ACH or check number

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the payment record was created

[`created_by_id` ](#field-created-by-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user who created this payment (for manual payments)

[`deposit_status` ](#field-deposit-status)· [`InsurancePaymentsDepositStatusEnum!` ](/reference/2026-01-01/enums/insurancepaymentsdepositstatusenum)· required · The deposit status of the insurance payment

[`era_id` ](#field-era-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The associated ERA ID

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The insurance payment ID

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI number

[`organization_id` ](#field-organization-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the organization this payment belongs to

[`paid_amount` ](#field-paid-amount)· [`Float!` ](/reference/2026-01-01/scalars/float)· required · The amount paid

[`paid_date` ](#field-paid-date)· [`ISO8601Date!` ](/reference/2026-01-01/scalars/iso8601date)· required · The date the payment was made

[`payer_name` ](#field-payer-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the payer

[`source` ](#field-source)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The source of the payment (automatic or manual)

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the payment record was last updated

## Used By

[`InsurancePaymentConnection.nodes`](/reference/2026-01-01/objects/insurancepaymentconnection)

[`InsurancePaymentEdge.node`](/reference/2026-01-01/objects/insurancepaymentedge)

[`createInsurancePaymentPayload.insurance_payment`](/reference/2026-01-01/objects/createinsurancepaymentpayload)

[`deleteManualInsurancePaymentPayload.insurance_payment`](/reference/2026-01-01/objects/deletemanualinsurancepaymentpayload)

[`updateInsurancePaymentDepositStatusPayload.insurance_payment`](/reference/2026-01-01/objects/updateinsurancepaymentdepositstatuspayload)

[`updateManualInsurancePaymentPayload.insurance_payment`](/reference/2026-01-01/objects/updatemanualinsurancepaymentpayload)

## Definition

```
"""
An insurance payment object
"""
type InsurancePayment {
  """
  The ACH or check number
  """
  ach_check_number: String


  """
  When the payment record was created
  """
  created_at: ISO8601DateTime!


  """
  The ID of the user who created this payment (for manual payments)
  """
  created_by_id: ID


  """
  The deposit status of the insurance payment
  """
  deposit_status: InsurancePaymentsDepositStatusEnum!


  """
  The associated ERA ID
  """
  era_id: ID


  """
  The insurance payment ID
  """
  id: ID!


  """
  The NPI number
  """
  npi: String


  """
  The ID of the organization this payment belongs to
  """
  organization_id: ID!


  """
  The amount paid
  """
  paid_amount: Float!


  """
  The date the payment was made
  """
  paid_date: ISO8601Date!


  """
  The name of the payer
  """
  payer_name: String!


  """
  The source of the payment (automatic or manual)
  """
  source: String!


  """
  When the payment record was last updated
  """
  updated_at: ISO8601DateTime!
}
```
