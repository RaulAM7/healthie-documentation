---
title: CompletedCourseItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/completedcourseitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/completedcourseitem/index.md
---

a completed course item

## Fields

[`completed_item_id` ](#field-completed-item-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the completed item

[`completed_item_type` ](#field-completed-item-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the completed item

[`course_item_id` ](#field-course-item-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of course related to the completed item

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date when the completed item was created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the item

[`next_item` ](#field-next-item)· [`CourseItem` ](/reference/2026-01-01/objects/courseitem)· The next item after the current item

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date when the completed item was updated

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user related to the completed item

## Used By

[`CourseItem.completed_course_item`](/reference/2026-01-01/objects/courseitem)

[`completeCourseDocumentPayload.completedCourseItem`](/reference/2026-01-01/objects/completecoursedocumentpayload)

[`createCompletedCourseItemPayload.completedCourseItem`](/reference/2026-01-01/objects/createcompletedcourseitempayload)

[`Query.completedCourseItem`](/reference/2026-01-01/queries/completedcourseitem)

## Definition

```
"""
a completed course item
"""
type CompletedCourseItem {
  """
  The ID of the completed item
  """
  completed_item_id: ID


  """
  The type of the completed item
  """
  completed_item_type: String


  """
  The ID of course related to the completed item
  """
  course_item_id: ID


  """
  The date when the completed item was created
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the item
  """
  id: ID!


  """
  The next item after the current item
  """
  next_item: CourseItem


  """
  The date when the completed item was updated
  """
  updated_at: ISO8601DateTime!


  """
  The ID of the user related to the completed item
  """
  user_id: ID
}
```
