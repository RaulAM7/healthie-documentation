---
title: labOptions | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/laboptions/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/laboptions/index.md
---

Fetch paginated lab options collection

## Arguments

[`search_by_organization` ](#argument-search-by-organization)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Optional. If true, search for your organization's options only.

[`search_string` ](#argument-search-string)· [`String` ](/reference/2026-01-01/scalars/string)· Optional. Search options by name.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`LabOptionPaginationConnection`](/reference/2026-01-01/objects/laboptionpaginationconnection)

## Example

```
query labOptions(
  $search_by_organization: Boolean
  $search_string: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  labOptions(
    search_by_organization: $search_by_organization
    search_string: $search_string
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
