---
title: createAddendum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createaddendum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createaddendum/index.md
---

Create a new addendum for the selected charting note

## Arguments

[`input` ](#argument-input)· [`createAddendumInput` ](/reference/2026-01-01/input-objects/createaddenduminput)· Parameters for createAddendum

## Returns

[`createAddendumPayload`](/reference/2026-01-01/objects/createaddendumpayload)

## Example

```
mutation createAddendum($input: createAddendumInput) {
  createAddendum(input: $input) {
    addendum
    messages
  }
}
```
