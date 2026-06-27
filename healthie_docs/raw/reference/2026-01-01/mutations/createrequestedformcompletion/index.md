---
title: createRequestedFormCompletion | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createrequestedformcompletion/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createrequestedformcompletion/index.md
---

create requested form, creates the RequestedFormCompletion in the background and returns only a status message unless using the legacy recipient\_id argument which returns the created RequestedFormCompletion

## Arguments

[`input` ](#argument-input)· [`createRequestedFormInput` ](/reference/2026-01-01/input-objects/createrequestedforminput)· Parameters for createRequestedForm

## Returns

[`createRequestedFormPayload`](/reference/2026-01-01/objects/createrequestedformpayload)

## Example

```
mutation createRequestedFormCompletion($input: createRequestedFormInput) {
  createRequestedFormCompletion(input: $input) {
    messages
    requestedFormCompletion
    requestedFormCompletionStatus
  }
}
```
