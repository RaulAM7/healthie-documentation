---
title: ClientSource | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/clientsource/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/clientsource/index.md
---

Info about how a client was acquire

## Fields

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the source

[`readable_source` ](#field-readable-source)· [`String` ](/reference/2026-01-01/scalars/string)· Get readable source based on ref\_type

[`ref_source` ](#field-ref-source)· [`String` ](/reference/2026-01-01/scalars/string)· The source of how a client was acquire: contain ID or a Other string

[`ref_source_other` ](#field-ref-source-other)· [`String` ](/reference/2026-01-01/scalars/string)· If ref\_source eq 'Other', than it may contain custom string or NULL

[`ref_type` ](#field-ref-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the source of how a client was acquire

[`related_insurance` ](#field-related-insurance)· [`InsurancePlan` ](/reference/2026-01-01/objects/insuranceplan)· related insurance

[`related_object` ](#field-related-object)· [`RelatedObject` ](/reference/2026-01-01/objects/relatedobject)· related object

[`related_object_name` ](#field-related-object-name)· [`String` ](/reference/2026-01-01/scalars/string)· related object

## Used By

[`User.client_source`](/reference/2026-01-01/objects/user)

## Definition

```
"""
Info about how a client was acquire
"""
type ClientSource {
  """
  The unique identifier of the source
  """
  id: String!


  """
  Get readable source based on ref_type
  """
  readable_source: String


  """
  The source of how a client was acquire: contain ID or a Other string
  """
  ref_source: String


  """
  If ref_source eq 'Other', than it may contain custom string or NULL
  """
  ref_source_other: String


  """
  The type of the source of how a client was acquire
  """
  ref_type: String


  """
  related insurance
  """
  related_insurance: InsurancePlan


  """
  related object
  """
  related_object: RelatedObject


  """
  related object
  """
  related_object_name: String
}
```
