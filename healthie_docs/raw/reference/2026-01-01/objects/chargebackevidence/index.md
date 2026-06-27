---
title: ChargeBackEvidence | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chargebackevidence/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chargebackevidence/index.md
---

A Chargeback Evidence object, contains info to contest the dispute

## Fields

[`billing_address` ](#field-billing-address)· [`String` ](/reference/2026-01-01/scalars/string)· The billing address provided by the customer.

[`cancellation_policy` ](#field-cancellation-policy)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the uploaded cancellation\_policy.

[`cancellation_policy_disclosure` ](#field-cancellation-policy-disclosure)· [`String` ](/reference/2026-01-01/scalars/string)· An explanation of how and when the customer was shown your refund policy prior to purchase.

[`cancellation_rebuttal` ](#field-cancellation-rebuttal)· [`String` ](/reference/2026-01-01/scalars/string)· A justification for why the customer’s subscription was not canceled.

[`customer_communication` ](#field-customer-communication)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the uploaded customer\_communication.

[`customer_email_address` ](#field-customer-email-address)· [`String` ](/reference/2026-01-01/scalars/string)· The email address of the customer.

[`customer_name` ](#field-customer-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the customer.

[`product_description` ](#field-product-description)· [`String` ](/reference/2026-01-01/scalars/string)· A description of the product or services that were sold.

[`refund_policy` ](#field-refund-policy)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the uploaded refund\_policy.

[`refund_policy_disclosure` ](#field-refund-policy-disclosure)· [`String` ](/reference/2026-01-01/scalars/string)· Documentation demonstrating that the customer was shown your refund policy prior to purchase.

[`refund_refusal_explanation` ](#field-refund-refusal-explanation)· [`String` ](/reference/2026-01-01/scalars/string)· A justification for why the customer is not entitled to a refund.

[`uncategorized_file` ](#field-uncategorized-file)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the uploaded uncategorized\_file.

[`uncategorized_text` ](#field-uncategorized-text)· [`String` ](/reference/2026-01-01/scalars/string)· Any additional evidence or statements.

## Used By

[`ChargeBack.evidence`](/reference/2026-01-01/objects/chargeback)

## Definition

```
"""
A Chargeback Evidence object, contains info to contest the dispute
"""
type ChargeBackEvidence {
  """
  The billing address provided by the customer.
  """
  billing_address: String


  """
  ID of the uploaded cancellation_policy.
  """
  cancellation_policy: String


  """
  An explanation of how and when the customer was shown your refund policy prior to purchase.
  """
  cancellation_policy_disclosure: String


  """
  A justification for why the customer’s subscription was not canceled.
  """
  cancellation_rebuttal: String


  """
  ID of the uploaded customer_communication.
  """
  customer_communication: String


  """
  The email address of the customer.
  """
  customer_email_address: String


  """
  The name of the customer.
  """
  customer_name: String


  """
  A description of the product or services that were sold.
  """
  product_description: String


  """
  ID of the uploaded refund_policy.
  """
  refund_policy: String


  """
  Documentation demonstrating that the customer was shown your refund policy prior to purchase.
  """
  refund_policy_disclosure: String


  """
  A justification for why the customer is not entitled to a refund.
  """
  refund_refusal_explanation: String


  """
  ID of the uploaded uncategorized_file.
  """
  uncategorized_file: String


  """
  Any additional evidence or statements.
  """
  uncategorized_text: String
}
```
