---
title: organizationMembers | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationmembers/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationmembers/index.md
---

fetch members of organization

## Arguments

[`conversation_id` ](#argument-conversation-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`licensed_in_state` ](#argument-licensed-in-state)· [`String` ](/reference/2026-01-01/scalars/string)· Two letter state abbreviation (e.g. "CA", "NY")

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`UserOrderKeys`](/reference/2026-01-01/enums/userorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`UserConnection`](/reference/2026-01-01/objects/userconnection)

## Example

```
query organizationMembers(
  $conversation_id: ID
  $keywords: String
  $licensed_in_state: String
  $sort_by: String
  $order_by: UserOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  organizationMembers(
    conversation_id: $conversation_id
    keywords: $keywords
    licensed_in_state: $licensed_in_state
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
