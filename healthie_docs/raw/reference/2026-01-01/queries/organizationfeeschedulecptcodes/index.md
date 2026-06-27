---
title: organizationFeeScheduleCptCodes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationfeeschedulecptcodes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationfeeschedulecptcodes/index.md
---

Provides CPT codes for an organization as configured in their fee schedule

## Arguments

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Search for CPT codes by code or description

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`OrganizationFeeScheduleCptCodeTypeConnection`](/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeconnection)

## Example

```
query organizationFeeScheduleCptCodes(
  $keywords: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  organizationFeeScheduleCptCodes(
    keywords: $keywords
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
