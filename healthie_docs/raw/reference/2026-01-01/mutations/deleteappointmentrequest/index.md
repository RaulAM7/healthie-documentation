---
title: deleteAppointmentRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointmentrequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointmentrequest/index.md
---

Delete an existing appointment request

## Arguments

[`input` ](#argument-input)· [`deleteAppointmentRequestInput` ](/reference/2026-01-01/input-objects/deleteappointmentrequestinput)· Parameters for deleteAppointmentRequest

## Returns

[`deleteAppointmentRequestPayload`](/reference/2026-01-01/objects/deleteappointmentrequestpayload)

## Example

```
mutation deleteAppointmentRequest($input: deleteAppointmentRequestInput) {
  deleteAppointmentRequest(input: $input) {
    appointmentRequest
    messages
  }
}
```
