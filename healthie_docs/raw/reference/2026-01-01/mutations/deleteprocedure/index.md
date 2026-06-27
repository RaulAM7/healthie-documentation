---
title: deleteProcedure | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteprocedure/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteprocedure/index.md
---

Delete a Procedure Object

## Arguments

[`input` ](#argument-input)· [`deleteProcedureInput` ](/reference/2026-01-01/input-objects/deleteprocedureinput)· Parameters for deleteProcedure

## Returns

[`deleteProcedurePayload`](/reference/2026-01-01/objects/deleteprocedurepayload)

## Example

```
mutation deleteProcedure($input: deleteProcedureInput) {
  deleteProcedure(input: $input) {
    messages
    procedure
  }
}
```
