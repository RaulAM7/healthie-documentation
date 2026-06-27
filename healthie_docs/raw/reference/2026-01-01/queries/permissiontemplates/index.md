---
title: permissionTemplates | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/permissiontemplates/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/permissiontemplates/index.md
---

Get Permission Templates

## Arguments

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`PermissionTemplateTypePaginationConnection`](/reference/2026-01-01/objects/permissiontemplatetypepaginationconnection)

## Example

```
query permissionTemplates(
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  permissionTemplates(
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
