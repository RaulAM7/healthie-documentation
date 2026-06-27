---
title: AuditEvent | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/auditevent/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/auditevent/index.md
---

An audit event.

## Fields

[`acting_user` ](#field-acting-user)· [`User` ](/reference/2026-01-01/objects/user)· The user who caused this event.

[`occurred_at` ](#field-occurred-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date and time that the event happened.

[`resource_changes` ](#field-resource-changes)· [`[AuditEventResourceChange!]` ](/reference/2026-01-01/objects/auditeventresourcechange)· The set of changes associated with the event

[`resource_id` ](#field-resource-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the resource that was affected by the event.

[`resource_name` ](#field-resource-name)· [`AuditEventResourceName!` ](/reference/2026-01-01/enums/auditeventresourcename)· required · The name of the resource that was affected by this event.

[`type` ](#field-type)· [`AuditEventType!` ](/reference/2026-01-01/enums/auditeventtype)· required · The type of the event.

## Used By

[`AuditEventEdge.node`](/reference/2026-01-01/objects/auditeventedge)

[`AuditEventPaginationConnection.nodes`](/reference/2026-01-01/objects/auditeventpaginationconnection)

## Definition

```
"""
An audit event.
"""
type AuditEvent {
  """
  The user who caused this event.
  """
  acting_user: User


  """
  Date and time that the event happened.
  """
  occurred_at: ISO8601DateTime!


  """
  The set of changes associated with the event
  """
  resource_changes: [AuditEventResourceChange!]


  """
  The ID of the resource that was affected by the event.
  """
  resource_id: ID!


  """
  The name of the resource that was affected by this event.
  """
  resource_name: AuditEventResourceName!


  """
  The type of the event.
  """
  type: AuditEventType!
}
```
