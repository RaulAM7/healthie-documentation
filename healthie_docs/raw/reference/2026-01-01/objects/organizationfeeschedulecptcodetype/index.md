---
title: OrganizationFeeScheduleCptCodeType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationfeeschedulecptcodetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationfeeschedulecptcodetype/index.md
---

represents a CPT code in an organization's fee schedule

## Fields

[`code` ](#field-code)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The CPT code itself

[`description` ](#field-description)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The description of the CPT code

[`display_name` ](#field-display-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name and Code of the CPT code for use in labels

[`fee_per_unit` ](#field-fee-per-unit)· [`Int` ](/reference/2026-01-01/scalars/int)· Deprecated. Fee (in cents) per unit

deprecated

Use \`fee\_per\_unit\_cents\` instead

[`fee_per_unit_cents` ](#field-fee-per-unit-cents)· [`Int` ](/reference/2026-01-01/scalars/int)· Fee (in cents) per unit

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique identifier for the CPT Code

## Used By

[`OrganizationFeeScheduleCptCodeTypeConnection.nodes`](/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeconnection)

[`OrganizationFeeScheduleCptCodeTypeEdge.node`](/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeedge)

[`Query.organizationFeeScheduleCptCode`](/reference/2026-01-01/queries/organizationfeeschedulecptcode)

## Definition

```
"""
represents a CPT code in an organization's fee schedule
"""
type OrganizationFeeScheduleCptCodeType {
  """
  The CPT code itself
  """
  code: String!


  """
  The description of the CPT code
  """
  description: String!


  """
  The name and Code of the CPT code for use in labels
  """
  display_name: String!


  """
  Deprecated. Fee (in cents) per unit
  """
  fee_per_unit: Int @deprecated(reason: "Use `fee_per_unit_cents` instead")


  """
  Fee (in cents) per unit
  """
  fee_per_unit_cents: Int


  """
  Unique identifier for the CPT Code
  """
  id: ID!
}
```
