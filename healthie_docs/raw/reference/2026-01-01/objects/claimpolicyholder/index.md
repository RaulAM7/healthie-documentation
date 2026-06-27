---
title: ClaimPolicyHolder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimpolicyholder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimpolicyholder/index.md
---

Insurance subscriber (policyholder) data from a submitted claim snapshot

## Fields

[`date_of_birth` ](#field-date-of-birth)· [`String` ](/reference/2026-01-01/scalars/string)· Date of birth

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· First name

[`gender` ](#field-gender)· [`String` ](/reference/2026-01-01/scalars/string)· Gender

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· Last name

[`location` ](#field-location)· [`ClaimLocation` ](/reference/2026-01-01/objects/claimlocation)· Address at time of submission

[`middle_initial` ](#field-middle-initial)· [`String` ](/reference/2026-01-01/scalars/string)· Middle initial

[`phone` ](#field-phone)· [`String` ](/reference/2026-01-01/scalars/string)· Phone number

[`relationship` ](#field-relationship)· [`HolderRelationship` ](/reference/2026-01-01/enums/holderrelationship)· Relationship to patient

## Used By

[`ClaimPolicy.holder`](/reference/2026-01-01/objects/claimpolicy)

## Definition

```
"""
Insurance subscriber (policyholder) data from a submitted claim snapshot
"""
type ClaimPolicyHolder {
  """
  Date of birth
  """
  date_of_birth: String


  """
  First name
  """
  first_name: String


  """
  Gender
  """
  gender: String


  """
  Last name
  """
  last_name: String


  """
  Address at time of submission
  """
  location: ClaimLocation


  """
  Middle initial
  """
  middle_initial: String


  """
  Phone number
  """
  phone: String


  """
  Relationship to patient
  """
  relationship: HolderRelationship
}
```
