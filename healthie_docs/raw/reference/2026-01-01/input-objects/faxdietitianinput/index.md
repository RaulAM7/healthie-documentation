---
title: FaxDietitianInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/faxdietitianinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/faxdietitianinput/index.md
---

Attributes to change a fax dietitian

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The custom identifier of the fax dietitian

[`location` ](#field-location)· [`FaxLocationInput` ](/reference/2026-01-01/input-objects/faxlocationinput)· The location of the fax dietitian

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the fax dietitian

[`qualifications` ](#field-qualifications)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifications of the fax dietitian

## Used By

[`createSentFaxInput.dietitian`](/reference/2026-01-01/input-objects/createsentfaxinput)

## Definition

```
"""
Attributes to change a fax dietitian
"""
input FaxDietitianInput {
  """
  The custom identifier of the fax dietitian
  """
  id: ID


  """
  The location of the fax dietitian
  """
  location: FaxLocationInput


  """
  The phone number of the fax dietitian
  """
  phone_number: String


  """
  The qualifications of the fax dietitian
  """
  qualifications: String
}
```
