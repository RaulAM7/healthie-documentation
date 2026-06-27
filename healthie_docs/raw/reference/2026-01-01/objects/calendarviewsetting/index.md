---
title: CalendarViewSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/calendarviewsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/calendarviewsetting/index.md
---

View settings for provider calendar

## Fields

[`appointment_status_filter` ](#field-appointment-status-filter)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Filter appointments by status

[`appointment_statuses_filter` ](#field-appointment-statuses-filter)· [`[String]` ](/reference/2026-01-01/scalars/string)· Filter appointments by statuses

[`appointment_type_filter` ](#field-appointment-type-filter)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · ID of appointment type to filter appointments

[`appointment_types_filter` ](#field-appointment-types-filter)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Array of IDs of appointment types to filter appointments

[`availability_appointment_types_filter` ](#field-availability-appointment-types-filter)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Array of IDs of appointment types to filter availabilities

[`availability_appt_type_filter` ](#field-availability-appt-type-filter)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of appointment type to filter availabilities

[`availability_contact_type_filter` ](#field-availability-contact-type-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Filter availabilities by contact type

[`availability_location_filter` ](#field-availability-location-filter)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of location to filter availabilities

[`availability_provider_filter` ](#field-availability-provider-filter)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of provider to filter availabilities

[`availablilty_appt_type_filter` ](#field-availablilty-appt-type-filter)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of appointment type to filter availabilities

deprecated

Use \`availability\_appt\_type\_filter\` instead

[`calendar_color_scheme_filter` ](#field-calendar-color-scheme-filter)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of selected calendar color scheme

[`calendar_interval` ](#field-calendar-interval)· [`String` ](/reference/2026-01-01/scalars/string)· Selected calendar interval

[`calendar_view_filter` ](#field-calendar-view-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Selected calendar view

[`client_confirmation_status` ](#field-client-confirmation-status)· [`String` ](/reference/2026-01-01/scalars/string)· Filter appointments by client confirmation status

[`contact_types_filter` ](#field-contact-types-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Comma separated names of contact types to filter appointments

[`document_area_sorting` ](#field-document-area-sorting)· [`String` ](/reference/2026-01-01/scalars/string)· Selected sorting for documents(This is not a calendar setting. Related to documents area)

[`expand_color_schemes` ](#field-expand-color-schemes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of color schemes section

[`expand_filter_appointments` ](#field-expand-filter-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of appointment filters section

[`expand_filter_availabilities` ](#field-expand-filter-availabilities)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of availability filters section

[`expand_filter_by_providers` ](#field-expand-filter-by-providers)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of 'Filter Providers' section in organization calendar

[`expand_filter_providers` ](#field-expand-filter-providers)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of 'View By Provider' section in organization calendar

[`expand_show_availabilities` ](#field-expand-show-availabilities)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of show section

[`favorite_saved_filter_id` ](#field-favorite-saved-filter-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of favorite saved filter

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the setting

[`insurance_plan_ids_filter` ](#field-insurance-plan-ids-filter)· [`[ID!]` ](/reference/2026-01-01/scalars/id)· Filter appointments by provider accepted insurance ids

[`location_filter` ](#field-location-filter)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of location to filter appointments

[`locations_filter` ](#field-locations-filter)· [`[ID]` ](/reference/2026-01-01/scalars/id)· IDs of locations to filter appointments

[`one_time_availabilities` ](#field-one-time-availabilities)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of one time availabilities in calendar

[`org_calendar_view_filter` ](#field-org-calendar-view-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Selected organization calendar view

[`potential_filtered_provider_ids` ](#field-potential-filtered-provider-ids)· [`[ID!]` ](/reference/2026-01-01/scalars/id)· A collection of providers that can be selected, given the state and tag filters. If no filters are selected, this will be empty

[`provider_confirmation_status` ](#field-provider-confirmation-status)· [`String` ](/reference/2026-01-01/scalars/string)· Filter appointments by provider confirmation status

[`selected_availability_provider_filter` ](#field-selected-availability-provider-filter)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of selected provider to filter availabilities in organization calendar

[`selected_availability_providers_filter` ](#field-selected-availability-providers-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Comma separated IDs of providers to filter availabilities in organization calendar

[`selected_provider_filter` ](#field-selected-provider-filter)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of selected provider in organization calendar

[`selected_providers_filter` ](#field-selected-providers-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Comma separated IDs of selected providers in organization calendar

[`show_appointments` ](#field-show-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of all appointments

[`show_availabilities` ](#field-show-availabilities)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of all availabilities

[`show_synced_appointments` ](#field-show-synced-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of all synced appointments

[`state_licenses_filter` ](#field-state-licenses-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Filter appointments by provider state licenses

[`tag_ids_filter` ](#field-tag-ids-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Filter appointments by provider tags

[`timezone` ](#field-timezone)· [`String` ](/reference/2026-01-01/scalars/string)· Selected calendar timezone

[`weekly_availabilities` ](#field-weekly-availabilities)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Visibility of weekly availabilities in calendar

## Used By

[`Query.calendarViewSetting`](/reference/2026-01-01/queries/calendarviewsetting)

[`updateCalendarViewSettingPayload.calendar_view_setting`](/reference/2026-01-01/objects/updatecalendarviewsettingpayload)

## Definition

```
"""
View settings for provider calendar
"""
type CalendarViewSetting {
  """
  Filter appointments by status
  """
  appointment_status_filter: String!


  """
  Filter appointments by statuses
  """
  appointment_statuses_filter: [String]


  """
  ID of appointment type to filter appointments
  """
  appointment_type_filter: ID!


  """
  Array of IDs of appointment types to filter appointments
  """
  appointment_types_filter: [ID]


  """
  Array of IDs of appointment types to filter availabilities
  """
  availability_appointment_types_filter: [ID]


  """
  ID of appointment type to filter availabilities
  """
  availability_appt_type_filter: ID


  """
  Filter availabilities by contact type
  """
  availability_contact_type_filter: String


  """
  ID of location to filter availabilities
  """
  availability_location_filter: ID


  """
  ID of provider to filter availabilities
  """
  availability_provider_filter: ID


  """
  ID of appointment type to filter availabilities
  """
  availablilty_appt_type_filter: ID
    @deprecated(reason: "Use `availability_appt_type_filter` instead")


  """
  ID of selected calendar color scheme
  """
  calendar_color_scheme_filter: ID


  """
  Selected calendar interval
  """
  calendar_interval: String


  """
  Selected calendar view
  """
  calendar_view_filter: String


  """
  Filter appointments by client confirmation status
  """
  client_confirmation_status: String


  """
  Comma separated names of contact types to filter appointments
  """
  contact_types_filter: String


  """
  Selected sorting for documents(This is not a calendar setting. Related to documents area)
  """
  document_area_sorting: String


  """
  Visibility of color schemes section
  """
  expand_color_schemes: Boolean


  """
  Visibility of appointment filters section
  """
  expand_filter_appointments: Boolean


  """
  Visibility of availability filters section
  """
  expand_filter_availabilities: Boolean


  """
  Visibility of 'Filter Providers' section in organization calendar
  """
  expand_filter_by_providers: Boolean


  """
  Visibility of 'View By Provider' section in organization calendar
  """
  expand_filter_providers: Boolean


  """
  Visibility of show section
  """
  expand_show_availabilities: Boolean


  """
  ID of favorite saved filter
  """
  favorite_saved_filter_id: ID


  """
  The unique identifier of the setting
  """
  id: ID!


  """
  Filter appointments by provider accepted insurance ids
  """
  insurance_plan_ids_filter: [ID!]


  """
  ID of location to filter appointments
  """
  location_filter: ID


  """
  IDs of locations to filter appointments
  """
  locations_filter: [ID]


  """
  Visibility of one time availabilities in calendar
  """
  one_time_availabilities: Boolean


  """
  Selected organization calendar view
  """
  org_calendar_view_filter: String


  """
  A collection of providers that can be selected, given the state and tag filters. If no filters are selected, this will be empty
  """
  potential_filtered_provider_ids: [ID!]


  """
  Filter appointments by provider confirmation status
  """
  provider_confirmation_status: String


  """
  ID of selected provider to filter availabilities in organization calendar
  """
  selected_availability_provider_filter: ID


  """
  Comma separated IDs of providers to filter availabilities in organization calendar
  """
  selected_availability_providers_filter: String


  """
  ID of selected provider in organization calendar
  """
  selected_provider_filter: ID


  """
  Comma separated IDs of selected providers in organization calendar
  """
  selected_providers_filter: String


  """
  Visibility of all appointments
  """
  show_appointments: Boolean


  """
  Visibility of all availabilities
  """
  show_availabilities: Boolean


  """
  Visibility of all synced appointments
  """
  show_synced_appointments: Boolean


  """
  Filter appointments by provider state licenses
  """
  state_licenses_filter: String


  """
  Filter appointments by provider tags
  """
  tag_ids_filter: String


  """
  Selected calendar timezone
  """
  timezone: String


  """
  Visibility of weekly availabilities in calendar
  """
  weekly_availabilities: Boolean
}
```
