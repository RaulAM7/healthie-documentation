---
title: policy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/policy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/policy/index.md
---

fetch a policy by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Policy`](/reference/2026-01-01/objects/policy)

## Example

```
query policy($id: ID) {
  policy(id: $id) {
    benefits
    call_reference
    claim_eligibility_check_errors
    coinsurance_value
    copay_value
    cpt_codes_policies
    created_at
    dob_to_use
    effective_end
    effective_start
    group_num
    holder_address
    holder_dob
    holder_first
    holder_gender
    holder_last
    holder_location
    holder_location_id
    holder_mi
    holder_name
    holder_phone
    holder_relationship
    icd_codes_policies
    id
    insurance_authorization
    insurance_authorization_required
    insurance_billing_method
    insurance_card_back_id
    insurance_card_front_id
    insurance_plan
    insurance_plan_id
    latest_eligibility_check
    metadata
    name
    notes
    num
    payer_location
    payer_location_id
    policy_phone_number
    priority_type
    referral
    referral_required
    same_address_as_client
    type_string
    updated_at
    user
    user_id
  }
}
```
