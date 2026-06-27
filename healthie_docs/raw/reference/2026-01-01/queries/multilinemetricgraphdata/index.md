---
title: multiLineMetricGraphData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/multilinemetricgraphdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/multilinemetricgraphdata/index.md
---

Graph data with multiple data series for a single specified metric category

## Arguments

[`category` ](#argument-category)· [`String` ](/reference/2026-01-01/scalars/string)· The metric category to fetch multi-line graph data for, e.g. Blood Pressure, Nutrition, or a growth chart. Defaults to empty string which returns no data.

[`end_date` ](#argument-end-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· End of the date range, must be sent in with a start date.

[`entry_type` ](#argument-entry-type)· [`String` ](/reference/2026-01-01/scalars/string)· The entry type to filter by. Defaults to MetricEntry.

[`food_graph_type` ](#argument-food-graph-type)· [`String` ](/reference/2026-01-01/scalars/string)· Type of nutrition graph breakdown: nutrients\_split, nutrients\_split\_full, or a specific nutrient. Defaults to nutrients\_split.

[`start_date` ](#argument-start-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Start of the date range, must be sent in with an end date.

[`sub_category` ](#argument-sub-category)· [`String` ](/reference/2026-01-01/scalars/string)· A sub-category filter within the selected category. When category is Client Sources, specifies which referral channel to break down into individual source lines. Not used by other categories currently. Defaults to empty string which returns no data.

[`user_id` ](#argument-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The user to fetch multi-line metric graph data for. Defaults to the current user.

## Returns

[`MultiLineMetricGraphDataType`](/reference/2026-01-01/objects/multilinemetricgraphdatatype)

## Example

```
query multiLineMetricGraphData(
  $category: String
  $end_date: ISO8601Date
  $entry_type: String
  $food_graph_type: String
  $start_date: ISO8601Date
  $sub_category: String
  $user_id: String
) {
  multiLineMetricGraphData(
    category: $category
    end_date: $end_date
    entry_type: $entry_type
    food_graph_type: $food_graph_type
    start_date: $start_date
    sub_category: $sub_category
    user_id: $user_id
  ) {
    category
    category_label
    has_entry
    metric_graph_datas
  }
}
```
