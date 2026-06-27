---
title: medication_options | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/medication-options/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/medication-options/index.md
---

Fetch an array of medications options. Considered Public

## Arguments

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Search term used to look up medications in Dosespot. Must be at least 3 characters (otherwise returns null).

## Returns

[`[MedicationOptionType!]`](/reference/2026-01-01/objects/medicationoptiontype)

## Example

```
query medication_options($keywords: String) {
  medication_options(keywords: $keywords) {
    dosage_options
    dosages
    id
    monograph
    name
  }
}
```
