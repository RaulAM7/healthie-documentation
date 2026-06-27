---
title: AppointmentAutocompleteFormCreateInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmentautocompleteformcreateinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmentautocompleteformcreateinput/index.md
---

Attributes for an appointment autocomplete form

## Fields

[`custom_module_form_id` ](#field-custom-module-form-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The custom module form used for AI scribe

## Used By

[`createAppointmentTypeInput.appointment_autocomplete_form`](/reference/2026-01-01/input-objects/createappointmenttypeinput)

## Definition

```
"""
Attributes for an appointment autocomplete form
"""
input AppointmentAutocompleteFormCreateInput {
  """
  The custom module form used for AI scribe
  """
  custom_module_form_id: ID!
}
```
