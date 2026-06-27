---
title: ProviderBioInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/providerbioinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/providerbioinput/index.md
---

Payload for a provider bio

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the provider bio (only required for updates, omit when creating)

[`bio` ](#field-bio)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The biography text for the provider

## Used By

[`updateOrganizationMemberInput.provider_bio`](/reference/2026-01-01/input-objects/updateorganizationmemberinput)

## Definition

```
"""
Payload for a provider bio
"""
input ProviderBioInput {
  """
  The ID of the provider bio (only required for updates, omit when creating)
  """
  id: ID


  """
  The biography text for the provider
  """
  bio: String!
}
```
