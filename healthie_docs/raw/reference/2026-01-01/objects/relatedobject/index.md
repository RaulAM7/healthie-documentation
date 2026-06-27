---
title: RelatedObject | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/relatedobject/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/relatedobject/index.md
---

A Related Object

## Fields

[`full_name` ](#field-full-name)· [`String` ](/reference/2026-01-01/scalars/string)· A combined string to use for labels

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The Healthie unique identifier

## Used By

[`ClientSource.related_object`](/reference/2026-01-01/objects/clientsource)

## Definition

```
"""
A Related Object
"""
type RelatedObject {
  """
  A combined string to use for labels
  """
  full_name: String


  """
  The Healthie unique identifier
  """
  id: ID!
}
```
