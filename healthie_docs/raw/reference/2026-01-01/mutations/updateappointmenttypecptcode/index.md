---
title: updateAppointmentTypeCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmenttypecptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmenttypecptcode/index.md
---

Update a AppointmentTypeCptCode Object

## Arguments

[`input` ](#argument-input)· [`updateAppointmentTypeCptCodeInput` ](/reference/2026-01-01/input-objects/updateappointmenttypecptcodeinput)· Parameters for updateAppointmentTypeCptCode

## Returns

[`updateAppointmentTypeCptCodePayload`](/reference/2026-01-01/objects/updateappointmenttypecptcodepayload)

## Example

```
mutation updateAppointmentTypeCptCode(
  $input: updateAppointmentTypeCptCodeInput
) {
  updateAppointmentTypeCptCode(input: $input) {
    appointment_type_cpt_code
    messages
  }
}
```
