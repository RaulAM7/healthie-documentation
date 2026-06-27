---
title: deleteAppointmentType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointmenttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointmenttype/index.md
---

Destroy an AppointmentType

## Arguments

[`input` ](#argument-input)· [`deleteAppointmentTypeInput` ](/reference/2026-01-01/input-objects/deleteappointmenttypeinput)· Parameters for deleteAppointmentType

## Returns

[`deleteAppointmentTypePayload`](/reference/2026-01-01/objects/deleteappointmenttypepayload)

## Example

```
mutation deleteAppointmentType($input: deleteAppointmentTypeInput) {
  deleteAppointmentType(input: $input) {
    appointmentType
    messages
  }
}
```
