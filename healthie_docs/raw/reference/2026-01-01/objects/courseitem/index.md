---
title: CourseItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/courseitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/courseitem/index.md
---

A Course Item

## Fields

[`attached_object_is_video` ](#field-attached-object-is-video)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· whether the attached object is a video form

[`blocked_by_prev_item` ](#field-blocked-by-prev-item)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Shows if the current course item is blocked by an incomplete previous required item

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· category of item

deprecated

This field is no longer used

[`completed_by_client` ](#field-completed-by-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Check if course item was completed by a client

[`completed_course_item` ](#field-completed-course-item)· [`CompletedCourseItem` ](/reference/2026-01-01/objects/completedcourseitem)· The completed course item

[`completed_memberships_count` ](#field-completed-memberships-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of members who completed the item

[`completion_required_for_next_module` ](#field-completion-required-for-next-module)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Determines whether or not completion of the course item is necessary to access the next

[`course` ](#field-course)· [`Course` ](/reference/2026-01-01/objects/course)· The associated course

[`course_id` ](#field-course-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of course associated with item

[`course_name` ](#field-course-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of course that item belongs to

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · when item was created

[`custom_module_type` ](#field-custom-module-type)· [`String` ](/reference/2026-01-01/scalars/string)· type of custom module of a course item (if app)

[`date_restricted` ](#field-date-restricted)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Shows if the current course item is blocked due to course membership date restriction

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· description of item

[`edit_url` ](#field-edit-url)· [`String` ](/reference/2026-01-01/scalars/string)· The path to edit the item

[`first_incomplete_required_module` ](#field-first-incomplete-required-module)· [`CourseItem` ](/reference/2026-01-01/objects/courseitem)· This is the first required module that is incomplete, and will block items in higher positions

[`has_matrix_field` ](#field-has-matrix-field)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Course item has matrix field

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the item

[`incomplete_course_item_id` ](#field-incomplete-course-item-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of an incomplete form associated with the item

[`item_id` ](#field-item-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of item

[`item_type` ](#field-item-type)· [`String` ](/reference/2026-01-01/scalars/string)· type of course item

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of item

[`next_item` ](#field-next-item)· [`CourseItem` ](/reference/2026-01-01/objects/courseitem)· The next item in the course

[`not_available_for_client` ](#field-not-available-for-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Check if course item is available to a client

[`not_available_to_any_clients` ](#field-not-available-to-any-clients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Check if course item is available to any client

[`position` ](#field-position)· [`Int` ](/reference/2026-01-01/scalars/int)· The position of the course item type when shown in a list of other modules on the same day

[`prev_item` ](#field-prev-item)· [`CourseItem` ](/reference/2026-01-01/objects/courseitem)· The previous item in the course

[`scheduled_release` ](#field-scheduled-release)· [`String` ](/reference/2026-01-01/scalars/string)· The number of days after a client's course start date when this item becomes available

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · when item was updated

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of user associated with item

[`view_url` ](#field-view-url)· [`String` ](/reference/2026-01-01/scalars/string)· The path to view the item

## Used By

[`CompletedCourseItem.next_item`](/reference/2026-01-01/objects/completedcourseitem)

[`Course.course_items`](/reference/2026-01-01/objects/course)

[`CourseItem.first_incomplete_required_module`](/reference/2026-01-01/objects/courseitem)

[`CourseItem.next_item`](/reference/2026-01-01/objects/courseitem)

[`CourseItem.prev_item`](/reference/2026-01-01/objects/courseitem)

[`CourseItemEdge.node`](/reference/2026-01-01/objects/courseitemedge)

[`CourseItemPaginationConnection.nodes`](/reference/2026-01-01/objects/courseitempaginationconnection)

[`CourseMembership.next_incomplete_item`](/reference/2026-01-01/objects/coursemembership)

[`CourseMembership.next_next_incomplete_item`](/reference/2026-01-01/objects/coursemembership)

[`createCourseItemPayload.courseItem`](/reference/2026-01-01/objects/createcourseitempayload)

[`deleteCourseItemPayload.courseItem`](/reference/2026-01-01/objects/deletecourseitempayload)

[`updateCourseItemPayload.courseItem`](/reference/2026-01-01/objects/updatecourseitempayload)

[`Query.courseItem`](/reference/2026-01-01/queries/courseitem)

[`Query.nextCourseItem`](/reference/2026-01-01/queries/nextcourseitem)

[`Query.prevCourseItem`](/reference/2026-01-01/queries/prevcourseitem)

## Definition

```
"""
A Course Item
"""
type CourseItem {
  """
  whether the attached object is a video form
  """
  attached_object_is_video: Boolean


  """
  Shows if the current course item is blocked by an incomplete previous required item
  """
  blocked_by_prev_item(
    """
    Get the completed course item for the given membership and course_item
    """
    course_membership_id: ID
  ): Boolean


  """
  category of item
  """
  category: String @deprecated(reason: "This field is no longer used")


  """
  Check if course item was completed by a client
  """
  completed_by_client(
    """
    The ID of the client
    """
    client_id: ID
  ): Boolean


  """
  The completed course item
  """
  completed_course_item(
    """
    Get the completed course item for the given membership and course_item
    """
    course_membership_id: ID
  ): CompletedCourseItem


  """
  The number of members who completed the item
  """
  completed_memberships_count: Int


  """
  Determines whether or not completion of the course item is necessary to access the next
  """
  completion_required_for_next_module: Boolean!


  """
  The associated course
  """
  course: Course


  """
  id of course associated with item
  """
  course_id: ID


  """
  name of course that item belongs to
  """
  course_name: String


  """
  when item was created
  """
  created_at: ISO8601DateTime!


  """
  type of custom module of a course item (if app)
  """
  custom_module_type: String


  """
  Shows if the current course item is blocked due to course membership date restriction
  """
  date_restricted(
    """
    The ID of a course membership
    """
    course_membership_id: ID
  ): Boolean


  """
  description of item
  """
  description: String


  """
  The path to edit the item
  """
  edit_url: String


  """
  This is the first required module that is incomplete, and will block items in higher positions
  """
  first_incomplete_required_module: CourseItem


  """
  Course item has matrix field
  """
  has_matrix_field: Boolean


  """
  The unique identifier of the item
  """
  id: ID!


  """
  The ID of an incomplete form associated with the item
  """
  incomplete_course_item_id(
    """
    The ID of a course membership
    """
    course_membership_id: ID
  ): ID


  """
  id of item
  """
  item_id: ID


  """
  type of course item
  """
  item_type: String


  """
  name of item
  """
  name: String


  """
  The next item in the course
  """
  next_item: CourseItem


  """
  Check if course item is available to a client
  """
  not_available_for_client(
    """
    The ID of a client
    """
    client_id: ID
  ): Boolean


  """
  Check if course item is available to any client
  """
  not_available_to_any_clients: Boolean


  """
  The position of the course item type when shown in a list of other modules on the same day
  """
  position: Int


  """
  The previous item in the course
  """
  prev_item: CourseItem


  """
  The number of days after a client's course start date when this item becomes available
  """
  scheduled_release: String


  """
  when item was updated
  """
  updated_at: ISO8601DateTime!


  """
  id of user associated with item
  """
  user_id: ID


  """
  The path to view the item
  """
  view_url: String
}
```
