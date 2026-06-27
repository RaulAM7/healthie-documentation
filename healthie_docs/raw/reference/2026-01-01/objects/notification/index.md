---
title: Notification | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/notification/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/notification/index.md
---

A notification

## Fields

[`associated_entry` ](#field-associated-entry)· [`Entry` ](/reference/2026-01-01/objects/entry)· returns the associated entry if type is EntryNotification, otherwise, nil

[`associated_object` ](#field-associated-object)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the object associated with the notification

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The creation time of the notification

[`creator_user_name` ](#field-creator-user-name)· [`String` ](/reference/2026-01-01/scalars/string)· creator name of this notification

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the notification

[`link` ](#field-link)· [`String` ](/reference/2026-01-01/scalars/string)· The link that the notification goes to

[`link_string` ](#field-link-string)· [`String` ](/reference/2026-01-01/scalars/string)· The full link that the notification goes to

[`message` ](#field-message)· [`String` ](/reference/2026-01-01/scalars/string)· The message body of the notification

[`other_party` ](#field-other-party)· [`User` ](/reference/2026-01-01/objects/user)· recipient of this notification

[`other_party_id` ](#field-other-party-id)· [`String` ](/reference/2026-01-01/scalars/string)· The recipient of the notification

[`read` ](#field-read)· [`String` ](/reference/2026-01-01/scalars/string)· This turns to true if the user clicks on the notification

[`seen` ](#field-seen)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · This turns to true if the user loads the notification

[`type` ](#field-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of notification

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· creator of this notification

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The creator of the notification

## Used By

[`NotificationEdge.node`](/reference/2026-01-01/objects/notificationedge)

[`NotificationPaginationConnection.nodes`](/reference/2026-01-01/objects/notificationpaginationconnection)

[`bulkUpdateNotificationsPayload.notifications`](/reference/2026-01-01/objects/bulkupdatenotificationspayload)

[`updateNotificationPayload.notification`](/reference/2026-01-01/objects/updatenotificationpayload)

## Definition

```
"""
A notification
"""
type Notification {
  """
  returns the associated entry if type is EntryNotification, otherwise, nil
  """
  associated_entry: Entry


  """
  The id of the object associated with the notification
  """
  associated_object: String


  """
  The creation time of the notification
  """
  created_at: ISO8601DateTime!


  """
  creator name of this notification
  """
  creator_user_name: String


  """
  The unique identifier of the notification
  """
  id: ID!


  """
  The link that the notification goes to
  """
  link: String


  """
  The full link that the notification goes to
  """
  link_string: String


  """
  The message body of the notification
  """
  message: String


  """
  recipient of this notification
  """
  other_party: User


  """
  The recipient of the notification
  """
  other_party_id: String


  """
  This turns to true if the user clicks on the notification
  """
  read: String


  """
  This turns to true if the user loads the notification
  """
  seen: Boolean!


  """
  The type of notification
  """
  type: String


  """
  creator of this notification
  """
  user: User


  """
  The creator of the notification
  """
  user_id: String
}
```
