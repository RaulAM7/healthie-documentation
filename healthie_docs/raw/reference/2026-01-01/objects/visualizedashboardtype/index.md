---
title: VisualizeDashboardType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/visualizedashboardtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/visualizedashboardtype/index.md
---

represents an embeddable static Visualize dashboard

## Fields

[`url` ](#field-url)· [`String` ](/reference/2026-01-01/scalars/string)· The IFrame URL for the embeddable static dashboard

## Used By

[`Query.visualizeDashboard`](/reference/2026-01-01/queries/visualizedashboard)

## Definition

```
"""
represents an embeddable static Visualize dashboard
"""
type VisualizeDashboardType {
  """
  The IFrame URL for the embeddable static dashboard
  """
  url: String
}
```
