---
title: cms1500s | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/cms1500s/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/cms1500s/index.md
---

Fetch paginated Cms1500s collection

## Arguments

[`appointment_id` ](#argument-appointment-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter by the associated appointment ID

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`Cms1500OrderKeys`](/reference/2026-01-01/enums/cms1500orderkeys)

[`status` ](#argument-status)· [`Cms1500Status`](/reference/2026-01-01/enums/cms1500status)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`Cms1500PaginationConnection`](/reference/2026-01-01/objects/cms1500paginationconnection)

## Example

```
query cms1500s(
  $appointment_id: ID
  $client_id: ID
  $keywords: String
  $provider_id: ID
  $sort_by: String
  $order_by: Cms1500OrderKeys
  $status: Cms1500Status
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  cms1500s(
    appointment_id: $appointment_id
    client_id: $client_id
    keywords: $keywords
    provider_id: $provider_id
    sort_by: $sort_by
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
