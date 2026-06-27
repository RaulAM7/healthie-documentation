---
title: SubentryInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/subentryinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/subentryinput/index.md
---

Payload for a sub-entry

## Fields

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of the sub-entry

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the sub-entry

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the sub-entry

[`metric_stat` ](#field-metric-stat)· [`String` ](/reference/2026-01-01/scalars/string)· The statistic of the sub-entry

[`type` ](#field-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the sub-entry

## Used By

[`BulkEntryInput.subentries`](/reference/2026-01-01/input-objects/bulkentryinput)

[`createEntryInput.subentries`](/reference/2026-01-01/input-objects/createentryinput)

[`updateEntryInput.subentries`](/reference/2026-01-01/input-objects/updateentryinput)

## Definition

```
"""
Payload for a sub-entry
"""
input SubentryInput {
  """
  The category of the sub-entry
  """
  category: String


  """
  The description of the sub-entry
  """
  description: String


  """
  The ID of the sub-entry
  """
  id: ID


  """
  The statistic of the sub-entry
  """
  metric_stat: String


  """
  The type of the sub-entry
  """
  type: String
}
```
