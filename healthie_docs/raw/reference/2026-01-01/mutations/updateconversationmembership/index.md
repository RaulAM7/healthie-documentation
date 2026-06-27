---
title: updateConversationMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateconversationmembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateconversationmembership/index.md
---

Update a ConversationMembership and return ConversationMembership

## Arguments

[`input` ](#argument-input)· [`updateConversationMembershipInput` ](/reference/2026-01-01/input-objects/updateconversationmembershipinput)· Parameters for updateConversationMembership

## Returns

[`updateConversationMembershipPayload`](/reference/2026-01-01/objects/updateconversationmembershippayload)

## Example

```
mutation updateConversationMembership(
  $input: updateConversationMembershipInput
) {
  updateConversationMembership(input: $input) {
    conversation_membership
    messages
  }
}
```
