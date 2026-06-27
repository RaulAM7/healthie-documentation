---
title: ProviderApptTypeConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/providerappttypeconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/providerappttypeconnection/index.md
---

Provider appointment type connection

## Fields

[`appointment_type_id` ](#field-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The appointment type ID associated with this connection

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connection

[`provider_name` ](#field-provider-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the provider associated with this appointment type connection

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· User ID of the provider associated with this appointment type connection

## Used By

[`AppointmentType.provider_appt_type_connections`](/reference/2026-01-01/objects/appointmenttype)

## Definition

```
"""
Provider appointment type connection
"""
type ProviderApptTypeConnection {
  """
  The appointment type ID associated with this connection
  """
  appointment_type_id: ID


  """
  The unique identifier of the connection
  """
  id: ID!


  """
  Name of the provider associated with this appointment type connection
  """
  provider_name: String


  """
  User ID of the provider associated with this appointment type connection
  """
  user_id: ID
}
```
