---
title: OfferingIncludesFields | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/offeringincludesfields/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/offeringincludesfields/index.md
---

Payload for an include to an offering

## Fields

[`appointment_type_id` ](#field-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the appointment type

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the object

[`is_repeating` ](#field-is-repeating)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the offering is repeating

[`quantity` ](#field-quantity)· [`String` ](/reference/2026-01-01/scalars/string)· The quantity of the offering

[`required_appointment_type` ](#field-required-appointment-type)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the appointment type is required

## Used By

[`createOfferingInput.offering_includes`](/reference/2026-01-01/input-objects/createofferinginput)

[`updateOfferingInput.offering_includes`](/reference/2026-01-01/input-objects/updateofferinginput)

## Definition

```
"""
Payload for an include to an offering
"""
input OfferingIncludesFields {
  """
  The unique identifier of the appointment type
  """
  appointment_type_id: ID


  """
  The unique identifier of the object
  """
  id: ID


  """
  Whether the offering is repeating
  """
  is_repeating: Boolean


  """
  The quantity of the offering
  """
  quantity: String


  """
  Whether the appointment type is required
  """
  required_appointment_type: Boolean
}
```
