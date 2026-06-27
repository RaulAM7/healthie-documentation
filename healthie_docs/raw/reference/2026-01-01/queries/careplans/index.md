---
title: carePlans | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/careplans/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/careplans/index.md
---

Fetch paginated care plan collection

## Arguments

[`patient_id` ](#argument-patient-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`template_search_keywords` ](#argument-template-search-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`templates_only` ](#argument-templates-only)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`order_by` ](#argument-order-by)· [`CarePlanOrderKeys`](/reference/2026-01-01/enums/careplanorderkeys)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CarePlanPaginationConnection`](/reference/2026-01-01/objects/careplanpaginationconnection)

## Example

```
query carePlans(
  $patient_id: ID
  $template_search_keywords: String
  $templates_only: Boolean
  $order_by: CarePlanOrderKeys
  $sort_by: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  carePlans(
    patient_id: $patient_id
    template_search_keywords: $template_search_keywords
    templates_only: $templates_only
    order_by: $order_by
    sort_by: $sort_by
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
