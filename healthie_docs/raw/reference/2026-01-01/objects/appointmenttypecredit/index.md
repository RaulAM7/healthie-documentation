---
title: AppointmentTypeCredit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypecredit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypecredit/index.md
---

An object containing information the clients' remaining credit for a given appointment type

## Fields

[`appointment_type` ](#field-appointment-type)· [`AppointmentType` ](/reference/2026-01-01/objects/appointmenttype)· The Appointment Type connected to the credit

[`appointment_type_id` ](#field-appointment-type-id)· [`String` ](/reference/2026-01-01/scalars/string)· the id of the appointment type

[`form_id` ](#field-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· An Alias of ID that makes creating the form easier

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the credit

[`quantity` ](#field-quantity)· [`String` ](/reference/2026-01-01/scalars/string)· The quantity of the credit

[`user_id` ](#field-user-id)· [`Int` ](/reference/2026-01-01/scalars/int)· The id of the holder of the credit

## Used By

[`User.appointment_type_credits`](/reference/2026-01-01/objects/user)

## Definition

```
"""
An object containing information the clients' remaining credit for a given appointment type
"""
type AppointmentTypeCredit {
  """
  The Appointment Type connected to the credit
  """
  appointment_type: AppointmentType


  """
  the id of the appointment type
  """
  appointment_type_id: String


  """
  An Alias of ID that makes creating the form easier
  """
  form_id: String


  """
  The unique identifier of the credit
  """
  id: ID


  """
  The quantity of the credit
  """
  quantity: String


  """
  The id of the holder of the credit
  """
  user_id: Int
}
```
