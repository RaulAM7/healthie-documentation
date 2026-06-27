---
title: PreferredMedicalCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/preferredmedicalcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/preferredmedicalcode/index.md
---

Preferred Medical Code

## Fields

[`code_description` ](#field-code-description)· [`String` ](/reference/2026-01-01/scalars/string)· ICD/CPT code description

[`code_identifier` ](#field-code-identifier)· [`String` ](/reference/2026-01-01/scalars/string)· ICD/CPT code

[`code_indentifier` ](#field-code-indentifier)· [`String` ](/reference/2026-01-01/scalars/string)· ICD/CPT code

deprecated

Use \`code\_identifier\` instead

[`cpt_code` ](#field-cpt-code)· [`CptCode` ](/reference/2026-01-01/objects/cptcode)· Connected Cpt Code Object

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· Formatted name: 'F19.20: psychotics unspecified'

[`icd_code` ](#field-icd-code)· [`IcdCode` ](/reference/2026-01-01/objects/icdcode)· Connected ICD Code Object

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the code

## Used By

[`PreferredMedicalCodeEdge.node`](/reference/2026-01-01/objects/preferredmedicalcodeedge)

[`PreferredMedicalCodePaginationConnection.nodes`](/reference/2026-01-01/objects/preferredmedicalcodepaginationconnection)

[`createPreferredMedicalCodePayload.preferred_medical_codes`](/reference/2026-01-01/objects/createpreferredmedicalcodepayload)

[`deletePreferredMedicalCodePayload.preferred_medical_codes`](/reference/2026-01-01/objects/deletepreferredmedicalcodepayload)

## Definition

```
"""
Preferred Medical Code
"""
type PreferredMedicalCode {
  """
  ICD/CPT code description
  """
  code_description: String


  """
  ICD/CPT code
  """
  code_identifier: String


  """
  ICD/CPT code
  """
  code_indentifier: String @deprecated(reason: "Use `code_identifier` instead")


  """
  Connected Cpt Code Object
  """
  cpt_code: CptCode


  """
  Formatted name: 'F19.20: psychotics unspecified'
  """
  display_name: String


  """
  Connected ICD Code Object
  """
  icd_code: IcdCode


  """
  The unique identifier of the code
  """
  id: ID!
}
```
