---
title: FaxLineRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/faxlinerequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/faxlinerequest/index.md
---

An object containing info about the user' s fax line requests

## Fields

[`area_code` ](#field-area-code)· [`String` ](/reference/2026-01-01/scalars/string)· The area\_code

[`bill` ](#field-bill)· [`String` ](/reference/2026-01-01/scalars/string)· The file type of the bill

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time that the fax line request was created

[`loa` ](#field-loa)· [`String` ](/reference/2026-01-01/scalars/string)· The file type of the loa

[`request_type` ](#field-request-type)· [`String` ](/reference/2026-01-01/scalars/string)· The request type

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state

## Used By

[`User.fax_line_request`](/reference/2026-01-01/objects/user)

[`createFaxLineRequestPayload.faxLineRequest`](/reference/2026-01-01/objects/createfaxlinerequestpayload)

## Definition

```
"""
An object containing info about the user' s fax line requests
"""
type FaxLineRequest {
  """
  The area_code
  """
  area_code: String


  """
  The file type of the bill
  """
  bill: String


  """
  The city
  """
  city: String


  """
  The date and time that the fax line request was created
  """
  created_at: ISO8601DateTime!


  """
  The file type of the loa
  """
  loa: String


  """
  The request type
  """
  request_type: String


  """
  The state
  """
  state: String
}
```
