---
title: recurringAppointment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/recurringappointment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/recurringappointment/index.md
---

Query a single recurring appointment

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the recurring appointment to fetch

## Returns

[`RecurringAppointment`](/reference/2026-01-01/objects/recurringappointment)

## Example

```
query recurringAppointment($id: ID!) {
  recurringAppointment(id: $id) {
    appointments
    id
    join_all
    previous_recurring_appointment_id
    repeat_interval
    repeat_times
  }
}
```
