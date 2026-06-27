---
title: updateAppointmentSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmentsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateappointmentsetting/index.md
---

update Appointment Setting

## Arguments

[`input` ](#argument-input)· [`updateAppointmentSettingInput` ](/reference/2026-01-01/input-objects/updateappointmentsettinginput)· Parameters for updateAppointmentSetting

## Returns

[`updateAppointmentSettingPayload`](/reference/2026-01-01/objects/updateappointmentsettingpayload)

## Example

```
mutation updateAppointmentSetting($input: updateAppointmentSettingInput) {
  updateAppointmentSetting(input: $input) {
    appointmentSetting
    messages
  }
}
```
