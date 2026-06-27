---
title: LabOptionMarker | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/laboptionmarker/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/laboptionmarker/index.md
---

Lab Option Marker

## Fields

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· A more detailed description of the marker

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the marker

## Used By

[`LabOption.markers`](/reference/2026-01-01/objects/laboption)

## Definition

```
"""
Lab Option Marker
"""
type LabOptionMarker {
  """
  A more detailed description of the marker
  """
  description: String


  """
  The name of the marker
  """
  name: String!
}
```
