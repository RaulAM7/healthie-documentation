---
title: createConversation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createconversation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createconversation/index.md
---

Create a conversation. Maximum of 256 members allowed per conversation.

## Arguments

[`input` ](#argument-input)· [`createConversationInput` ](/reference/2026-01-01/input-objects/createconversationinput)· Parameters for createConversation

## Returns

[`createConversationPayload`](/reference/2026-01-01/objects/createconversationpayload)

## Example

```
mutation createConversation($input: createConversationInput) {
  createConversation(input: $input) {
    conversation
    messages
  }
}
```
