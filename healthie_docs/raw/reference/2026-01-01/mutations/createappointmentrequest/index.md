---
title: createAppointmentRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmentrequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmentrequest/index.md
---

Create a new appointment request as a part of the booking flow

## Arguments

[`input` ](#argument-input)· [`createAppointmentRequestInput` ](/reference/2026-01-01/input-objects/createappointmentrequestinput)· Parameters for createAppointmentRequest

## Returns

[`createAppointmentRequestPayload`](/reference/2026-01-01/objects/createappointmentrequestpayload)

## Example

```
mutation createAppointmentRequest($input: createAppointmentRequestInput) {
  createAppointmentRequest(input: $input) {
    appointmentRequest
    messages
  }
}
```
