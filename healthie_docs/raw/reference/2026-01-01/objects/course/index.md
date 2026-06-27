---
title: Course | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/course/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/course/index.md
---

A Course

## Fields

[`active` ](#field-active)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the course is active

[`clients` ](#field-clients)· [`[CourseMembership!]` ](/reference/2026-01-01/objects/coursemembership)· Course clients

[`clients_groups` ](#field-clients-groups)· [`[CourseGroup!]` ](/reference/2026-01-01/objects/coursegroup)· Course group memberships for the course

[`completed_course_memberships_count` ](#field-completed-course-memberships-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of completed memberships in the course

[`course_benefits` ](#field-course-benefits)· [`[CourseBenefit!]!` ](/reference/2026-01-01/objects/coursebenefit)· required · The benefits of a course

[`course_groups` ](#field-course-groups)· [`[CourseGroup!]` ](/reference/2026-01-01/objects/coursegroup)· Course group memberships for the course

[`course_items` ](#field-course-items)· [`[CourseItem!]!` ](/reference/2026-01-01/objects/courseitem)· required · The items of a course

[`course_memberships` ](#field-course-memberships)· [`[CourseMembership!]` ](/reference/2026-01-01/objects/coursemembership)· Course memberships for the course

[`course_memberships_count` ](#field-course-memberships-count)· [`String` ](/reference/2026-01-01/scalars/string)· The number of members in the course

[`course_type` ](#field-course-type)· [`CourseType!` ](/reference/2026-01-01/enums/coursetype)· required · type of the course

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date course was created

[`deleted_at` ](#field-deleted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date course was deleted

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· Description of course

[`end_date` ](#field-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· end date of the course based on included items

[`formatted_benefits` ](#field-formatted-benefits)· [`String` ](/reference/2026-01-01/scalars/string)· HTML-formatted benefits of the course

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the course

[`in_progress_course_memberships_count` ](#field-in-progress-course-memberships-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of in progress memberships in the course

[`late_enroll` ](#field-late-enroll)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· late enrollment for fixed type courses

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of course

[`not_started_course_memberships_count` ](#field-not-started-course-memberships-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of not started memberships in the course

[`offerings` ](#field-offerings)· [`[Offering!]` ](/reference/2026-01-01/objects/offering)· Offerings contains current course

[`preview_image_url` ](#field-preview-image-url)· [`String` ](/reference/2026-01-01/scalars/string)· url for course image

[`preview_video_content` ](#field-preview-video-content)· [`String` ](/reference/2026-01-01/scalars/string)· url for course video

[`start_date` ](#field-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· start date for fixed type course

[`ungrouped_course_memberships` ](#field-ungrouped-course-memberships)· [`[CourseMembership!]` ](/reference/2026-01-01/objects/coursemembership)· Ungrouped Course memberships for the course

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date course was updated

[`use_category` ](#field-use-category)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Use category toggle

deprecated

This field is no longer used

[`use_video_label` ](#field-use-video-label)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Use video label toggle

[`user_groups` ](#field-user-groups)· [`[UserGroup!]!` ](/reference/2026-01-01/objects/usergroup)· required · The user groups who have access to this course

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· User id of course

[`users` ](#field-users)· [`[User!]!` ](/reference/2026-01-01/objects/user)· required · The users who have access to this course

[`users_course_items_progress` ](#field-users-course-items-progress)· [`String` ](/reference/2026-01-01/scalars/string)· The progress of users who completed the course item

[`users_progress` ](#field-users-progress)· [`String` ](/reference/2026-01-01/scalars/string)· The users course progress

## Used By

[`CourseEdge.node`](/reference/2026-01-01/objects/courseedge)

[`CourseGroup.course`](/reference/2026-01-01/objects/coursegroup)

[`CourseItem.course`](/reference/2026-01-01/objects/courseitem)

[`CourseMembership.course`](/reference/2026-01-01/objects/coursemembership)

[`CoursePaginationConnection.nodes`](/reference/2026-01-01/objects/coursepaginationconnection)

[`OfferingCourse.course`](/reference/2026-01-01/objects/offeringcourse)

[`copyCoursePayload.course`](/reference/2026-01-01/objects/copycoursepayload)

[`createCoursePayload.course`](/reference/2026-01-01/objects/createcoursepayload)

[`deleteCoursePayload.course`](/reference/2026-01-01/objects/deletecoursepayload)

[`shareCoursePayload.course`](/reference/2026-01-01/objects/sharecoursepayload)

[`updateCoursePayload.course`](/reference/2026-01-01/objects/updatecoursepayload)

[`updateStatePayload.course`](/reference/2026-01-01/objects/updatestatepayload)

[`Query.course`](/reference/2026-01-01/queries/course)

## Definition

```
"""
A Course
"""
type Course {
  """
  Whether the course is active
  """
  active: Boolean!


  """
  Course clients
  """
  clients(
    """
    Filter by course status
    """
    course_status: String
  ): [CourseMembership!]


  """
  Course group memberships for the course
  """
  clients_groups(
    """
    Filter by course status
    """
    course_status: String
  ): [CourseGroup!]


  """
  The number of completed memberships in the course
  """
  completed_course_memberships_count: Int


  """
  The benefits of a course
  """
  course_benefits: [CourseBenefit!]!


  """
  Course group memberships for the course
  """
  course_groups: [CourseGroup!]


  """
  The items of a course
  """
  course_items(
    """
    Include custom emails
    """
    include_emails: Boolean = true
  ): [CourseItem!]!


  """
  Course memberships for the course
  """
  course_memberships: [CourseMembership!]


  """
  The number of members in the course
  """
  course_memberships_count: String


  """
  type of the course
  """
  course_type: CourseType!


  """
  date course was created
  """
  created_at: ISO8601DateTime!


  """
  date course was deleted
  """
  deleted_at: ISO8601DateTime


  """
  Description of course
  """
  description: String


  """
  end date of the course based on included items
  """
  end_date: ISO8601DateTime


  """
  HTML-formatted benefits of the course
  """
  formatted_benefits: String


  """
  The unique identifier of the course
  """
  id: ID!


  """
  The number of in progress memberships in the course
  """
  in_progress_course_memberships_count: Int


  """
  late enrollment for fixed type courses
  """
  late_enroll: Boolean


  """
  Name of course
  """
  name: String


  """
  The number of not started memberships in the course
  """
  not_started_course_memberships_count: Int


  """
  Offerings contains current course
  """
  offerings: [Offering!]


  """
  url for course image
  """
  preview_image_url: String


  """
  url for course video
  """
  preview_video_content: String


  """
  start date for fixed type course
  """
  start_date: ISO8601DateTime


  """
  Ungrouped Course memberships for the course
  """
  ungrouped_course_memberships: [CourseMembership!]


  """
  date course was updated
  """
  updated_at: ISO8601DateTime


  """
  Use category toggle
  """
  use_category: Boolean @deprecated(reason: "This field is no longer used")


  """
  Use video label toggle
  """
  use_video_label: Boolean


  """
  The user groups who have access to this course
  """
  user_groups: [UserGroup!]!


  """
  User id of course
  """
  user_id: ID


  """
  The users who have access to this course
  """
  users: [User!]!


  """
  The progress of users who completed the course item
  """
  users_course_items_progress: String


  """
  The users course progress
  """
  users_progress: String
}
```
