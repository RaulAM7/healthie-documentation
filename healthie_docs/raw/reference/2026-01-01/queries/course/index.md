---
title: course | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/course/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/course/index.md
---

fetch a course by id (considered public)

## Arguments

[`course_id` ](#argument-course-id)· [`ID` ](/reference/2026-01-01/scalars/id)· deprecated, use \`id\` instead

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Course`](/reference/2026-01-01/objects/course)

## Example

```
query course($course_id: ID, $id: ID) {
  course(course_id: $course_id, id: $id) {
    active
    clients
    clients_groups
    completed_course_memberships_count
    course_benefits
    course_groups
    course_items
    course_memberships
    course_memberships_count
    course_type
    created_at
    deleted_at
    description
    end_date
    formatted_benefits
    id
    in_progress_course_memberships_count
    late_enroll
    name
    not_started_course_memberships_count
    offerings
    preview_image_url
    preview_video_content
    start_date
    ungrouped_course_memberships
    updated_at
    use_video_label
    user_groups
    user_id
    users
    users_course_items_progress
    users_progress
  }
}
```
