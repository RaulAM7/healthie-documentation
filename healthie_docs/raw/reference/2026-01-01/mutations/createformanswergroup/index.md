---
title: createFormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createformanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createformanswergroup/index.md
---

create FormAnswerGroup

## Arguments

[`input` ](#argument-input)· [`createFormAnswerGroupInput` ](/reference/2026-01-01/input-objects/createformanswergroupinput)· Parameters for createFormAnswerGroup

## Returns

[`createFormAnswerGroupPayload`](/reference/2026-01-01/objects/createformanswergrouppayload)

## Example

```
mutation createFormAnswerGroup($input: createFormAnswerGroupInput) {
  createFormAnswerGroup(input: $input) {
    form_answer_group
    messages
  }
}
```
