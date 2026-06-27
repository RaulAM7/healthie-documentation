---
title: createImportDataRequest | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createimportdatarequest/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createimportdatarequest/index.md
---

Create an import data request

## Arguments

[`input` ](#argument-input)· [`createImportDataRequestInput` ](/reference/2026-01-01/input-objects/createimportdatarequestinput)· Parameters for createImportDataRequest

## Returns

[`createImportDataRequestPayload`](/reference/2026-01-01/objects/createimportdatarequestpayload)

## Example

```
mutation createImportDataRequest($input: createImportDataRequestInput) {
  createImportDataRequest(input: $input) {
    importDataRequest
    messages
  }
}
```
