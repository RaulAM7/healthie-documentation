---
title: preferred_medical_codes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/preferred-medical-codes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/preferred-medical-codes/index.md
---

Fetch paginated preferred medical codes collection

## Arguments

[`code_type` ](#argument-code-type)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`PreferredMedicalCodePaginationConnection`](/reference/2026-01-01/objects/preferredmedicalcodepaginationconnection)

## Example

```
query preferred_medical_codes(
  $code_type: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  preferred_medical_codes(
    code_type: $code_type
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
