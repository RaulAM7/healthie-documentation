---
title: ContactType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/contacttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/contacttype/index.md
---

A object containing information about whether a specific contact type can be booked

## Fields

[`appointment_setting_id` ](#field-appointment-setting-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the connected appointment setting

[`appointment_type_id` ](#field-appointment-type-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the connected appointment type

[`form_id` ](#field-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· An Alias of ID that makes creating the form easier

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the contact type

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the contact type

[`show` ](#field-show)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether this contact type can be used

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the connected user

## Used By

[`AppointmentSetting.contact_type_overrides`](/reference/2026-01-01/objects/appointmentsetting)

## Definition

```
"""
A object containing information about whether a specific contact type can be booked
"""
type ContactType {
  """
  ID of the connected appointment setting
  """
  appointment_setting_id: String


  """
  ID of the connected appointment type
  """
  appointment_type_id: String


  """
  An Alias of ID that makes creating the form easier
  """
  form_id: String


  """
  The unique identifier of the contact type
  """
  id: ID


  """
  The graphql_name of the contact type
  """
  name: String


  """
  Whether this contact type can be used
  """
  show: Boolean!


  """
  The ID of the connected user
  """
  user_id: String
}
```
