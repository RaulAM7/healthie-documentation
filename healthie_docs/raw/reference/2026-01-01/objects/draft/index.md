---
title: Draft | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/draft/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/draft/index.md
---

draft of a conversation note

## Fields

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· content of draft

[`conversation_membership_id` ](#field-conversation-membership-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of linked conversation membership

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the draft

## Used By

[`Query.draft`](/reference/2026-01-01/queries/draft)

[`createDraftPayload.draft`](/reference/2026-01-01/objects/createdraftpayload)

[`removeDraftPayload.draft`](/reference/2026-01-01/objects/removedraftpayload)

## Definition

```
"""
draft of a conversation note
"""
type Draft {
  """
  content of draft
  """
  content: String


  """
  id of linked conversation membership
  """
  conversation_membership_id: ID


  """
  The unique identifier of the draft
  """
  id: ID!
}
```
