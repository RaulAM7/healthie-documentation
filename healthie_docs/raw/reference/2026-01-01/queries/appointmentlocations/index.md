---
title: appointmentLocations | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentlocations/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentlocations/index.md
---

Fetch paginated appointment locations collection

## Arguments

[`appointment_date` ](#argument-appointment-date)· [`String` ](/reference/2026-01-01/scalars/string)· Pass in datetime of the appointment to limit the locations based on room availability

[`appointment_type_id` ](#argument-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Pass in id of the appointment type to limit the locations based on room availability

[`ids` ](#argument-ids)· [`[Int]`](/reference/2026-01-01/scalars/int)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`location_ids` ](#argument-location-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`org_level` ](#argument-org-level)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`provider_ids` ](#argument-provider-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`resource` ](#argument-resource)· [`String`](/reference/2026-01-01/scalars/string)

[`with_availability` ](#argument-with-availability)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only locations with associated availabilities are returned. When false, only locations with no associated availabilities are returned. Does nothing unless availability by location enabled.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`AppointmentLocationPaginationConnection`](/reference/2026-01-01/objects/appointmentlocationpaginationconnection)

## Example

```
query appointmentLocations(
  $appointment_date: String
  $appointment_type_id: ID
  $ids: [Int]
  $keywords: String
  $location_ids: [ID]
  $org_level: Boolean
  $provider_id: ID
  $provider_ids: [ID]
  $resource: String
  $with_availability: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  appointmentLocations(
    appointment_date: $appointment_date
    appointment_type_id: $appointment_type_id
    ids: $ids
    keywords: $keywords
    location_ids: $location_ids
    org_level: $org_level
    provider_id: $provider_id
    provider_ids: $provider_ids
    resource: $resource
    with_availability: $with_availability
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
