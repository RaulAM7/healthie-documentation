---
title: ClaimIcdCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimicdcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimicdcode/index.md
---

Frozen ICD code data from a submitted claim snapshot

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· ICD code

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· ICD code description

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· ICD display name

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ICD code ID

## Used By

[`ClaimDiagnosis.icd_code`](/reference/2026-01-01/objects/claimdiagnosis)

## Definition

```
"""
Frozen ICD code data from a submitted claim snapshot
"""
type ClaimIcdCode {
  """
  ICD code
  """
  code: String


  """
  ICD code description
  """
  description: String


  """
  ICD display name
  """
  display_name: String


  """
  ICD code ID
  """
  id: ID
}
```
