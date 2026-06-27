---
title: documentViewings | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/documentviewings/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/documentviewings/index.md
---

Get Document Viewings for a specific document. A 'View' is when a document is downloaded or opened in a new tab

## Arguments

[`document_id` ](#argument-document-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`DocumentViewingPaginationConnection`](/reference/2026-01-01/objects/documentviewingpaginationconnection)

## Example

```
query documentViewings(
  $document_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  documentViewings(
    document_id: $document_id
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
