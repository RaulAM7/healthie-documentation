---
title: ClaimReferralInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimreferralinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimreferralinfo/index.md
---

Frozen referral info data from a submitted claim snapshot

## Fields

[`case_date` ](#field-case-date)· [`String` ](/reference/2026-01-01/scalars/string)· Case date

[`case_qualifier` ](#field-case-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Case qualifier

[`condition_related_to` ](#field-condition-related-to)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Condition related to values

[`hospitalization_end` ](#field-hospitalization-end)· [`String` ](/reference/2026-01-01/scalars/string)· Hospitalization end date

[`hospitalization_start` ](#field-hospitalization-start)· [`String` ](/reference/2026-01-01/scalars/string)· Hospitalization start date

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Referral info ID

[`other_associated_date` ](#field-other-associated-date)· [`String` ](/reference/2026-01-01/scalars/string)· Other associated date

[`other_associated_qualifier` ](#field-other-associated-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Other associated date qualifier

[`prior_auth_number` ](#field-prior-auth-number)· [`String` ](/reference/2026-01-01/scalars/string)· Prior authorization number

[`referring_physician` ](#field-referring-physician)· [`ClaimReferringPhysician` ](/reference/2026-01-01/objects/claimreferringphysician)· Referring physician

[`referring_provider_first_name` ](#field-referring-provider-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· Referring provider first name

[`referring_provider_last_name` ](#field-referring-provider-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· Referring provider last name

[`referring_provider_middle_name` ](#field-referring-provider-middle-name)· [`String` ](/reference/2026-01-01/scalars/string)· Referring provider middle name

[`referring_provider_npi` ](#field-referring-provider-npi)· [`String` ](/reference/2026-01-01/scalars/string)· Referring provider NPI

[`referring_provider_other_id` ](#field-referring-provider-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· Referring provider other ID

[`referring_provider_other_id_qualifier` ](#field-referring-provider-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Referring provider other ID qualifier

[`referring_provider_qualifier` ](#field-referring-provider-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Referring provider qualifier

[`unable_to_work_end` ](#field-unable-to-work-end)· [`String` ](/reference/2026-01-01/scalars/string)· Unable to work end date

[`unable_to_work_start` ](#field-unable-to-work-start)· [`String` ](/reference/2026-01-01/scalars/string)· Unable to work start date

## Used By

[`Claim.referral_info`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
Frozen referral info data from a submitted claim snapshot
"""
type ClaimReferralInfo {
  """
  Case date
  """
  case_date: String


  """
  Case qualifier
  """
  case_qualifier: String


  """
  Condition related to values
  """
  condition_related_to: [String!]


  """
  Hospitalization end date
  """
  hospitalization_end: String


  """
  Hospitalization start date
  """
  hospitalization_start: String


  """
  Referral info ID
  """
  id: ID


  """
  Other associated date
  """
  other_associated_date: String


  """
  Other associated date qualifier
  """
  other_associated_qualifier: String


  """
  Prior authorization number
  """
  prior_auth_number: String


  """
  Referring physician
  """
  referring_physician: ClaimReferringPhysician


  """
  Referring provider first name
  """
  referring_provider_first_name: String


  """
  Referring provider last name
  """
  referring_provider_last_name: String


  """
  Referring provider middle name
  """
  referring_provider_middle_name: String


  """
  Referring provider NPI
  """
  referring_provider_npi: String


  """
  Referring provider other ID
  """
  referring_provider_other_id: String


  """
  Referring provider other ID qualifier
  """
  referring_provider_other_id_qualifier: String


  """
  Referring provider qualifier
  """
  referring_provider_qualifier: String


  """
  Unable to work end date
  """
  unable_to_work_end: String


  """
  Unable to work start date
  """
  unable_to_work_start: String
}
```
