---
title: deleteSharings | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesharings/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesharings/index.md
---

Destroy document or folder sharings for clients, providers, and/or groups

## Arguments

[`input` ](#argument-input)· [`DestroySharingsInput` ](/reference/2026-01-01/input-objects/destroysharingsinput)· Parameters for DestroySharings

## Returns

[`Shareable`](/reference/2026-01-01/unions/shareable)

## Example

```
mutation deleteSharings($input: DestroySharingsInput) {
  deleteSharings(input: $input)
}
```
