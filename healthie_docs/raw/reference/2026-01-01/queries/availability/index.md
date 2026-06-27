---
title: availability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/availability/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/availability/index.md
---

Fetch availability

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Availability`](/reference/2026-01-01/objects/availability)

## Example

```
query availability($id: ID) {
  availability(id: $id) {
    appointment_location_id
    appointment_type_id
    appointment_types
    contact_type_id
    created_at
    day_of_week
    duration_string
    end_on
    id
    is_repeating
    origin_start_date
    range_end
    range_start
    repeating_availability_id
    resourceId
    timezone
    timezone_abbr
    updated_at
    user
    user_id
  }
}
```
