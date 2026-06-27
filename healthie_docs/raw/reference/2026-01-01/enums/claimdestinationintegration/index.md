---
title: ClaimDestinationIntegration | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/claimdestinationintegration/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/claimdestinationintegration/index.md
---

Options for the service to submit a claim to

## Used By

[`ClaimSubmission.integration`](/reference/2026-01-01/objects/claimsubmission)

[`User.claim_destination_options`](/reference/2026-01-01/objects/user)

[`uploadToIntegrationsInput.destination_integration`](/reference/2026-01-01/input-objects/uploadtointegrationsinput)

## Definition

```
"""
Options for the service to submit a claim to
"""
enum ClaimDestinationIntegration {
  candid
  claim_md
  change_health
    @deprecated(
      reason: "ChangeHealth claims integration has been discontinued."
    )
  office_ally
}
```
