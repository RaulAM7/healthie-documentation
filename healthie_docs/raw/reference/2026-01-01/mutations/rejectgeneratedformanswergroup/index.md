---
title: rejectGeneratedFormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/rejectgeneratedformanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/rejectgeneratedformanswergroup/index.md
---

Rejects an AI-generated form answer group

## Arguments

[`input` ](#argument-input)· [`rejectGeneratedFormAnswerGroupInput` ](/reference/2026-01-01/input-objects/rejectgeneratedformanswergroupinput)· Parameters for rejectGeneratedFormAnswerGroup

## Returns

[`rejectGeneratedFormAnswerGroupPayload`](/reference/2026-01-01/objects/rejectgeneratedformanswergrouppayload)

## Example

```
mutation rejectGeneratedFormAnswerGroup(
  $input: rejectGeneratedFormAnswerGroupInput
) {
  rejectGeneratedFormAnswerGroup(input: $input) {
    generated_form_answer_group
    messages
  }
}
```
