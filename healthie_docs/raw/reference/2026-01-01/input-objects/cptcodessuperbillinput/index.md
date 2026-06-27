---
title: CptCodesSuperBillInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cptcodessuperbillinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cptcodessuperbillinput/index.md
---

Payload for a CPT code super bill

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the CPT code super bill will be destroyed

[`cpt_code_id` ](#field-cpt-code-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the CPT code

[`fee` ](#field-fee)· [`String` ](/reference/2026-01-01/scalars/string)· The fee

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the CPT code super bill

[`mod1` ](#field-mod1)· [`String` ](/reference/2026-01-01/scalars/string)· The first modifier

[`mod2` ](#field-mod2)· [`String` ](/reference/2026-01-01/scalars/string)· The second modifier

[`mod3` ](#field-mod3)· [`String` ](/reference/2026-01-01/scalars/string)· The third modifier

[`mod4` ](#field-mod4)· [`String` ](/reference/2026-01-01/scalars/string)· The fourth modifier

[`pointers` ](#field-pointers)· [`[String]` ](/reference/2026-01-01/scalars/string)· The list of pointers

[`service_date` ](#field-service-date)· [`String` ](/reference/2026-01-01/scalars/string)· The date of the service

[`units` ](#field-units)· [`String` ](/reference/2026-01-01/scalars/string)· The number of units

## Used By

[`createSuperBillInput.cpt_codes_super_bills`](/reference/2026-01-01/input-objects/createsuperbillinput)

[`updateSuperBillInput.cpt_codes_super_bills`](/reference/2026-01-01/input-objects/updatesuperbillinput)

## Definition

```
"""
Payload for a CPT code super bill
"""
input CptCodesSuperBillInput {
  """
  If true, the CPT code super bill will be destroyed
  """
  _destroy: Boolean


  """
  The ID of the CPT code
  """
  cpt_code_id: String


  """
  The fee
  """
  fee: String


  """
  The ID of the CPT code super bill
  """
  id: ID


  """
  The first modifier
  """
  mod1: String


  """
  The second modifier
  """
  mod2: String


  """
  The third modifier
  """
  mod3: String


  """
  The fourth modifier
  """
  mod4: String


  """
  The list of pointers
  """
  pointers: [String]


  """
  The date of the service
  """
  service_date: String


  """
  The number of units
  """
  units: String
}
```
