---
title: SentNotificationRecord | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentnotificationrecord/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentnotificationrecord/index.md
---

A Sent Notification

## Fields

[`category` ](#field-category)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The enumerated values: \[:sms, :push, :email]

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time when the record was created

[`delivery_status` ](#field-delivery-status)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The enumerated values: \[:sent, :delivered, :bounced]

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the record

[`notification_description` ](#field-notification-description)· [`String` ](/reference/2026-01-01/scalars/string)· Description of notification context. (Ex: 'Follow-up Session on Nov 16 at 1:00 PM EST with Joe Smith')

[`notification_type` ](#field-notification-type)· [`String` ](/reference/2026-01-01/scalars/string)· Examples: 'appointment\_reminder', 'folder\_shared', 'reminder\_to\_work\_on\_a\_goal'

[`representation_type` ](#field-representation-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type categorizing notification\_type into subgroups. Accepted values: \[appointments, billing, chat\_messages, accounting, documents, forms, goals, journals, packages, programs]

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user this notification was sent to

## Used By

[`Query.sentNotificationRecord`](/reference/2026-01-01/queries/sentnotificationrecord)

[`SentNotificationRecordEdge.node`](/reference/2026-01-01/objects/sentnotificationrecordedge)

[`SentNotificationRecordPaginationConnection.nodes`](/reference/2026-01-01/objects/sentnotificationrecordpaginationconnection)

## Definition

```
"""
A Sent Notification
"""
type SentNotificationRecord {
  """
  The enumerated values: [:sms, :push, :email]
  """
  category: String!


  """
  The time when the record was created
  """
  created_at: ISO8601DateTime!


  """
  The enumerated values: [:sent, :delivered, :bounced]
  """
  delivery_status: String!


  """
  The unique identifier of the record
  """
  id: ID!


  """
  Description of notification context. (Ex: 'Follow-up Session on Nov 16 at 1:00 PM EST with Joe Smith')
  """
  notification_description: String


  """
  Examples: 'appointment_reminder', 'folder_shared', 'reminder_to_work_on_a_goal'
  """
  notification_type: String


  """
  The type categorizing notification_type into subgroups. Accepted values: [appointments, billing, chat_messages, accounting, documents, forms, goals, journals, packages, programs]
  """
  representation_type: String


  """
  The ID of the user this notification was sent to
  """
  user_id: ID
}
```
