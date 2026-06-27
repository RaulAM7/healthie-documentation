---
title: formHistories | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/formhistories/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/formhistories/index.md
---

Fetch paginated form histories collection

## Arguments

[`patient_id` ](#argument-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The patient ID who owns the form

[`sourceable_id` ](#argument-sourceable-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Source object ID

[`sourceable_type` ](#argument-sourceable-type)· [`FormHistorySourceable` ](/reference/2026-01-01/enums/formhistorysourceable)· Source object type

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`FormHistoryPaginationConnection`](/reference/2026-01-01/objects/formhistorypaginationconnection)

## Example

```
query formHistories(
  $patient_id: ID
  $sourceable_id: ID
  $sourceable_type: FormHistorySourceable
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  formHistories(
    patient_id: $patient_id
    sourceable_id: $sourceable_id
    sourceable_type: $sourceable_type
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
