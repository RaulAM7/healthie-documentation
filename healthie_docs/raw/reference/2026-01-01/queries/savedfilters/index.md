---
title: savedFilters | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/savedfilters/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/savedfilters/index.md
---

Fetch paginated saved filters collection

## Arguments

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`organization_id` ](#argument-organization-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`SavedFilterPaginationConnection`](/reference/2026-01-01/objects/savedfilterpaginationconnection)

## Example

```
query savedFilters(
  $user_id: ID
  $organization_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  savedFilters(
    user_id: $user_id
    organization_id: $organization_id
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
