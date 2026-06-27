---
title: offerings | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/offerings/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/offerings/index.md
---

Fetch paginated offerings collection (considered public)

## Arguments

[`client_visibility` ](#argument-client-visibility)· [`String`](/reference/2026-01-01/scalars/string)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`offering_id` ](#argument-offering-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`offering_ids` ](#argument-offering-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`offering_user_group_id` ](#argument-offering-user-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`only_client_visible` ](#argument-only-client-visible)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`show_only_visible` ](#argument-show-only-visible)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`order_by` ](#argument-order-by)· [`OfferingOrderKeys`](/reference/2026-01-01/enums/offeringorderkeys)

[`status` ](#argument-status)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`OfferingPaginationConnection`](/reference/2026-01-01/objects/offeringpaginationconnection)

## Example

```
query offerings(
  $client_visibility: String
  $keywords: String
  $offering_id: ID
  $offering_ids: [ID]
  $offering_user_group_id: ID
  $only_client_visible: Boolean
  $provider_id: ID
  $show_only_visible: Boolean
  $order_by: OfferingOrderKeys
  $status: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  offerings(
    client_visibility: $client_visibility
    keywords: $keywords
    offering_id: $offering_id
    offering_ids: $offering_ids
    offering_user_group_id: $offering_user_group_id
    only_client_visible: $only_client_visible
    provider_id: $provider_id
    show_only_visible: $show_only_visible
    order_by: $order_by
    status: $status
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
