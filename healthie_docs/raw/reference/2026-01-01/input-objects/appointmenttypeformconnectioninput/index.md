---
title: AppointmentTypeFormConnectionInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmenttypeformconnectioninput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmenttypeformconnectioninput/index.md
---

Payload for connecting an appointment type to a custom module form

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the appointment type form connection will be destroyed

[`custom_module_form_id` ](#field-custom-module-form-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the custom module form

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment type form connection

[`interval` ](#field-interval)· [`ISO8601Duration` ](/reference/2026-01-01/scalars/iso8601duration)· Form requests will be sent before or after given interval, depends on \`send\_trigger\`

## Used By

[`createAppointmentTypeInput.form_requests_before_appointment`](/reference/2026-01-01/input-objects/createappointmenttypeinput)

[`createAppointmentTypeInput.form_requests_after_appointment`](/reference/2026-01-01/input-objects/createappointmenttypeinput)

[`createAppointmentTypeInput.form_requests_after_appointment_booking`](/reference/2026-01-01/input-objects/createappointmenttypeinput)

[`updateAppointmentTypeInput.form_requests_before_appointment`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

[`updateAppointmentTypeInput.form_requests_after_appointment`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

[`updateAppointmentTypeInput.form_requests_after_appointment_booking`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

## Definition

```
"""
Payload for connecting an appointment type to a custom module form
"""
input AppointmentTypeFormConnectionInput {
  """
  If true, the appointment type form connection will be destroyed
  """
  _destroy: Boolean


  """
  The ID of the custom module form
  """
  custom_module_form_id: ID


  """
  The ID of the appointment type form connection
  """
  id: ID


  """
  Form requests will be sent before or after given interval, depends on `send_trigger`
  """
  interval: ISO8601Duration
}
```
