---
title: ProviderAppointmentLocationsInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/providerappointmentlocationsinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/providerappointmentlocationsinput/index.md
---

Payload to bind an appointment location to a provider

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the join table record will be deleted

[`appointment_location_id` ](#field-appointment-location-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment location

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the join table record

## Used By

[`updateOrganizationMemberInput.provider_appointment_locations`](/reference/2026-01-01/input-objects/updateorganizationmemberinput)

## Definition

```
"""
Payload to bind an appointment location to a provider
"""
input ProviderAppointmentLocationsInput {
  """
  If true, the join table record will be deleted
  """
  _destroy: Boolean


  """
  The ID of the appointment location
  """
  appointment_location_id: ID


  """
  The ID of the join table record
  """
  id: ID
}
```
