---
title: updateExternalCalendar | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateexternalcalendar/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateexternalcalendar/index.md
---

Update an External Calendar

## Arguments

[`input` ](#argument-input)· [`updateExternalCalendarInput` ](/reference/2026-01-01/input-objects/updateexternalcalendarinput)· Parameters for updateExternalCalendar

## Returns

[`updateExternalCalendarPayload`](/reference/2026-01-01/objects/updateexternalcalendarpayload)

## Example

```
mutation updateExternalCalendar($input: updateExternalCalendarInput) {
  updateExternalCalendar(input: $input) {
    external_calendar
    messages
  }
}
```
