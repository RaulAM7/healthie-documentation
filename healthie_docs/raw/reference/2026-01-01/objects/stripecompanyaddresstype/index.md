---
title: StripeCompanyAddressType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecompanyaddresstype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecompanyaddresstype/index.md
---

A Stripe company address object

## Fields

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city or town of the address.

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· The two-letter country code of the address.

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· The first line of the address.

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· The second line of the address.

[`postal_code` ](#field-postal-code)· [`String` ](/reference/2026-01-01/scalars/string)· The postal code of the address.

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state or province of the address.

## Used By

[`StripeCompanyType.address`](/reference/2026-01-01/objects/stripecompanytype)

## Definition

```
"""
A Stripe company address object
"""
type StripeCompanyAddressType {
  """
  The city or town of the address.
  """
  city: String


  """
  The two-letter country code of the address.
  """
  country: String


  """
  The first line of the address.
  """
  line1: String


  """
  The second line of the address.
  """
  line2: String


  """
  The postal code of the address.
  """
  postal_code: String


  """
  The state or province of the address.
  """
  state: String
}
```
