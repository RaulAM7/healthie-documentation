---
title: VideoUrlDefaultInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/videourldefaultinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/videourldefaultinput/index.md
---

Payload for a new VideoUrlDefault

## Fields

[`default_url` ](#field-default-url)· [`String` ](/reference/2026-01-01/scalars/string)· The default url for the video url default

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the video url default

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user who owns the video url default

[`video_url_options` ](#field-video-url-options)· [`[VideoUrlOptionInput]` ](/reference/2026-01-01/input-objects/videourloptioninput)· The video url options

## Used By

[`createAppointmentSettingInput.video_url_default`](/reference/2026-01-01/input-objects/createappointmentsettinginput)

[`updateAppointmentSettingInput.video_url_default`](/reference/2026-01-01/input-objects/updateappointmentsettinginput)

## Definition

```
"""
Payload for a new VideoUrlDefault
"""
input VideoUrlDefaultInput {
  """
  The default url for the video url default
  """
  default_url: String


  """
  The ID of the video url default
  """
  id: ID


  """
  The ID of the user who owns the video url default
  """
  user_id: ID


  """
  The video url options
  """
  video_url_options: [VideoUrlOptionInput]
}
```
