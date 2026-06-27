---
title: initialServiceDate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/initialservicedate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/initialservicedate/index.md
---

Initial date of service for a new form answer group

## Arguments

[`appointment_id` ](#argument-appointment-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

## Example

```
query initialServiceDate($appointment_id: ID, $user_id: ID) {
  initialServiceDate(appointment_id: $appointment_id, user_id: $user_id)
}
```
