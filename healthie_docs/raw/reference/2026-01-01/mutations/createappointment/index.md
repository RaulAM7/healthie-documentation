---
title: createAppointment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointment/index.md
---

create appointment mutation for providers. Clients use the completeCheckout mutation

## Arguments

[`input` ](#argument-input)· [`createAppointmentInput!` ](/reference/2026-01-01/input-objects/createappointmentinput)· required · Parameters for createAppointment

## Returns

[`createAppointmentPayload`](/reference/2026-01-01/objects/createappointmentpayload)

## Example

```
mutation createAppointment($input: createAppointmentInput!) {
  createAppointment(input: $input) {
    appointment
    messages
  }
}
```
