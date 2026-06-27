---
title: appliedTags | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appliedtags/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appliedtags/index.md
---

Fetch paginated applied tags collection

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`tag_id` ](#argument-tag-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The tag ID

[`order_by` ](#argument-order-by)· [`AppliedTagOrderKeys`](/reference/2026-01-01/enums/appliedtagorderkeys)

[`updated_after` ](#argument-updated-after)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When passed in, only applied tags updated after the specified datetime are returned.

[`updated_before` ](#argument-updated-before)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When passed in, only applied tags updated before the specified datetime are returned.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`AppliedTagPaginationConnection`](/reference/2026-01-01/objects/appliedtagpaginationconnection)

## Example

```
query appliedTags(
  $id: ID
  $tag_id: ID
  $order_by: AppliedTagOrderKeys
  $updated_after: ISO8601DateTime
  $updated_before: ISO8601DateTime
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  appliedTags(
    id: $id
    tag_id: $tag_id
    order_by: $order_by
    updated_after: $updated_after
    updated_before: $updated_before
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
