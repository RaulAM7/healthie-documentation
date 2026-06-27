---
title: CptCodesSuperBill | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodessuperbill/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodessuperbill/index.md
---

cpt codes super bills join table

## Fields

[`billing_item_id` ](#field-billing-item-id)· [`ID` ](/reference/2026-01-01/scalars/id)· billing item id

[`cpt_code` ](#field-cpt-code)· [`CptCode` ](/reference/2026-01-01/objects/cptcode)· cpt code

[`cpt_code_id` ](#field-cpt-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· cpt code id

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date created

[`fee` ](#field-fee)· [`String` ](/reference/2026-01-01/scalars/string)· fee

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the join

[`mod1` ](#field-mod1)· [`String` ](/reference/2026-01-01/scalars/string)· First Modification

[`mod2` ](#field-mod2)· [`String` ](/reference/2026-01-01/scalars/string)· Second Modification

[`mod3` ](#field-mod3)· [`String` ](/reference/2026-01-01/scalars/string)· Third Modification

[`mod4` ](#field-mod4)· [`String` ](/reference/2026-01-01/scalars/string)· Fourth Modification

[`pointers` ](#field-pointers)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Pointers

[`service_date` ](#field-service-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· service date

[`super_bill_id` ](#field-super-bill-id)· [`ID` ](/reference/2026-01-01/scalars/id)· super bill id

[`units` ](#field-units)· [`Int` ](/reference/2026-01-01/scalars/int)· units

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date updated

## Used By

[`Query.startingSuperBillCptCodes`](/reference/2026-01-01/queries/startingsuperbillcptcodes)

[`SuperBill.cpt_codes_super_bills`](/reference/2026-01-01/objects/superbill)

## Definition

```
"""
cpt codes super bills join table
"""
type CptCodesSuperBill {
  """
  billing item id
  """
  billing_item_id: ID


  """
  cpt code
  """
  cpt_code: CptCode


  """
  cpt code id
  """
  cpt_code_id: ID


  """
  date created
  """
  created_at: ISO8601DateTime!


  """
  fee
  """
  fee: String


  """
  The unique identifier of the join
  """
  id: ID!


  """
  First Modification
  """
  mod1: String


  """
  Second Modification
  """
  mod2: String


  """
  Third Modification
  """
  mod3: String


  """
  Fourth Modification
  """
  mod4: String


  """
  Pointers
  """
  pointers: [String!]


  """
  service date
  """
  service_date: ISO8601Date


  """
  super bill id
  """
  super_bill_id: ID


  """
  units
  """
  units: Int


  """
  date updated
  """
  updated_at: ISO8601DateTime!
}
```
