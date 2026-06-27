---
title: signedStreamName | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/signedstreamname/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/signedstreamname/index.md
---

Get the signed stream name for a given stream name

## Arguments

[`conversation_id` ](#argument-conversation-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the conversation to get the signed stream name for

[`type` ](#argument-type)· [`SignedStreamName!` ](/reference/2026-01-01/enums/signedstreamname)· required · The type of stream to get the signed stream name for

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query signedStreamName($conversation_id: ID, $type: SignedStreamName!) {
  signedStreamName(conversation_id: $conversation_id, type: $type)
}
```
