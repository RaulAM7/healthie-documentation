---
title: ClaimCobOverridesInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/claimcoboverridesinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/claimcoboverridesinput/index.md
---

Manual overrides for claim-level COB data on a secondary claim. Only provided fields are updated; omitted fields are left unchanged.

## Fields

[`primary_adjudication_date` ](#field-primary-adjudication-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Date primary payer adjudicated the claim

[`primary_paid_amount` ](#field-primary-paid-amount)· [`Float` ](/reference/2026-01-01/scalars/float)· Total amount paid by primary insurance

## Used By

[`UpdateSecondaryClaimInput.claim_cob_overrides`](/reference/2026-01-01/input-objects/updatesecondaryclaiminput)

## Definition

```
"""
Manual overrides for claim-level COB data on a secondary claim. Only provided fields are updated; omitted fields are left unchanged.
"""
input ClaimCobOverridesInput {
  """
  Date primary payer adjudicated the claim
  """
  primary_adjudication_date: ISO8601Date


  """
  Total amount paid by primary insurance
  """
  primary_paid_amount: Float
}
```
