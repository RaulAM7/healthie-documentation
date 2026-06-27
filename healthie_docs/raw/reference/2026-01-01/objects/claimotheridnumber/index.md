---
title: ClaimOtherIdNumber | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimotheridnumber/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimotheridnumber/index.md
---

Frozen other ID number data from a submitted claim snapshot

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Other ID number ID

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· Display label for the other ID

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· Other ID

[`other_id_qualifier` ](#field-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Other ID qualifier

## Used By

[`ClaimProvider.rendering_provider_other_id_number`](/reference/2026-01-01/objects/claimprovider)

## Definition

```
"""
Frozen other ID number data from a submitted claim snapshot
"""
type ClaimOtherIdNumber {
  """
  Other ID number ID
  """
  id: ID


  """
  Display label for the other ID
  """
  label: String


  """
  Other ID
  """
  other_id: String


  """
  Other ID qualifier
  """
  other_id_qualifier: String
}
```
