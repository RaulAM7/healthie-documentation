---
title: ClaimSubmission | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimsubmission/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimsubmission/index.md
---

A claim submission event (to a clearinghouse or RCM system)

## Fields

[`claim_data` ](#field-claim-data)· [`JSON` ](/reference/2026-01-01/scalars/json)· a Healthie-formatted JSON representation of the CMS1500 claim at the time it was submitted

[`cms1500_id` ](#field-cms1500-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the CMS1500 that was submitted

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time of the claim submission

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the Claim Submission

[`integration` ](#field-integration)· [`ClaimDestinationIntegration` ](/reference/2026-01-01/enums/claimdestinationintegration)· The integration that the claim was submitted to

[`integration_formatted_claim_data` ](#field-integration-formatted-claim-data)· [`JSON` ](/reference/2026-01-01/scalars/json)· An JSON representation of the CMS1500 claim, formatted for the specific integration

[`pcn` ](#field-pcn)· [`String` ](/reference/2026-01-01/scalars/string)· The PCN (Patient Control Number) returned by the clearinghouse

## Used By

[`ClaimSubmissionEdge.node`](/reference/2026-01-01/objects/claimsubmissionedge)

[`ClaimSubmissionPaginationConnection.nodes`](/reference/2026-01-01/objects/claimsubmissionpaginationconnection)

[`Cms1500.claim_submissions`](/reference/2026-01-01/objects/cms1500)

## Definition

```
"""
A claim submission event (to a clearinghouse or RCM system)
"""
type ClaimSubmission {
  """
  a Healthie-formatted JSON representation of the CMS1500 claim at the time it was submitted
  """
  claim_data: JSON


  """
  The ID of the CMS1500 that was submitted
  """
  cms1500_id: ID


  """
  The time of the claim submission
  """
  created_at: ISO8601DateTime


  """
  The unique identifier of the Claim Submission
  """
  id: ID!


  """
  The integration that the claim was submitted to
  """
  integration: ClaimDestinationIntegration


  """
  An JSON representation of the CMS1500 claim, formatted for the specific integration
  """
  integration_formatted_claim_data: JSON


  """
  The PCN (Patient Control Number) returned by the clearinghouse
  """
  pcn: String
}
```
