---
title: updateAppointment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointment/index.md
---

Update the Appointment

## Arguments

[`input` ](#argument-input)· [`updateAppointmentInput!` ](/reference/2026-01-01/input-objects/updateappointmentinput)· required · Parameters for updateAppointment

## Returns

[`updateAppointmentPayload`](/reference/2026-01-01/objects/updateappointmentpayload)

## Example

```
mutation updateAppointment($input: updateAppointmentInput!) {
  updateAppointment(input: $input) {
    appointment
    messages
  }
}
```
