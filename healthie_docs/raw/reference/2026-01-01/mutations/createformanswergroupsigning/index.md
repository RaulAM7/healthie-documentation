---
title: createFormAnswerGroupSigning | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createformanswergroupsigning/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createformanswergroupsigning/index.md
---

deprecated Use \`signFormAnswerGroup\` mutation

Create FormAnswerGroupSigning

## Arguments

[`input` ](#argument-input)· [`createFormAnswerGroupSigningInput` ](/reference/2026-01-01/input-objects/createformanswergroupsigninginput)· Parameters for createFormAnswerGroupSigning

## Returns

[`createFormAnswerGroupSigningPayload`](/reference/2026-01-01/objects/createformanswergroupsigningpayload)

## Example

```
mutation createFormAnswerGroupSigning(
  $input: createFormAnswerGroupSigningInput
) {
  createFormAnswerGroupSigning(input: $input) {
    formAnswerGroupSigning
    messages
  }
}
```
