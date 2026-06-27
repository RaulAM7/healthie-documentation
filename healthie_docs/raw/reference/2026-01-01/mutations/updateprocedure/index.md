---
title: updateProcedure | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateprocedure/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateprocedure/index.md
---

Update a Procedure Object

## Arguments

[`input` ](#argument-input)· [`updateProcedureInput` ](/reference/2026-01-01/input-objects/updateprocedureinput)· Parameters for updateProcedure

## Returns

[`updateProcedurePayload`](/reference/2026-01-01/objects/updateprocedurepayload)

## Example

```
mutation updateProcedure($input: updateProcedureInput) {
  updateProcedure(input: $input) {
    messages
    procedure
  }
}
```
