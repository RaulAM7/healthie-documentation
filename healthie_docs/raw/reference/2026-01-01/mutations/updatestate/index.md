---
title: updateState | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatestate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatestate/index.md
---

Archive/Unarchive a Course

## Arguments

[`input` ](#argument-input)· [`updateStateInput` ](/reference/2026-01-01/input-objects/updatestateinput)· Parameters for updateState

## Returns

[`updateStatePayload`](/reference/2026-01-01/objects/updatestatepayload)

## Example

```
mutation updateState($input: updateStateInput) {
  updateState(input: $input) {
    course
    messages
  }
}
```
