---
title: customModuleForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/custommoduleform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/custommoduleform/index.md
---

fetch a custom module form by ID (templates are considered public)

## Arguments

[`charting` ](#argument-charting)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`default` ](#argument-default)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the custom module form

## Returns

[`CustomModuleForm`](/reference/2026-01-01/objects/custommoduleform)

## Example

```
query customModuleForm($charting: Boolean, $default: Boolean, $id: ID) {
  customModuleForm(charting: $charting, default: $default, id: $id) {
    created_at
    customInstructions
    custom_modules
    deleted_at
    external_id
    external_id_type
    form_answer_groups
    has_matrix_field
    has_non_readonly_modules
    id
    is_video
    last_updated_by_user
    metadata
    name
    prefill
    updated_at
    uploaded_by_healthie_team
    use_for_charting
    use_for_program
    user
  }
}
```
