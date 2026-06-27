---
title: updateAddendum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateaddendum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateaddendum/index.md
---

deprecated Deprecated. Does nothing

THIS MUTATION DOES NOTHING, AND SHOULD NOT BE USED.

## Arguments

[`input` ](#argument-input)· [`updateAddendumInput` ](/reference/2026-01-01/input-objects/updateaddenduminput)· Parameters for updateAddendum

## Returns

[`updateAddendumPayload`](/reference/2026-01-01/objects/updateaddendumpayload)

## Example

```
mutation updateAddendum($input: updateAddendumInput) {
  updateAddendum(input: $input) {
    addendum
    messages
  }
}
```
