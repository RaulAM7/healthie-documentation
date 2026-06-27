---
title: MedicationType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationtype/index.md
---

Medication belonging to client

## Fields

[`active` ](#field-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicates if medication is still active (medication can also be inactive if current date doesn't fall between start and end date)

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· CCDA code for this medication

[`comment` ](#field-comment)· [`String` ](/reference/2026-01-01/scalars/string)· Comments entered by provider

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the medication was created

[`directions` ](#field-directions)· [`String` ](/reference/2026-01-01/scalars/string)· Directions to use medication entered by provider

[`dosage` ](#field-dosage)· [`String` ](/reference/2026-01-01/scalars/string)· Dosage of medication entered by provider

[`end_date` ](#field-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· last date patient should be able to use medication

[`frequency` ](#field-frequency)· [`String` ](/reference/2026-01-01/scalars/string)· Frequency of this medication

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the medication

[`mirrored` ](#field-mirrored)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If the medication is synchronized with an external system (e.g., an E-Rx system)

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of medication

[`normalized_status` ](#field-normalized-status)· [`PrescriptionMedicationStatus` ](/reference/2026-01-01/enums/prescriptionmedicationstatus)· The normalized status of the medication

[`requires_consolidation` ](#field-requires-consolidation)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, this object must be consolidated as part of a CCDA Ingest

[`route` ](#field-route)· [`String` ](/reference/2026-01-01/scalars/string)· The way this medication is administered

[`start_date` ](#field-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· First active date of medication

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last time the medication was updated

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· User ID of the client this medication belongs to

## Used By

[`MedicationTypeEdge.node`](/reference/2026-01-01/objects/medicationtypeedge)

[`MedicationTypePaginationConnection.nodes`](/reference/2026-01-01/objects/medicationtypepaginationconnection)

[`createMedicationPayload.medication`](/reference/2026-01-01/objects/createmedicationpayload)

[`destroyMedicationPayload.medication`](/reference/2026-01-01/objects/destroymedicationpayload)

[`updateMedicationPayload.medication`](/reference/2026-01-01/objects/updatemedicationpayload)

[`Query.medication`](/reference/2026-01-01/queries/medication)

## Definition

```
"""
Medication belonging to client
"""
type MedicationType {
  """
  Indicates if medication is still active (medication can also be inactive if current date doesn't fall between start and end date)
  """
  active: Boolean


  """
  CCDA code for this medication
  """
  code: String


  """
  Comments entered by provider
  """
  comment: String


  """
  The time the medication was created
  """
  created_at: ISO8601DateTime!


  """
  Directions to use medication entered by provider
  """
  directions: String


  """
  Dosage of medication entered by provider
  """
  dosage: String


  """
  last date patient should be able to use medication
  """
  end_date: ISO8601DateTime


  """
  Frequency of this medication
  """
  frequency: String


  """
  The unique identifier of the medication
  """
  id: ID!


  """
  If the medication is synchronized with an external system (e.g., an E-Rx system)
  """
  mirrored: Boolean!


  """
  Name of medication
  """
  name: String


  """
  The normalized status of the medication
  """
  normalized_status: PrescriptionMedicationStatus


  """
  When true, this object must be consolidated as part of a CCDA Ingest
  """
  requires_consolidation: Boolean


  """
  The way this medication is administered
  """
  route: String


  """
  First active date of medication
  """
  start_date: ISO8601DateTime


  """
  The last time the medication was updated
  """
  updated_at: ISO8601DateTime


  """
  User ID of the client this medication belongs to
  """
  user_id: ID
}
```
