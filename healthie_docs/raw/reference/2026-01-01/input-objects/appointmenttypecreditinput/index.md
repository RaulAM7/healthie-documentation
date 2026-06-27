---
title: AppointmentTypeCreditInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmenttypecreditinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmenttypecreditinput/index.md
---

Payload for appointment type credit

## Fields

[`appointment_type_id` ](#field-appointment-type-id)· [`String` ](/reference/2026-01-01/scalars/string)· The appointment type ID of the credit

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the credit

[`quantity` ](#field-quantity)· [`String` ](/reference/2026-01-01/scalars/string)· The quantity of the credit

## Used By

[`updateClientInput.appointment_type_credits_attributes`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateStripeVerificationDetailsInput.appointment_type_credits_attributes`](/reference/2026-01-01/input-objects/updatestripeverificationdetailsinput)

## Definition

```
"""
Payload for appointment type credit
"""
input AppointmentTypeCreditInput {
  """
  The appointment type ID of the credit
  """
  appointment_type_id: String


  """
  The ID of the credit
  """
  id: ID


  """
  The quantity of the credit
  """
  quantity: String
}
```
