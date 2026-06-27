---
title: deleteNotificationContact | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletenotificationcontact/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletenotificationcontact/index.md
---

delete a Notification Contact

## Arguments

[`input` ](#argument-input)· [`deleteNotificationContactInput` ](/reference/2026-01-01/input-objects/deletenotificationcontactinput)· Parameters for deleteNotificationContact

## Returns

[`deleteNotificationContactPayload`](/reference/2026-01-01/objects/deletenotificationcontactpayload)

## Example

```
mutation deleteNotificationContact($input: deleteNotificationContactInput) {
  deleteNotificationContact(input: $input) {
    messages
    notificationContact
  }
}
```
