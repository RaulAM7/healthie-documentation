---
title: SentFaxOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/sentfaxorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/sentfaxorderkeys/index.md
---

SentFax sorting enum

## Used By

[`Query.sentFaxes`](/reference/2026-01-01/queries/sentfaxes)

## Definition

```
"""
SentFax sorting enum
"""
enum SentFaxOrderKeys {
  CREATED_AT_ASC
  CREATED_AT_DESC
  NUMBER_ASC
  NUMBER_DESC
  STATUS
  STATUS_ASC
  STATUS_DESC
  CLIENT_LAST_NAME_ASC
  CLIENT_LAST_NAME_DESC
  SENDER_LAST_NAME_ASC
  SENDER_LAST_NAME_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC
}
```
