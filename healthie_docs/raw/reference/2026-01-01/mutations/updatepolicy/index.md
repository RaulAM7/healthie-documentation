---
title: updatePolicy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatepolicy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatepolicy/index.md
---

Update a policy

## Arguments

[`input` ](#argument-input)· [`updatePolicyMutationInput` ](/reference/2026-01-01/input-objects/updatepolicymutationinput)· Parameters for updatePolicyMutation

## Returns

[`updatePolicyMutationPayload`](/reference/2026-01-01/objects/updatepolicymutationpayload)

## Example

```
mutation updatePolicy($input: updatePolicyMutationInput) {
  updatePolicy(input: $input) {
    messages
    policy
  }
}
```
