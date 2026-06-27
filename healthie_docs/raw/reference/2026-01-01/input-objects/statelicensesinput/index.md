---
title: StateLicensesInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/statelicensesinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/statelicensesinput/index.md
---

Payload for a state license

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the state license will be destroyed

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the state license

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The code of the state

## Used By

[`updateOrganizationMemberInput.state_licenses`](/reference/2026-01-01/input-objects/updateorganizationmemberinput)

## Definition

```
"""
Payload for a state license
"""
input StateLicensesInput {
  """
  If true, the state license will be destroyed
  """
  _destroy: Boolean


  """
  The ID of the state license
  """
  id: ID


  """
  The code of the state
  """
  state: String
}
```
