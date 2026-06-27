---
title: Era | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/era/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/era/index.md
---

An Electronic Remittance Advice (ERA) type

## Fields

[`ach_check_number` ](#field-ach-check-number)· [`String` ](/reference/2026-01-01/scalars/string)· The ACH or check number for the payment

[`era_service_lines` ](#field-era-service-lines)· [`EraServiceLineConnection!` ](/reference/2026-01-01/objects/eraservicelineconnection)· required · The service lines for the claim

[`external_era_id` ](#field-external-era-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The ID of the ERA in the remote system

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the ERA

[`insurance_status` ](#field-insurance-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the insurance

[`member_id` ](#field-member-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the member

[`member_name` ](#field-member-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the member

[`paid_date` ](#field-paid-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The date the payment was made

[`payer_id` ](#field-payer-id)· [`String` ](/reference/2026-01-01/scalars/string)· The contact information for the payer

[`payer_name` ](#field-payer-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the payer

[`pcn` ](#field-pcn)· [`String` ](/reference/2026-01-01/scalars/string)· The PCN (Processor Control Number)

## Used By

[`EraConnection.nodes`](/reference/2026-01-01/objects/eraconnection)

[`EraEdge.node`](/reference/2026-01-01/objects/eraedge)

## Definition

```
"""
An Electronic Remittance Advice (ERA) type
"""
type Era {
  """
  The ACH or check number for the payment
  """
  ach_check_number: String


  """
  The service lines for the claim
  """
  era_service_lines(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): EraServiceLineConnection!


  """
  The ID of the ERA in the remote system
  """
  external_era_id: String!


  """
  The unique identifier of the ERA
  """
  id: ID!


  """
  The status of the insurance
  """
  insurance_status: String


  """
  The ID of the member
  """
  member_id: String


  """
  The name of the member
  """
  member_name: String


  """
  The date the payment was made
  """
  paid_date: ISO8601Date


  """
  The contact information for the payer
  """
  payer_id: String


  """
  The name of the payer
  """
  payer_name: String


  """
  The PCN (Processor Control Number)
  """
  pcn: String
}
```
