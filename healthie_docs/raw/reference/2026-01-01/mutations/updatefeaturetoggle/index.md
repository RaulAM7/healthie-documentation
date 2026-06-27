---
title: updateFeatureToggle | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefeaturetoggle/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefeaturetoggle/index.md
---

Update a FeatureToggle and Return FeatureToggle

## Arguments

[`input` ](#argument-input)· [`updateFeatureToggleInput` ](/reference/2026-01-01/input-objects/updatefeaturetoggleinput)· Parameters for updateFeatureToggle

## Returns

[`updateFeatureTogglePayload`](/reference/2026-01-01/objects/updatefeaturetogglepayload)

## Example

```
mutation updateFeatureToggle($input: updateFeatureToggleInput) {
  updateFeatureToggle(input: $input) {
    feature_toggle
    messages
  }
}
```
