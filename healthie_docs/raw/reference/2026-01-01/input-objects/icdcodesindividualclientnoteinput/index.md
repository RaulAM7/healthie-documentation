---
title: IcdCodesIndividualClientNoteInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/icdcodesindividualclientnoteinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/icdcodesindividualclientnoteinput/index.md
---

Payload for an ICD Code connection to an individual client note

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the ICD Code connection to the individual client note

[`icd_code_id` ](#field-icd-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the ICD Code

[`position` ](#field-position)· [`Int` ](/reference/2026-01-01/scalars/int)· The position of this diagnosis, in relation to other diagnoses for this appointment inclusion.

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the ICD Code connection to the individual client note will be deleted

## Used By

[`IndividualClientNoteInput.icd_codes_individual_client_notes_attributes`](/reference/2026-01-01/input-objects/individualclientnoteinput)

## Definition

```
"""
Payload for an ICD Code connection to an individual client note
"""
input IcdCodesIndividualClientNoteInput {
  """
  The ID of the ICD Code connection to the individual client note
  """
  id: ID


  """
  The ID of the ICD Code
  """
  icd_code_id: ID


  """
  The position of this diagnosis, in relation to other diagnoses for this appointment inclusion.
  """
  position: Int


  """
  If true, the ICD Code connection to the individual client note will be deleted
  """
  _destroy: Boolean
}
```
