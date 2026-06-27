---
title: createEpisodeOfCare | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createepisodeofcare/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createepisodeofcare/index.md
---

Create an Episode of Care

## Arguments

[`input` ](#argument-input)· [`createEpisodeOfCareInput` ](/reference/2026-01-01/input-objects/createepisodeofcareinput)· Parameters for createEpisodeOfCare

## Returns

[`createEpisodeOfCarePayload`](/reference/2026-01-01/objects/createepisodeofcarepayload)

## Example

```
mutation createEpisodeOfCare($input: createEpisodeOfCareInput) {
  createEpisodeOfCare(input: $input) {
    episode_of_care
    messages
  }
}
```
