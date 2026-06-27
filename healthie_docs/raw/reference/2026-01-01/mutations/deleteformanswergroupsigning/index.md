---
title: deleteFormAnswerGroupSigning | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteformanswergroupsigning/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteformanswergroupsigning/index.md
---

Destroy FormAnswerGroupSigning

## Arguments

[`input` ](#argument-input)· [`deleteFormAnswerGroupSigningInput` ](/reference/2026-01-01/input-objects/deleteformanswergroupsigninginput)· Parameters for deleteFormAnswerGroupSigning

## Returns

[`deleteFormAnswerGroupSigningPayload`](/reference/2026-01-01/objects/deleteformanswergroupsigningpayload)

## Example

```
mutation deleteFormAnswerGroupSigning(
  $input: deleteFormAnswerGroupSigningInput
) {
  deleteFormAnswerGroupSigning(input: $input) {
    formAnswerGroupSigning
    messages
  }
}
```
