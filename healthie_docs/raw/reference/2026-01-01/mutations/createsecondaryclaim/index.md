---
title: createSecondaryClaim | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsecondaryclaim/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsecondaryclaim/index.md
---

Create a secondary claim from a primary claim for COB submission

## Arguments

[`input` ](#argument-input)· [`CreateSecondaryClaimInput` ](/reference/2026-01-01/input-objects/createsecondaryclaiminput)· Parameters for CreateSecondaryClaim

## Returns

[`CreateSecondaryClaimPayload`](/reference/2026-01-01/objects/createsecondaryclaimpayload)

## Example

```
mutation createSecondaryClaim($input: CreateSecondaryClaimInput) {
  createSecondaryClaim(input: $input) {
    claim
    messages
  }
}
```
