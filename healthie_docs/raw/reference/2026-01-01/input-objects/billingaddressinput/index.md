---
title: BillingAddressInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/billingaddressinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/billingaddressinput/index.md
---

Payload for a billing address to create a new Healthie subscription.

## Fields

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· The country code

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· The first line of the address

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· The second line of the address

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state

[`postal_code` ](#field-postal-code)· [`String` ](/reference/2026-01-01/scalars/string)· The zip code

## Used By

[`createPersonalizationQuestionnaireInput.billing_address`](/reference/2026-01-01/input-objects/createpersonalizationquestionnaireinput)

[`createSubscriptionInput.billing_address`](/reference/2026-01-01/input-objects/createsubscriptioninput)

## Definition

```
"""
Payload for a billing address to create a new Healthie subscription.
"""
input BillingAddressInput {
  """
  The city
  """
  city: String


  """
  The country code
  """
  country: String


  """
  The first line of the address
  """
  line1: String


  """
  The second line of the address
  """
  line2: String


  """
  The state
  """
  state: String


  """
  The zip code
  """
  postal_code: String
}
```
