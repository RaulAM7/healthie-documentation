---
title: CourseGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursegroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursegroup/index.md
---

Relationship between a user group and a course

## Fields

[`course` ](#field-course)· [`Course` ](/reference/2026-01-01/objects/course)· the course associated with this membership

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the group

[`is_paused` ](#field-is-paused)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the course group is currently paused

[`paused_at` ](#field-paused-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· When the group was paused; nil if not paused

[`start_at` ](#field-start-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· start of course

[`start_on_group_assignment` ](#field-start-on-group-assignment)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, new group members start the course at the current time, overriding start\_at

[`user_group` ](#field-user-group)· [`UserGroup` ](/reference/2026-01-01/objects/usergroup)· the user group associated with this membership

## Used By

[`Course.clients_groups`](/reference/2026-01-01/objects/course)

[`Course.course_groups`](/reference/2026-01-01/objects/course)

[`PauseCourseGroupPayload.courseGroup`](/reference/2026-01-01/objects/pausecoursegrouppayload)

[`ResumeCourseGroupPayload.courseGroup`](/reference/2026-01-01/objects/resumecoursegrouppayload)

[`deleteCourseGroupPayload.courseGroup`](/reference/2026-01-01/objects/deletecoursegrouppayload)

[`updateCourseGroupPayload.courseGroup`](/reference/2026-01-01/objects/updatecoursegrouppayload)

## Definition

```
"""
Relationship between a user group and a course
"""
type CourseGroup {
  """
  the course associated with this membership
  """
  course: Course


  """
  The unique identifier of the group
  """
  id: ID!


  """
  Whether the course group is currently paused
  """
  is_paused: Boolean!


  """
  When the group was paused; nil if not paused
  """
  paused_at: ISO8601DateTime


  """
  start of course
  """
  start_at: ISO8601DateTime


  """
  When true, new group members start the course at the current time, overriding start_at
  """
  start_on_group_assignment: Boolean!


  """
  the user group associated with this membership
  """
  user_group: UserGroup
}
```
