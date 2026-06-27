---
title: VideoUrlOption | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/videourloption/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/videourloption/index.md
---

A video URL option

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the option

[`url` ](#field-url)· [`String` ](/reference/2026-01-01/scalars/string)· The default URL to use for the connected provider

[`url_by_item_id` ](#field-url-by-item-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the connected provider

## Used By

[`VideoUrlDefault.video_url_options`](/reference/2026-01-01/objects/videourldefault)

## Definition

```
"""
A video URL option
"""
type VideoUrlOption {
  """
  The unique identifier of the option
  """
  id: ID!


  """
  The default URL to use for the connected provider
  """
  url: String


  """
  The ID of the connected provider
  """
  url_by_item_id: String
}
```
