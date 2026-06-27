---
title: timesForRange | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/timesforrange/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/timesforrange/index.md
---

deprecated use availableSlotsForRange.

## Arguments

[`appt_loc_id` ](#argument-appt-loc-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`appt_type_id` ](#argument-appt-type-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`endDate` ](#argument-enddate)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`length` ](#argument-length)· [`String`](/reference/2026-01-01/scalars/string)

[`startDate` ](#argument-startdate)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

## Returns

[`[String]`](/reference/2026-01-01/scalars/string)

## Example

```
query timesForRange(
  $appt_loc_id: ID
  $appt_type_id: ID
  $endDate: ISO8601DateTime
  $length: String
  $startDate: ISO8601DateTime
) {
  timesForRange(
    appt_loc_id: $appt_loc_id
    appt_type_id: $appt_type_id
    endDate: $endDate
    length: $length
    startDate: $startDate
  )
}
```
