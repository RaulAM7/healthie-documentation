---
title: VideoUrlDefault | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/videourldefault/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/videourldefault/index.md
---

A default video URL

## Fields

[`default_url` ](#field-default-url)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The default URL to use for anyone with the connected appointment setting

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the url

[`user_id` ](#field-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the connected user

[`video_url_options` ](#field-video-url-options)· [`[VideoUrlOption!]` ](/reference/2026-01-01/objects/videourloption)· The options for the connected video URL

## Used By

[`AppointmentSetting.video_url_default`](/reference/2026-01-01/objects/appointmentsetting)

## Definition

```
"""
A default video URL
"""
type VideoUrlDefault {
  """
  The default URL to use for anyone with the connected appointment setting
  """
  default_url: String!


  """
  The unique identifier of the url
  """
  id: ID!


  """
  The ID of the connected user
  """
  user_id: ID!


  """
  The options for the connected video URL
  """
  video_url_options: [VideoUrlOption!]
}
```
