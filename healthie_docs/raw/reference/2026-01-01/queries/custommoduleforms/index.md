---
title: customModuleForms | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/custommoduleforms/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/custommoduleforms/index.md
---

All form templates for the current user

## Arguments

[`active_status` ](#argument-active-status)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`category` ](#argument-category)· [`String`](/reference/2026-01-01/scalars/string)

[`include_default_templates` ](#argument-include-default-templates)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Default templates are global form templates that are available to any organization (specifically Free Text and ADIME form templates)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`CustomModuleFormOrderKeys`](/reference/2026-01-01/enums/custommoduleformorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CustomModuleFormPaginationConnection`](/reference/2026-01-01/objects/custommoduleformpaginationconnection)

## Example

```
query customModuleForms(
  $active_status: Boolean
  $category: String
  $include_default_templates: Boolean
  $keywords: String
  $sort_by: String
  $order_by: CustomModuleFormOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  customModuleForms(
    active_status: $active_status
    category: $category
    include_default_templates: $include_default_templates
    keywords: $keywords
    sort_by: $sort_by
    order_by: $order_by
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
