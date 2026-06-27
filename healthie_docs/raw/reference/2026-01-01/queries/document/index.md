---
title: document | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/document/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/document/index.md
---

fetch a document by id

## Arguments

[`care_plan_id` ](#argument-care-plan-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the associated care plan.

[`course_id` ](#argument-course-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the associated program.

[`course_item_id` ](#argument-course-item-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the associated program item.

[`custom_module_id` ](#argument-custom-module-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the associated custom module.

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the document.

## Returns

[`Document`](/reference/2026-01-01/objects/document)

## Example

```
query document(
  $care_plan_id: ID
  $course_id: ID
  $course_item_id: ID
  $custom_module_id: ID
  $id: ID
) {
  document(
    care_plan_id: $care_plan_id
    course_id: $course_id
    course_item_id: $course_item_id
    custom_module_id: $custom_module_id
    id: $id
  ) {
    can_only_share
    created_at
    description
    display_name
    email_on_welcome
    expiring_url
    extension
    file_content_type
    form_answer_groups
    friendly_type
    id
    include_in_charting
    internal_notes
    metadata
    opens
    owner
    rel_user
    rel_user_id
    shareable_org_members
    shareable_patients
    shareable_user_groups
    shared
    shared_on_welcome
    shared_user_groups_count
    shared_users_count
    shared_with_dietitians
    unshared_patients_count
    updated_at
    user_groups
    users
  }
}
```
