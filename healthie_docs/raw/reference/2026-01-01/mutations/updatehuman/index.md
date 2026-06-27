---
title: updateHuman | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatehuman/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatehuman/index.md
---

Update a Human

## Arguments

[`input` ](#argument-input)· [`updateHumanInput` ](/reference/2026-01-01/input-objects/updatehumaninput)· Parameters for updateHuman

## Returns

[`updateHumanPayload`](/reference/2026-01-01/objects/updatehumanpayload)

## Example

```
mutation updateHuman($input: updateHumanInput) {
  updateHuman(input: $input) {
    human
    messages
  }
}
```
