---
title: insurancePlans | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/insuranceplans/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/insuranceplans/index.md
---

Get all potential insurance plans

## Arguments

[`ids` ](#argument-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· List of plan ids

[`is_accepted` ](#argument-is-accepted)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The accepted status of the insurance plan

[`is_custom` ](#argument-is-custom)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Get custom insurance plans

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Search keywords

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`InsurancePlanOrderKeys`](/reference/2026-01-01/enums/insuranceplanorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`InsurancePlanPaginationConnection`](/reference/2026-01-01/objects/insuranceplanpaginationconnection)

## Example

```
query insurancePlans(
  $ids: [ID]
  $is_accepted: Boolean
  $is_custom: Boolean
  $keywords: String
  $sort_by: String
  $order_by: InsurancePlanOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  insurancePlans(
    ids: $ids
    is_accepted: $is_accepted
    is_custom: $is_custom
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
