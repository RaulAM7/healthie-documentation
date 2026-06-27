---
title: CptCodesCms1500Input | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cptcodescms1500input/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cptcodescms1500input/index.md
---

Payload for a CPT code on a CMS 1500 form

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, this record will be marked for destruction

[`cpt_code_id` ](#field-cpt-code-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the CPT code

[`epsdt` ](#field-epsdt)· [`String` ](/reference/2026-01-01/scalars/string)· The EPSDT code

[`family_planning_service` ](#field-family-planning-service)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The family planning service

[`fee` ](#field-fee)· [`String` ](/reference/2026-01-01/scalars/string)· The fee for the service

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the join record

[`mod1` ](#field-mod1)· [`String` ](/reference/2026-01-01/scalars/string)· The first modifier

[`mod2` ](#field-mod2)· [`String` ](/reference/2026-01-01/scalars/string)· The second modifier

[`mod3` ](#field-mod3)· [`String` ](/reference/2026-01-01/scalars/string)· The third modifier

[`mod4` ](#field-mod4)· [`String` ](/reference/2026-01-01/scalars/string)· The fourth modifier

[`pointers` ](#field-pointers)· [`[String]` ](/reference/2026-01-01/scalars/string)· The list of pointers to the service line

[`service_date` ](#field-service-date)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`service_end_date` ](#field-service-end-date)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`units` ](#field-units)· [`String` ](/reference/2026-01-01/scalars/string)· The units for the service

## Used By

[`createCms1500Input.cpt_codes_cms1500s`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.cpt_codes_cms1500s`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for a CPT code on a CMS 1500 form
"""
input CptCodesCms1500Input {
  """
  If true, this record will be marked for destruction
  """
  _destroy: Boolean


  """
  The ID of the CPT code
  """
  cpt_code_id: String


  """
  The EPSDT code
  """
  epsdt: String


  """
  The family planning service
  """
  family_planning_service: Boolean


  """
  The fee for the service
  """
  fee: String


  """
  The ID of the join record
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
  The list of pointers to the service line
  """
  pointers: [String]
  service_date: ISO8601DateTime
  service_end_date: ISO8601DateTime


  """
  The units for the service
  """
  units: String
}
```
