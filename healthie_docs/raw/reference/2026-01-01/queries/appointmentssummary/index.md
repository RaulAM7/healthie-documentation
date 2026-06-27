---
title: appointmentsSummary | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentssummary/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentssummary/index.md
---

Data summary for appointment reports

## Arguments

[`provider_ids` ](#argument-provider-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`range_end` ](#argument-range-end)· [`String` ](/reference/2026-01-01/scalars/string)· If not provided, defaults to the current date

[`range_start` ](#argument-range-start)· [`String` ](/reference/2026-01-01/scalars/string)· If not provided, defaults to the current date

[`range_type` ](#argument-range-type)· [`String`](/reference/2026-01-01/scalars/string)

[`require_cache_threshold` ](#argument-require-cache-threshold)· [`Int` ](/reference/2026-01-01/scalars/int)· When provided, the query will require data to be loaded from cache if the appointment count is over the provided number. If data is not in the cache, it will return without data, and load the data in the cache in the background.

## Returns

[`AppointmentSummaryData`](/reference/2026-01-01/objects/appointmentsummarydata)

## Example

```
query appointmentsSummary(
  $provider_ids: [ID]
  $range_end: String
  $range_start: String
  $range_type: String
  $require_cache_threshold: Int
) {
  appointmentsSummary(
    provider_ids: $provider_ids
    range_end: $range_end
    range_start: $range_start
    range_type: $range_type
    require_cache_threshold: $require_cache_threshold
  ) {
    appointment_history
    appointment_history_per_provider
    appointment_history_per_provider_and_type
    appointment_history_per_type
    appointments_per_type_count
    avg_per_day
    avg_per_day_percent_diff
    busiest_days_of_week
    cache_generation_in_progress
    percent_diff
    total_count
  }
}
```
