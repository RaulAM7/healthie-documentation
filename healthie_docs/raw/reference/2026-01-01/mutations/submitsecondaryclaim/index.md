---
title: submitSecondaryClaim | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/submitsecondaryclaim/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/submitsecondaryclaim/index.md
---

Submit secondary claims with COB data to ClaimMD

## Arguments

[`input` ](#argument-input)· [`SubmitSecondaryClaimInput` ](/reference/2026-01-01/input-objects/submitsecondaryclaiminput)· Parameters for SubmitSecondaryClaim

## Returns

[`SubmitSecondaryClaimPayload`](/reference/2026-01-01/objects/submitsecondaryclaimpayload)

## Example

```
mutation submitSecondaryClaim($input: SubmitSecondaryClaimInput) {
  submitSecondaryClaim(input: $input) {
    claims
    messages
    success_message
  }
}
```
