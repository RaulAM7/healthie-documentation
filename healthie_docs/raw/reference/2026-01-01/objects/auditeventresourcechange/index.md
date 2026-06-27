---
title: AuditEventResourceChange | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/auditeventresourcechange/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/auditeventresourcechange/index.md
---

The details of a change associated with a audit event.

## Fields

[`field` ](#field-field)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The field that was changed.

[`value_after_change` ](#field-value-after-change)· [`String` ](/reference/2026-01-01/scalars/string)· The value after the change.

[`value_before_change` ](#field-value-before-change)· [`String` ](/reference/2026-01-01/scalars/string)· The value before the change.

## Used By

[`AuditEvent.resource_changes`](/reference/2026-01-01/objects/auditevent)

## Definition

```
"""
The details of a change associated with a audit event.
"""
type AuditEventResourceChange {
  """
  The field that was changed.
  """
  field: String!


  """
  The value after the change.
  """
  value_after_change: String


  """
  The value before the change.
  """
  value_before_change: String
}
```
