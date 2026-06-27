---
title: receivedDirectMessage | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/receiveddirectmessage/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/receiveddirectmessage/index.md
---

Fetch received direct message via ID

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`ReceivedDirectMessage`](/reference/2026-01-01/objects/receiveddirectmessage)

## Example

```
query receivedDirectMessage($id: ID) {
  receivedDirectMessage(id: $id) {
    attachments_count
    cda_xml
    created_at
    direct_message_attachments
    has_cda
    id
    listed_recipient
    listed_sender
    message_body
    patient
    subject
  }
}
```
