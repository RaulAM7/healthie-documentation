---
title: deleteExternalCalendar | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteexternalcalendar/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteexternalcalendar/index.md
---

Destroy an External Calendar

## Arguments

[`input` ](#argument-input)· [`deleteExternalCalendarInput` ](/reference/2026-01-01/input-objects/deleteexternalcalendarinput)· Parameters for deleteExternalCalendar

## Returns

[`deleteExternalCalendarPayload`](/reference/2026-01-01/objects/deleteexternalcalendarpayload)

## Example

```
mutation deleteExternalCalendar($input: deleteExternalCalendarInput) {
  deleteExternalCalendar(input: $input) {
    external_calendar
    messages
  }
}
```
