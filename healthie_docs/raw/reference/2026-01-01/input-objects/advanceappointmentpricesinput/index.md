---
title: AdvanceAppointmentPricesInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/advanceappointmentpricesinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/advanceappointmentpricesinput/index.md
---

Payload for overriding an advance appointment price

## Fields

[`appointment_type_id` ](#field-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment type

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the price

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· The price of the appointment type

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user

## Used By

[`updateUserAppointmentPricingInput.advance_appointment_prices`](/reference/2026-01-01/input-objects/updateuserappointmentpricinginput)

## Definition

```
"""
Payload for overriding an advance appointment price
"""
input AdvanceAppointmentPricesInput {
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


  """
  The ID of the user
  """
  user_id: ID
}
```
