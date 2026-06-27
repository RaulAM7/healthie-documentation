---
title: draft | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/draft/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/draft/index.md
---

draft by conversation\_membership id

## Arguments

[`conversation_membership_id` ](#argument-conversation-membership-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Draft`](/reference/2026-01-01/objects/draft)

## Example

```
query draft($conversation_membership_id: ID) {
  draft(conversation_membership_id: $conversation_membership_id) {
    content
    conversation_membership_id
    id
  }
}
```
