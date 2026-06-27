---
title: superBill | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/superbill/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/superbill/index.md
---

fetch a superbill by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`SuperBill`](/reference/2026-01-01/objects/superbill)

## Example

```
query superBill($id: ID) {
  superBill(id: $id) {
    address
    amount_paid
    balance_due
    cpt_code_names
    cpt_codes_super_bills
    created_at
    deleted_at
    dietitian_id
    icd_codes_super_bills
    id
    license_num
    location
    location_id
    npi
    patient
    patient_dob
    patient_id
    patient_location
    patient_location_id
    patient_name
    patient_phone
    place_of_service
    place_of_service_id
    prov_city
    prov_email
    prov_line1
    prov_line2
    prov_phone
    prov_state
    prov_zip
    provider
    provider_name
    receipt_line_items
    referrer_name
    referrer_npi
    service_date
    status
    tax_id
    total_fee
    updated_at
  }
}
```
