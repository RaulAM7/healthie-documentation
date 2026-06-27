---
title: updateConversation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateconversation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateconversation/index.md
---

Update a conversation and return the conversation. Maximum of 256 members allowed per conversation.

## Arguments

[`input` ](#argument-input)· [`updateConversationInput` ](/reference/2026-01-01/input-objects/updateconversationinput)· Parameters for updateConversation

## Returns

[`updateConversationPayload`](/reference/2026-01-01/objects/updateconversationpayload)

## Example

```
mutation updateConversation($input: updateConversationInput) {
  updateConversation(input: $input) {
    conversation
    messages
  }
}
```
