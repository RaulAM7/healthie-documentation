---
title: NotificationContactInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/notificationcontactinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/notificationcontactinput/index.md
---

Payload for a notification contact

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the notification contact will be deleted

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· The email of the notification contact

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the notification contact

## Used By

[`updateClientInput.notification_contacts`](/reference/2026-01-01/input-objects/updateclientinput)

## Definition

```
"""
Payload for a notification contact
"""
input NotificationContactInput {
  """
  If true, the notification contact will be deleted
  """
  _destroy: Boolean


  """
  The email of the notification contact
  """
  email: String


  """
  The ID of the notification contact
  """
  id: ID
}
```
