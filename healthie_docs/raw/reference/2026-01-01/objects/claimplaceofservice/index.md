---
title: ClaimPlaceOfService | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimplaceofservice/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimplaceofservice/index.md
---

Frozen place of service data from a submitted claim snapshot

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· Place of service code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Place of service ID

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Place of service name

## Used By

[`ClaimLocation.place_of_service`](/reference/2026-01-01/objects/claimlocation)

## Definition

```
"""
Frozen place of service data from a submitted claim snapshot
"""
type ClaimPlaceOfService {
  """
  Place of service code
  """
  code: String


  """
  Place of service ID
  """
  id: ID


  """
  Place of service name
  """
  name: String
}
```
