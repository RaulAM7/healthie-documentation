---
title: appointmentNumberPerDayOfMonth | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentnumberperdayofmonth/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentnumberperdayofmonth/index.md
---

Returns a json hash of the number of appointments in each day of the month. The month is the month that the passed day is in.

## Arguments

[`date` ](#argument-date)· [`String` ](/reference/2026-01-01/scalars/string)· If not provided, defaults to the current date

[`include_blockers` ](#argument-include-blockers)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query appointmentNumberPerDayOfMonth(
  $date: String
  $include_blockers: Boolean
) {
  appointmentNumberPerDayOfMonth(
    date: $date
    include_blockers: $include_blockers
  )
}
```
