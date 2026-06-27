---
title: updateAppointmentInclusion | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmentinclusion/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmentinclusion/index.md
---

Update AppointmentInclusion

## Arguments

[`input` ](#argument-input)· [`updateAppointmentInclusionInput` ](/reference/2026-01-01/input-objects/updateappointmentinclusioninput)· Parameters for updateAppointmentInclusion

## Returns

[`updateAppointmentInclusionPayload`](/reference/2026-01-01/objects/updateappointmentinclusionpayload)

## Example

```
mutation updateAppointmentInclusion($input: updateAppointmentInclusionInput) {
  updateAppointmentInclusion(input: $input) {
    appointment_inclusion
    messages
  }
}
```
