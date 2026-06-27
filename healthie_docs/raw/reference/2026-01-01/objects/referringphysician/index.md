---
title: ReferringPhysician | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/referringphysician/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/referringphysician/index.md
---

a referring physician

## Fields

[`accepts_insurance` ](#field-accepts-insurance)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`business_name` ](#field-business-name)· [`String` ](/reference/2026-01-01/scalars/string)· Business Name of physician

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· email of physician

[`fax_number` ](#field-fax-number)· [`String` ](/reference/2026-01-01/scalars/string)· fax number of physician

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· first name of physician

[`full_name` ](#field-full-name)· [`String` ](/reference/2026-01-01/scalars/string)· full name of physician

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the physician

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· last name of physician

[`location` ](#field-location)· [`Location` ](/reference/2026-01-01/objects/location)· The associated location

[`location_id` ](#field-location-id)· [`ID` ](/reference/2026-01-01/scalars/id)· location id

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000.

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Dietitian's notes

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· npi of physician

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· Saved Other ID associated with this provider

[`other_id_qualifier` ](#field-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Qualifier for Other ID

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· phone number of physician

[`provider` ](#field-provider)· [`User!` ](/reference/2026-01-01/objects/user)· required · The user who entered the referring physician

[`referrals` ](#field-referrals)· [`[Referral!]` ](/reference/2026-01-01/objects/referral)· Associated users

[`referrals_count` ](#field-referrals-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Associated users count

[`speciality` ](#field-speciality)· [`String` ](/reference/2026-01-01/scalars/string)· Physician's speciality

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

[`website` ](#field-website)· [`String` ](/reference/2026-01-01/scalars/string)· Physician's website

## Used By

[`Query.referringPhysician`](/reference/2026-01-01/queries/referringphysician)

[`Referral.referring_physician`](/reference/2026-01-01/objects/referral)

[`ReferralInfo.referring_physician`](/reference/2026-01-01/objects/referralinfo)

[`ReferringPhysicianEdge.node`](/reference/2026-01-01/objects/referringphysicianedge)

[`ReferringPhysicianPaginationConnection.nodes`](/reference/2026-01-01/objects/referringphysicianpaginationconnection)

[`User.referring_physicians`](/reference/2026-01-01/objects/user)

[`createReferringPhysicianPayload.duplicated_physician`](/reference/2026-01-01/objects/createreferringphysicianpayload)

[`createReferringPhysicianPayload.referring_physician`](/reference/2026-01-01/objects/createreferringphysicianpayload)

[`deleteReferringPhysicianPayload.referringPhysician`](/reference/2026-01-01/objects/deletereferringphysicianpayload)

[`updateReferringPhysicianPayload.referring_physician`](/reference/2026-01-01/objects/updatereferringphysicianpayload)

## Definition

```
"""
a referring physician
"""
type ReferringPhysician {
  """
  """
  accepts_insurance: Boolean


  """
  Business Name of physician
  """
  business_name: String


  """
  created at
  """
  created_at: ISO8601DateTime!


  """
  email of physician
  """
  email: String


  """
  fax number of physician
  """
  fax_number: String


  """
  first name of physician
  """
  first_name: String


  """
  full name of physician
  """
  full_name: String


  """
  The unique identifier of the physician
  """
  id: ID!


  """
  last name of physician
  """
  last_name: String


  """
  The associated location
  """
  location: Location


  """
  location id
  """
  location_id: ID


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000.
  """
  metadata: String


  """
  Dietitian's notes
  """
  notes: String


  """
  npi of physician
  """
  npi: String


  """
  Saved Other ID associated with this provider
  """
  other_id: String


  """
  Qualifier for Other ID
  """
  other_id_qualifier: String


  """
  phone number of physician
  """
  phone_number: String


  """
  The user who entered the referring physician
  """
  provider: User!


  """
  Associated users
  """
  referrals: [Referral!]


  """
  Associated users count
  """
  referrals_count: Int


  """
  Physician's speciality
  """
  speciality: String


  """
  updated at
  """
  updated_at: ISO8601DateTime!


  """
  Physician's website
  """
  website: String
}
```
