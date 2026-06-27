---
title: deleteConversationMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteconversationmembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteconversationmembership/index.md
---

Destroy a Conversation Membership

## Arguments

[`input` ](#argument-input)· [`deleteConversationMembershipInput` ](/reference/2026-01-01/input-objects/deleteconversationmembershipinput)· Parameters for deleteConversationMembership

## Returns

[`deleteConversationMembershipPayload`](/reference/2026-01-01/objects/deleteconversationmembershippayload)

## Example

```
mutation deleteConversationMembership(
  $input: deleteConversationMembershipInput
) {
  deleteConversationMembership(input: $input) {
    conversationMembership
    messages
  }
}
```
