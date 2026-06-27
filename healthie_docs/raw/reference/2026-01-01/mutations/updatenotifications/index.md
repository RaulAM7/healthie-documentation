---
title: updateNotifications | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotifications/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotifications/index.md
---

update multiple notifications at once

## Arguments

[`input` ](#argument-input)· [`bulkUpdateNotificationsInput` ](/reference/2026-01-01/input-objects/bulkupdatenotificationsinput)· Parameters for bulkUpdateNotifications

## Returns

[`bulkUpdateNotificationsPayload`](/reference/2026-01-01/objects/bulkupdatenotificationspayload)

## Example

```
mutation updateNotifications($input: bulkUpdateNotificationsInput) {
  updateNotifications(input: $input) {
    current_user
    messages
    notifications
  }
}
```
