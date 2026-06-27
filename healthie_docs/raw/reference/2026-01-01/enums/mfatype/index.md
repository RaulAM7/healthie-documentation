---
title: MfaType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/mfatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/mfatype/index.md
---

Type of multi-factor authentication used

## Used By

[`signInPayload.blocked_by_2fa_type`](/reference/2026-01-01/objects/signinpayload)

## Definition

```
"""
Type of multi-factor authentication used
"""
enum MfaType {
  SMS
  EMAIL
}
```
