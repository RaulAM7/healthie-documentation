---
title: ReceivedFax | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receivedfax/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receivedfax/index.md
---

A Received Fax

## Fields

[`archived` ](#field-archived)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The archived status of the fax

[`comments` ](#field-comments)· [`String` ](/reference/2026-01-01/scalars/string)· Any user added comments on the fax

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The received date of the fax

[`from_number` ](#field-from-number)· [`String` ](/reference/2026-01-01/scalars/string)· The number of the sender of the fax

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the fax

[`referring_provider_name` ](#field-referring-provider-name)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the referral provider name if fax number is found

[`viewed_by_current_user` ](#field-viewed-by-current-user)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the received fax has been viewed by the current user

## Used By

[`Query.receivedFax`](/reference/2026-01-01/queries/receivedfax)

[`ReceivedFaxEdge.node`](/reference/2026-01-01/objects/receivedfaxedge)

[`ReceivedFaxPaginationConnection.nodes`](/reference/2026-01-01/objects/receivedfaxpaginationconnection)

[`deleteReceivedFaxPayload.receivedFax`](/reference/2026-01-01/objects/deletereceivedfaxpayload)

[`updateReceivedFaxPayload.receivedFax`](/reference/2026-01-01/objects/updatereceivedfaxpayload)

## Definition

```
"""
A Received Fax
"""
type ReceivedFax {
  """
  The archived status of the fax
  """
  archived: Boolean!


  """
  Any user added comments on the fax
  """
  comments: String


  """
  The received date of the fax
  """
  created_at: ISO8601DateTime!


  """
  The number of the sender of the fax
  """
  from_number: String


  """
  The unique identifier of the fax
  """
  id: ID!


  """
  Returns the referral provider name if fax number is found
  """
  referring_provider_name: String


  """
  Whether the received fax has been viewed by the current user
  """
  viewed_by_current_user: Boolean
}
```
