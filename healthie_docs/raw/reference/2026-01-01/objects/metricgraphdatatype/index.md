---
title: MetricGraphDataType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/metricgraphdatatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/metricgraphdatatype/index.md
---

Metric Graph data

## Fields

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· Category of the metric, e.g. "Weight" or "Steps"

[`category_label` ](#field-category-label)· [`String` ](/reference/2026-01-01/scalars/string)· Label for the category, e.g. "Weight" or "Steps"

[`data_points` ](#field-data-points)· [`[MetricDataPointType!]` ](/reference/2026-01-01/objects/metricdatapointtype)· Data points for the graph

[`has_entry` ](#field-has-entry)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· False if the category has no entry

[`max` ](#field-max)· [`Float` ](/reference/2026-01-01/scalars/float)· Maximum value of the data points

[`min` ](#field-min)· [`Float` ](/reference/2026-01-01/scalars/float)· Minimum value of the data points

[`xtick_type` ](#field-xtick-type)· [`String` ](/reference/2026-01-01/scalars/string)· Type of xtick, e.g. "date" or "time"

[`ytick_type` ](#field-ytick-type)· [`String` ](/reference/2026-01-01/scalars/string)· Type of ytick, e.g. "date" or "time"

## Used By

[`MultiLineMetricGraphDataType.metric_graph_datas`](/reference/2026-01-01/objects/multilinemetricgraphdatatype)

[`Query.metricGraphData`](/reference/2026-01-01/queries/metricgraphdata)

[`Query.metricGraphsData`](/reference/2026-01-01/queries/metricgraphsdata)

## Definition

```
"""
Metric Graph data
"""
type MetricGraphDataType {
  """
  Category of the metric, e.g. "Weight" or "Steps"
  """
  category: String


  """
  Label for the category, e.g. "Weight" or "Steps"
  """
  category_label: String


  """
  Data points for the graph
  """
  data_points: [MetricDataPointType!]


  """
  False if the category has no entry
  """
  has_entry: Boolean


  """
  Maximum value of the data points
  """
  max: Float


  """
  Minimum value of the data points
  """
  min: Float


  """
  Type of xtick, e.g. "date" or "time"
  """
  xtick_type: String


  """
  Type of ytick, e.g. "date" or "time"
  """
  ytick_type: String
}
```
