---
title: DietitianInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/dietitianinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/dietitianinput/index.md
---

Payload for a dietitian

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the dietitian

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the dietitian

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID of the dietitian

[`other_id_qualifier` ](#field-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID qualifier of the dietitian

[`qualifications` ](#field-qualifications)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifications of the dietitian

## Used By

[`createCms1500Input.dietitian`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.dietitian`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for a dietitian
"""
input DietitianInput {
  """
  The ID of the dietitian
  """
  id: ID


  """
  The NPI of the dietitian
  """
  npi: String


  """
  The other ID of the dietitian
  """
  other_id: String


  """
  The other ID qualifier of the dietitian
  """
  other_id_qualifier: String


  """
  The qualifications of the dietitian
  """
  qualifications: String
}
```
