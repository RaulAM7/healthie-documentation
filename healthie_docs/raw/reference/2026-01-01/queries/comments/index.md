---
title: comments | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/comments/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/comments/index.md
---

Fetch comments collection

## Arguments

[`entry_id` ](#argument-entry-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`entry_ids` ](#argument-entry-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· An array of entry IDs to grab comments for. Overrides entry\_id if passed in

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CommentPaginationConnection`](/reference/2026-01-01/objects/commentpaginationconnection)

## Example

```
query comments(
  $entry_id: ID
  $entry_ids: [ID]
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  comments(
    entry_id: $entry_id
    entry_ids: $entry_ids
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
