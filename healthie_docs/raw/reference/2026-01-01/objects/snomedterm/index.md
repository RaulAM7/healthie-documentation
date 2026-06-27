---
title: SnomedTerm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/snomedterm/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/snomedterm/index.md
---

Snomed terms

## Fields

[`concept_id` ](#field-concept-id)· [`String` ](/reference/2026-01-01/scalars/string)· id for snomed term

[`term` ](#field-term)· [`String` ](/reference/2026-01-01/scalars/string)· snomed term name

## Used By

[`FamilyHistoryCondition.snomed_term`](/reference/2026-01-01/objects/familyhistorycondition)

## Definition

```
"""
Snomed terms
"""
type SnomedTerm {
  """
  id for snomed term
  """
  concept_id: String


  """
  snomed term name
  """
  term: String
}
```
