---
title: EligibilityCheck | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/eligibilitycheck/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/eligibilitycheck/index.md
---

A processed eligibility check

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time the eligibility check was run

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the check

[`policy` ](#field-policy)· [`Policy` ](/reference/2026-01-01/objects/policy)· The policy associated with this check

[`policy_id` ](#field-policy-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the associated policy

[`response` ](#field-response)· [`String` ](/reference/2026-01-01/scalars/string)· A JSON object containing the eligibility details

[`response_as_html` ](#field-response-as-html)· [`String` ](/reference/2026-01-01/scalars/string)· A basic HTML representation of the eligibility response (nil if errors exist)

## Used By

[`Policy.latest_eligibility_check`](/reference/2026-01-01/objects/policy)

[`runEligibilityCheckMutationPayload.eligibility_check`](/reference/2026-01-01/objects/runeligibilitycheckmutationpayload)

## Definition

```
"""
A processed eligibility check
"""
type EligibilityCheck {
  """
  The time the eligibility check was run
  """
  created_at: ISO8601DateTime


  """
  The unique identifier of the check
  """
  id: ID!


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


  """
  A basic HTML representation of the eligibility response (nil if errors exist)
  """
  response_as_html: String
}
```
