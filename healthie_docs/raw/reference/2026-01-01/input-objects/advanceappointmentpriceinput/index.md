---
title: AdvanceAppointmentPriceInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/advanceappointmentpriceinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/advanceappointmentpriceinput/index.md
---

Payload for an advance appointment price

## Fields

[`appointment_type_id` ](#field-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment type

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the price

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· The price of the appointment type

## Used By

[`updateClientInput.advance_appointment_prices`](/reference/2026-01-01/input-objects/updateclientinput)

## Definition

```
"""
Payload for an advance appointment price
"""
input AdvanceAppointmentPriceInput {
  """
  The ID of the appointment type
  """
  appointment_type_id: ID


  """
  The ID of the price
  """
  id: ID


  """
  The price of the appointment type
  """
  price: String
}
```
