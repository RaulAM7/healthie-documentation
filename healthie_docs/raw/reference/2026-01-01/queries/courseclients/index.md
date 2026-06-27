---
title: courseClients | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/courseclients/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/courseclients/index.md
---

fetch clients belonging to a course by course\_id

## Arguments

[`course_id` ](#argument-course-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`course_status` ](#argument-course-status)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CourseMembershipPaginationConnection`](/reference/2026-01-01/objects/coursemembershippaginationconnection)

## Example

```
query courseClients(
  $course_id: ID
  $course_status: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  courseClients(
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
