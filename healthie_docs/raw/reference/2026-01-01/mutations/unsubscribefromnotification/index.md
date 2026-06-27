---
title: unsubscribeFromNotification | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/unsubscribefromnotification/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/unsubscribefromnotification/index.md
---

Update a Notification Setting to unsubscribe from a specific notification type

## Arguments

[`input` ](#argument-input)· [`unsubscribeFromNotificationInput` ](/reference/2026-01-01/input-objects/unsubscribefromnotificationinput)· Parameters for unsubscribeFromNotification

## Returns

[`unsubscribeFromNotificationPayload`](/reference/2026-01-01/objects/unsubscribefromnotificationpayload)

## Example

```
mutation unsubscribeFromNotification($input: unsubscribeFromNotificationInput) {
  unsubscribeFromNotification(input: $input) {
    messages
    notificationSettingUpdated
  }
}
```
