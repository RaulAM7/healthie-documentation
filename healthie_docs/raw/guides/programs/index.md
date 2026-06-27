---
title: Programs | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/programs/index
  md: https://docs.gethealthie.com/guides/programs/index.md
---

# Programs

You can learn more about the Programs feature in general [on Healthie’s Help platform](https://help.gethealthie.com/article/143-getting-started-education-platform).

## The Program Object

```
{
  "id": "2",
  "name": "Program 1",
  "description": null,
  "created_at": "2022-08-16 08:33:14 -0400",
  "course_memberships_count": "0",
  "course_type": "rolling",
  "start_date": null,
  "end_date": null,
  "course_items": [
    {
      "id": "4",
      "scheduled_release": "1"
    }
  ]
}
```

Programs are `Course` objects.

Programs consist of one or many Modules ([`CourseItem` objects](/reference/2024-06-01/objects/courseitem)).

You can view the full list of available fields [here](/reference/2024-06-01/objects/course).

## Listing Programs

```
query courses(
  $offset: Int
  $keywords: String
  $course_type: String
  $should_paginate: Boolean
  $only_available: Boolean
) {
  courses(
    offset: $offset
    keywords: $keywords
    course_type: $course_type
    should_paginate: $should_paginate
    only_available: $only_available
  ) {
    id
    name
    description
    course_type
    course_items {
      id
      category
      item_type
      item_id
    }
    start_date
  }
}
```

Listing Programs is done via the `courses` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/courses#arguments).

| Input            | Info                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `offset`         | Optional. Offset for pagination.                                                                                               |
| `keywords`       | Optional. Keywords to search by. Programs can be searched by name and description.                                             |
| `course_type`    | Optional. Can be either `rolling` or `fixed`.                                                                                  |
| `only_available` | Optional. If set to `true`, will return Programs that are either rolling or with a fixed start date that occurs in the future. |

Returns a list of [`Course`](/reference/2024-06-01/objects/course) objects.

## Retrieving a Program

```
query course($course_id: ID) {
  course(course_id: $course_id) {
    id
    name
    description
    course_type
    course_items {
      id
      category
      item_type
      item_id
    }
    start_date
  }
}
```

Retrieving a specific Program is done via the `course` query. This query is considered public.

| Input       | Info                        |
| ----------- | --------------------------- |
| `course_id` | ID of the Program to query. |

Returns a [`Course`](/reference/2024-06-01/objects/course) object.

## Creating a Program

```
mutation createCourse(
  $name: String
  $description: String
  $preview_video_content: String
  $formatted_benefits: String
  $external_preview_image_url: String
  $preview_image: Upload
  $course_type: String
  $start_date: String
  $late_enroll: Boolean
) {
  createCourse(
    input: {
      name: $name
      description: $description
      preview_video_content: $preview_video_content
      formatted_benefits: $formatted_benefits
      external_preview_image_url: $external_preview_image_url
      preview_image: $preview_image
      course_type: $course_type
      start_date: $start_date
      late_enroll: $late_enroll
    }
  ) {
    course {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Programs are created via the `createCourse` mutation. Let’s break down the inputs that mutation accepts.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createcourseinput).

| Input                        | Info                                                                                                                                                                                                                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`                       | **Required**.                                                                                                                                                                                                                                                                                          |
| `course_type`                | **Required**. Valid options are- `rolling`
- `fixed`                                                                                                                                                                                                                                                   |
| `start_date`                 | Required when `course_type` is `fixed`.                                                                                                                                                                                                                                                                |
| `preview_image`              | Optional. Use this to upload a preview image for the Program. Please refer to the [File Uploads](/guides/api-concepts/file-uploads/) section for more information.                                                                                                                                     |
| `external_preview_image_url` | Optional. Link to external preview image. Can be used instead of uploading via the `preview_image.`                                                                                                                                                                                                    |
| `formatted_benefits`         | Optional. A HTML-formatted string with an `<ul>` or `<ol>` list of Program benefits.                                                                                                                                                                                                                   |
| `late_enroll`                | Optional. This is an option for a `fixed` Program that determines whether clients can be enrolled in the program after the fixed start date has passed. If enabled, a client who is enrolled late will immediately receive access to all modules that all other clients in the program have access to. |

Returns a [`createCoursePayload`](/reference/2024-06-01/objects/createcoursepayload) object.

## Updating a Program

```
mutation updateCourse(
  $id: String
  $name: String
  $description: String
  $preview_video_content: String
  $formatted_benefits: String
  $external_preview_image_url: String
  $preview_image: Upload
  $course_type: String
  $start_date: String
  $late_enroll: Boolean
  $course_members: [CourseMembersInput]
) {
  updateCourse(
    input: {
      id: $id
      name: $name
      description: $description
      preview_video_content: $preview_video_content
      formatted_benefits: $formatted_benefits
      external_preview_image_url: $external_preview_image_url
      preview_image: $preview_image
      course_type: $course_type
      start_date: $start_date
      late_enroll: $late_enroll
      course_members: $course_members
    }
  ) {
    course {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateCourse` mutation shares many common inputs with [`createCourse`](#creating-a-program) and those inputs (e.g `preview_image` or `start_date` work the same in both places).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatecourseinput).

| Input            | Info                                                                                                                                                                                                            |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`             | **Required**. The ID of the Program to update.                                                                                                                                                                  |
| `course_members` | Optional. A list of [`CourseMembersInput`](/reference/2024-06-01/input-objects/coursemembersinput) objects that defines Program membership for groups and users. See [table below](#the-course-members-object). |

Returns an [`updateCoursePayload`](/reference/2024-06-01/objects/updatecoursepayload) object.

### The Course Members Object

```
{
  "label": "John Doe",
  "value": "user-1" // 1 is the ID of the user
}
```

Please refer to the GraphQL definition of the input [here](/reference/2024-06-01/input-objects/coursemembersinput).

| Input   | Info                                                                                                                         |
| ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `label` | **Required**. An arbitrary label, usually user or group name.                                                                |
| `value` | **Required**. A prefixed string representing either a Client Group ID or User (Patient) ID. Examples: `group-1` or `user-2`. |

## Deleting a Program

Programs can be (soft) deleted by authorized providers and staff members via the `deleteCourse` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletecourseinput).

```
mutation deleteCourse($id: ID) {
  deleteCourse(input: { id: $id }) {
    course {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteCourse` mutation is called from an authenticated provider/staff account.

| Input | Info                                       |
| ----- | ------------------------------------------ |
| `id`  | **Required**. ID of the Program to delete. |

Returns a [`deleteCoursePayload`](/reference/2024-06-01/objects/deletecoursepayload) object.
