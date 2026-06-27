---
title: initialCms1500 | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/initialcms1500/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/initialcms1500/index.md
---

A new CMS1500 form with some objects already prefilled

## Arguments

[`form_answer_group_id` ](#argument-form-answer-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`patient_id` ](#argument-patient-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Cms1500`](/reference/2026-01-01/objects/cms1500)

## Example

```
query initialCms1500(
  $form_answer_group_id: ID
  $patient_id: ID
  $provider_id: ID
) {
  initialCms1500(
    form_answer_group_id: $form_answer_group_id
    patient_id: $patient_id
    provider_id: $provider_id
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
