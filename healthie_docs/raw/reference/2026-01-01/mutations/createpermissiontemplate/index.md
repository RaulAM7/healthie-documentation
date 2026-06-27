---
title: createPermissionTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpermissiontemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpermissiontemplate/index.md
---

create Permission Template

## Arguments

[`input` ](#argument-input)· [`createPermissionTemplateInput` ](/reference/2026-01-01/input-objects/createpermissiontemplateinput)· Parameters for createPermissionTemplate

## Returns

[`createPermissionTemplatePayload`](/reference/2026-01-01/objects/createpermissiontemplatepayload)

## Example

```
mutation createPermissionTemplate($input: createPermissionTemplateInput) {
  createPermissionTemplate(input: $input) {
    messages
    newPermissionTemplate
  }
}
```
