---
title: refetchChangeHealthLabOrder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/refetchchangehealthlaborder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/refetchchangehealthlaborder/index.md
---

refetch ChangeHealth Lab Orders for a specified patient

## Arguments

[`input` ](#argument-input)· [`RefetchChangeHealthLabOrderInput` ](/reference/2026-01-01/input-objects/refetchchangehealthlaborderinput)· Parameters for RefetchChangeHealthLabOrder

## Returns

[`RefetchChangeHealthLabOrderPayload`](/reference/2026-01-01/objects/refetchchangehealthlaborderpayload)

## Example

```
mutation refetchChangeHealthLabOrder($input: RefetchChangeHealthLabOrderInput) {
  refetchChangeHealthLabOrder(input: $input) {
    messages
    success_string
  }
}
```
