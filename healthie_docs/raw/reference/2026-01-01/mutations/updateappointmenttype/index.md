---
title: updateAppointmentType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmenttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmenttype/index.md
---

Update an Appointment Type and return Appointment Type

## Arguments

[`input` ](#argument-input)· [`updateAppointmentTypeInput` ](/reference/2026-01-01/input-objects/updateappointmenttypeinput)· Parameters for updateAppointmentType

## Returns

[`updateAppointmentTypePayload`](/reference/2026-01-01/objects/updateappointmenttypepayload)

## Example

```
mutation updateAppointmentType($input: updateAppointmentTypeInput) {
  updateAppointmentType(input: $input) {
    appointmentType
    messages
    sms_template_warning
  }
}
```
