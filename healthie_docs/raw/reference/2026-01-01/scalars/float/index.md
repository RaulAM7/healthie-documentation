---
title: Float | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/scalars/float/index
  md: https://docs.gethealthie.com/reference/2026-01-01/scalars/float/index.md
---

The \`Float\` scalar type represents signed double-precision fractional values as specified by \[IEEE 754]\(https\://en.wikipedia.org/wiki/IEEE\_floating\_point).

## Used By

[`AutoTaskGenerator.number_to_check`](/reference/2026-01-01/objects/autotaskgenerator)

[`AutoscoredSectionType.value`](/reference/2026-01-01/objects/autoscoredsectiontype)

[`CobAdjustment.amount`](/reference/2026-01-01/objects/cobadjustment)

[`CobServiceLineAdjustment.line_paid_amount`](/reference/2026-01-01/objects/cobservicelineadjustment)

[`CoordinationOfBenefits.primary_paid_amount`](/reference/2026-01-01/objects/coordinationofbenefits)

[`CptCode.last_fee`](/reference/2026-01-01/objects/cptcode)

[`CustomModule.position`](/reference/2026-01-01/objects/custommodule)

[`Entry.metric_stat`](/reference/2026-01-01/objects/entry)

[`Entry.percieved_hungriness`](/reference/2026-01-01/objects/entry)

[`EraAdjustment.amount`](/reference/2026-01-01/objects/eraadjustment)

[`EraServiceLine.billed_amount`](/reference/2026-01-01/objects/eraserviceline)

[`EraServiceLine.paid_amount`](/reference/2026-01-01/objects/eraserviceline)

[`FoodItem.modifier`](/reference/2026-01-01/objects/fooditem)

[`FoodNutrient.nutrient_value`](/reference/2026-01-01/objects/foodnutrient)

[`InsurancePayment.paid_amount`](/reference/2026-01-01/objects/insurancepayment)

[`MetricDataPointType.value`](/reference/2026-01-01/objects/metricdatapointtype)

[`MetricGraphDataType.max`](/reference/2026-01-01/objects/metricgraphdatatype)

[`MetricGraphDataType.min`](/reference/2026-01-01/objects/metricgraphdatatype)

[`Offering.offering_product_taxes`](/reference/2026-01-01/objects/offering)

[`Offering.total_revenue`](/reference/2026-01-01/objects/offering)

[`Pharmacy.latitude`](/reference/2026-01-01/objects/pharmacy)

[`Pharmacy.longitude`](/reference/2026-01-01/objects/pharmacy)

[`RequestedPayment.balance_due`](/reference/2026-01-01/objects/requestedpayment)

[`RequestedPayment.debt_decimal`](/reference/2026-01-01/objects/requestedpayment)

[`RequestedPayment.write_off_amount`](/reference/2026-01-01/objects/requestedpayment)

[`ServingSize.amount`](/reference/2026-01-01/objects/servingsize)

[`ServingSize.calories`](/reference/2026-01-01/objects/servingsize)

[`ServingSize.modifier`](/reference/2026-01-01/objects/servingsize)

[`SubscriptionInstance.credit_balance`](/reference/2026-01-01/objects/subscriptioninstance)

[`User.estimated_future_payouts`](/reference/2026-01-01/objects/user)

[`User.height`](/reference/2026-01-01/objects/user)

[`WriteOff.amount`](/reference/2026-01-01/objects/writeoff)

[`ClaimCobOverridesInput.primary_paid_amount`](/reference/2026-01-01/input-objects/claimcoboverridesinput)

[`ClaimLineCobOverridesInput.line_paid_amount`](/reference/2026-01-01/input-objects/claimlinecoboverridesinput)

[`CobAdjustmentInput.amount`](/reference/2026-01-01/input-objects/cobadjustmentinput)

[`WriteOffInput.amount`](/reference/2026-01-01/input-objects/writeoffinput)

[`createInsurancePaymentInput.paid_amount`](/reference/2026-01-01/input-objects/createinsurancepaymentinput)

[`createWriteOffInput.amount`](/reference/2026-01-01/input-objects/createwriteoffinput)

[`updateManualInsurancePaymentInput.paid_amount`](/reference/2026-01-01/input-objects/updatemanualinsurancepaymentinput)

[`updateWriteOffInput.amount`](/reference/2026-01-01/input-objects/updatewriteoffinput)

## Definition

```
"""
The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).
"""
scalar Float
```
