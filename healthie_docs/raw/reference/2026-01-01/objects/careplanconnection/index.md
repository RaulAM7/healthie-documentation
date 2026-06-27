---
title: CarePlanConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/careplanconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/careplanconnection/index.md
---

A connection between a care plan and a connectable item

## Fields

[`care_plan_id` ](#field-care-plan-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the connected care plan

[`connectable_id` ](#field-connectable-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the connected item

[`connectable_type` ](#field-connectable-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the connected item

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connection

## Used By

[`deleteCarePlanConnectionPayload.connection`](/reference/2026-01-01/objects/deletecareplanconnectionpayload)

[`updateByTemplatePayload.care_plan`](/reference/2026-01-01/objects/updatebytemplatepayload)

## Definition

```
"""
A connection between a care plan and a connectable item
"""
type CarePlanConnection {
  """
  The ID of the connected care plan
  """
  care_plan_id: ID


  """
  The ID of the connected item
  """
  connectable_id: ID


  """
  The type of the connected item
  """
  connectable_type: String


  """
  The unique identifier of the connection
  """
  id: ID!
}
```
