---
title: exportCarePlanToTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/exportcareplantotemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/exportcareplantotemplate/index.md
---

Creates a template from existing Care Plan. Original object is not touched

## Arguments

[`input` ](#argument-input)· [`exportToTemplateInput` ](/reference/2026-01-01/input-objects/exporttotemplateinput)· Parameters for exportToTemplate

## Returns

[`exportToTemplatePayload`](/reference/2026-01-01/objects/exporttotemplatepayload)

## Example

```
mutation exportCarePlanToTemplate($input: exportToTemplateInput) {
  exportCarePlanToTemplate(input: $input) {
    carePlan
    messages
  }
}
```
