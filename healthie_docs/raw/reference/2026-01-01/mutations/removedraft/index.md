---
title: removeDraft | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/removedraft/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/removedraft/index.md
---

remove Draft

## Arguments

[`input` ](#argument-input)· [`removeDraftInput` ](/reference/2026-01-01/input-objects/removedraftinput)· Parameters for removeDraft

## Returns

[`removeDraftPayload`](/reference/2026-01-01/objects/removedraftpayload)

## Example

```
mutation removeDraft($input: removeDraftInput) {
  removeDraft(input: $input) {
    draft
    messages
  }
}
```
