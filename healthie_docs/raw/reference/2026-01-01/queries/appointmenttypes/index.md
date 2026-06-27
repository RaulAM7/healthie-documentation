---
title: appointmentTypes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmenttypes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmenttypes/index.md
---

Fetch paginated Appointment Type collection (considered public)

## Arguments

[`appointment_type_ids` ](#argument-appointment-type-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Array of ids to include

[`clients_can_book` ](#argument-clients-can-book)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`embed_or_sharing_link` ](#argument-embed-or-sharing-link)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`offering_id` ](#argument-offering-id)· [`String`](/reference/2026-01-01/scalars/string)

[`org_level` ](#argument-org-level)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`provider_id` ](#argument-provider-id)· [`String`](/reference/2026-01-01/scalars/string)

[`provider_ids` ](#argument-provider-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· Bookable provider ids; with clients\_can\_book, limits provider-specific types to these providers (org-level / no preference).

[`show_group` ](#argument-show-group)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only group appointment types; when false, only non-group types. When omitted, returns both.

[`with_deleted_appt_types` ](#argument-with-deleted-appt-types)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`order_by` ](#argument-order-by)· [`AppointmentTypeOrderKeys`](/reference/2026-01-01/enums/appointmenttypeorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`AppointmentTypePaginationConnection`](/reference/2026-01-01/objects/appointmenttypepaginationconnection)

## Example

```
query appointmentTypes(
  $appointment_type_ids: [ID]
  $clients_can_book: Boolean
  $embed_or_sharing_link: Boolean
  $keywords: String
  $offering_id: String
  $org_level: Boolean
  $provider_id: String
  $provider_ids: [ID]
  $show_group: Boolean
  $with_deleted_appt_types: Boolean
  $order_by: AppointmentTypeOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  appointmentTypes(
    appointment_type_ids: $appointment_type_ids
    clients_can_book: $clients_can_book
    embed_or_sharing_link: $embed_or_sharing_link
    keywords: $keywords
    offering_id: $offering_id
    org_level: $org_level
    provider_id: $provider_id
    provider_ids: $provider_ids
    show_group: $show_group
    with_deleted_appt_types: $with_deleted_appt_types
    order_by: $order_by
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
