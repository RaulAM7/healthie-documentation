---
title: visualizeDashboard | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/visualizedashboard/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/visualizedashboard/index.md
---

Fetch static Visualize dashboard by type

## Arguments

[`dashboard_type` ](#argument-dashboard-type)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The type of dashboard to display

## Returns

[`VisualizeDashboardType`](/reference/2026-01-01/objects/visualizedashboardtype)

## Example

```
query visualizeDashboard($dashboard_type: String!) {
  visualizeDashboard(dashboard_type: $dashboard_type) {
    url
  }
}
```
