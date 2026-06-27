---
title: updateMacronutrientSplit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatemacronutrientsplit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatemacronutrientsplit/index.md
---

deprecated Deprecated, do not use

Update Macronutrient Split in the Health Assessment Service

## Arguments

[`input` ](#argument-input)· [`UpdateMacronutrientSplitInput` ](/reference/2026-01-01/input-objects/updatemacronutrientsplitinput)· Parameters for UpdateMacronutrientSplit

## Returns

[`UpdateMacronutrientSplitPayload`](/reference/2026-01-01/objects/updatemacronutrientsplitpayload)

## Example

```
mutation updateMacronutrientSplit($input: UpdateMacronutrientSplitInput) {
  updateMacronutrientSplit(input: $input) {
    assessment
    messages
  }
}
```
