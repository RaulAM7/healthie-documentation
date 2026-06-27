---
title: notifications | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/notifications/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/notifications/index.md
---

Get notifications for a given user (or for the current user)

## Arguments

[`other_party_id` ](#argument-other-party-id)· [`String`](/reference/2026-01-01/scalars/string)

[`read_status` ](#argument-read-status)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`seen_status` ](#argument-seen-status)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`types` ](#argument-types)· [`[String]`](/reference/2026-01-01/scalars/string)

[`sort_by` ](#argument-sort-by)· [`String` ](/reference/2026-01-01/scalars/string)· Options are created\_at\_asc and created\_at\_desc. Defaults to created\_at\_desc

[`order_by` ](#argument-order-by)· [`NotificationOrderKeys`](/reference/2026-01-01/enums/notificationorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`NotificationPaginationConnection`](/reference/2026-01-01/objects/notificationpaginationconnection)

## Example

```
query notifications(
  $other_party_id: String
  $read_status: Boolean
  $seen_status: Boolean
  $types: [String]
  $sort_by: String
  $order_by: NotificationOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  notifications(
    other_party_id: $other_party_id
    read_status: $read_status
    seen_status: $seen_status
    types: $types
    sort_by: $sort_by
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
