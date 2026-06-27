---
title: lockFormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/lockformanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/lockformanswergroup/index.md
---

Lock \`FormAnswerGroup\`

## Arguments

[`input` ](#argument-input)· [`LockInput` ](/reference/2026-01-01/input-objects/lockinput)· Parameters for Lock

## Returns

[`LockPayload`](/reference/2026-01-01/objects/lockpayload)

## Example

```
mutation lockFormAnswerGroup($input: LockInput) {
  lockFormAnswerGroup(input: $input) {
    form_answer_group
    messages
  }
}
```
