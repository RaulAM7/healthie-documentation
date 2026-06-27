---
title: courses | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/courses/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/courses/index.md
---

Fetch paginated course collection

## Arguments

[`active` ](#argument-active)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`course_type` ](#argument-course-type)· [`CourseTypeFilter`](/reference/2026-01-01/enums/coursetypefilter)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`only_available` ](#argument-only-available)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CoursePaginationConnection`](/reference/2026-01-01/objects/coursepaginationconnection)

## Example

```
query courses(
  $active: Boolean
  $course_type: CourseTypeFilter
  $keywords: String
  $only_available: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  courses(
    active: $active
    course_type: $course_type
    keywords: $keywords
    only_available: $only_available
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
