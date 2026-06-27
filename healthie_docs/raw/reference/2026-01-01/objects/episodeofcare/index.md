---
title: EpisodeOfCare | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/episodeofcare/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/episodeofcare/index.md
---

The episode of care for a patient encounter

## Fields

[`diagnosis` ](#field-diagnosis)· [`Diagnosis` ](/reference/2026-01-01/objects/diagnosis)· The diagnosis code for the episode of care

[`end_date` ](#field-end-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The end date for the episode of care

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the episode of care

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· The patient associated with the episode of care

[`patient_encounters` ](#field-patient-encounters)· [`[PatientEncounter!]` ](/reference/2026-01-01/objects/patientencounter)· All patient encounters associated with this episode of care

[`provider` ](#field-provider)· [`User` ](/reference/2026-01-01/objects/user)· The provider associated with the episode of care

[`start_date` ](#field-start-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The start date for the episode of care

## Used By

[`EpisodeOfCareConnection.nodes`](/reference/2026-01-01/objects/episodeofcareconnection)

[`EpisodeOfCareEdge.node`](/reference/2026-01-01/objects/episodeofcareedge)

[`createEpisodeOfCarePayload.episode_of_care`](/reference/2026-01-01/objects/createepisodeofcarepayload)

[`deleteEpisodeOfCarePayload.episode_of_care`](/reference/2026-01-01/objects/deleteepisodeofcarepayload)

[`updateEpisodeOfCarePayload.episode_of_care`](/reference/2026-01-01/objects/updateepisodeofcarepayload)

## Definition

```
"""
The episode of care for a patient encounter
"""
type EpisodeOfCare {
  """
  The diagnosis code for the episode of care
  """
  diagnosis: Diagnosis


  """
  The end date for the episode of care
  """
  end_date: ISO8601Date


  """
  The unique identifier of the episode of care
  """
  id: ID!


  """
  The patient associated with the episode of care
  """
  patient: User


  """
  All patient encounters associated with this episode of care
  """
  patient_encounters: [PatientEncounter!]


  """
  The provider associated with the episode of care
  """
  provider: User


  """
  The start date for the episode of care
  """
  start_date: ISO8601Date
}
```
