---
title: createAppointmentTypeCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmenttypecptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmenttypecptcode/index.md
---

Create an Appointment Type CPT Code Object

## Arguments

[`input` ](#argument-input)· [`createAppointmentTypeCptCodeInput` ](/reference/2026-01-01/input-objects/createappointmenttypecptcodeinput)· Parameters for createAppointmentTypeCptCode

## Returns

[`createAppointmentTypeCptCodePayload`](/reference/2026-01-01/objects/createappointmenttypecptcodepayload)

## Example

```
mutation createAppointmentTypeCptCode(
  $input: createAppointmentTypeCptCodeInput
) {
  createAppointmentTypeCptCode(input: $input) {
    appointment_type_cpt_code
    messages
  }
}
```
