---
title: unlinkEncounterToEpisodeOfCare | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/unlinkencountertoepisodeofcare/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/unlinkencountertoepisodeofcare/index.md
---

Unlink patient encounter(s) from an Episode of Care

## Arguments

[`input` ](#argument-input)· [`unlinkEncounterToEpisodeOfCareInput` ](/reference/2026-01-01/input-objects/unlinkencountertoepisodeofcareinput)· Parameters for unlinkEncounterToEpisodeOfCare

## Returns

[`unlinkEncounterToEpisodeOfCarePayload`](/reference/2026-01-01/objects/unlinkencountertoepisodeofcarepayload)

## Example

```
mutation unlinkEncounterToEpisodeOfCare(
  $input: unlinkEncounterToEpisodeOfCareInput
) {
  unlinkEncounterToEpisodeOfCare(input: $input) {
    messages
    results
  }
}
```
