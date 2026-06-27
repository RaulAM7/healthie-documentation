---
title: updateFormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateformanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateformanswergroup/index.md
---

update FormAnswerGroup

## Arguments

[`input` ](#argument-input)· [`updateFormAnswerGroupInput` ](/reference/2026-01-01/input-objects/updateformanswergroupinput)· Parameters for updateFormAnswerGroup

## Returns

[`updateFormAnswerGroupPayload`](/reference/2026-01-01/objects/updateformanswergrouppayload)

## Example

```
mutation updateFormAnswerGroup($input: updateFormAnswerGroupInput) {
  updateFormAnswerGroup(input: $input) {
    form_answer_group
    messages
  }
}
```
