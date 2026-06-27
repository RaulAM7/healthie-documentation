---
title: sendSpeakToTrainerNotification | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/sendspeaktotrainernotification/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/sendspeaktotrainernotification/index.md
---

deprecated Deprecated, do not use

Send the trainer an email that the client wants to speak to them

## Arguments

[`input` ](#argument-input)· [`SendSpeakToTrainerNotificationInput` ](/reference/2026-01-01/input-objects/sendspeaktotrainernotificationinput)· Parameters for SendSpeakToTrainerNotification

## Returns

[`SendSpeakToTrainerNotificationPayload`](/reference/2026-01-01/objects/sendspeaktotrainernotificationpayload)

## Example

```
mutation sendSpeakToTrainerNotification(
  $input: SendSpeakToTrainerNotificationInput
) {
  sendSpeakToTrainerNotification(input: $input) {
    messages
    success_string
  }
}
```
