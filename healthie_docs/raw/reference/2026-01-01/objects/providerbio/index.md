---
title: ProviderBio | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/providerbio/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/providerbio/index.md
---

A provider bio object

## Fields

[`bio` ](#field-bio)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The biography of the provider

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the provider bio

## Used By

[`User.provider_bio`](/reference/2026-01-01/objects/user)

## Definition

```
"""
A provider bio object
"""
type ProviderBio {
  """
  The biography of the provider
  """
  bio: String!


  """
  The unique identifier of the provider bio
  """
  id: ID!
}
```
