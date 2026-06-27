---
title: WriteOffType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/writeofftype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/writeofftype/index.md
---

Write-off type enum

## Used By

[`WriteOff.write_off_type`](/reference/2026-01-01/objects/writeoff)

[`WriteOffInput.write_off_type`](/reference/2026-01-01/input-objects/writeoffinput)

[`createWriteOffInput.write_off_type`](/reference/2026-01-01/input-objects/createwriteoffinput)

[`updateWriteOffInput.write_off_type`](/reference/2026-01-01/input-objects/updatewriteoffinput)

## Definition

```
"""
Write-off type enum
"""
enum WriteOffType {
  DISCOUNT
  UNCOLLECTABLE
  FINANCIAL_HARDSHIP
  BILLING_ERROR
  OTHER
}
```
