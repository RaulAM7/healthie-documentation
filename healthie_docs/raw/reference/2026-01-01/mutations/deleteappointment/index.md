---
title: deleteAppointment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointment/index.md
---

Delete an Appointment

## Arguments

[`input` ](#argument-input)· [`deleteAppointmentInput` ](/reference/2026-01-01/input-objects/deleteappointmentinput)· Parameters for deleteAppointment

## Returns

[`deleteAppointmentPayload`](/reference/2026-01-01/objects/deleteappointmentpayload)

## Example

```
mutation deleteAppointment($input: deleteAppointmentInput) {
  deleteAppointment(input: $input) {
    appointment
    messages
  }
}
```
