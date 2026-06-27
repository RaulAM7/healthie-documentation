---
title: CourseMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursemembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursemembership/index.md
---

Relationship between a user and a course

## Fields

[`course` ](#field-course)· [`Course` ](/reference/2026-01-01/objects/course)· the course associated with this membership

[`course_id` ](#field-course-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of course related to this membership

[`course_status` ](#field-course-status)· [`CourseMembershipStatus!` ](/reference/2026-01-01/enums/coursemembershipstatus)· required · status of related course completion

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date membership was created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the membership

[`is_paused` ](#field-is-paused)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the membership is currently paused

[`next_incomplete_item` ](#field-next-incomplete-item)· [`CourseItem` ](/reference/2026-01-01/objects/courseitem)· The next incomplete item

[`next_next_incomplete_item` ](#field-next-next-incomplete-item)· [`CourseItem` ](/reference/2026-01-01/objects/courseitem)· The incomplete item after the next incomplete item

[`paused_at` ](#field-paused-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Timestamp the membership was paused; null when not paused

[`start_at` ](#field-start-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· start of course

[`total_paused_duration` ](#field-total-paused-duration)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Cumulative paused duration in seconds across all pause/resume cycles

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date membership was updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· the user associated with this membership

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of user related to this membership

## Used By

[`Course.clients`](/reference/2026-01-01/objects/course)

[`Course.course_memberships`](/reference/2026-01-01/objects/course)

[`Course.ungrouped_course_memberships`](/reference/2026-01-01/objects/course)

[`CourseMembershipEdge.node`](/reference/2026-01-01/objects/coursemembershipedge)

[`CourseMembershipPaginationConnection.nodes`](/reference/2026-01-01/objects/coursemembershippaginationconnection)

[`PauseCourseMembershipPayload.courseMembership`](/reference/2026-01-01/objects/pausecoursemembershippayload)

[`ResumeCourseMembershipPayload.courseMembership`](/reference/2026-01-01/objects/resumecoursemembershippayload)

[`User.course_membership_via_course`](/reference/2026-01-01/objects/user)

[`User.course_memberships`](/reference/2026-01-01/objects/user)

[`User.course_membrships`](/reference/2026-01-01/objects/user)

[`deleteCourseMembershipPayload.courseMembership`](/reference/2026-01-01/objects/deletecoursemembershippayload)

[`updateCourseMembershipPayload.courseMembership`](/reference/2026-01-01/objects/updatecoursemembershippayload)

[`Query.courseMembership`](/reference/2026-01-01/queries/coursemembership)

## Definition

```
"""
Relationship between a user and a course
"""
type CourseMembership {
  """
  the course associated with this membership
  """
  course: Course


  """
  id of course related to this membership
  """
  course_id: ID


  """
  status of related course completion
  """
  course_status: CourseMembershipStatus!


  """
  date membership was created
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the membership
  """
  id: ID!


  """
  Whether the membership is currently paused
  """
  is_paused: Boolean!


  """
  The next incomplete item
  """
  next_incomplete_item: CourseItem


  """
  The incomplete item after the next incomplete item
  """
  next_next_incomplete_item: CourseItem


  """
  Timestamp the membership was paused; null when not paused
  """
  paused_at: ISO8601DateTime


  """
  start of course
  """
  start_at: ISO8601DateTime


  """
  Cumulative paused duration in seconds across all pause/resume cycles
  """
  total_paused_duration: Int!


  """
  date membership was updated
  """
  updated_at: ISO8601DateTime!


  """
  the user associated with this membership
  """
  user: User


  """
  id of user related to this membership
  """
  user_id: ID
}
```
