---
title: completedCourseItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/completedcourseitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/completedcourseitem/index.md
---

fetch a completedCourseItem by course\_item\_id and user\_id

## Arguments

[`course_item_id` ](#argument-course-item-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`CompletedCourseItem`](/reference/2026-01-01/objects/completedcourseitem)

## Example

```
query completedCourseItem($course_item_id: ID, $user_id: ID) {
  completedCourseItem(course_item_id: $course_item_id, user_id: $user_id) {
    completed_item_id
    completed_item_type
    course_item_id
    created_at
    id
    next_item
    updated_at
    user_id
  }
}
```
