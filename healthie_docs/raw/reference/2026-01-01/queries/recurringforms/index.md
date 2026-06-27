---
title: recurringForms | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/recurringforms/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/recurringforms/index.md
---

Fetch paginated recurring forms collection

## Arguments

[`connectable_id` ](#argument-connectable-id)· [`String`](/reference/2026-01-01/scalars/string)

[`connectable_type` ](#argument-connectable-type)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`RecurringFormPaginationConnection`](/reference/2026-01-01/objects/recurringformpaginationconnection)

## Example

```
query recurringForms(
  $connectable_id: String
  $connectable_type: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  recurringForms(
    connectable_id: $connectable_id
    connectable_type: $connectable_type
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
