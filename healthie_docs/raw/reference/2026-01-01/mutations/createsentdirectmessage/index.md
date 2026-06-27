---
title: createSentDirectMessage | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsentdirectmessage/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsentdirectmessage/index.md
---

Create a sent direct message

## Arguments

[`input` ](#argument-input)· [`createSentDirectMessageInput` ](/reference/2026-01-01/input-objects/createsentdirectmessageinput)· Parameters for createSentDirectMessage

## Returns

[`createSentDirectMessagePayload`](/reference/2026-01-01/objects/createsentdirectmessagepayload)

## Example

```
mutation createSentDirectMessage($input: createSentDirectMessageInput) {
  createSentDirectMessage(input: $input) {
    messages
    sent_direct_message
  }
}
```
