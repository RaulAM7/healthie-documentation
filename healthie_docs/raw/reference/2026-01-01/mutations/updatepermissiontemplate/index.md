---
title: updatePermissionTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatepermissiontemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatepermissiontemplate/index.md
---

update Permission Template

## Arguments

[`input` ](#argument-input)· [`updatePermissionTemplateInput` ](/reference/2026-01-01/input-objects/updatepermissiontemplateinput)· Parameters for updatePermissionTemplate

## Returns

[`updatePermissionTemplatePayload`](/reference/2026-01-01/objects/updatepermissiontemplatepayload)

## Example

```
mutation updatePermissionTemplate($input: updatePermissionTemplateInput) {
  updatePermissionTemplate(input: $input) {
    messages
    permissionTemplate
  }
}
```
