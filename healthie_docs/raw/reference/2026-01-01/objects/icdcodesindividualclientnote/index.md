---
title: IcdCodesIndividualClientNote | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodesindividualclientnote/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodesindividualclientnote/index.md
---

icd codes individual client note join table

## Fields

[`icd_code` ](#field-icd-code)· [`IcdCode` ](/reference/2026-01-01/objects/icdcode)· icd code

[`icd_code_id` ](#field-icd-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Attached ICD Code ID

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the CMS 1500 ICD code

[`position` ](#field-position)· [`Int` ](/reference/2026-01-01/scalars/int)· Position of the diagnosis

## Used By

[`IndividualClientType.icd_codes_individual_client_notes`](/reference/2026-01-01/objects/individualclienttype)

## Definition

```
"""
icd codes individual client note join table
"""
type IcdCodesIndividualClientNote {
  """
  icd code
  """
  icd_code: IcdCode


  """
  Attached ICD Code ID
  """
  icd_code_id: ID


  """
  The unique identifier of the CMS 1500 ICD code
  """
  id: ID


  """
  Position of the diagnosis
  """
  position: Int
}
```
