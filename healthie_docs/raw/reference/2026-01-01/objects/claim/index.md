---
title: Claim | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claim/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claim/index.md
---

A claim (CMS1500) with snapshot data for submitted claims, live data for drafts, and correction tracking

## Fields

[`accept_assignment` ](#field-accept-assignment)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether assignment is accepted

[`additional_claim_information` ](#field-additional-claim-information)· [`String` ](/reference/2026-01-01/scalars/string)· Additional claim info from Box 19

[`amount_paid` ](#field-amount-paid)· [`String` ](/reference/2026-01-01/scalars/string)· Amount paid by the patient

[`billing_provider` ](#field-billing-provider)· [`ClaimProvider` ](/reference/2026-01-01/objects/claimprovider)· Billing provider / organization info

[`claim_codes` ](#field-claim-codes)· [`String` ](/reference/2026-01-01/scalars/string)· Condition codes from Box 10d

[`claim_md_rejection_messages` ](#field-claim-md-rejection-messages)· [`[ClaimMdMessage!]!` ](/reference/2026-01-01/objects/claimmdmessage)· required · Most recent Claim MD rejection messages

[`claim_submissions` ](#field-claim-submissions)· [`ClaimSubmissionPaginationConnection!` ](/reference/2026-01-01/objects/claimsubmissionpaginationconnection)· required · Submission history for this claim

[`client_sig_on_file` ](#field-client-sig-on-file)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the client signature is on file

[`coordination_of_benefits` ](#field-coordination-of-benefits)· [`CoordinationOfBenefits` ](/reference/2026-01-01/objects/coordinationofbenefits)· COB data derived from primary claim ERA and manual overrides

[`correction_claims` ](#field-correction-claims)· [`ClaimPaginationConnection!` ](/reference/2026-01-01/objects/claimpaginationconnection)· required · Child correction claims

[`diagnoses` ](#field-diagnoses)· [`[ClaimDiagnosis!]!` ](/reference/2026-01-01/objects/claimdiagnosis)· required · ICD-10 diagnoses

[`has_been_submitted` ](#field-has-been-submitted)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the claim has been submitted

[`has_claim_submission_claim_data` ](#field-has-claim-submission-claim-data)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether frozen claim submission data exists for this claim

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

[`include_referrer_information` ](#field-include-referrer-information)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether referrer information should be included

[`insured_sig_on_file` ](#field-insured-sig-on-file)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the insured signature is on file

[`is_correction` ](#field-is-correction)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if this claim is a correction of another claim

[`is_locked` ](#field-is-locked)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the claim is in a locked status

[`org_info` ](#field-org-info)· [`OrganizationInfo` ](/reference/2026-01-01/objects/organizationinfo)· The Organization Info in use on this claim

[`original_claim` ](#field-original-claim)· [`Claim` ](/reference/2026-01-01/objects/claim)· The parent claim if this is a correction

[`original_claim_id` ](#field-original-claim-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the original claim if this is a correction

[`original_reference_number` ](#field-original-reference-number)· [`String` ](/reference/2026-01-01/scalars/string)· Original reference number from Box 22

[`patient` ](#field-patient)· [`ClaimPatient` ](/reference/2026-01-01/objects/claimpatient)· Patient demographics

[`patient_account_num` ](#field-patient-account-num)· [`String` ](/reference/2026-01-01/scalars/string)· Patient account number

[`payer_order` ](#field-payer-order)· [`PayerOrder` ](/reference/2026-01-01/enums/payerorder)· Whether this is a primary or secondary claim

[`policies` ](#field-policies)· [`[ClaimPolicy!]!` ](/reference/2026-01-01/objects/claimpolicy)· required · Insurance policies on this claim

[`primary_claim` ](#field-primary-claim)· [`Claim` ](/reference/2026-01-01/objects/claim)· The primary claim if this is a secondary claim

[`primary_claim_id` ](#field-primary-claim-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the primary claim if this is a secondary claim

[`prior_authorization_number` ](#field-prior-authorization-number)· [`String` ](/reference/2026-01-01/scalars/string)· Prior authorization number from Box 23

[`referral_info` ](#field-referral-info)· [`ClaimReferralInfo` ](/reference/2026-01-01/objects/claimreferralinfo)· Referral information

[`referring_provider` ](#field-referring-provider)· [`ClaimProvider` ](/reference/2026-01-01/objects/claimprovider)· Referring provider

[`rendering_provider` ](#field-rendering-provider)· [`ClaimProvider` ](/reference/2026-01-01/objects/claimprovider)· Rendering provider

[`resubmission_code` ](#field-resubmission-code)· [`String` ](/reference/2026-01-01/scalars/string)· Frequency/resubmission code from Box 22

[`service_lines` ](#field-service-lines)· [`[ClaimServiceLine!]!` ](/reference/2026-01-01/objects/claimserviceline)· required · CPT service lines

[`service_location` ](#field-service-location)· [`ClaimLocation` ](/reference/2026-01-01/objects/claimlocation)· Service location

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· Current claim status (live, not from snapshot)

[`submission_method` ](#field-submission-method)· [`String` ](/reference/2026-01-01/scalars/string)· Submission method (e.g. office\_ally, change\_health, manual)

[`submitted_at` ](#field-submitted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Timestamp when the claim was last submitted

[`use_indiv_npi` ](#field-use-indiv-npi)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the claim uses the individual NPI

## Used By

[`Claim.original_claim`](/reference/2026-01-01/objects/claim)

[`Claim.primary_claim`](/reference/2026-01-01/objects/claim)

[`ClaimEdge.node`](/reference/2026-01-01/objects/claimedge)

[`ClaimPaginationConnection.nodes`](/reference/2026-01-01/objects/claimpaginationconnection)

[`CreateSecondaryClaimPayload.claim`](/reference/2026-01-01/objects/createsecondaryclaimpayload)

[`SubmitSecondaryClaimPayload.claims`](/reference/2026-01-01/objects/submitsecondaryclaimpayload)

[`UpdateSecondaryClaimPayload.claim`](/reference/2026-01-01/objects/updatesecondaryclaimpayload)

## Definition

```
"""
A claim (CMS1500) with snapshot data for submitted claims, live data for drafts, and correction tracking
"""
type Claim {
  """
  Whether assignment is accepted
  """
  accept_assignment: Boolean


  """
  Additional claim info from Box 19
  """
  additional_claim_information: String


  """
  Amount paid by the patient
  """
  amount_paid: String


  """
  Billing provider / organization info
  """
  billing_provider: ClaimProvider


  """
  Condition codes from Box 10d
  """
  claim_codes: String


  """
  Most recent Claim MD rejection messages
  """
  claim_md_rejection_messages: [ClaimMdMessage!]!


  """
  Submission history for this claim
  """
  claim_submissions(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): ClaimSubmissionPaginationConnection!


  """
  Whether the client signature is on file
  """
  client_sig_on_file: Boolean


  """
  COB data derived from primary claim ERA and manual overrides
  """
  coordination_of_benefits: CoordinationOfBenefits


  """
  Child correction claims
  """
  correction_claims(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): ClaimPaginationConnection!


  """
  ICD-10 diagnoses
  """
  diagnoses: [ClaimDiagnosis!]!


  """
  Whether the claim has been submitted
  """
  has_been_submitted: Boolean!


  """
  Whether frozen claim submission data exists for this claim
  """
  has_claim_submission_claim_data: Boolean!
  id: ID!


  """
  Whether referrer information should be included
  """
  include_referrer_information: Boolean


  """
  Whether the insured signature is on file
  """
  insured_sig_on_file: Boolean


  """
  True if this claim is a correction of another claim
  """
  is_correction: Boolean!


  """
  Whether the claim is in a locked status
  """
  is_locked: Boolean!


  """
  The Organization Info in use on this claim
  """
  org_info: OrganizationInfo


  """
  The parent claim if this is a correction
  """
  original_claim: Claim


  """
  The ID of the original claim if this is a correction
  """
  original_claim_id: ID


  """
  Original reference number from Box 22
  """
  original_reference_number: String


  """
  Patient demographics
  """
  patient: ClaimPatient


  """
  Patient account number
  """
  patient_account_num: String


  """
  Whether this is a primary or secondary claim
  """
  payer_order: PayerOrder


  """
  Insurance policies on this claim
  """
  policies: [ClaimPolicy!]!


  """
  The primary claim if this is a secondary claim
  """
  primary_claim: Claim


  """
  The ID of the primary claim if this is a secondary claim
  """
  primary_claim_id: ID


  """
  Prior authorization number from Box 23
  """
  prior_authorization_number: String


  """
  Referral information
  """
  referral_info: ClaimReferralInfo


  """
  Referring provider
  """
  referring_provider: ClaimProvider


  """
  Rendering provider
  """
  rendering_provider: ClaimProvider


  """
  Frequency/resubmission code from Box 22
  """
  resubmission_code: String


  """
  CPT service lines
  """
  service_lines: [ClaimServiceLine!]!


  """
  Service location
  """
  service_location: ClaimLocation


  """
  Current claim status (live, not from snapshot)
  """
  status: String


  """
  Submission method (e.g. office_ally, change_health, manual)
  """
  submission_method: String


  """
  Timestamp when the claim was last submitted
  """
  submitted_at: ISO8601DateTime


  """
  Whether the claim uses the individual NPI
  """
  use_indiv_npi: Boolean
}
```
