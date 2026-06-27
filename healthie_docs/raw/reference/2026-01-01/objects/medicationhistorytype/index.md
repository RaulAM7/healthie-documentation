---
title: MedicationHistoryType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationhistorytype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationhistorytype/index.md
---

Medication history record from Surescripts via DoseSpot

## Fields

[`days_supply` ](#field-days-supply)· [`Int` ](/reference/2026-01-01/scalars/int)· Number of days the medication supply should last

[`directions` ](#field-directions)· [`String` ](/reference/2026-01-01/scalars/string)· Instructions for taking the medication

[`dispensable_drug_id` ](#field-dispensable-drug-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot dispensable drug identifier

[`dispense_unit_description` ](#field-dispense-unit-description)· [`String` ](/reference/2026-01-01/scalars/string)· Description of the dispense unit (e.g., Tablets)

[`display_name` ](#field-display-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The display name of the medication

[`dose_form` ](#field-dose-form)· [`String` ](/reference/2026-01-01/scalars/string)· The form of the medication (e.g., Tablet, Capsule)

[`drug_classification` ](#field-drug-classification)· [`String` ](/reference/2026-01-01/scalars/string)· The drug classification (e.g., ANTIHYPERTENSIVE)

[`effective_date` ](#field-effective-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Date medication was effective

[`expiration_date` ](#field-expiration-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Expiration date of medication

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · DoseSpot's unique identifier for patient medication history

[`last_fill_date` ](#field-last-fill-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date medication was last filled

[`ndc` ](#field-ndc)· [`ID` ](/reference/2026-01-01/scalars/id)· National Drug Code (drug identifier)

[`no_substitutions` ](#field-no-substitutions)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether substitutions were allowed for this medication

[`otc` ](#field-otc)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether this is an over-the-counter medication

[`payer` ](#field-payer)· [`String` ](/reference/2026-01-01/scalars/string)· PBM/Payer name

[`pharmacy_notes` ](#field-pharmacy-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Additional notes from the pharmacy

[`quantity` ](#field-quantity)· [`String` ](/reference/2026-01-01/scalars/string)· The quantity of medication prescribed

[`refills` ](#field-refills)· [`String` ](/reference/2026-01-01/scalars/string)· Number of refills allowed

[`route` ](#field-route)· [`String` ](/reference/2026-01-01/scalars/string)· Method of administration (e.g., Oral)

[`rxcui` ](#field-rxcui)· [`ID` ](/reference/2026-01-01/scalars/id)· RxNorm Concept Unique Identifier

[`schedule` ](#field-schedule)· [`String` ](/reference/2026-01-01/scalars/string)· DEA controlled substance schedule

[`written_date` ](#field-written-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date when the prescription was written

## Used By

[`MedicationHistoryTypeEdge.node`](/reference/2026-01-01/objects/medicationhistorytypeedge)

[`MedicationHistoryTypePaginationConnection.nodes`](/reference/2026-01-01/objects/medicationhistorytypepaginationconnection)

## Definition

```
"""
Medication history record from Surescripts via DoseSpot
"""
type MedicationHistoryType {
  """
  Number of days the medication supply should last
  """
  days_supply: Int


  """
  Instructions for taking the medication
  """
  directions: String


  """
  DoseSpot dispensable drug identifier
  """
  dispensable_drug_id: ID


  """
  Description of the dispense unit (e.g., Tablets)
  """
  dispense_unit_description: String


  """
  The display name of the medication
  """
  display_name: String!


  """
  The form of the medication (e.g., Tablet, Capsule)
  """
  dose_form: String


  """
  The drug classification (e.g., ANTIHYPERTENSIVE)
  """
  drug_classification: String


  """
  Date medication was effective
  """
  effective_date: ISO8601Date


  """
  Expiration date of medication
  """
  expiration_date: ISO8601DateTime


  """
  DoseSpot's unique identifier for patient medication history
  """
  id: ID!


  """
  Date medication was last filled
  """
  last_fill_date: ISO8601DateTime


  """
  National Drug Code (drug identifier)
  """
  ndc: ID


  """
  Whether substitutions were allowed for this medication
  """
  no_substitutions: Boolean!


  """
  Whether this is an over-the-counter medication
  """
  otc: Boolean!


  """
  PBM/Payer name
  """
  payer: String


  """
  Additional notes from the pharmacy
  """
  pharmacy_notes: String


  """
  The quantity of medication prescribed
  """
  quantity: String


  """
  Number of refills allowed
  """
  refills: String


  """
  Method of administration (e.g., Oral)
  """
  route: String


  """
  RxNorm Concept Unique Identifier
  """
  rxcui: ID


  """
  DEA controlled substance schedule
  """
  schedule: String


  """
  The date when the prescription was written
  """
  written_date: ISO8601DateTime
}
```
