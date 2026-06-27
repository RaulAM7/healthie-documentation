---
title: OfferingInclude | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringinclude/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringinclude/index.md
---

Offering Include

## Fields

[`appointment_type` ](#field-appointment-type)· [`AppointmentType` ](/reference/2026-01-01/objects/appointmenttype)· appointment type

[`appointment_type_id` ](#field-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of related appointment type

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at

[`expires_in` ](#field-expires-in)· [`String` ](/reference/2026-01-01/scalars/string)· expires in

[`form_id` ](#field-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· form id

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the offering include.

[`is_repeating` ](#field-is-repeating)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · whether or not the offering\_include (appointment type) should be recurring

[`offering_id` ](#field-offering-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of related offering

[`quantity` ](#field-quantity)· [`String` ](/reference/2026-01-01/scalars/string)· quantity of appointments in package

[`required_appointment_type` ](#field-required-appointment-type)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · whether or not the offering book

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

## Used By

[`Offering.offering_includes`](/reference/2026-01-01/objects/offering)

[`Query.initializedOfferingIncludes`](/reference/2026-01-01/queries/initializedofferingincludes)

## Definition

```
"""
Offering Include
"""
type OfferingInclude {
  """
  appointment type
  """
  appointment_type: AppointmentType


  """
  id of related appointment type
  """
  appointment_type_id: ID


  """
  created at
  """
  created_at: ISO8601DateTime!


  """
  expires in
  """
  expires_in: String


  """
  form id
  """
  form_id: String


  """
  The unique identifier of the offering include.
  """
  id: ID!


  """
  whether or not the offering_include (appointment type) should be recurring
  """
  is_repeating: Boolean!


  """
  id of related offering
  """
  offering_id: ID


  """
  quantity of appointments in package
  """
  quantity: String


  """
  whether or not the offering book
  """
  required_appointment_type: Boolean!


  """
  updated at
  """
  updated_at: ISO8601DateTime!
}
```
