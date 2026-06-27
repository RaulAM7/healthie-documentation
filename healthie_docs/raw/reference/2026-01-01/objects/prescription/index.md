---
title: Prescription | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/prescription/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/prescription/index.md
---

Prescription created in Dosespot

## Fields

[`clinic_id` ](#field-clinic-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot clinic identifier

[`comment` ](#field-comment)· [`String` ](/reference/2026-01-01/scalars/string)· Comment entered by provider

[`date_inactive` ](#field-date-inactive)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date when prescription became ineffective

[`date_written` ](#field-date-written)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date prescription was written

[`days_supply` ](#field-days-supply)· [`Int` ](/reference/2026-01-01/scalars/int)· Number of days supplied prescription should last

[`directions` ](#field-directions)· [`String` ](/reference/2026-01-01/scalars/string)· Direction provided to patient when taking prescription. Entered by provider

[`dispensable_drug_id` ](#field-dispensable-drug-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot dispensable drug identifier

[`dispense_unit_id` ](#field-dispense-unit-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot dispense unit identifier

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· Display name for the prescription

[`dosage` ](#field-dosage)· [`String` ](/reference/2026-01-01/scalars/string)· The dosage (strength) of the prescription

[`dose_form` ](#field-dose-form)· [`String` ](/reference/2026-01-01/scalars/string)· The form of the prescription. Example: tablet, capsule, teaspoon

[`drug_classification` ](#field-drug-classification)· [`String` ](/reference/2026-01-01/scalars/string)· The classification of the drug

[`effective_date` ](#field-effective-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date when prescription became effective

[`eligibility_id` ](#field-eligibility-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot eligibility identifier

[`encounter` ](#field-encounter)· [`String` ](/reference/2026-01-01/scalars/string)· Encounter entered by provider

[`error_ignored` ](#field-error-ignored)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if Transmission Error; otherwise it is false

[`first_prescription_diagnosis` ](#field-first-prescription-diagnosis)· [`[PrescriptionDiagnosis!]` ](/reference/2026-01-01/objects/prescriptiondiagnosis)· First prescription diagnosis in dosespot

[`formulary` ](#field-formulary)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the prescription was added after a patient's eligibility is retrieved; otherwise, it is false

[`free_text_type` ](#field-free-text-type)· [`String` ](/reference/2026-01-01/scalars/string)· Free text type information

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the prescription

[`is_rx_renewal` ](#field-is-rx-renewal)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether this is a renewal prescription

[`is_urgent` ](#field-is-urgent)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If the prescription is urgent

[`last_fill_date` ](#field-last-fill-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date prescription was last refilled

[`medication_status` ](#field-medication-status)· [`String` ](/reference/2026-01-01/scalars/string)· Patient Medication Status

[`monograph_path` ](#field-monograph-path)· [`String` ](/reference/2026-01-01/scalars/string)· Monograph path entered by provider

deprecated

Deprecated by vendor, use MedicationOptionType.monograph instead

[`ndc` ](#field-ndc)· [`String` ](/reference/2026-01-01/scalars/string)· The prescription's national drug code

[`no_substitutions` ](#field-no-substitutions)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, pharmacy has been instructed not to dispense a substitute/generic version

[`non_dose_spot_prescription_id` ](#field-non-dose-spot-prescription-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Non-DoseSpot prescription reference identifier

[`normalized_status` ](#field-normalized-status)· [`PrescriptionMedicationStatus` ](/reference/2026-01-01/enums/prescriptionmedicationstatus)· The normalized status of the prescription

[`otc` ](#field-otc)· [`String` ](/reference/2026-01-01/scalars/string)· Over the counter drug

[`patient_medication_id` ](#field-patient-medication-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot patient medication identifier

[`pharmacy` ](#field-pharmacy)· [`Pharmacy` ](/reference/2026-01-01/objects/pharmacy)· Pharmacy information assigned in dosespot (Not stored in db)

[`pharmacy_notes` ](#field-pharmacy-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Notes for pharmacy entered by provider

[`prescriber_agent_id` ](#field-prescriber-agent-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot prescriber agent identifier

[`prescriber_id` ](#field-prescriber-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot prescriber identifier

[`prescriber_name` ](#field-prescriber-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the prescriber

[`product_name` ](#field-product-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name and dosage of the prescription. Example: ibuprofen 200 mg tablet

[`quantity` ](#field-quantity)· [`String` ](/reference/2026-01-01/scalars/string)· Quantity of medication per refill

[`refills` ](#field-refills)· [`String` ](/reference/2026-01-01/scalars/string)· Number of refills prescribed

[`route` ](#field-route)· [`String` ](/reference/2026-01-01/scalars/string)· Form in which prescription is delivered

[`rx_reference_number` ](#field-rx-reference-number)· [`String` ](/reference/2026-01-01/scalars/string)· The prescription reference number

[`rx_renewal_note` ](#field-rx-renewal-note)· [`String` ](/reference/2026-01-01/scalars/string)· Notes about the prescription renewal

[`rxcui` ](#field-rxcui)· [`String` ](/reference/2026-01-01/scalars/string)· The prescription rxcui

[`schedule` ](#field-schedule)· [`String` ](/reference/2026-01-01/scalars/string)· Controlled substance schedule

[`second_prescription_diagnosis` ](#field-second-prescription-diagnosis)· [`[PrescriptionDiagnosis!]` ](/reference/2026-01-01/objects/prescriptiondiagnosis)· Second prescription diagnosis in dosespot

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· Status of prescription. Example: Entered, Printed, Sending, eRxSent, Deleted

[`supervisor_id` ](#field-supervisor-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot supervisor identifier

[`supply_id` ](#field-supply-id)· [`ID` ](/reference/2026-01-01/scalars/id)· DoseSpot supply identifier

[`type` ](#field-type)· [`String` ](/reference/2026-01-01/scalars/string)· Prescription type. Example: Coded, Supply, Compound

[`unit` ](#field-unit)· [`String` ](/reference/2026-01-01/scalars/string)· Unit of medication. Example: tablet, capsule, teaspoon

## Used By

[`FormAnswerGroup.form_answer_group_prescriptions`](/reference/2026-01-01/objects/formanswergroup)

[`Query.prescription`](/reference/2026-01-01/queries/prescription)

[`Query.prescriptions`](/reference/2026-01-01/queries/prescriptions)

## Definition

```
"""
Prescription created in Dosespot
"""
type Prescription {
  """
  DoseSpot clinic identifier
  """
  clinic_id: ID


  """
  Comment entered by provider
  """
  comment: String


  """
  Date when prescription became ineffective
  """
  date_inactive: ISO8601DateTime


  """
  Date prescription was written
  """
  date_written: ISO8601DateTime


  """
  Number of days supplied prescription should last
  """
  days_supply: Int


  """
  Direction provided to patient when taking prescription. Entered by provider
  """
  directions: String


  """
  DoseSpot dispensable drug identifier
  """
  dispensable_drug_id: ID


  """
  DoseSpot dispense unit identifier
  """
  dispense_unit_id: ID


  """
  Display name for the prescription
  """
  display_name: String


  """
  The dosage (strength) of the prescription
  """
  dosage: String


  """
  The form of the prescription. Example: tablet, capsule, teaspoon
  """
  dose_form: String


  """
  The classification of the drug
  """
  drug_classification: String


  """
  Date when prescription became effective
  """
  effective_date: ISO8601DateTime


  """
  DoseSpot eligibility identifier
  """
  eligibility_id: ID


  """
  Encounter entered by provider
  """
  encounter: String


  """
  True if Transmission Error; otherwise it is false
  """
  error_ignored: Boolean


  """
  First prescription diagnosis in dosespot
  """
  first_prescription_diagnosis: [PrescriptionDiagnosis!]


  """
  True if the prescription was added after a patient's eligibility is retrieved; otherwise, it is false
  """
  formulary: Boolean


  """
  Free text type information
  """
  free_text_type: String


  """
  The unique identifier of the prescription
  """
  id: ID!


  """
  Whether this is a renewal prescription
  """
  is_rx_renewal: Boolean


  """
  If the prescription is urgent
  """
  is_urgent: Boolean


  """
  Date prescription was last refilled
  """
  last_fill_date: ISO8601DateTime


  """
  Patient Medication Status
  """
  medication_status: String


  """
  Monograph path entered by provider
  """
  monograph_path: String
    @deprecated(
      reason: "Deprecated by vendor, use MedicationOptionType.monograph instead"
    )


  """
  The prescription's national drug code
  """
  ndc: String


  """
  If true, pharmacy has been instructed not to dispense a substitute/generic version
  """
  no_substitutions: Boolean


  """
  Non-DoseSpot prescription reference identifier
  """
  non_dose_spot_prescription_id: ID


  """
  The normalized status of the prescription
  """
  normalized_status: PrescriptionMedicationStatus


  """
  Over the counter drug
  """
  otc: String


  """
  DoseSpot patient medication identifier
  """
  patient_medication_id: ID


  """
  Pharmacy information assigned in dosespot (Not stored in db)
  """
  pharmacy: Pharmacy


  """
  Notes for pharmacy entered by provider
  """
  pharmacy_notes: String


  """
  DoseSpot prescriber agent identifier
  """
  prescriber_agent_id: ID


  """
  DoseSpot prescriber identifier
  """
  prescriber_id: ID


  """
  The name of the prescriber
  """
  prescriber_name: String


  """
  Name and dosage of the prescription. Example: ibuprofen 200 mg tablet
  """
  product_name: String


  """
  Quantity of medication per refill
  """
  quantity: String


  """
  Number of refills prescribed
  """
  refills: String


  """
  Form in which prescription is delivered
  """
  route: String


  """
  The prescription reference number
  """
  rx_reference_number: String


  """
  Notes about the prescription renewal
  """
  rx_renewal_note: String


  """
  The prescription rxcui
  """
  rxcui: String


  """
  Controlled substance schedule
  """
  schedule: String


  """
  Second prescription diagnosis in dosespot
  """
  second_prescription_diagnosis: [PrescriptionDiagnosis!]


  """
  Status of prescription. Example: Entered, Printed, Sending, eRxSent, Deleted
  """
  status: String


  """
  DoseSpot supervisor identifier
  """
  supervisor_id: ID


  """
  DoseSpot supply identifier
  """
  supply_id: ID


  """
  Prescription type. Example: Coded, Supply, Compound
  """
  type: String


  """
  Unit of medication. Example: tablet, capsule, teaspoon
  """
  unit: String
}
```
