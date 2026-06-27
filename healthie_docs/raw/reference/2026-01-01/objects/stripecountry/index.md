---
title: StripeCountry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecountry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecountry/index.md
---

A Stripe country

## Fields

[`accepted_currencies` ](#field-accepted-currencies)· [`[String]` ](/reference/2026-01-01/scalars/string)· The accepted currencies for this country

[`country_code` ](#field-country-code)· [`String` ](/reference/2026-01-01/scalars/string)· The country code

[`currency` ](#field-currency)· [`String` ](/reference/2026-01-01/scalars/string)· The currency of the country

[`field1` ](#field-field1)· [`String` ](/reference/2026-01-01/scalars/string)· A custom field 1

[`field2` ](#field-field2)· [`String` ](/reference/2026-01-01/scalars/string)· A custom field 2

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the country

## Used By

[`Query.stripeCountries`](/reference/2026-01-01/queries/stripecountries)

[`Query.stripeCountry`](/reference/2026-01-01/queries/stripecountry)

## Definition

```
"""
A Stripe country
"""
type StripeCountry {
  """
  The accepted currencies for this country
  """
  accepted_currencies: [String]


  """
  The country code
  """
  country_code: String


  """
  The currency of the country
  """
  currency: String


  """
  A custom field 1
  """
  field1: String


  """
  A custom field 2
  """
  field2: String


  """
  The name of the country
  """
  name: String
}
```
