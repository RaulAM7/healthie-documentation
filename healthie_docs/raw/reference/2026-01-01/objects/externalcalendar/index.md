---
title: ExternalCalendar | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/externalcalendar/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/externalcalendar/index.md
---

An object containing info about the provider's external calendar

## Fields

[`add_to_calendar` ](#field-add-to-calendar)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send appointments to the external calendar

[`calendar_list` ](#field-calendar-list)· [`[String]` ](/reference/2026-01-01/scalars/string)· A list of potential calendars

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· Email of external calendar

[`external_type` ](#field-external-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of external calendar

[`has_ran_first_sync` ](#field-has-ran-first-sync)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Calendar has ran first sync

[`has_refresh_token` ](#field-has-refresh-token)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Calendar has refresh token

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the calendar

[`pull_from_calendar` ](#field-pull-from-calendar)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Pull in appointments from the external calendar

[`pull_in_event_details` ](#field-pull-in-event-details)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Calendar has pulled in location and note info otherwise it will contain 'Busy'

[`pulled_in_calendars` ](#field-pulled-in-calendars)· [`[String]` ](/reference/2026-01-01/scalars/string)· Selected calendars to pull in appointments from

[`resource_name` ](#field-resource-name)· [`String` ](/reference/2026-01-01/scalars/string)· The resource name (sync partner assigned ID) for the sync

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the provider associated with the calendar

## Used By

[`ExternalCalendarConnection.nodes`](/reference/2026-01-01/objects/externalcalendarconnection)

[`ExternalCalendarEdge.node`](/reference/2026-01-01/objects/externalcalendaredge)

[`User.broken_synced_cal`](/reference/2026-01-01/objects/user)

[`User.google_calendar`](/reference/2026-01-01/objects/user)

[`User.outlook`](/reference/2026-01-01/objects/user)

[`createExternalCalendarPayload.external_calendar`](/reference/2026-01-01/objects/createexternalcalendarpayload)

[`deleteExternalCalendarPayload.external_calendar`](/reference/2026-01-01/objects/deleteexternalcalendarpayload)

[`updateExternalCalendarPayload.external_calendar`](/reference/2026-01-01/objects/updateexternalcalendarpayload)

## Definition

```
"""
An object containing info about the provider's external calendar
"""
type ExternalCalendar {
  """
  Send appointments to the external calendar
  """
  add_to_calendar: Boolean


  """
  A list of potential calendars
  """
  calendar_list: [String]


  """
  Email of external calendar
  """
  email: String


  """
  The type of external calendar
  """
  external_type: String


  """
  Calendar has ran first sync
  """
  has_ran_first_sync: Boolean


  """
  Calendar has refresh token
  """
  has_refresh_token: Boolean


  """
  The unique identifier of the calendar
  """
  id: ID!


  """
  Pull in appointments from the external calendar
  """
  pull_from_calendar: Boolean


  """
  Calendar has pulled in location and note info otherwise it will contain 'Busy'
  """
  pull_in_event_details: Boolean


  """
  Selected calendars to pull in appointments from
  """
  pulled_in_calendars: [String]


  """
  The resource name (sync partner assigned ID) for the sync
  """
  resource_name: String


  """
  ID of the provider associated with the calendar
  """
  user_id: ID
}
```
