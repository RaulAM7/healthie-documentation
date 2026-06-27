---
title: deleteEpisodeOfCare | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteepisodeofcare/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteepisodeofcare/index.md
---

Delete an Episode of Care

## Arguments

[`input` ](#argument-input)· [`deleteEpisodeOfCareInput` ](/reference/2026-01-01/input-objects/deleteepisodeofcareinput)· Parameters for deleteEpisodeOfCare

## Returns

[`deleteEpisodeOfCarePayload`](/reference/2026-01-01/objects/deleteepisodeofcarepayload)

## Example

```
mutation deleteEpisodeOfCare($input: deleteEpisodeOfCareInput) {
  deleteEpisodeOfCare(input: $input) {
    episode_of_care
    messages
  }
}
```
