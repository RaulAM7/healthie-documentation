---
title: updateNotificationSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotificationsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotificationsetting/index.md
---

Update a Notification Setting and return Notification Setting

## Arguments

[`input` ](#argument-input)· [`updateNotificationSettingInput` ](/reference/2026-01-01/input-objects/updatenotificationsettinginput)· Parameters for updateNotificationSetting

## Returns

[`updateNotificationSettingPayload`](/reference/2026-01-01/objects/updatenotificationsettingpayload)

## Example

```
mutation updateNotificationSetting($input: updateNotificationSettingInput) {
  updateNotificationSetting(input: $input) {
    messages
    notificationSetting
  }
}
```
