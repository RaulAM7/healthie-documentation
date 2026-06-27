---
title: episodesOfCare | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/episodesofcare/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/episodesofcare/index.md
---

Fetch paginated episodes of care collection

## Arguments

[`ids` ](#argument-ids)· [`[ID!]`](/reference/2026-01-01/scalars/id)

[`patient_id` ](#argument-patient-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`EpisodeOfCareConnection`](/reference/2026-01-01/objects/episodeofcareconnection)

## Example

```
query episodesOfCare(
  $ids: [ID!]
  $patient_id: ID
  $provider_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  episodesOfCare(
    ids: $ids
    patient_id: $patient_id
    provider_id: $provider_id
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
