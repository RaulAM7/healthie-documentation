---
title: ZoomCoHostLink | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/zoomcohostlink/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/zoomcohostlink/index.md
---

A co-host entry for a Zoom group appointment, containing a ZAK token for automatic co-host promotion

## Fields

[`full_name` ](#field-full-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Full name of the co-host

[`user_id` ](#field-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · User ID of the co-host

[`zak_token` ](#field-zak-token)· [`String!` ](/reference/2026-01-01/scalars/string)· required · ZAK token used to build a co-host join URL

## Used By

[`Appointment.zoom_co_host_links`](/reference/2026-01-01/objects/appointment)

## Definition

```
"""
A co-host entry for a Zoom group appointment, containing a ZAK token for automatic co-host promotion
"""
type ZoomCoHostLink {
  """
  Full name of the co-host
  """
  full_name: String!


  """
  User ID of the co-host
  """
  user_id: ID!


  """
  ZAK token used to build a co-host join URL
  """
  zak_token: String!
}
```
