---
title: externalCalendars | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/externalcalendars/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/externalcalendars/index.md
---

Fetch paginated external calendars collection

## Arguments

[`calendar_type` ](#argument-calendar-type)· [`CalendarType`](/reference/2026-01-01/enums/calendartype)

[`calendar_status` ](#argument-calendar-status)· [`CalendarStatus`](/reference/2026-01-01/enums/calendarstatus)

[`is_org` ](#argument-is-org)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns external calendars for all providers in the org

[`include_suborganizations` ](#argument-include-suborganizations)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· include all providers in the organization and sub-organizations

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ExternalCalendarConnection`](/reference/2026-01-01/objects/externalcalendarconnection)

## Example

```
query externalCalendars(
  $calendar_type: CalendarType
  $calendar_status: CalendarStatus
  $is_org: Boolean
  $include_suborganizations: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  externalCalendars(
    calendar_type: $calendar_type
    calendar_status: $calendar_status
    is_org: $is_org
    include_suborganizations: $include_suborganizations
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
