---
title: customModuleFormsCount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/custommoduleformscount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/custommoduleformscount/index.md
---

Fetch paginated count for provider custom module forms

## Arguments

[`active_status` ](#argument-active-status)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`category` ](#argument-category)· [`String`](/reference/2026-01-01/scalars/string)

[`include_default_templates` ](#argument-include-default-templates)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Default templates are global form templates that are available to any organization (specifically Free Text and ADIME form templates)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`Int`](/reference/2026-01-01/scalars/int)

## Example

```
query customModuleFormsCount(
  $active_status: Boolean
  $category: String
  $include_default_templates: Boolean
  $keywords: String
  $sort_by: String
) {
  customModuleFormsCount(
    active_status: $active_status
    category: $category
    include_default_templates: $include_default_templates
    keywords: $keywords
    sort_by: $sort_by
  )
}
```
