---
title: createNotificationContact | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createnotificationcontact/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createnotificationcontact/index.md
---

create a Notification Contact

## Arguments

[`input` ](#argument-input)· [`createNotificationContactInput` ](/reference/2026-01-01/input-objects/createnotificationcontactinput)· Parameters for createNotificationContact

## Returns

[`createNotificationContactPayload`](/reference/2026-01-01/objects/createnotificationcontactpayload)

## Example

```
mutation createNotificationContact($input: createNotificationContactInput) {
  createNotificationContact(input: $input) {
    messages
    notificationContact
  }
}
```
