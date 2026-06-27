---
title: ingestMedicationsFromSurescripts | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/ingestmedicationsfromsurescripts/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/ingestmedicationsfromsurescripts/index.md
---

ingest med history from surescripts

## Arguments

[`input` ](#argument-input)· [`ingestMedicationsFromSurescriptsInput` ](/reference/2026-01-01/input-objects/ingestmedicationsfromsurescriptsinput)· Parameters for ingestMedicationsFromSurescripts

## Returns

[`ingestMedicationsFromSurescriptsPayload`](/reference/2026-01-01/objects/ingestmedicationsfromsurescriptspayload)

## Example

```
mutation ingestMedicationsFromSurescripts(
  $input: ingestMedicationsFromSurescriptsInput
) {
  ingestMedicationsFromSurescripts(input: $input) {
    messages
    success_string
  }
}
```
