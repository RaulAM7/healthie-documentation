---
title: courseItems | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/courseitems/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/courseitems/index.md
---

Fetch paginated course items collection

## Arguments

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`course_id` ](#argument-course-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`find_for_provider` ](#argument-find-for-provider)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`include_emails` ](#argument-include-emails)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CourseItemPaginationConnection`](/reference/2026-01-01/objects/courseitempaginationconnection)

## Example

```
query courseItems(
  $client_id: ID
  $course_id: ID
  $find_for_provider: Boolean
  $include_emails: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  courseItems(
    client_id: $client_id
    course_id: $course_id
    find_for_provider: $find_for_provider
    include_emails: $include_emails
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
