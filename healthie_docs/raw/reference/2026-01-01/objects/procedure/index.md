---
title: Procedure | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/procedure/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/procedure/index.md
---

Procedure object

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The code of the procedure

[`code_system_name` ](#field-code-system-name)· [`String` ](/reference/2026-01-01/scalars/string)· The code system name of the procedure

[`cpt_code_id` ](#field-cpt-code-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The CPT code id of the procedure

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The display name of the procedure

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the procedure

[`procedure_end_datetime` ](#field-procedure-end-datetime)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The end date time of the procedure

[`procedure_start_datetime` ](#field-procedure-start-datetime)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The start date time of the procedure

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the procedure

[`target_site` ](#field-target-site)· [`String` ](/reference/2026-01-01/scalars/string)· The target site of the procedure

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The user id of the procedure

## Used By

[`createProcedurePayload.procedure`](/reference/2026-01-01/objects/createprocedurepayload)

[`deleteProcedurePayload.procedure`](/reference/2026-01-01/objects/deleteprocedurepayload)

[`updateProcedurePayload.procedure`](/reference/2026-01-01/objects/updateprocedurepayload)

## Definition

```
"""
Procedure object
"""
type Procedure {
  """
  The code of the procedure
  """
  code: String


  """
  The code system name of the procedure
  """
  code_system_name: String


  """
  The CPT code id of the procedure
  """
  cpt_code_id: ID!


  """
  The display name of the procedure
  """
  display_name: String


  """
  The unique identifier of the procedure
  """
  id: ID!


  """
  The end date time of the procedure
  """
  procedure_end_datetime: ISO8601DateTime


  """
  The start date time of the procedure
  """
  procedure_start_datetime: ISO8601DateTime


  """
  The status of the procedure
  """
  status: String


  """
  The target site of the procedure
  """
  target_site: String


  """
  The user id of the procedure
  """
  user_id: ID
}
```
