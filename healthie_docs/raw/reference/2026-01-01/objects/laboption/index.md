---
title: LabOption | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/laboption/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/laboption/index.md
---

Lab Option

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the option

[`lab_name` ](#field-lab-name)· [`String` ](/reference/2026-01-01/scalars/string)· If available, the name of the Lab that offers this option

[`markers` ](#field-markers)· [`[LabOptionMarker!]` ](/reference/2026-01-01/objects/laboptionmarker)· If available, markers included in the test will be returned

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Name of the option

[`provider_identifier` ](#field-provider-identifier)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the option

## Used By

[`LabOptionEdge.node`](/reference/2026-01-01/objects/laboptionedge)

[`LabOptionPaginationConnection.nodes`](/reference/2026-01-01/objects/laboptionpaginationconnection)

[`LabOrder.lab_options`](/reference/2026-01-01/objects/laborder)

[`OfferingLabOption.lab_option`](/reference/2026-01-01/objects/offeringlaboption)

## Definition

```
"""
Lab Option
"""
type LabOption {
  """
  The unique identifier of the option
  """
  id: ID!


  """
  If available, the name of the Lab that offers this option
  """
  lab_name: String


  """
  If available, markers included in the test will be returned
  """
  markers: [LabOptionMarker!]


  """
  Name of the option
  """
  name: String!


  """
  The unique identifier of the option
  """
  provider_identifier: ID
}
```
