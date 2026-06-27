---
title: EmbedWidgetStepType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/embedwidgetsteptype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/embedwidgetsteptype/index.md
---

A step that embeds a widget

## Fields

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the step

[`title` ](#field-title)· [`String` ](/reference/2026-01-01/scalars/string)· The title of the step

## Used By

[`Query.embedWidgetSteps`](/reference/2026-01-01/queries/embedwidgetsteps)

## Definition

```
"""
A step that embeds a widget
"""
type EmbedWidgetStepType {
  """
  The unique identifier of the step
  """
  id: String!


  """
  The title of the step
  """
  title: String
}
```
