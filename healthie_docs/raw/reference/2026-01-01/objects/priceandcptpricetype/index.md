---
title: PriceAndCptPriceType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/priceandcptpricetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/priceandcptpricetype/index.md
---

Appointment type price and cpt\_code\_price

## Fields

[`cpt_price` ](#field-cpt-price)· [`String` ](/reference/2026-01-01/scalars/string)· The cpt\_code\_price for this appointment type

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· The price for this appointment type

## Used By

[`AppointmentType.price_and_cpt_price`](/reference/2026-01-01/objects/appointmenttype)

## Definition

```
"""
Appointment type price and cpt_code_price
"""
type PriceAndCptPriceType {
  """
  The cpt_code_price for this appointment type
  """
  cpt_price: String


  """
  The price for this appointment type
  """
  price: String
}
```
