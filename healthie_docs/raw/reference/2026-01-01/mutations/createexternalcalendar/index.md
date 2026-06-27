---
title: createExternalCalendar | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createexternalcalendar/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createexternalcalendar/index.md
---

Create an External Calendar

## Arguments

[`input` ](#argument-input)· [`createExternalCalendarInput` ](/reference/2026-01-01/input-objects/createexternalcalendarinput)· Parameters for createExternalCalendar

## Returns

[`createExternalCalendarPayload`](/reference/2026-01-01/objects/createexternalcalendarpayload)

## Example

```
mutation createExternalCalendar($input: createExternalCalendarInput) {
  createExternalCalendar(input: $input) {
    external_calendar
    messages
  }
}
```
