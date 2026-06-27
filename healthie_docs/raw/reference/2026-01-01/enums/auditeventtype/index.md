---
title: AuditEventType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/auditeventtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/auditeventtype/index.md
---

The different kinds of AuditEvents

## Used By

[`AuditEvent.type`](/reference/2026-01-01/objects/auditevent)

[`Query.auditLog`](/reference/2026-01-01/queries/auditlog)

## Definition

```
"""
The different kinds of AuditEvents
"""
enum AuditEventType {
  CREATE
  UPDATE
  DESTROY
}
```
