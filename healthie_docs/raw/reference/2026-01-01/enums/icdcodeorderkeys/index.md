---
title: IcdCodeOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/icdcodeorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/icdcodeorderkeys/index.md
---

ICD Code sorting enum

## Used By

[`Query.icdCodes`](/reference/2026-01-01/queries/icdcodes)

## Definition

```
"""
ICD Code sorting enum
"""
enum IcdCodeOrderKeys {
  CREATED_AT_ASC
  CREATED_AT_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC
  CODE_ASC
  CODE_DESC
  FAVORITES_ASC
  FAVORITES_DESC
}
```
