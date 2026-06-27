---
title: otherIdNumbers | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/otheridnumbers/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/otheridnumbers/index.md
---

Fetch paginated other ID numbers collection

## Arguments

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`OtherIdNumberPaginationConnection`](/reference/2026-01-01/objects/otheridnumberpaginationconnection)

## Example

```
query otherIdNumbers(
  $user_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  otherIdNumbers(
    user_id: $user_id
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
