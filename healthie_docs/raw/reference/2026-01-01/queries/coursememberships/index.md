---
title: courseMemberships | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/coursememberships/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/coursememberships/index.md
---

Fetch paginated course membership collection

## Arguments

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`fetch_all` ](#argument-fetch-all)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CourseMembershipPaginationConnection`](/reference/2026-01-01/objects/coursemembershippaginationconnection)

## Example

```
query courseMemberships(
  $client_id: ID
  $fetch_all: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  courseMemberships(
    client_id: $client_id
    fetch_all: $fetch_all
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
