---
title: CarePlanOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/careplanorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/careplanorderkeys/index.md
---

CarePlan sorting enum

## Used By

[`Query.carePlans`](/reference/2026-01-01/queries/careplans)

## Definition

```
"""
CarePlan sorting enum
"""
enum CarePlanOrderKeys {
  CREATED_AT_ASC
  CREATED_AT_DESC
  NAME_ASC
  NAME_DESC
  STATUS_ASC
  STATUS_DESC
  CLIENT_FIRST_NAME_DESC
  CLIENT_FIRST_NAME_ASC
  DEACTIVATED_DESC
  DEACTIVATED_ASC
}
```
