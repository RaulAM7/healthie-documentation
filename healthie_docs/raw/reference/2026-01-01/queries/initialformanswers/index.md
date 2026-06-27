---
title: initialFormAnswers | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/initialformanswers/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/initialformanswers/index.md
---

Initial form answers for a given user and template

## Arguments

[`custom_module_form_id` ](#argument-custom-module-form-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`incomplete_form_id` ](#argument-incomplete-form-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`[FormAnswer!]`](/reference/2026-01-01/objects/formanswer)

## Example

```
query initialFormAnswers(
  $custom_module_form_id: ID
  $incomplete_form_id: ID
  $user_id: ID
) {
  initialFormAnswers(
    custom_module_form_id: $custom_module_form_id
    incomplete_form_id: $incomplete_form_id
    user_id: $user_id
  ) {
    answer
    conditional_custom_module_id
    created_at
    custom_module
    custom_module_id
    displayed_answer
    file_attachments
    filter_type
    form_answer_group
    id
    label
    metadata
    updated_at
    user_id
    value_to_filter
  }
}
```
