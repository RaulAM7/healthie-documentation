---
title: createAppointmentSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmentsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmentsetting/index.md
---

create an Appointment Setting

## Arguments

[`input` ](#argument-input)· [`createAppointmentSettingInput!` ](/reference/2026-01-01/input-objects/createappointmentsettinginput)· required · Parameters for createAppointmentSetting

## Returns

[`createAppointmentSettingPayload`](/reference/2026-01-01/objects/createappointmentsettingpayload)

## Example

```
mutation createAppointmentSetting($input: createAppointmentSettingInput!) {
  createAppointmentSetting(input: $input) {
    appointmentSetting
    messages
  }
}
```
