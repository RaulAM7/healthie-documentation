---
title: MultiLineMetricGraphDataType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/multilinemetricgraphdatatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/multilinemetricgraphdatatype/index.md
---

Multi line metric graph data type

## Fields

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· Category name

[`category_label` ](#field-category-label)· [`String` ](/reference/2026-01-01/scalars/string)· Category label

[`has_entry` ](#field-has-entry)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· False if the category has no entry

[`metric_graph_datas` ](#field-metric-graph-datas)· [`[MetricGraphDataType!]` ](/reference/2026-01-01/objects/metricgraphdatatype)· Metric graph data

## Used By

[`Query.multiLineMetricGraphData`](/reference/2026-01-01/queries/multilinemetricgraphdata)

## Definition

```
"""
Multi line metric graph data type
"""
type MultiLineMetricGraphDataType {
  """
  Category name
  """
  category: String


  """
  Category label
  """
  category_label: String


  """
  False if the category has no entry
  """
  has_entry: Boolean


  """
  Metric graph data
  """
  metric_graph_datas: [MetricGraphDataType!]
}
```
