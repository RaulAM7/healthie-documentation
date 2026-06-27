---
title: EligibilityCheckService | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/eligibilitycheckservice/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/eligibilitycheckservice/index.md
---

Options for the service to run the eligibiliy check with

## Used By

[`User.default_eligibility_check_service`](/reference/2026-01-01/objects/user)

[`runEligibilityCheckMutationInput.eligibility_check_service`](/reference/2026-01-01/input-objects/runeligibilitycheckmutationinput)

## Definition

```
"""
Options for the service to run the eligibiliy check with
"""
enum EligibilityCheckService {
  change_health
    @deprecated(
      reason: "ChangeHealth integration has been discontinued. Use claim_md instead."
    )
  claim_md
}
```
