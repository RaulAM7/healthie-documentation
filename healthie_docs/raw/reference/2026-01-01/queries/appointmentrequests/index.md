---
title: appointmentRequests | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentrequests/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentrequests/index.md
---

Fetch a collection of appointment requests for a provider or organization

## Arguments

[`order_by` ](#argument-order-by)· [`AppointmentRequestOrderKeys`](/reference/2026-01-01/enums/appointmentrequestorderkeys)

[`with_org` ](#argument-with-org)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· (DEPRECATED) Not in use.

[`appointment_location_ids` ](#argument-appointment-location-ids)· [`[ID!]` ](/reference/2026-01-01/scalars/id)· Filter by one or more appointment location IDs

[`current_status` ](#argument-current-status)· [`AppointmentRequestStatus` ](/reference/2026-01-01/enums/appointmentrequeststatus)· (DEPRECATED) Not in use.

[`current_statuses` ](#argument-current-statuses)· [`[AppointmentRequestStatus!]` ](/reference/2026-01-01/enums/appointmentrequeststatus)· Filter appointment requests by their current statuses

[`range_start` ](#argument-range-start)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Filter requests where the appointment requested slot is after this date

[`range_end` ](#argument-range-end)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Filter requests where the appointment requested slot is before this date

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`AppointmentRequestTypeConnection`](/reference/2026-01-01/objects/appointmentrequesttypeconnection)

## Example

```
query appointmentRequests(
  $order_by: AppointmentRequestOrderKeys
  $with_org: Boolean
  $appointment_location_ids: [ID!]
  $current_status: AppointmentRequestStatus
  $current_statuses: [AppointmentRequestStatus!]
  $range_start: ISO8601Date
  $range_end: ISO8601Date
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  appointmentRequests(
    order_by: $order_by
    with_org: $with_org
    appointment_location_ids: $appointment_location_ids
    current_status: $current_status
    current_statuses: $current_statuses
    range_start: $range_start
    range_end: $range_end
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
