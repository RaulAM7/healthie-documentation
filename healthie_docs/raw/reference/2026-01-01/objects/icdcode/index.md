---
title: IcdCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcode/index.md
---

icd code

## Fields

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of the ICD code

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The ICD code

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the ICD code was created

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the ICD code

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· A display name - for use in labels

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the ICD code

[`is_favorite` ](#field-is-favorite)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the ICD code is marked as favorite

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the ICD code was updated

## Used By

[`Diagnosis.icd_code`](/reference/2026-01-01/objects/diagnosis)

[`IcdCodeEdge.node`](/reference/2026-01-01/objects/icdcodeedge)

[`IcdCodePaginationConnection.nodes`](/reference/2026-01-01/objects/icdcodepaginationconnection)

[`IcdCodesCms1500.icd_code`](/reference/2026-01-01/objects/icdcodescms1500)

[`IcdCodesIndividualClientNote.icd_code`](/reference/2026-01-01/objects/icdcodesindividualclientnote)

[`IcdCodesPolicy.icd_code`](/reference/2026-01-01/objects/icdcodespolicy)

[`IcdCodesSuperBill.icd_code`](/reference/2026-01-01/objects/icdcodessuperbill)

[`PreferredMedicalCode.icd_code`](/reference/2026-01-01/objects/preferredmedicalcode)

[`Query.billableIcdCodes`](/reference/2026-01-01/queries/billableicdcodes)

[`Query.icdCode`](/reference/2026-01-01/queries/icdcode)

## Definition

```
"""
icd code
"""
type IcdCode {
  """
  The category of the ICD code
  """
  category: String


  """
  The ICD code
  """
  code: String


  """
  The date the ICD code was created
  """
  created_at: ISO8601DateTime!


  """
  The description of the ICD code
  """
  description: String


  """
  A display name - for use in labels
  """
  display_name: String


  """
  The unique identifier of the ICD code
  """
  id: ID!


  """
  Whether the ICD code is marked as favorite
  """
  is_favorite(
    """
    The known value of is_favorite (from the query argument)
    """
    known_value: Boolean
  ): Boolean


  """
  The date the ICD code was updated
  """
  updated_at: ISO8601DateTime!
}
```
