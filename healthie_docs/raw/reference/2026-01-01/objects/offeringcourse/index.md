---
title: OfferingCourse | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringcourse/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringcourse/index.md
---

Offering Course

## Fields

[`course` ](#field-course)· [`Course` ](/reference/2026-01-01/objects/course)· course

[`course_id` ](#field-course-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · id of related course

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the join

[`offering_id` ](#field-offering-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of related offering

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

## Used By

[`Offering.offering_courses`](/reference/2026-01-01/objects/offering)

## Definition

```
"""
Offering Course
"""
type OfferingCourse {
  """
  course
  """
  course: Course


  """
  id of related course
  """
  course_id: ID!


  """
  created at
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the join
  """
  id: ID!


  """
  id of related offering
  """
  offering_id: ID


  """
  updated at
  """
  updated_at: ISO8601DateTime!
}
```
