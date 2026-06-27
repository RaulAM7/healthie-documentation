---
title: runEligibilityCheck | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/runeligibilitycheck/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/runeligibilitycheck/index.md
---

Run an eligibility check on a policy

## Arguments

[`input` ](#argument-input)· [`runEligibilityCheckMutationInput` ](/reference/2026-01-01/input-objects/runeligibilitycheckmutationinput)· Parameters for runEligibilityCheckMutation

## Returns

[`runEligibilityCheckMutationPayload`](/reference/2026-01-01/objects/runeligibilitycheckmutationpayload)

## Example

```
mutation runEligibilityCheck($input: runEligibilityCheckMutationInput) {
  runEligibilityCheck(input: $input) {
    eligibility_check
    messages
  }
}
```
