---
title: deleteFormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteformanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteformanswergroup/index.md
---

Destroy a Form Answer Group

## Arguments

[`input` ](#argument-input)· [`deleteFormAnswerGroupInput` ](/reference/2026-01-01/input-objects/deleteformanswergroupinput)· Parameters for deleteFormAnswerGroup

## Returns

[`deleteFormAnswerGroupPayload`](/reference/2026-01-01/objects/deleteformanswergrouppayload)

## Example

```
mutation deleteFormAnswerGroup($input: deleteFormAnswerGroupInput) {
  deleteFormAnswerGroup(input: $input) {
    form_answer_group
    messages
  }
}
```
