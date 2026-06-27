---
title: ReferralInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/referralinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/referralinfo/index.md
---

The referral information for a CMS1500 claim

## Fields

[`auto_accident_state` ](#field-auto-accident-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state the auto accident occurred in

[`case_date` ](#field-case-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The date of current illness, injury, or pregnancy

[`case_qualifier` ](#field-case-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifier for case\_date

[`cms1500` ](#field-cms1500)· [`Cms1500` ](/reference/2026-01-01/objects/cms1500)· The associated CMS1500

deprecated

You are no longer able to get the cms1500 from the referral info

[`cms1500_id` ](#field-cms1500-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the associated CMS1500

[`condition_related_to` ](#field-condition-related-to)· [`[String]` ](/reference/2026-01-01/scalars/string)· Options that the condition can be related to

[`hospitalization_end` ](#field-hospitalization-end)· [`String` ](/reference/2026-01-01/scalars/string)· The end of the hospitalization period

[`hospitalization_start` ](#field-hospitalization-start)· [`String` ](/reference/2026-01-01/scalars/string)· The start of the hospitalization period

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the referral info

[`other_associated_date` ](#field-other-associated-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· This field identifies additional date information about the patient's condition or treatment.

[`other_associated_qualifier` ](#field-other-associated-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifier for other\_associated\_date

[`prior_auth_number` ](#field-prior-auth-number)· [`String` ](/reference/2026-01-01/scalars/string)· The prior authorization number

[`ref_provider_first` ](#field-ref-provider-first)· [`String` ](/reference/2026-01-01/scalars/string)· The first name of the referring provider

[`ref_provider_last` ](#field-ref-provider-last)· [`String` ](/reference/2026-01-01/scalars/string)· The last name of the referring provider

[`ref_provider_middle` ](#field-ref-provider-middle)· [`String` ](/reference/2026-01-01/scalars/string)· The middle name of the referring provider

[`ref_provider_npi` ](#field-ref-provider-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the referring provider

[`ref_provider_other_id` ](#field-ref-provider-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other id of the referring provider

[`ref_provider_other_id_qual` ](#field-ref-provider-other-id-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The other id qualifier of the referring provider

[`ref_provider_qual` ](#field-ref-provider-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifications of the referring provider

[`referral_date` ](#field-referral-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The date of the referral

[`referring_physician` ](#field-referring-physician)· [`ReferringPhysician` ](/reference/2026-01-01/objects/referringphysician)· The associated referring physician

[`referring_physician_id` ](#field-referring-physician-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of associated referring physician

[`unable_to_work_end` ](#field-unable-to-work-end)· [`String` ](/reference/2026-01-01/scalars/string)· The end of the unable to work period

[`unable_to_work_start` ](#field-unable-to-work-start)· [`String` ](/reference/2026-01-01/scalars/string)· The start of the unable to work period

## Used By

[`Cms1500.referral_info`](/reference/2026-01-01/objects/cms1500)

## Definition

```
"""
The referral information for a CMS1500 claim
"""
type ReferralInfo {
  """
  The state the auto accident occurred in
  """
  auto_accident_state: String


  """
  The date of current illness, injury, or pregnancy
  """
  case_date: ISO8601Date


  """
  The qualifier for case_date
  """
  case_qualifier: String


  """
  The associated CMS1500
  """
  cms1500: Cms1500
    @deprecated(
      reason: "You are no longer able to get the cms1500 from the referral info"
    )


  """
  The id of the associated CMS1500
  """
  cms1500_id: String


  """
  Options that the condition can be related to
  """
  condition_related_to: [String]


  """
  The end of the hospitalization period
  """
  hospitalization_end: String


  """
  The start of the hospitalization period
  """
  hospitalization_start: String


  """
  The unique identifier of the referral info
  """
  id: ID


  """
  This field identifies additional date information about the patient's condition or treatment.
  """
  other_associated_date: ISO8601Date


  """
  The qualifier for other_associated_date
  """
  other_associated_qualifier: String


  """
  The prior authorization number
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
  The qualifications of the referring provider
  """
  ref_provider_qual: String


  """
  The date of the referral
  """
  referral_date: ISO8601Date


  """
  The associated referring physician
  """
  referring_physician: ReferringPhysician


  """
  The id of associated referring physician
  """
  referring_physician_id: ID


  """
  The end of the unable to work period
  """
  unable_to_work_end: String


  """
  The start of the unable to work period
  """
  unable_to_work_start: String
}
```
