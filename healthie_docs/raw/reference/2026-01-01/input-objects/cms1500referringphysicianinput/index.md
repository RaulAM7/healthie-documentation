---
title: Cms1500ReferringPhysicianInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cms1500referringphysicianinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cms1500referringphysicianinput/index.md
---

Payload for referring physician

## Fields

[`full_name` ](#field-full-name)· [`String` ](/reference/2026-01-01/scalars/string)· The full name of the referring physician

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the referring physician

## Used By

[`PatientInput.referring_physicians`](/reference/2026-01-01/input-objects/patientinput)

## Definition

```
"""
Payload for referring physician
"""
input Cms1500ReferringPhysicianInput {
  """
  The full name of the referring physician
  """
  full_name: String


  """
  The ID of the referring physician
  """
  id: ID
}
```
