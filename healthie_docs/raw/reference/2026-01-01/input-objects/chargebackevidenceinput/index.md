---
title: ChargeBackEvidenceInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/chargebackevidenceinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/chargebackevidenceinput/index.md
---

Payload for a chargeback evidence

## Fields

[`billing_address` ](#field-billing-address)· [`String` ](/reference/2026-01-01/scalars/string)· The billing address of the customer

[`cancellation_policy` ](#field-cancellation-policy)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The cancellation policy file

[`cancellation_policy_disclosure` ](#field-cancellation-policy-disclosure)· [`String` ](/reference/2026-01-01/scalars/string)· The disclosure of the cancellation policy

[`cancellation_rebuttal` ](#field-cancellation-rebuttal)· [`String` ](/reference/2026-01-01/scalars/string)· The rebuttal of the cancellation

[`customer_communication` ](#field-customer-communication)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The communication with the customer

[`customer_email_address` ](#field-customer-email-address)· [`String` ](/reference/2026-01-01/scalars/string)· The email address of the customer

[`customer_name` ](#field-customer-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the customer

[`product_description` ](#field-product-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the product

[`refund_policy` ](#field-refund-policy)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The refund policy file

[`refund_policy_disclosure` ](#field-refund-policy-disclosure)· [`String` ](/reference/2026-01-01/scalars/string)· The disclosure of the refund policy

[`refund_refusal_explanation` ](#field-refund-refusal-explanation)· [`String` ](/reference/2026-01-01/scalars/string)· The explanation of the refund refusal

[`uncategorized_file` ](#field-uncategorized-file)· [`Upload` ](/reference/2026-01-01/scalars/upload)· The uncategorized file related to the chargeback

[`uncategorized_text` ](#field-uncategorized-text)· [`String` ](/reference/2026-01-01/scalars/string)· The uncategorized reason of the chargeback

## Used By

[`updateChargeBackInput.charge_back_evidence`](/reference/2026-01-01/input-objects/updatechargebackinput)

## Definition

```
"""
Payload for a chargeback evidence
"""
input ChargeBackEvidenceInput {
  """
  The billing address of the customer
  """
  billing_address: String


  """
  The cancellation policy file
  """
  cancellation_policy: Upload


  """
  The disclosure of the cancellation policy
  """
  cancellation_policy_disclosure: String


  """
  The rebuttal of the cancellation
  """
  cancellation_rebuttal: String


  """
  The communication with the customer
  """
  customer_communication: Upload


  """
  The email address of the customer
  """
  customer_email_address: String


  """
  The name of the customer
  """
  customer_name: String


  """
  The description of the product
  """
  product_description: String


  """
  The refund policy file
  """
  refund_policy: Upload


  """
  The disclosure of the refund policy
  """
  refund_policy_disclosure: String


  """
  The explanation of the refund refusal
  """
  refund_refusal_explanation: String


  """
  The uncategorized file related to the chargeback
  """
  uncategorized_file: Upload


  """
  The uncategorized reason of the chargeback
  """
  uncategorized_text: String
}
```
