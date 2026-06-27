---
title: OrganizationSettingsInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/organizationsettingsinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/organizationsettingsinput/index.md
---

Configuration options for an organization

## Fields

[`conditional_form_questions` ](#field-conditional-form-questions)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Enables conditional logic in the form builder

[`booking_state_license_restrictions` ](#field-booking-state-license-restrictions)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Enables restricting booking based on provider state licensure

[`appointment_type_specific_appointment_settings` ](#field-appointment-type-specific-appointment-settings)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Enables configuring appointment settings for specific appointment types

[`sync_calendar_events_with_main_cal` ](#field-sync-calendar-events-with-main-cal)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Enables pushing Healthie events to the primary Google Calendar of the synced user (vs a sub-calendar)

[`scheduling_priority_levels` ](#field-scheduling-priority-levels)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Enables configuring priority levels for individual providers (used by our availability algorithm)

## Used By

[`SubOrganizationInfoInput.organization_settings`](/reference/2026-01-01/input-objects/suborganizationinfoinput)

## Definition

```
"""
Configuration options for an organization
"""
input OrganizationSettingsInput {
  """
  Enables conditional logic in the form builder
  """
  conditional_form_questions: Boolean = false


  """
  Enables restricting booking based on provider state licensure
  """
  booking_state_license_restrictions: Boolean = false


  """
  Enables configuring appointment settings for specific appointment types
  """
  appointment_type_specific_appointment_settings: Boolean = false


  """
  Enables pushing Healthie events to the primary Google Calendar of the synced user (vs a sub-calendar)
  """
  sync_calendar_events_with_main_cal: Boolean = false


  """
  Enables configuring priority levels for individual providers (used by our availability algorithm)
  """
  scheduling_priority_levels: Boolean = false
}
```
