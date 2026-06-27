---
title: updateEpisodeOfCare | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateepisodeofcare/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateepisodeofcare/index.md
---

Update an Episode of Care

## Arguments

[`input` ](#argument-input)· [`updateEpisodeOfCareInput` ](/reference/2026-01-01/input-objects/updateepisodeofcareinput)· Parameters for updateEpisodeOfCare

## Returns

[`updateEpisodeOfCarePayload`](/reference/2026-01-01/objects/updateepisodeofcarepayload)

## Example

```
mutation updateEpisodeOfCare($input: updateEpisodeOfCareInput) {
  updateEpisodeOfCare(input: $input) {
    episode_of_care
    messages
  }
}
```
