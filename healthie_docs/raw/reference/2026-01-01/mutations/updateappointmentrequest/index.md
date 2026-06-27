---
title: updateAppointmentRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmentrequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmentrequest/index.md
---

Update an existing appointment request

## Arguments

[`input` ](#argument-input)· [`updateAppointmentRequestInput` ](/reference/2026-01-01/input-objects/updateappointmentrequestinput)· Parameters for updateAppointmentRequest

## Returns

[`updateAppointmentRequestPayload`](/reference/2026-01-01/objects/updateappointmentrequestpayload)

## Example

```
mutation updateAppointmentRequest($input: updateAppointmentRequestInput) {
  updateAppointmentRequest(input: $input) {
    appointmentRequest
    messages
  }
}
```
