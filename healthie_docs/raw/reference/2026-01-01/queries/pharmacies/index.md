---
title: pharmacies | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/pharmacies/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/pharmacies/index.md
---

Fetch an array of pharmacies given search parameters. One of zip, ncpdp\_id, or phone\_or\_fax is required

## Arguments

[`address` ](#argument-address)· [`String` ](/reference/2026-01-01/scalars/string)· requires at least 3 characters

[`city` ](#argument-city)· [`String` ](/reference/2026-01-01/scalars/string)· requires at least 3 characters

[`name` ](#argument-name)· [`String` ](/reference/2026-01-01/scalars/string)· keywords for name of pharmacy, requires at least 3 characters

[`ncpdp_id` ](#argument-ncpdp-id)· [`ID` ](/reference/2026-01-01/scalars/id)· NCPDP ID assigned to the pharmacy

[`phone_or_fax` ](#argument-phone-or-fax)· [`String` ](/reference/2026-01-01/scalars/string)· phone or fax number of the pharmacy, requires at least 3 characters

[`specialties` ](#argument-specialties)· [`[PharmacySpecialty]` ](/reference/2026-01-01/enums/pharmacyspecialty)· Array of pharmacy specialties

[`state` ](#argument-state)· [`States` ](/reference/2026-01-01/enums/states)· two letter abbreviation (e.g., NY, CA, MD)

[`zip` ](#argument-zip)· [`String` ](/reference/2026-01-01/scalars/string)· requires at least 3 numeric characters

[`after` ](#argument-after)· [`Cursor`](/reference/2026-01-01/scalars/cursor)

[`before` ](#argument-before)· [`Cursor`](/reference/2026-01-01/scalars/cursor)

## Returns

[`PharmacyPaginationConnection`](/reference/2026-01-01/objects/pharmacypaginationconnection)

## Example

```
query pharmacies(
  $address: String
  $city: String
  $name: String
  $ncpdp_id: ID
  $phone_or_fax: String
  $specialties: [PharmacySpecialty]
  $state: States
  $zip: String
  $after: Cursor
  $before: Cursor
) {
  pharmacies(
    address: $address
    city: $city
    name: $name
    ncpdp_id: $ncpdp_id
    phone_or_fax: $phone_or_fax
    specialties: $specialties
    state: $state
    zip: $zip
    after: $after
    before: $before
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
