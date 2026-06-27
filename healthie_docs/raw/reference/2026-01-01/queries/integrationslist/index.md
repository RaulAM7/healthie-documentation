---
title: integrationsList | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/integrationslist/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/integrationslist/index.md
---

Fetch paginated integrations list collection

## Arguments

[`category` ](#argument-category)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`IntegrationCategoryTypePaginationConnection`](/reference/2026-01-01/objects/integrationcategorytypepaginationconnection)

## Example

```
query integrationsList(
  $category: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  integrationsList(
    category: $category
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
