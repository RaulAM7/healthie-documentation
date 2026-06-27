---
title: medication_option | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/medication-option/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/medication-option/index.md
---

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

## Returns

[`MedicationOptionType`](/reference/2026-01-01/objects/medicationoptiontype)

## Example

```
query medication_option($id: ID!) {
  medication_option(id: $id) {
    dosage_options
    dosages
    id
    monograph
    name
  }
}
```
