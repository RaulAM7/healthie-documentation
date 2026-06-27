---
title: createAvailabilityWithAppointmentTypes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createavailabilitywithappointmenttypes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createavailabilitywithappointmenttypes/index.md
---

Create a one-time availability associated with multiple appointment types

## Arguments

[`input` ](#argument-input)· [`CreateAvailabilityWithAppointmentTypesInput!` ](/reference/2026-01-01/input-objects/createavailabilitywithappointmenttypesinput)· required · Parameters for CreateAvailabilityWithAppointmentTypes

## Returns

[`CreateAvailabilityWithAppointmentTypesPayload`](/reference/2026-01-01/objects/createavailabilitywithappointmenttypespayload)

## Example

```
mutation createAvailabilityWithAppointmentTypes(
  $input: CreateAvailabilityWithAppointmentTypesInput!
) {
  createAvailabilityWithAppointmentTypes(input: $input) {
    availability
    messages
  }
}
```
