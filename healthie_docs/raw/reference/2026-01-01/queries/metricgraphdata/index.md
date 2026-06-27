---
title: metricGraphData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/metricgraphdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/metricgraphdata/index.md
---

Fetch data for the metric graphs for a given user

## Arguments

[`category` ](#argument-category)· [`String`](/reference/2026-01-01/scalars/string)

[`end_date` ](#argument-end-date)· [`ISO8601Date`](/reference/2026-01-01/scalars/iso8601date)

[`entry_type` ](#argument-entry-type)· [`String`](/reference/2026-01-01/scalars/string)

[`has_third_party_source` ](#argument-has-third-party-source)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, returns no third-party data. When true, returns only third-party data. If not passed in, will return all data

[`multiplier` ](#argument-multiplier)· [`String`](/reference/2026-01-01/scalars/string)

[`start_date` ](#argument-start-date)· [`ISO8601Date`](/reference/2026-01-01/scalars/iso8601date)

[`user_id` ](#argument-user-id)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`MetricGraphDataType`](/reference/2026-01-01/objects/metricgraphdatatype)

## Example

```
query metricGraphData(
  $category: String
  $end_date: ISO8601Date
  $entry_type: String
  $has_third_party_source: Boolean
  $multiplier: String
  $start_date: ISO8601Date
  $user_id: String
) {
  metricGraphData(
    category: $category
    end_date: $end_date
    entry_type: $entry_type
    has_third_party_source: $has_third_party_source
    multiplier: $multiplier
    start_date: $start_date
    user_id: $user_id
  ) {
    category
    category_label
    data_points
    has_entry
    max
    min
    xtick_type
    ytick_type
  }
}
```
