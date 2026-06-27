---
title: AppointmentAutocompleteForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentautocompleteform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentautocompleteform/index.md
---

Autocomplete form for appointment type. Used for AI-generated charting notes.

## Fields

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· Custom module form for the appointment type

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the appointment autocomplete form

## Used By

[`AppointmentType.appointment_autocomplete_form`](/reference/2026-01-01/objects/appointmenttype)

## Definition

```
"""
Autocomplete form for appointment type. Used for AI-generated charting notes.
"""
type AppointmentAutocompleteForm {
  """
  Custom module form for the appointment type
  """
  custom_module_form: CustomModuleForm


  """
  ID of the appointment autocomplete form
  """
  id: ID
}
```
