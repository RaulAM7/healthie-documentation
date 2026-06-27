---
title: SignedStreamName | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/signedstreamname/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/signedstreamname/index.md
---

The type of offered signed stream names

## Used By

[`Query.signedStreamName`](/reference/2026-01-01/queries/signedstreamname)

## Definition

```
"""
The type of offered signed stream names
"""
enum SignedStreamName {
  """
  For new/updated notes in a conversation
  """
  NOTES


  """
  For a user's conversation membership updates
  """
  CONVERSATION_MEMBERSHIPS


  """
  For a user's notification count updates
  """
  USER_NOTIFICATIONS_COUNT
}
```
