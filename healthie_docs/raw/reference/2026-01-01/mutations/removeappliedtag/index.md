---
title: removeAppliedTag | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/removeappliedtag/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/removeappliedtag/index.md
---

Remove applied tag on a specific user

## Arguments

[`input` ](#argument-input)· [`removeAppliedTagInput` ](/reference/2026-01-01/input-objects/removeappliedtaginput)· Parameters for removeAppliedTag

## Returns

[`removeAppliedTagPayload`](/reference/2026-01-01/objects/removeappliedtagpayload)

## Example

```
mutation removeAppliedTag($input: removeAppliedTagInput) {
  removeAppliedTag(input: $input) {
    messages
    tag
  }
}
```
