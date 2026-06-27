---
title: FaxLocationInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/faxlocationinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/faxlocationinput/index.md
---

Attributes to change a fax location

## Fields

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city of the fax location

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· The country of the fax location

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The custom identifier of the fax location

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· The first line of the fax location address

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· The second line of the fax location address

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state of the fax location

[`zip` ](#field-zip)· [`String` ](/reference/2026-01-01/scalars/string)· The zip code of the fax location

## Used By

[`FaxDietitianInput.location`](/reference/2026-01-01/input-objects/faxdietitianinput)

## Definition

```
"""
Attributes to change a fax location
"""
input FaxLocationInput {
  """
  The city of the fax location
  """
  city: String


  """
  The country of the fax location
  """
  country: String


  """
  The custom identifier of the fax location
  """
  id: ID


  """
  The first line of the fax location address
  """
  line1: String


  """
  The second line of the fax location address
  """
  line2: String


  """
  The state of the fax location
  """
  state: String


  """
  The zip code of the fax location
  """
  zip: String
}
```
