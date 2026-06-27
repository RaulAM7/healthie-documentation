---
title: updateSecondaryClaim | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesecondaryclaim/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesecondaryclaim/index.md
---

Update COB overrides on a secondary claim

## Arguments

[`input` ](#argument-input)· [`UpdateSecondaryClaimInput` ](/reference/2026-01-01/input-objects/updatesecondaryclaiminput)· Parameters for UpdateSecondaryClaim

## Returns

[`UpdateSecondaryClaimPayload`](/reference/2026-01-01/objects/updatesecondaryclaimpayload)

## Example

```
mutation updateSecondaryClaim($input: UpdateSecondaryClaimInput) {
  updateSecondaryClaim(input: $input) {
    claim
    messages
  }
}
```
