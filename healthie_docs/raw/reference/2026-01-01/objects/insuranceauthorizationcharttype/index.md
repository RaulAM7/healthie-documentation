---
title: InsuranceAuthorizationChartType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceauthorizationcharttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceauthorizationcharttype/index.md
---

An object containing information about the chart for an insurance authorization type

## Fields

[`earliest_date_title` ](#field-earliest-date-title)· [`String` ](/reference/2026-01-01/scalars/string)· The title of the earliest date value of the chart

[`earliest_date_value` ](#field-earliest-date-value)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The value of the earliest date value of the chart

[`latest_date_title` ](#field-latest-date-title)· [`String` ](/reference/2026-01-01/scalars/string)· The title of the latest date value of the chart

[`latest_date_value` ](#field-latest-date-value)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The value of the latest date value of the chart

[`left_section_width` ](#field-left-section-width)· [`String` ](/reference/2026-01-01/scalars/string)· The percentage width of the left section of the chart

[`middle_date_title` ](#field-middle-date-title)· [`String` ](/reference/2026-01-01/scalars/string)· The title of the middle date value of the chart

[`middle_date_value` ](#field-middle-date-value)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The value of the middle date value of the chart

[`right_section_width` ](#field-right-section-width)· [`String` ](/reference/2026-01-01/scalars/string)· The percentage width of the right section of the chart

## Used By

[`InsuranceAuthorizationType.chart_info`](/reference/2026-01-01/objects/insuranceauthorizationtype)

## Definition

```
"""
An object containing information about the chart for an insurance authorization type
"""
type InsuranceAuthorizationChartType {
  """
  The title of the earliest date value of the chart
  """
  earliest_date_title: String


  """
  The value of the earliest date value of the chart
  """
  earliest_date_value: ISO8601Date


  """
  The title of the latest date value of the chart
  """
  latest_date_title: String


  """
  The value of the latest date value of the chart
  """
  latest_date_value: ISO8601Date


  """
  The percentage width of the left section of the chart
  """
  left_section_width: String


  """
  The title of the middle date value of the chart
  """
  middle_date_title: String


  """
  The value of the middle date value of the chart
  """
  middle_date_value: ISO8601Date


  """
  The percentage width of the right section of the chart
  """
  right_section_width: String
}
```
