---
title: prevCourseItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/prevcourseitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/prevcourseitem/index.md
---

fetch a courseitem by id (considered public)

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`CourseItem`](/reference/2026-01-01/objects/courseitem)

## Example

```
query prevCourseItem($id: ID) {
  prevCourseItem(id: $id) {
    attached_object_is_video
    blocked_by_prev_item
    completed_by_client
    completed_course_item
    completed_memberships_count
    completion_required_for_next_module
    course
    course_id
    course_name
    created_at
    custom_module_type
    date_restricted
    description
    edit_url
    first_incomplete_required_module
    has_matrix_field
    id
    incomplete_course_item_id
    item_id
    item_type
    name
    next_item
    not_available_for_client
    not_available_to_any_clients
    position
    prev_item
    scheduled_release
    updated_at
    user_id
    view_url
  }
}
```
