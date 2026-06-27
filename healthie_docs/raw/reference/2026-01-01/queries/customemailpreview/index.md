---
title: customEmailPreview | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/customemailpreview/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/customemailpreview/index.md
---

A HTML string containing mailer template for certain email type

## Arguments

[`course_id` ](#argument-course-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`email_body_only` ](#argument-email-body-only)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`email_type` ](#argument-email-type)· [`String`](/reference/2026-01-01/scalars/string)

[`find_record` ](#argument-find-record)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`greeting` ](#argument-greeting)· [`String`](/reference/2026-01-01/scalars/string)

[`id` ](#argument-id)· [`String`](/reference/2026-01-01/scalars/string)

[`message_body` ](#argument-message-body)· [`String`](/reference/2026-01-01/scalars/string)

[`preview_email_type` ](#argument-preview-email-type)· [`String`](/reference/2026-01-01/scalars/string)

[`reactivation_wait_days` ](#argument-reactivation-wait-days)· [`String`](/reference/2026-01-01/scalars/string)

[`subject` ](#argument-subject)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query customEmailPreview(
  $course_id: ID
  $email_body_only: Boolean
  $email_type: String
  $find_record: Boolean
  $greeting: String
  $id: String
  $message_body: String
  $preview_email_type: String
  $reactivation_wait_days: String
  $subject: String
) {
  customEmailPreview(
    course_id: $course_id
    email_body_only: $email_body_only
    email_type: $email_type
    find_record: $find_record
    greeting: $greeting
    id: $id
    message_body: $message_body
    preview_email_type: $preview_email_type
    reactivation_wait_days: $reactivation_wait_days
    subject: $subject
  )
}
```
