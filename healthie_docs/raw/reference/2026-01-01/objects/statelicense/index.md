---
title: StateLicense | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/statelicense/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/statelicense/index.md
---

A state license object

## Fields

[`full_state_name` ](#field-full-state-name)· [`String` ](/reference/2026-01-01/scalars/string)· The full name of the state

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the state license

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The abbreviation of the state

## Used By

[`StateLicenseEdge.node`](/reference/2026-01-01/objects/statelicenseedge)

[`StateLicensePaginationConnection.nodes`](/reference/2026-01-01/objects/statelicensepaginationconnection)

[`User.state_licenses`](/reference/2026-01-01/objects/user)

## Definition

```
"""
A state license object
"""
type StateLicense {
  """
  The full name of the state
  """
  full_state_name: String


  """
  The unique identifier of the state license
  """
  id: ID!


  """
  The abbreviation of the state
  """
  state: String
}
```
