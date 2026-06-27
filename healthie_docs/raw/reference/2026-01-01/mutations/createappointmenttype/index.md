---
title: createAppointmentType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmenttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmenttype/index.md
---

create Appointment Type

## Arguments

[`input` ](#argument-input)· [`createAppointmentTypeInput` ](/reference/2026-01-01/input-objects/createappointmenttypeinput)· Parameters for createAppointmentType

## Returns

[`createAppointmentTypePayload`](/reference/2026-01-01/objects/createappointmenttypepayload)

## Example

```
mutation createAppointmentType($input: createAppointmentTypeInput) {
  createAppointmentType(input: $input) {
    appointmentType
    messages
    sms_template_warning
  }
}
```
