---
title: CustomModuleFormOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/custommoduleformorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/custommoduleformorderkeys/index.md
---

CustomModuleForm sorting enum

## Used By

[`Query.customModuleForms`](/reference/2026-01-01/queries/custommoduleforms)

## Definition

```
"""
CustomModuleForm sorting enum
"""
enum CustomModuleFormOrderKeys {
  NAME_ASC
  NAME_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC


  """
  Sort by owner last name descending
  """
  USER_LAST_NAME_DESC


  """
  Sort by owner last name ascending
  """
  USER_LAST_NAME_ASC
  TYPE_ASC
  TYPE_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
}
```
