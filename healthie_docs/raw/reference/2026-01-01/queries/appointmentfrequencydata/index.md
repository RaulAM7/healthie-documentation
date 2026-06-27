---
title: appointmentFrequencyData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentfrequencydata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentfrequencydata/index.md
---

returns metadata about appointments for provider dashboard

## Arguments

[`only_to_current_date` ](#argument-only-to-current-date)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`org_level` ](#argument-org-level)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

## Returns

[`[AppointmentDataType!]`](/reference/2026-01-01/objects/appointmentdatatype)

## Example

```
query appointmentFrequencyData(
  $only_to_current_date: Boolean
  $org_level: Boolean
) {
  appointmentFrequencyData(
    only_to_current_date: $only_to_current_date
    org_level: $org_level
  ) {
    freq
    month
  }
}
```
