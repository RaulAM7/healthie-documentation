---
title: ClaimLineCobOverridesInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/claimlinecoboverridesinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/claimlinecoboverridesinput/index.md
---

Manual overrides for line-level COB data on a secondary claim service line. Only provided fields are updated; omitted fields are left unchanged.

## Fields

[`adjustments` ](#field-adjustments)· [`[CobAdjustmentInput!]` ](/reference/2026-01-01/input-objects/cobadjustmentinput)· Up to 6 adjustments for this service line

[`cpt_codes_cms1500_id` ](#field-cpt-codes-cms1500-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the service line to override

[`line_adjudication_date` ](#field-line-adjudication-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Date primary payer adjudicated this service line

[`line_paid_amount` ](#field-line-paid-amount)· [`Float` ](/reference/2026-01-01/scalars/float)· Amount paid by primary payer for this line

## Used By

[`UpdateSecondaryClaimInput.claim_line_cob_overrides`](/reference/2026-01-01/input-objects/updatesecondaryclaiminput)

## Definition

```
"""
Manual overrides for line-level COB data on a secondary claim service line. Only provided fields are updated; omitted fields are left unchanged.
"""
input ClaimLineCobOverridesInput {
  """
  Up to 6 adjustments for this service line
  """
  adjustments: [CobAdjustmentInput!]


  """
  The ID of the service line to override
  """
  cpt_codes_cms1500_id: ID!


  """
  Date primary payer adjudicated this service line
  """
  line_adjudication_date: ISO8601Date


  """
  Amount paid by primary payer for this line
  """
  line_paid_amount: Float
}
```
