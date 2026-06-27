---
title: PatientInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/patientinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/patientinput/index.md
---

Payload for a patient

## Fields

[`dob` ](#field-dob)· [`String` ](/reference/2026-01-01/scalars/string)· The date of birth of the patient

[`gender` ](#field-gender)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: The gender of the patient

deprecated

Deprecated

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the patient

[`location` ](#field-location)· [`LocationInput` ](/reference/2026-01-01/input-objects/locationinput)· The location of the patient

[`policies` ](#field-policies)· [`[PolicyInput]` ](/reference/2026-01-01/input-objects/policyinput)· The list of policies of the patient

[`referring_physicians` ](#field-referring-physicians)· [`[Cms1500ReferringPhysicianInput]` ](/reference/2026-01-01/input-objects/cms1500referringphysicianinput)· The list of referring physicians of the patient

[`sex` ](#field-sex)· [`String` ](/reference/2026-01-01/scalars/string)· The sex of the patient

[`ssn` ](#field-ssn)· [`String` ](/reference/2026-01-01/scalars/string)· The social security number of the patient

[`full_legal_name_with_preferred` ](#field-full-legal-name-with-preferred)· [`String` ](/reference/2026-01-01/scalars/string)· The full legal name and preferred name of the patient

## Used By

[`createCms1500Input.patient`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.patient`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for a patient
"""
input PatientInput {
  """
  The date of birth of the patient
  """
  dob: String


  """
  DEPRECATED: The gender of the patient
  """
  gender: String @deprecated(reason: "Deprecated")


  """
  The ID of the patient
  """
  id: ID


  """
  The location of the patient
  """
  location: LocationInput


  """
  The list of policies of the patient
  """
  policies: [PolicyInput]


  """
  The list of referring physicians of the patient
  """
  referring_physicians: [Cms1500ReferringPhysicianInput]


  """
  The sex of the patient
  """
  sex: String


  """
  The social security number of the patient
  """
  ssn: String


  """
  The full legal name and preferred name of the patient
  """
  full_legal_name_with_preferred: String
}
```
