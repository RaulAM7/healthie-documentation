---
title: CptCodesCms1500 | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodescms1500/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodescms1500/index.md
---

cpt codes cms 1500s join table

## Fields

[`cms1500_id` ](#field-cms1500-id)· [`ID` ](/reference/2026-01-01/scalars/id)· cms 1500 id

[`cpt_code` ](#field-cpt-code)· [`CptCode` ](/reference/2026-01-01/objects/cptcode)· The CPT code itself

[`cpt_code_id` ](#field-cpt-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· icd code id

deprecated

Use cpt\_code instead

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date created

[`epsdt` ](#field-epsdt)· [`String` ](/reference/2026-01-01/scalars/string)· The Early and Periodic Screening, Diagnostic and Treatment

[`family_planning_service` ](#field-family-planning-service)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Self descriptive

[`fee` ](#field-fee)· [`String` ](/reference/2026-01-01/scalars/string)· fee

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the cms 1500

[`mod1` ](#field-mod1)· [`String` ](/reference/2026-01-01/scalars/string)· First Modification

[`mod2` ](#field-mod2)· [`String` ](/reference/2026-01-01/scalars/string)· Second Modification

[`mod3` ](#field-mod3)· [`String` ](/reference/2026-01-01/scalars/string)· Third Modification

[`mod4` ](#field-mod4)· [`String` ](/reference/2026-01-01/scalars/string)· Fourth Modification

[`pointers` ](#field-pointers)· [`[String]` ](/reference/2026-01-01/scalars/string)· Diagnostic pointers. These are used to connect Diagnosis(ICD) with appropriate Billing Item(CPT) in CMS1500 form

[`service_date` ](#field-service-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· service date

[`service_end_date` ](#field-service-end-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The end date of service (if the line item covers a date range). Can be nil if service was delivered on one day

[`units` ](#field-units)· [`Int` ](/reference/2026-01-01/scalars/int)· units

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date updated

## Used By

[`Cms1500.cpt_codes_cms1500s`](/reference/2026-01-01/objects/cms1500)

[`Cms1500.estimated_cpt_fees_for_user`](/reference/2026-01-01/objects/cms1500)

## Definition

```
"""
cpt codes cms 1500s join table
"""
type CptCodesCms1500 {
  """
  cms 1500 id
  """
  cms1500_id: ID


  """
  The CPT code itself
  """
  cpt_code: CptCode


  """
  icd code id
  """
  cpt_code_id: ID @deprecated(reason: "Use cpt_code instead")


  """
  date created
  """
  created_at: ISO8601DateTime


  """
  The Early and Periodic Screening, Diagnostic and Treatment
  """
  epsdt: String


  """
  Self descriptive
  """
  family_planning_service: Boolean


  """
  fee
  """
  fee: String


  """
  The unique identifier of the cms 1500
  """
  id: ID


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
  Diagnostic pointers. These are used to connect Diagnosis(ICD) with appropriate Billing Item(CPT) in CMS1500 form
  """
  pointers: [String]


  """
  service date
  """
  service_date: ISO8601Date


  """
  The end date of service (if the line item covers a date range). Can be nil if service was delivered on one day
  """
  service_end_date: ISO8601Date


  """
  units
  """
  units: Int


  """
  date updated
  """
  updated_at: ISO8601DateTime
}
```
