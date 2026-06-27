---
title: StripeCompanyType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecompanytype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecompanytype/index.md
---

A Stripe company

## Fields

[`address` ](#field-address)· [`StripeCompanyAddressType` ](/reference/2026-01-01/objects/stripecompanyaddresstype)· The company address

[`directors_provided` ](#field-directors-provided)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the company directors have been provided

[`executives_provided` ](#field-executives-provided)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the company executives have been provided

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The legal name of the company

[`owners_provided` ](#field-owners-provided)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the company owners have been provided

[`phone` ](#field-phone)· [`String` ](/reference/2026-01-01/scalars/string)· The company phone number

[`tax_id_provided` ](#field-tax-id-provided)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the company tax ID has been provided

[`verification` ](#field-verification)· [`String` ](/reference/2026-01-01/scalars/string)· The verification status of the company

## Used By

[`Query.stripeCompany`](/reference/2026-01-01/queries/stripecompany)

## Definition

```
"""
A Stripe company
"""
type StripeCompanyType {
  """
  The company address
  """
  address: StripeCompanyAddressType


  """
  Whether the company directors have been provided
  """
  directors_provided: Boolean


  """
  Whether the company executives have been provided
  """
  executives_provided: Boolean


  """
  The legal name of the company
  """
  name: String


  """
  Whether the company owners have been provided
  """
  owners_provided: Boolean


  """
  The company phone number
  """
  phone: String


  """
  Whether the company tax ID has been provided
  """
  tax_id_provided: Boolean


  """
  The verification status of the company
  """
  verification: String
}
```
