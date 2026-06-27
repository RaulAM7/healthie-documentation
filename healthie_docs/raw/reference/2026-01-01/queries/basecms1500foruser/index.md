---
title: baseCms1500ForUser | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/basecms1500foruser/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/basecms1500foruser/index.md
---

Get the Cms1500 Policies object for a given claim and client

## Arguments

[`base_date` ](#argument-base-date)· [`ISO8601DateTime`](/reference/2026-01-01/scalars/iso8601datetime)

[`cms1500_id` ](#argument-cms1500-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`form_answer_group_id` ](#argument-form-answer-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`only_active_policies` ](#argument-only-active-policies)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`patient_id` ](#argument-patient-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`rendering_provider_id` ](#argument-rendering-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Cms1500`](/reference/2026-01-01/objects/cms1500)

## Example

```
query baseCms1500ForUser(
  $base_date: ISO8601DateTime
  $cms1500_id: ID
  $form_answer_group_id: ID
  $only_active_policies: Boolean
  $patient_id: ID
  $rendering_provider_id: ID
) {
  baseCms1500ForUser(
    base_date: $base_date
    cms1500_id: $cms1500_id
    form_answer_group_id: $form_answer_group_id
    only_active_policies: $only_active_policies
    patient_id: $patient_id
    rendering_provider_id: $rendering_provider_id
  ) {
    accept_assignment
    additional_text
    adjustment
    amount_paid
    amount_reimbursed
    billing_provider
    billing_provider_id
    check_numbers
    claim_md_rejection_messages
    claim_md_rejection_messages_info
    claim_submissions
    client_responsibility
    client_responsibility_removed
    client_sig_on_file
    cms1500_policies
    copay
    copay_still_owed
    cpt_code_names
    cpt_codes_cms1500s
    created_at
    date_of_service
    dietitian_id
    eras
    form_answer_group_id
    has_been_submitted
    icd_codes_cms1500s
    id
    include_referrer_information
    insured_sig_on_file
    nineteen_reserved
    org_info
    organization_info_id
    orig_ref_number
    paid_out_at
    patient
    patient_account_num
    patient_id
    primary_plan_name
    reasons
    referral_info
    reimbursed_at
    rendering_provider
    rendering_provider_other_id
    rendering_provider_other_id_object
    resubmission_code
    service_location
    service_location_id
    status
    tend_reserved
    total_charge
    updated_at
    updated_by_sftp
    use_indiv_npi
  }
}
```
