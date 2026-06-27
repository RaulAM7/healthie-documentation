---
title: InterventionType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/interventiontype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/interventiontype/index.md
---

The type of intervention for a DSI comment

## Used By

[`DsiComment.intervention_type`](/reference/2026-01-01/objects/dsicomment)

[`Query.dsiComment`](/reference/2026-01-01/queries/dsicomment)

[`createDsiCommentInput.intervention_type`](/reference/2026-01-01/input-objects/createdsicommentinput)

[`updateDsiCommentInput.intervention_type`](/reference/2026-01-01/input-objects/updatedsicommentinput)

## Definition

```
"""
The type of intervention for a DSI comment
"""
enum InterventionType {
  GENDER_MISMATCHED_DIAGNOSIS
  INCOMPATIBLE_DIABETES_DIAGNOSIS
  UDI_NOT_UNIQUE
  BREAST_CANCER_PROCEDURE_RECOMMENDATION
  ALLERGY_DRUG_INTERACTIONS
  LAB_BASED_ASSESSMENTS
  DRUG_DRUG_INTERACTIONS
  VITALS_OUTSIDE_OF_RANGE
}
```
