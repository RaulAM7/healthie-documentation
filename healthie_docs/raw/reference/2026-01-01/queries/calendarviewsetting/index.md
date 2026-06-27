---
title: calendarViewSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/calendarviewsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/calendarviewsetting/index.md
---

Fetch a calendar view settings for current user

## Arguments

[`saved_filter_id` ](#argument-saved-filter-id)· [`ID` ](/reference/2026-01-01/scalars/id)· If passed values from a Saved Filter will be returned for the calendar settings

## Returns

[`CalendarViewSetting`](/reference/2026-01-01/objects/calendarviewsetting)

## Example

```
query calendarViewSetting($saved_filter_id: ID) {
  calendarViewSetting(saved_filter_id: $saved_filter_id) {
    appointment_status_filter
    appointment_statuses_filter
    appointment_type_filter
    appointment_types_filter
    availability_appointment_types_filter
    availability_appt_type_filter
    availability_contact_type_filter
    availability_location_filter
    availability_provider_filter
    calendar_color_scheme_filter
    calendar_interval
    calendar_view_filter
    client_confirmation_status
    contact_types_filter
    document_area_sorting
    expand_color_schemes
    expand_filter_appointments
    expand_filter_availabilities
    expand_filter_by_providers
    expand_filter_providers
    expand_show_availabilities
    favorite_saved_filter_id
    id
    insurance_plan_ids_filter
    location_filter
    locations_filter
    one_time_availabilities
    org_calendar_view_filter
    potential_filtered_provider_ids
    provider_confirmation_status
    selected_availability_provider_filter
    selected_availability_providers_filter
    selected_provider_filter
    selected_providers_filter
    show_appointments
    show_availabilities
    show_synced_appointments
    state_licenses_filter
    tag_ids_filter
    timezone
    weekly_availabilities
  }
}
```
