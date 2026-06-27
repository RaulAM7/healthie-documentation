---
title: createFeatureToggle | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfeaturetoggle/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfeaturetoggle/index.md
---

Create a FeatureToggle and Return FeatureToggle

## Arguments

[`input` ](#argument-input)· [`createFeatureToggleInput` ](/reference/2026-01-01/input-objects/createfeaturetoggleinput)· Parameters for createFeatureToggle

## Returns

[`createFeatureTogglePayload`](/reference/2026-01-01/objects/createfeaturetogglepayload)

## Example

```
mutation createFeatureToggle($input: createFeatureToggleInput) {
  createFeatureToggle(input: $input) {
    feature_toggle
    messages
  }
}
```
