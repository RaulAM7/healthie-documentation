---
title: AppointmentAutocompleteFormUpdateInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmentautocompleteformupdateinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmentautocompleteformupdateinput/index.md
---

Attributes for an appointment autocomplete form

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the appointment autocomplete form

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, will destroy the autocomplete form association

[`custom_module_form_id` ](#field-custom-module-form-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The custom module form used for AI scribe

## Used By

[`updateAppointmentTypeInput.appointment_autocomplete_form`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

## Definition

```
"""
Attributes for an appointment autocomplete form
"""
input AppointmentAutocompleteFormUpdateInput {
  """
  The ID of the appointment autocomplete form
  """
  id: ID


  """
  If true, will destroy the autocomplete form association
  """
  _destroy: Boolean


  """
  The custom module form used for AI scribe
  """
  custom_module_form_id: ID
}
```
