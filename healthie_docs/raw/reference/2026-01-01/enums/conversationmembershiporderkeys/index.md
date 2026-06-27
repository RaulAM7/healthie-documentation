---
title: ConversationMembershipOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/conversationmembershiporderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/conversationmembershiporderkeys/index.md
---

Conversation Membership sorting enum

## Used By

[`Query.conversationMemberships`](/reference/2026-01-01/queries/conversationmemberships)

## Definition

```
"""
Conversation Membership sorting enum
"""
enum ConversationMembershipOrderKeys {
  CREATED_AT_ASC
  CREATED_AT_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC
  CONVERSATION_CREATED_AT_ASC
  CONVERSATION_CREATED_AT_DESC
  CONVERSATION_UPDATED_AT_ASC
  CONVERSATION_UPDATED_AT_DESC
}
```
