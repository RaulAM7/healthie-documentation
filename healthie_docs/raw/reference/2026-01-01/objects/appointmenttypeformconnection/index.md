---
title: AppointmentTypeFormConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypeformconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypeformconnection/index.md
---

An object containing event which should be taken before or after appointment

## Fields

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· ID of the form for the form completion request

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the form

[`interval` ](#field-interval)· [`ISO8601Duration` ](/reference/2026-01-01/scalars/iso8601duration)· Form requests will be sent before or after given interval, depends on \`send\_trigger\`

[`send_trigger` ](#field-send-trigger)· [`String` ](/reference/2026-01-01/scalars/string)· Determines when action should be taken(before or after appointment)

## Used By

[`AppointmentType.form_requests_after_appointment`](/reference/2026-01-01/objects/appointmenttype)

[`AppointmentType.form_requests_after_appointment_booking`](/reference/2026-01-01/objects/appointmenttype)

[`AppointmentType.form_requests_before_appointment`](/reference/2026-01-01/objects/appointmenttype)

## Definition

```
"""
An object containing event which should be taken before or after appointment
"""
type AppointmentTypeFormConnection {
  """
  ID of the form for the form completion request
  """
  custom_module_form: CustomModuleForm


  """
  The unique identifier of the form
  """
  id: ID!


  """
  Form requests will be sent before or after given interval, depends on `send_trigger`
  """
  interval: ISO8601Duration


  """
  Determines when action should be taken(before or after appointment)
  """
  send_trigger: String
}
```
