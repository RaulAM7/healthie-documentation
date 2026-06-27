---
title: LocationResourceType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/locationresourcetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/locationresourcetype/index.md
---

Location resource

## Fields

[`resourceId` ](#field-resourceid)· [`String` ](/reference/2026-01-01/scalars/string)· The resource ID

[`resourceTitle` ](#field-resourcetitle)· [`String` ](/reference/2026-01-01/scalars/string)· The resource title

## Used By

[`Query.locationResources`](/reference/2026-01-01/queries/locationresources)

## Definition

```
"""
Location resource
"""
type LocationResourceType {
  """
  The resource ID
  """
  resourceId: String


  """
  The resource title
  """
  resourceTitle: String
}
```
