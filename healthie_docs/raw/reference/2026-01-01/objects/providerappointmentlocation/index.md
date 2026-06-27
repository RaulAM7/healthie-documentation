---
title: ProviderAppointmentLocation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/providerappointmentlocation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/providerappointmentlocation/index.md
---

A provider appointment location object

## Fields

[`appointment_location_id` ](#field-appointment-location-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the appointment location

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the location

[`location` ](#field-location)· [`String` ](/reference/2026-01-01/scalars/string)· The location (in plain text)

## Used By

[`User.provider_appointment_locations`](/reference/2026-01-01/objects/user)

## Definition

```
"""
A provider appointment location object
"""
type ProviderAppointmentLocation {
  """
  The unique identifier of the appointment location
  """
  appointment_location_id: ID


  """
  The unique identifier of the location
  """
  id: ID!


  """
  The location (in plain text)
  """
  location: String
}
```
