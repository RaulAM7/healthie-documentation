---
title: MetricDataPointType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/metricdatapointtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/metricdatapointtype/index.md
---

A data point for a metric

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the data point was created

[`entry_id` ](#field-entry-id)· [`String` ](/reference/2026-01-01/scalars/string)· The entry id of the data point

[`flex_value` ](#field-flex-value)· [`String` ](/reference/2026-01-01/scalars/string)· The value of the data point

[`value` ](#field-value)· [`Float` ](/reference/2026-01-01/scalars/float)· The value of the data point

deprecated

Use flex value, which supports both string and number values

## Used By

[`MetricGraphDataType.data_points`](/reference/2026-01-01/objects/metricgraphdatatype)

## Definition

```
"""
A data point for a metric
"""
type MetricDataPointType {
  """
  The time the data point was created
  """
  created_at: ISO8601DateTime!


  """
  The entry id of the data point
  """
  entry_id: String


  """
  The value of the data point
  """
  flex_value: String


  """
  The value of the data point
  """
  value: Float
    @deprecated(
      reason: "Use flex value, which supports both string and number values"
    )
}
```
