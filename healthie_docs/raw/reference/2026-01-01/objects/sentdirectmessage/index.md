---
title: SentDirectMessage | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentdirectmessage/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentdirectmessage/index.md
---

A Sent Direct Message

## Fields

[`attachments` ](#field-attachments)· [`[Document!]` ](/reference/2026-01-01/objects/document)· Array of attachments

[`attachments_count` ](#field-attachments-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of attachments for the sent direct message

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The sent date of the direct message

[`has_binary_attachment` ](#field-has-binary-attachment)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the message has an attached binary document

[`has_cda` ](#field-has-cda)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the message has an attached CDA

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the fax

[`message_body` ](#field-message-body)· [`String` ](/reference/2026-01-01/scalars/string)· The body of the direct message

[`outbound_recipient` ](#field-outbound-recipient)· [`String` ](/reference/2026-01-01/scalars/string)· The outbound recipient

[`patient_id` ](#field-patient-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the related patient

[`sender_id` ](#field-sender-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the related sender

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status

[`subject` ](#field-subject)· [`String` ](/reference/2026-01-01/scalars/string)· The subject of the direct message

## Used By

[`Query.sentDirectMessage`](/reference/2026-01-01/queries/sentdirectmessage)

[`SentDirectMessageEdge.node`](/reference/2026-01-01/objects/sentdirectmessageedge)

[`SentDirectMessagePaginationConnection.nodes`](/reference/2026-01-01/objects/sentdirectmessagepaginationconnection)

[`createSentDirectMessagePayload.sent_direct_message`](/reference/2026-01-01/objects/createsentdirectmessagepayload)

## Definition

```
"""
A Sent Direct Message
"""
type SentDirectMessage {
  """
  Array of attachments
  """
  attachments: [Document!]


  """
  The number of attachments for the sent direct message
  """
  attachments_count: Int


  """
  The sent date of the direct message
  """
  created_at: ISO8601DateTime


  """
  When true, the message has an attached binary document
  """
  has_binary_attachment: Boolean


  """
  When true, the message has an attached CDA
  """
  has_cda: Boolean


  """
  The unique identifier of the fax
  """
  id: ID!


  """
  The body of the direct message
  """
  message_body: String


  """
  The outbound recipient
  """
  outbound_recipient: String


  """
  ID of the related patient
  """
  patient_id: String


  """
  ID of the related sender
  """
  sender_id: String


  """
  The status
  """
  status: String


  """
  The subject of the direct message
  """
  subject: String
}
```
