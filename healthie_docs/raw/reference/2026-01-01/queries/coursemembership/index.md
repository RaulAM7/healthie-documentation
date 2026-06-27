---
title: courseMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/coursemembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/coursemembership/index.md
---

fetch a courseMembership by id

## Arguments

[`course_id` ](#argument-course-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`course_item_id` ](#argument-course-item-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`course_membership_id` ](#argument-course-membership-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_group_id` ](#argument-user-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`CourseMembership`](/reference/2026-01-01/objects/coursemembership)

## Example

```
query courseMembership(
  $course_id: ID
  $course_item_id: ID
  $course_membership_id: ID
  $id: ID
  $user_group_id: ID
  $user_id: ID
) {
  courseMembership(
    course_id: $course_id
    course_item_id: $course_item_id
    course_membership_id: $course_membership_id
    id: $id
    user_group_id: $user_group_id
    user_id: $user_id
  ) {
    course
    course_id
    course_status
    created_at
    id
    is_paused
    next_incomplete_item
    next_next_incomplete_item
    paused_at
    start_at
    total_paused_duration
    updated_at
    user
    user_id
  }
}
```
