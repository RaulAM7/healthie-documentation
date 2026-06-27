---
title: convertGeneratedFormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/convertgeneratedformanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/convertgeneratedformanswergroup/index.md
---

Converts a generated form answer group to a form answer group

## Arguments

[`input` ](#argument-input)· [`convertGeneratedFormAnswerGroupInput` ](/reference/2026-01-01/input-objects/convertgeneratedformanswergroupinput)· Parameters for convertGeneratedFormAnswerGroup

## Returns

[`convertGeneratedFormAnswerGroupPayload`](/reference/2026-01-01/objects/convertgeneratedformanswergrouppayload)

## Example

```
mutation convertGeneratedFormAnswerGroup(
  $input: convertGeneratedFormAnswerGroupInput
) {
  convertGeneratedFormAnswerGroup(input: $input) {
    form_answer_group
    generated_form_answer_group
    messages
  }
}
```
