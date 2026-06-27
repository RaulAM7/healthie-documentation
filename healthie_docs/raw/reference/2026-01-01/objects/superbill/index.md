---
title: SuperBill | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/superbill/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/superbill/index.md
---

SuperBill

## Fields

[`address` ](#field-address)· [`String` ](/reference/2026-01-01/scalars/string)· address

[`amount_paid` ](#field-amount-paid)· [`String` ](/reference/2026-01-01/scalars/string)· amount of super bill

[`balance_due` ](#field-balance-due)· [`String` ](/reference/2026-01-01/scalars/string)· amount due after amount paid is subtracted from total fee

[`cpt_code_names` ](#field-cpt-code-names)· [`String` ](/reference/2026-01-01/scalars/string)· Returns cpt codes names list comma separated

[`cpt_codes_super_bills` ](#field-cpt-codes-super-bills)· [`[CptCodesSuperBill!]` ](/reference/2026-01-01/objects/cptcodessuperbill)· CPT codes in use for this super bill

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date super bill was created

[`deleted_at` ](#field-deleted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· date superbill was deleted

[`dietitian_id` ](#field-dietitian-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of dietitian

[`icd_codes_super_bills` ](#field-icd-codes-super-bills)· [`[IcdCodesSuperBill!]` ](/reference/2026-01-01/objects/icdcodessuperbill)· ICD codes in use for this super bill

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the bill

[`license_num` ](#field-license-num)· [`String` ](/reference/2026-01-01/scalars/string)· license number

[`location` ](#field-location)· [`Location` ](/reference/2026-01-01/objects/location)· location

[`location_id` ](#field-location-id)· [`ID` ](/reference/2026-01-01/scalars/id)· location id

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· npi number

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· patient of this superbill

[`patient_dob` ](#field-patient-dob)· [`String` ](/reference/2026-01-01/scalars/string)· dob of patient

[`patient_id` ](#field-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of patient

[`patient_location` ](#field-patient-location)· [`Location` ](/reference/2026-01-01/objects/location)· location

[`patient_location_id` ](#field-patient-location-id)· [`ID` ](/reference/2026-01-01/scalars/id)· patient location id

[`patient_name` ](#field-patient-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of patient

[`patient_phone` ](#field-patient-phone)· [`String` ](/reference/2026-01-01/scalars/string)· phone number of patient

[`place_of_service` ](#field-place-of-service)· [`PlaceOfService` ](/reference/2026-01-01/objects/placeofservice)· place of service

[`place_of_service_id` ](#field-place-of-service-id)· [`ID` ](/reference/2026-01-01/scalars/id)· place of service id

[`prov_city` ](#field-prov-city)· [`String` ](/reference/2026-01-01/scalars/string)· city

[`prov_email` ](#field-prov-email)· [`String` ](/reference/2026-01-01/scalars/string)· email

[`prov_line1` ](#field-prov-line1)· [`String` ](/reference/2026-01-01/scalars/string)· address line one

[`prov_line2` ](#field-prov-line2)· [`String` ](/reference/2026-01-01/scalars/string)· address line one

[`prov_phone` ](#field-prov-phone)· [`String` ](/reference/2026-01-01/scalars/string)· phone

[`prov_state` ](#field-prov-state)· [`String` ](/reference/2026-01-01/scalars/string)· state

[`prov_zip` ](#field-prov-zip)· [`String` ](/reference/2026-01-01/scalars/string)· zip

[`provider` ](#field-provider)· [`User` ](/reference/2026-01-01/objects/user)· provider

[`provider_name` ](#field-provider-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of provider

[`receipt_line_items` ](#field-receipt-line-items)· [`[ReceiptLineItem!]` ](/reference/2026-01-01/objects/receiptlineitem)· receipt line items of this super bill

[`referrer_name` ](#field-referrer-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of referrer

[`referrer_npi` ](#field-referrer-npi)· [`String` ](/reference/2026-01-01/scalars/string)· npi of referrer

[`service_date` ](#field-service-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date of service (as a date)

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· status

[`tax_id` ](#field-tax-id)· [`String` ](/reference/2026-01-01/scalars/string)· tax id

[`total_fee` ](#field-total-fee)· [`String` ](/reference/2026-01-01/scalars/string)· total fee for superbill

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date super bill was updated

## Used By

[`Query.superBill`](/reference/2026-01-01/queries/superbill)

[`SuperBillEdge.node`](/reference/2026-01-01/objects/superbilledge)

[`SuperBillPaginationConnection.nodes`](/reference/2026-01-01/objects/superbillpaginationconnection)

[`createSuperBillPayload.superBill`](/reference/2026-01-01/objects/createsuperbillpayload)

[`deleteSuperBillPayload.superBill`](/reference/2026-01-01/objects/deletesuperbillpayload)

[`updateSuperBillPayload.superBill`](/reference/2026-01-01/objects/updatesuperbillpayload)

## Definition

```
"""
SuperBill
"""
type SuperBill {
  """
  address
  """
  address: String


  """
  amount of super bill
  """
  amount_paid: String


  """
  amount due after amount paid is subtracted from total fee
  """
  balance_due: String


  """
  Returns cpt codes names list comma separated
  """
  cpt_code_names: String


  """
  CPT codes in use for this super bill
  """
  cpt_codes_super_bills: [CptCodesSuperBill!]


  """
  date super bill was created
  """
  created_at: ISO8601DateTime!


  """
  date superbill was deleted
  """
  deleted_at: ISO8601DateTime


  """
  id of dietitian
  """
  dietitian_id: ID


  """
  ICD codes in use for this super bill
  """
  icd_codes_super_bills: [IcdCodesSuperBill!]


  """
  The unique identifier of the bill
  """
  id: ID!


  """
  license number
  """
  license_num: String


  """
  location
  """
  location: Location


  """
  location id
  """
  location_id: ID


  """
  npi number
  """
  npi: String


  """
  patient of this superbill
  """
  patient: User


  """
  dob of patient
  """
  patient_dob: String


  """
  id of patient
  """
  patient_id: ID


  """
  location
  """
  patient_location: Location


  """
  patient location id
  """
  patient_location_id: ID


  """
  name of patient
  """
  patient_name: String


  """
  phone number of patient
  """
  patient_phone: String


  """
  place of service
  """
  place_of_service: PlaceOfService


  """
  place of service id
  """
  place_of_service_id: ID


  """
  city
  """
  prov_city: String


  """
  email
  """
  prov_email: String


  """
  address line one
  """
  prov_line1: String


  """
  address line one
  """
  prov_line2: String


  """
  phone
  """
  prov_phone: String


  """
  state
  """
  prov_state: String


  """
  zip
  """
  prov_zip: String


  """
  provider
  """
  provider: User


  """
  name of provider
  """
  provider_name: String


  """
  receipt line items of this super bill
  """
  receipt_line_items: [ReceiptLineItem!]


  """
  name of referrer
  """
  referrer_name: String


  """
  npi of referrer
  """
  referrer_npi: String


  """
  Date of service (as a date)
  """
  service_date: ISO8601DateTime


  """
  status
  """
  status: String


  """
  tax id
  """
  tax_id: String


  """
  total fee for superbill
  """
  total_fee: String


  """
  date super bill was updated
  """
  updated_at: ISO8601DateTime!
}
```
