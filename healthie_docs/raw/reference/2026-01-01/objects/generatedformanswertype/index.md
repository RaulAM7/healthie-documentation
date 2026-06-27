---
title: GeneratedFormAnswerType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/generatedformanswertype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/generatedformanswertype/index.md
---

AI-Generated Form Answer

## Fields

[`answer` ](#field-answer)· [`String` ](/reference/2026-01-01/scalars/string)· The answer to the custom module

[`custom_module` ](#field-custom-module)· [`CustomModule` ](/reference/2026-01-01/objects/custommodule)· The custom module associated with the generated answer

[`displayed_answer` ](#field-displayed-answer)· [`String` ](/reference/2026-01-01/scalars/string)· The user-friendly displayable answer to the custom module

[`id` ](#field-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Used By

[`GeneratedFormAnswerGroupType.generated_form_answers`](/reference/2026-01-01/objects/generatedformanswergrouptype)

## Definition

```
"""
AI-Generated Form Answer
"""
type GeneratedFormAnswerType {
  """
  The answer to the custom module
  """
  answer: String


  """
  The custom module associated with the generated answer
  """
  custom_module: CustomModule


  """
  The user-friendly displayable answer to the custom module
  """
  displayed_answer: String
  id: ID
}
```
