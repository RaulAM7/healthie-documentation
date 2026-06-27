---
title: createSharings | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsharings/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsharings/index.md
---

Create document or folder sharings for clients, providers, and/or groups

## Arguments

[`input` ](#argument-input)· [`CreateSharingsInput` ](/reference/2026-01-01/input-objects/createsharingsinput)· Parameters for CreateSharings

## Returns

[`Shareable`](/reference/2026-01-01/unions/shareable)

## Example

```
mutation createSharings($input: CreateSharingsInput) {
  createSharings(input: $input)
}
```
