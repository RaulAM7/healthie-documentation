---
title: Action | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/action/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/action/index.md
---

The action recorded by an audit event on a form answer group, such as locking, unlocking, or signing.

## Used By

[`FormAnswerGroupAuditEvent.action`](/reference/2026-01-01/objects/formanswergroupauditevent)

## Definition

```
"""
The action recorded by an audit event on a form answer group, such as locking, unlocking, or signing.
"""
enum Action {
  LOCKED
  UNLOCKED
  SIGNED
  ADDENDUM_CREATED
  REMOVE_SIGNATURE
}
```
