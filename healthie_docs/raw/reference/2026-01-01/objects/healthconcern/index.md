---
title: HealthConcern | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/healthconcern/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/healthconcern/index.md
---

HealthConcern object

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The code for the health concern

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the health concern

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The display name of the health concern

[`effective_time` ](#field-effective-time)· [`String` ](/reference/2026-01-01/scalars/string)· The effective time of the health concern

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the

## Used By

[`createHealthConcernPayload.health_concern`](/reference/2026-01-01/objects/createhealthconcernpayload)

[`deleteHealthConcernPayload.health_concern`](/reference/2026-01-01/objects/deletehealthconcernpayload)

[`updateHealthConcernPayload.health_concern`](/reference/2026-01-01/objects/updatehealthconcernpayload)

## Definition

```
"""
HealthConcern object
"""
type HealthConcern {
  """
  The code for the health concern
  """
  code: String


  """
  The description of the health concern
  """
  description: String


  """
  The display name of the health concern
  """
  display_name: String


  """
  The effective time of the health concern
  """
  effective_time: String


  """
  The unique identifier of the
  """
  id: ID!
}
```
