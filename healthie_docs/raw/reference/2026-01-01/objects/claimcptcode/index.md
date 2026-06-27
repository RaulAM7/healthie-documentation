---
title: ClaimCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimcptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimcptcode/index.md
---

Frozen CPT code data from a submitted claim snapshot

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· CPT code

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· CPT code description

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· CPT display name

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· CPT code ID

## Used By

[`ClaimServiceLine.cpt_code`](/reference/2026-01-01/objects/claimserviceline)

## Definition

```
"""
Frozen CPT code data from a submitted claim snapshot
"""
type ClaimCptCode {
  """
  CPT code
  """
  code: String


  """
  CPT code description
  """
  description: String


  """
  CPT display name
  """
  display_name: String


  """
  CPT code ID
  """
  id: ID
}
```
