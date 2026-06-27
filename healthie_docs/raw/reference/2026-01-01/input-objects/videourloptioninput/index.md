---
title: VideoUrlOptionInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/videourloptioninput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/videourloptioninput/index.md
---

Payload for a video url

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the video url

[`url` ](#field-url)· [`String` ](/reference/2026-01-01/scalars/string)· The url of the video

[`url_by_item_id` ](#field-url-by-item-id)· [`String` ](/reference/2026-01-01/scalars/string)· The url of the video by item id

## Used By

[`VideoUrlDefaultInput.video_url_options`](/reference/2026-01-01/input-objects/videourldefaultinput)

## Definition

```
"""
Payload for a video url
"""
input VideoUrlOptionInput {
  """
  The ID of the video url
  """
  id: ID


  """
  The url of the video
  """
  url: String


  """
  The url of the video by item id
  """
  url_by_item_id: String
}
```
