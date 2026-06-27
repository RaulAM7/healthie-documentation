---
title: logMedicationHistoryConsent | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/logmedicationhistoryconsent/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/logmedicationhistoryconsent/index.md
---

Log that a patient has consented to having their medication history pulled via Surescripts/Dosespot

## Arguments

[`input` ](#argument-input)· [`logMedicationHistoryConsentInput` ](/reference/2026-01-01/input-objects/logmedicationhistoryconsentinput)· Parameters for logMedicationHistoryConsent

## Returns

[`logMedicationHistoryConsentPayload`](/reference/2026-01-01/objects/logmedicationhistoryconsentpayload)

## Example

```
mutation logMedicationHistoryConsent($input: logMedicationHistoryConsentInput) {
  logMedicationHistoryConsent(input: $input) {
    consented_at
    messages
  }
}
```
