---
title: courseGroupClients | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/coursegroupclients/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/coursegroupclients/index.md
---

Fetch paginated course group clients collection

## Arguments

[`course_group_id` ](#argument-course-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`course_id` ](#argument-course-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`course_status` ](#argument-course-status)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`UserConnection`](/reference/2026-01-01/objects/userconnection)

## Example

```
query courseGroupClients(
  $course_group_id: ID
  $course_id: ID
  $course_status: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  courseGroupClients(
    course_group_id: $course_group_id
    course_id: $course_id
    course_status: $course_status
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
