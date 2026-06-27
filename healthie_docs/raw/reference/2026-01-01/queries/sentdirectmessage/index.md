---
title: sentDirectMessage | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sentdirectmessage/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sentdirectmessage/index.md
---

Fetch sent direct message via ID

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`SentDirectMessage`](/reference/2026-01-01/objects/sentdirectmessage)

## Example

```
query sentDirectMessage($id: ID) {
  sentDirectMessage(id: $id) {
    attachments
    attachments_count
    created_at
    has_binary_attachment
    has_cda
    id
    message_body
    outbound_recipient
    patient_id
    sender_id
    status
    subject
  }
}
```
