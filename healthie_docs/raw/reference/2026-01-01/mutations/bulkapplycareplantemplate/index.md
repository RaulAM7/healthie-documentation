---
title: bulkApplyCarePlanTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkapplycareplantemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkapplycareplantemplate/index.md
---

Apply care plan to the passed array of clients and/or groups

## Arguments

[`input` ](#argument-input)· [`bulkApplyCarePlanTemplateInput` ](/reference/2026-01-01/input-objects/bulkapplycareplantemplateinput)· Parameters for bulkApplyCarePlanTemplate

## Returns

[`bulkApplyCarePlanTemplatePayload`](/reference/2026-01-01/objects/bulkapplycareplantemplatepayload)

## Example

```
mutation bulkApplyCarePlanTemplate($input: bulkApplyCarePlanTemplateInput) {
  bulkApplyCarePlanTemplate(input: $input) {
    carePlans
    messages
  }
}
```
