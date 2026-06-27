---
title: editAvailabilityWithAppointmentTypes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/editavailabilitywithappointmenttypes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/editavailabilitywithappointmenttypes/index.md
---

Edit a one-time availability associated with multiple appointment types

## Arguments

[`input` ](#argument-input)· [`EditAvailabilityWithAppointmentTypesInput!` ](/reference/2026-01-01/input-objects/editavailabilitywithappointmenttypesinput)· required · Parameters for EditAvailabilityWithAppointmentTypes

## Returns

[`EditAvailabilityWithAppointmentTypesPayload`](/reference/2026-01-01/objects/editavailabilitywithappointmenttypespayload)

## Example

```
mutation editAvailabilityWithAppointmentTypes(
  $input: EditAvailabilityWithAppointmentTypesInput!
) {
  editAvailabilityWithAppointmentTypes(input: $input) {
    availability
    messages
  }
}
```
