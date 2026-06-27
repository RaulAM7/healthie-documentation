---
title: ClaimPatient | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimpatient/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimpatient/index.md
---

Frozen patient data from a submitted claim snapshot

## Fields

[`dob` ](#field-dob)· [`String` ](/reference/2026-01-01/scalars/string)· Date of birth

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· First name

[`full_name` ](#field-full-name)· [`String` ](/reference/2026-01-01/scalars/string)· Full name

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Patient ID

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· Last name

[`location` ](#field-location)· [`ClaimLocation` ](/reference/2026-01-01/objects/claimlocation)· Patient address at time of submission

[`sex` ](#field-sex)· [`String` ](/reference/2026-01-01/scalars/string)· Biological sex (CMS-1500 Box 3)

## Used By

[`Claim.patient`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
Frozen patient data from a submitted claim snapshot
"""
type ClaimPatient {
  """
  Date of birth
  """
  dob: String


  """
  First name
  """
  first_name: String


  """
  Full name
  """
  full_name: String


  """
  Patient ID
  """
  id: ID


  """
  Last name
  """
  last_name: String


  """
  Patient address at time of submission
  """
  location: ClaimLocation


  """
  Biological sex (CMS-1500 Box 3)
  """
  sex: String
}
```
