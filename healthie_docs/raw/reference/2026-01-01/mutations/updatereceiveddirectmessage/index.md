---
title: updateReceivedDirectMessage | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatereceiveddirectmessage/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatereceiveddirectmessage/index.md
---

Update a Received Direct Message

## Arguments

[`input` ](#argument-input)· [`updateReceivedDirectMessageInput` ](/reference/2026-01-01/input-objects/updatereceiveddirectmessageinput)· Parameters for updateReceivedDirectMessage

## Returns

[`updateReceivedDirectMessagePayload`](/reference/2026-01-01/objects/updatereceiveddirectmessagepayload)

## Example

```
mutation updateReceivedDirectMessage($input: updateReceivedDirectMessageInput) {
  updateReceivedDirectMessage(input: $input) {
    messages
    received_direct_message
  }
}
```
