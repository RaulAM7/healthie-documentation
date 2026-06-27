---
title: createDraft | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createdraft/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createdraft/index.md
---

create Draft

## Arguments

[`input` ](#argument-input)· [`createDraftInput` ](/reference/2026-01-01/input-objects/createdraftinput)· Parameters for createDraft

## Returns

[`createDraftPayload`](/reference/2026-01-01/objects/createdraftpayload)

## Example

```
mutation createDraft($input: createDraftInput) {
  createDraft(input: $input) {
    draft
    messages
  }
}
```
