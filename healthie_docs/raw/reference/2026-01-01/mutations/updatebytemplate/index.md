---
title: updateByTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatebytemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatebytemplate/index.md
---

Update Care Plan by Care Plan Template

## Arguments

[`input` ](#argument-input)· [`updateByTemplateInput` ](/reference/2026-01-01/input-objects/updatebytemplateinput)· Parameters for updateByTemplate

## Returns

[`updateByTemplatePayload`](/reference/2026-01-01/objects/updatebytemplatepayload)

## Example

```
mutation updateByTemplate($input: updateByTemplateInput) {
  updateByTemplate(input: $input) {
    care_plan
    messages
  }
}
```
