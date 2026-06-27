---
title: updateNotificationContact | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotificationcontact/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotificationcontact/index.md
---

Update a Notification Contact

## Arguments

[`input` ](#argument-input)· [`updateNotificationContactInput` ](/reference/2026-01-01/input-objects/updatenotificationcontactinput)· Parameters for updateNotificationContact

## Returns

[`updateNotificationContactPayload`](/reference/2026-01-01/objects/updatenotificationcontactpayload)

## Example

```
mutation updateNotificationContact($input: updateNotificationContactInput) {
  updateNotificationContact(input: $input) {
    messages
    notificationContact
  }
}
```
