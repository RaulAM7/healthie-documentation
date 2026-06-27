---
title: referringPhysician | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/referringphysician/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/referringphysician/index.md
---

Get referring physician based on id

## Arguments

[`has_fax_number` ](#argument-has-fax-number)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the patient the referring physician is associated with

## Returns

[`ReferringPhysician`](/reference/2026-01-01/objects/referringphysician)

## Example

```
query referringPhysician($has_fax_number: Boolean, $id: ID, $user_id: String) {
  referringPhysician(
    has_fax_number: $has_fax_number
    id: $id
    user_id: $user_id
  ) {
    accepts_insurance
    business_name
    created_at
    email
    fax_number
    first_name
    full_name
    id
    last_name
    location
    location_id
    metadata
    notes
    npi
    other_id
    other_id_qualifier
    phone_number
    provider
    referrals
    referrals_count
    speciality
    updated_at
    website
  }
}
```
