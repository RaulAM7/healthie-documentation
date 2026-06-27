---
title: linkEncounterToEpisodeOfCare | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/linkencountertoepisodeofcare/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/linkencountertoepisodeofcare/index.md
---

Link patient encounter(s) to an Episode of Care

## Arguments

[`input` ](#argument-input)· [`linkEncounterToEpisodeOfCareInput` ](/reference/2026-01-01/input-objects/linkencountertoepisodeofcareinput)· Parameters for linkEncounterToEpisodeOfCare

## Returns

[`linkEncounterToEpisodeOfCarePayload`](/reference/2026-01-01/objects/linkencountertoepisodeofcarepayload)

## Example

```
mutation linkEncounterToEpisodeOfCare(
  $input: linkEncounterToEpisodeOfCareInput
) {
  linkEncounterToEpisodeOfCare(input: $input) {
    messages
    results
  }
}
```
