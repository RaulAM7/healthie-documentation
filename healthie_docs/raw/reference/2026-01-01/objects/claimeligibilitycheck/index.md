---
title: ClaimEligibilityCheck | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimeligibilitycheck/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimeligibilitycheck/index.md
---

Deprecated (use EligiblityCheck instead). A ChangeHealth eligibility check

## Fields

[`control_number` ](#field-control-number)· [`String!` ](/reference/2026-01-01/scalars/string)· required · A string used to identify the eligibility check in the Change system.

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the eligibility check was run

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the check

[`plan_status` ](#field-plan-status)· [`String` ](/reference/2026-01-01/scalars/string)· The retrieved plan status

[`policy` ](#field-policy)· [`Policy` ](/reference/2026-01-01/objects/policy)· The policy associated with this check

[`policy_id` ](#field-policy-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the associated policy

[`response` ](#field-response)· [`String` ](/reference/2026-01-01/scalars/string)· A JSON object containing the eligibility details

## Used By

[`Policy.last_eligibility_check`](/reference/2026-01-01/objects/policy)

[`runEligibilityCheckMutationPayload.claim_eligibility_check`](/reference/2026-01-01/objects/runeligibilitycheckmutationpayload)

## Definition

```
"""
Deprecated (use EligiblityCheck instead). A ChangeHealth eligibility check
"""
type ClaimEligibilityCheck {
  """
  A string used to identify the eligibility check in the Change system.
  """
  control_number: String!


  """
  The time the eligibility check was run
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the check
  """
  id: ID!


  """
  The retrieved plan status
  """
  plan_status: String


  """
  The policy associated with this check
  """
  policy: Policy


  """
  The ID of the associated policy
  """
  policy_id: ID!


  """
  A JSON object containing the eligibility details
  """
  response: String
}
```
