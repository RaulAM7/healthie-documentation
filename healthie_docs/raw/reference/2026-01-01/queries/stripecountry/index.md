---
title: stripeCountry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/stripecountry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/stripecountry/index.md
---

An object containing info about a country that stripe supports

## Arguments

[`country_code` ](#argument-country-code)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`StripeCountry`](/reference/2026-01-01/objects/stripecountry)

## Example

```
query stripeCountry($country_code: String) {
  stripeCountry(country_code: $country_code) {
    accepted_currencies
    country_code
    currency
    field1
    field2
    name
  }
}
```
