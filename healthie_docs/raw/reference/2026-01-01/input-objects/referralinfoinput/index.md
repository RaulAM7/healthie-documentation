---
title: ReferralInfoInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/referralinfoinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/referralinfoinput/index.md
---

Payload for a referral info

## Fields

[`auto_accident_state` ](#field-auto-accident-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state of the auto accident

[`case_date` ](#field-case-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The date of the case

[`case_qualifier` ](#field-case-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifier of the case

[`condition_related_to` ](#field-condition-related-to)· [`[String]` ](/reference/2026-01-01/scalars/string)· The condition relationships

[`hospitalization_end` ](#field-hospitalization-end)· [`String` ](/reference/2026-01-01/scalars/string)· The end date of the hospitalization

[`hospitalization_start` ](#field-hospitalization-start)· [`String` ](/reference/2026-01-01/scalars/string)· The start date of the hospitalization

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the referral info

[`other_associated_date` ](#field-other-associated-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The other associated date

[`other_associated_qualifier` ](#field-other-associated-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· The other qualifier

[`prior_auth_number` ](#field-prior-auth-number)· [`String` ](/reference/2026-01-01/scalars/string)· The prior auth number

[`ref_provider_first` ](#field-ref-provider-first)· [`String` ](/reference/2026-01-01/scalars/string)· The first name of the referring provider

[`ref_provider_last` ](#field-ref-provider-last)· [`String` ](/reference/2026-01-01/scalars/string)· The last name of the referring provider

[`ref_provider_middle` ](#field-ref-provider-middle)· [`String` ](/reference/2026-01-01/scalars/string)· The middle name of the referring provider

[`ref_provider_npi` ](#field-ref-provider-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the referring provider

[`ref_provider_other_id` ](#field-ref-provider-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other id of the referring provider

[`ref_provider_other_id_qual` ](#field-ref-provider-other-id-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The other id qualifier of the referring provider

[`ref_provider_qual` ](#field-ref-provider-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifier of the referring provider

[`referring_physician_id` ](#field-referring-physician-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the referring physician

[`unable_to_work_end` ](#field-unable-to-work-end)· [`String` ](/reference/2026-01-01/scalars/string)· The end date of the unable to work

[`unable_to_work_start` ](#field-unable-to-work-start)· [`String` ](/reference/2026-01-01/scalars/string)· The start date of the unable to work

## Used By

[`createCms1500Input.referral_info`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.referral_info`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for a referral info
"""
input ReferralInfoInput {
  """
  The state of the auto accident
  """
  auto_accident_state: String


  """
  The date of the case
  """
  case_date: ISO8601Date


  """
  The qualifier of the case
  """
  case_qualifier: String


  """
  The condition relationships
  """
  condition_related_to: [String]


  """
  The end date of the hospitalization
  """
  hospitalization_end: String


  """
  The start date of the hospitalization
  """
  hospitalization_start: String


  """
  The id of the referral info
  """
  id: ID


  """
  The other associated date
  """
  other_associated_date: ISO8601Date


  """
  The other qualifier
  """
  other_associated_qualifier: String


  """
  The prior auth number
  """
  prior_auth_number: String


  """
  The first name of the referring provider
  """
  ref_provider_first: String


  """
  The last name of the referring provider
  """
  ref_provider_last: String


  """
  The middle name of the referring provider
  """
  ref_provider_middle: String


  """
  The NPI of the referring provider
  """
  ref_provider_npi: String


  """
  The other id of the referring provider
  """
  ref_provider_other_id: String


  """
  The other id qualifier of the referring provider
  """
  ref_provider_other_id_qual: String


  """
  The qualifier of the referring provider
  """
  ref_provider_qual: String


  """
  The id of the referring physician
  """
  referring_physician_id: ID


  """
  The end date of the unable to work
  """
  unable_to_work_end: String


  """
  The start date of the unable to work
  """
  unable_to_work_start: String
}
```
