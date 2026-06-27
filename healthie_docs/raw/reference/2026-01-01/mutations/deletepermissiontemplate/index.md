---
title: deletePermissionTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletepermissiontemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletepermissiontemplate/index.md
---

delete Permission Template

## Arguments

[`input` ](#argument-input)· [`deletePermissionTemplateInput` ](/reference/2026-01-01/input-objects/deletepermissiontemplateinput)· Parameters for deletePermissionTemplate

## Returns

[`deletePermissionTemplatePayload`](/reference/2026-01-01/objects/deletepermissiontemplatepayload)

## Example

```
mutation deletePermissionTemplate($input: deletePermissionTemplateInput) {
  deletePermissionTemplate(input: $input) {
    messages
    permission_template
  }
}
```
