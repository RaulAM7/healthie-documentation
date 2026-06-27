---
title: UserNotificationsCount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/usernotificationscount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/usernotificationscount/index.md
---

Counts of different types of notifications for a user

## Fields

[`conversation_notification_count` ](#field-conversation-notification-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of unread conversation notifications

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the counter

[`unscheduled_lab_orders_count` ](#field-unscheduled-lab-orders-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of unscheduled lab orders

## Used By

[`Subscription.userUpdatedSubscription`](/reference/2026-01-01/objects/subscription)

[`createLabOrderPayload.currentUserNotificationsCount`](/reference/2026-01-01/objects/createlaborderpayload)

[`updateLabOrderPayload.currentUserNotificationsCount`](/reference/2026-01-01/objects/updatelaborderpayload)

## Definition

```
"""
Counts of different types of notifications for a user
"""
type UserNotificationsCount {
  """
  The number of unread conversation notifications
  """
  conversation_notification_count: Int


  """
  The unique identifier of the counter
  """
  id: ID


  """
  The number of unscheduled lab orders
  """
  unscheduled_lab_orders_count: Int
}
```
