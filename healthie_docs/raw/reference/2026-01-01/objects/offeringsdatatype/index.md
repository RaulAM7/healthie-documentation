---
title: OfferingsDataType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringsdatatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringsdatatype/index.md
---

Offerings data type

## Fields

[`freq` ](#field-freq)· [`String` ](/reference/2026-01-01/scalars/string)· The frequency of the offering

[`month` ](#field-month)· [`String` ](/reference/2026-01-01/scalars/string)· The month of the offering

## Used By

[`Query.offeringsData`](/reference/2026-01-01/queries/offeringsdata)

## Definition

```
"""
Offerings data type
"""
type OfferingsDataType {
  """
  The frequency of the offering
  """
  freq: String


  """
  The month of the offering
  """
  month: String
}
```
