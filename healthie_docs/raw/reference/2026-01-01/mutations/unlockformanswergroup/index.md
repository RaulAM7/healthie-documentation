---
title: unlockFormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/unlockformanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/unlockformanswergroup/index.md
---

Unlock \`FormAnswerGroup\`

## Arguments

[`input` ](#argument-input)· [`UnlockInput` ](/reference/2026-01-01/input-objects/unlockinput)· Parameters for Unlock

## Returns

[`UnlockPayload`](/reference/2026-01-01/objects/unlockpayload)

## Example

```
mutation unlockFormAnswerGroup($input: UnlockInput) {
  unlockFormAnswerGroup(input: $input) {
    form_answer_group
    messages
  }
}
```
