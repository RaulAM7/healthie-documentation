---
title: SentFax | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentfax/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentfax/index.md
---

A Sent Fax

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The creation date of the fax

[`destination_number` ](#field-destination-number)· [`String` ](/reference/2026-01-01/scalars/string)· Where the fax was sent

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the fax

[`parsed_form_answer_group_ids` ](#field-parsed-form-answer-group-ids)· [`[ID!]` ](/reference/2026-01-01/scalars/id)· The ids of the chart notes sent with the fax

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· The patient that the fax is in regards to

[`resendable` ](#field-resendable)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· False if no document ids or form answer group ids (fax existed before the addition of document ids column)

[`sender` ](#field-sender)· [`User` ](/reference/2026-01-01/objects/user)· The sender of the fax

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the fax

[`status_display_string` ](#field-status-display-string)· [`String` ](/reference/2026-01-01/scalars/string)· The display string of the fax status

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The updated date of the sent fax

## Used By

[`Query.sentFax`](/reference/2026-01-01/queries/sentfax)

[`SentFaxEdge.node`](/reference/2026-01-01/objects/sentfaxedge)

[`SentFaxPaginationConnection.nodes`](/reference/2026-01-01/objects/sentfaxpaginationconnection)

[`createSentFaxPayload.sent_fax`](/reference/2026-01-01/objects/createsentfaxpayload)

[`resendSentFaxPayload.sent_fax`](/reference/2026-01-01/objects/resendsentfaxpayload)

## Definition

```
"""
A Sent Fax
"""
type SentFax {
  """
  The creation date of the fax
  """
  created_at: ISO8601DateTime!


  """
  Where the fax was sent
  """
  destination_number: String


  """
  The unique identifier of the fax
  """
  id: ID!


  """
  The ids of the chart notes sent with the fax
  """
  parsed_form_answer_group_ids: [ID!]


  """
  The patient that the fax is in regards to
  """
  patient: User


  """
  False if no document ids or form answer group ids (fax existed before the addition of document ids column)
  """
  resendable: Boolean


  """
  The sender of the fax
  """
  sender: User


  """
  The status of the fax
  """
  status: String


  """
  The display string of the fax status
  """
  status_display_string: String


  """
  The updated date of the sent fax
  """
  updated_at: ISO8601DateTime
}
```
