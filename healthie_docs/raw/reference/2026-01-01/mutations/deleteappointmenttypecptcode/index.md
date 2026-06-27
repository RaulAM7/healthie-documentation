---
title: deleteAppointmentTypeCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointmenttypecptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointmenttypecptcode/index.md
---

Delete a AppointmentTypeCptCode Object

## Arguments

[`input` ](#argument-input)· [`deleteAppointmentTypeCptCodeInput` ](/reference/2026-01-01/input-objects/deleteappointmenttypecptcodeinput)· Parameters for deleteAppointmentTypeCptCode

## Returns

[`deleteAppointmentTypeCptCodePayload`](/reference/2026-01-01/objects/deleteappointmenttypecptcodepayload)

## Example

```
mutation deleteAppointmentTypeCptCode(
  $input: deleteAppointmentTypeCptCodeInput
) {
  deleteAppointmentTypeCptCode(input: $input) {
    appointment_type_cpt_code
    messages
  }
}
```
