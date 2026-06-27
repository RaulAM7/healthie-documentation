---
title: createFaxLineRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfaxlinerequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfaxlinerequest/index.md
---

Create and return a fax line request

## Arguments

[`input` ](#argument-input)· [`createFaxLineRequestInput` ](/reference/2026-01-01/input-objects/createfaxlinerequestinput)· Parameters for createFaxLineRequest

## Returns

[`createFaxLineRequestPayload`](/reference/2026-01-01/objects/createfaxlinerequestpayload)

## Example

```
mutation createFaxLineRequest($input: createFaxLineRequestInput) {
  createFaxLineRequest(input: $input) {
    faxLineRequest
    messages
  }
}
```
