---
title: updateNotification | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotification/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotification/index.md
---

update a notification

## Arguments

[`input` ](#argument-input)· [`updateNotificationInput` ](/reference/2026-01-01/input-objects/updatenotificationinput)· Parameters for updateNotification

## Returns

[`updateNotificationPayload`](/reference/2026-01-01/objects/updatenotificationpayload)

## Example

```
mutation updateNotification($input: updateNotificationInput) {
  updateNotification(input: $input) {
    currentUser
    messages
    notification
  }
}
```
