---
title: VideoChat | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/videochat/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/videochat/index.md
---

Video chat info for subscriptions

## Fields

[`contact_type` ](#field-contact-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of contact for the video chat

[`date` ](#field-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date of the video chat

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the video chat

[`is_group` ](#field-is-group)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the video chat is a group chat

[`provider_name` ](#field-provider-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the video chat provider

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The user who created the video chat

## Used By

[`VideoChatsSubscriptionPayload.current_video_chat`](/reference/2026-01-01/objects/videochatssubscriptionpayload)

[`VideoChatsSubscriptionPayload.ended_video_chat`](/reference/2026-01-01/objects/videochatssubscriptionpayload)

[`VideoChatsSubscriptionPayload.upcoming_video_chat`](/reference/2026-01-01/objects/videochatssubscriptionpayload)

## Definition

```
"""
Video chat info for subscriptions
"""
type VideoChat {
  """
  The type of contact for the video chat
  """
  contact_type: String


  """
  The date of the video chat
  """
  date: ISO8601DateTime


  """
  The ID of the video chat
  """
  id: ID!


  """
  Whether the video chat is a group chat
  """
  is_group: Boolean


  """
  The name of the video chat provider
  """
  provider_name: String


  """
  The user who created the video chat
  """
  user: User
}
```
