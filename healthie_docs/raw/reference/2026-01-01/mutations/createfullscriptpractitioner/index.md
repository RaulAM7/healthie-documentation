---
title: createFullscriptPractitioner | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfullscriptpractitioner/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfullscriptpractitioner/index.md
---

Create a Fullscript practitioner account using the Fullscript API

## Arguments

[`input` ](#argument-input)· [`createFullscriptPractitionerInput` ](/reference/2026-01-01/input-objects/createfullscriptpractitionerinput)· Parameters for createFullscriptPractitioner

## Returns

[`createFullscriptPractitionerPayload`](/reference/2026-01-01/objects/createfullscriptpractitionerpayload)

## Example

```
mutation createFullscriptPractitioner(
  $input: createFullscriptPractitionerInput
) {
  createFullscriptPractitioner(input: $input) {
    fullscript_practitioner
    messages
  }
}
```
