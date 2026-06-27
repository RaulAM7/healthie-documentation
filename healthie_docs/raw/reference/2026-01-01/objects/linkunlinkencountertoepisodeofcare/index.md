---
title: LinkUnlinkEncounterToEpisodeOfCare | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/linkunlinkencountertoepisodeofcare/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/linkunlinkencountertoepisodeofcare/index.md
---

Link/Unlink type for patient encounter and episode of care

## Fields

[`episode_of_care_id` ](#field-episode-of-care-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the episode of care

[`failed_reason` ](#field-failed-reason)· [`String` ](/reference/2026-01-01/scalars/string)· Short description if the linking/unlinking failed

[`patient_encounter_id` ](#field-patient-encounter-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier for the patient encounter

[`success` ](#field-success)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not the link/unlinking was successful

## Used By

[`linkEncounterToEpisodeOfCarePayload.results`](/reference/2026-01-01/objects/linkencountertoepisodeofcarepayload)

[`unlinkEncounterToEpisodeOfCarePayload.results`](/reference/2026-01-01/objects/unlinkencountertoepisodeofcarepayload)

## Definition

```
"""
Link/Unlink type for patient encounter and episode of care
"""
type LinkUnlinkEncounterToEpisodeOfCare {
  """
  The unique identifier of the episode of care
  """
  episode_of_care_id: ID


  """
  Short description if the linking/unlinking failed
  """
  failed_reason: String


  """
  The unique identifier for the patient encounter
  """
  patient_encounter_id: ID


  """
  Whether or not the link/unlinking was successful
  """
  success: Boolean
}
```
