---
title: clearUnreconciledObjects | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/clearunreconciledobjects/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/clearunreconciledobjects/index.md
---

Delete unreconciled allergies/problems/medications

## Arguments

[`input` ](#argument-input)· [`clearUnreconciledObjectsInput` ](/reference/2026-01-01/input-objects/clearunreconciledobjectsinput)· Parameters for clearUnreconciledObjects

## Returns

[`clearUnreconciledObjectsPayload`](/reference/2026-01-01/objects/clearunreconciledobjectspayload)

## Example

```
mutation clearUnreconciledObjects($input: clearUnreconciledObjectsInput) {
  clearUnreconciledObjects(input: $input) {
    messages
  }
}
```
