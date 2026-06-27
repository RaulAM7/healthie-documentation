---
title: createProcedure | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createprocedure/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createprocedure/index.md
---

Create a Procedure Object

## Arguments

[`input` ](#argument-input)· [`createProcedureInput` ](/reference/2026-01-01/input-objects/createprocedureinput)· Parameters for createProcedure

## Returns

[`createProcedurePayload`](/reference/2026-01-01/objects/createprocedurepayload)

## Example

```
mutation createProcedure($input: createProcedureInput) {
  createProcedure(input: $input) {
    messages
    procedure
  }
}
```
