---
title: signFormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/signformanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/signformanswergroup/index.md
---

Sign \`FormAnswerGroup\`

## Arguments

[`input` ](#argument-input)· [`SignInput` ](/reference/2026-01-01/input-objects/signinput)· Parameters for Sign

## Returns

[`SignPayload`](/reference/2026-01-01/objects/signpayload)

## Example

```
mutation signFormAnswerGroup($input: SignInput) {
  signFormAnswerGroup(input: $input) {
    form_answer_group
    form_answer_group_signing
    messages
  }
}
```
