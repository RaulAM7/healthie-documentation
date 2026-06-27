---
title: PlaceOfService | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/placeofservice/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/placeofservice/index.md
---

Alternative ID numbers for a provider

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The code for the place of service

[`code_name` ](#field-code-name)· [`String` ](/reference/2026-01-01/scalars/string)· A combined name and code string, correctly formatted

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the place of service

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the place of service

## Used By

[`Location.place_of_service`](/reference/2026-01-01/objects/location)

[`PlaceOfServiceEdge.node`](/reference/2026-01-01/objects/placeofserviceedge)

[`PlaceOfServicePaginationConnection.nodes`](/reference/2026-01-01/objects/placeofservicepaginationconnection)

[`SuperBill.place_of_service`](/reference/2026-01-01/objects/superbill)

[`User.place_of_service`](/reference/2026-01-01/objects/user)

## Definition

```
"""
Alternative ID numbers for a provider
"""
type PlaceOfService {
  """
  The code for the place of service
  """
  code: String


  """
  A combined name and code string, correctly formatted
  """
  code_name: String


  """
  The unique identifier of the place of service
  """
  id: ID!


  """
  The name of the place of service
  """
  name: String
}
```
