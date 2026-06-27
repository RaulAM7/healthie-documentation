---
title: ClaimEligibilityCheckErrors | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimeligibilitycheckerrors/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimeligibilitycheckerrors/index.md
---

Claim Eligibility Check Errors

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The error code

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the error

## Used By

[`Policy.claim_eligibility_check_errors`](/reference/2026-01-01/objects/policy)

## Definition

```
"""
Claim Eligibility Check Errors
"""
type ClaimEligibilityCheckErrors {
  """
  The error code
  """
  code: String


  """
  The description of the error
  """
  description: String
}
```
