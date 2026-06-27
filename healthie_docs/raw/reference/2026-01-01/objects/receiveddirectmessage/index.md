---
title: ReceivedDirectMessage | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receiveddirectmessage/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receiveddirectmessage/index.md
---

A Received Direct Message

## Fields

[`attachments_count` ](#field-attachments-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of attachments for the received direct message

[`cda_xml` ](#field-cda-xml)· [`String` ](/reference/2026-01-01/scalars/string)· The XML data contained in the attach CDA file

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The received date of the direct message

[`direct_message_attachments` ](#field-direct-message-attachments)· [`[DirectMessageAttachment!]` ](/reference/2026-01-01/objects/directmessageattachment)· Array of direct message attachments

[`has_cda` ](#field-has-cda)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the message has an attached CDA

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the fax

[`listed_recipient` ](#field-listed-recipient)· [`String` ](/reference/2026-01-01/scalars/string)· The listed recipient

[`listed_sender` ](#field-listed-sender)· [`String` ](/reference/2026-01-01/scalars/string)· The listed sender

[`message_body` ](#field-message-body)· [`String` ](/reference/2026-01-01/scalars/string)· The message body of the direct message

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· The patient associated with the direct message. Will be nil if the direct message is not associated

[`subject` ](#field-subject)· [`String` ](/reference/2026-01-01/scalars/string)· The subject

## Used By

[`Query.receivedDirectMessage`](/reference/2026-01-01/queries/receiveddirectmessage)

[`ReceivedDirectMessageEdge.node`](/reference/2026-01-01/objects/receiveddirectmessageedge)

[`ReceivedDirectMessagePaginationConnection.nodes`](/reference/2026-01-01/objects/receiveddirectmessagepaginationconnection)

[`updateReceivedDirectMessagePayload.received_direct_message`](/reference/2026-01-01/objects/updatereceiveddirectmessagepayload)

## Definition

```
"""
A Received Direct Message
"""
type ReceivedDirectMessage {
  """
  The number of attachments for the received direct message
  """
  attachments_count: Int


  """
  The XML data contained in the attach CDA file
  """
  cda_xml: String


  """
  The received date of the direct message
  """
  created_at: ISO8601DateTime


  """
  Array of direct message attachments
  """
  direct_message_attachments: [DirectMessageAttachment!]


  """
  When true, the message has an attached CDA
  """
  has_cda: Boolean


  """
  The unique identifier of the fax
  """
  id: ID!


  """
  The listed recipient
  """
  listed_recipient: String


  """
  The listed sender
  """
  listed_sender: String


  """
  The message body of the direct message
  """
  message_body: String


  """
  The patient associated with the direct message. Will be nil if the direct message is not associated
  """
  patient: User


  """
  The subject
  """
  subject: String
}
```
