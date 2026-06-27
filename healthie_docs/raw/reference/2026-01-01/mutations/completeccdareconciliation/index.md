---
title: completeCcdaReconciliation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/completeccdareconciliation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/completeccdareconciliation/index.md
---

Complete a CCDA Reconciliation, based on user choice

## Arguments

[`input` ](#argument-input)· [`CompleteCcdaReconciliationInput` ](/reference/2026-01-01/input-objects/completeccdareconciliationinput)· Parameters for CompleteCcdaReconciliation

## Returns

[`CompleteCcdaReconciliationPayload`](/reference/2026-01-01/objects/completeccdareconciliationpayload)

## Example

```
mutation completeCcdaReconciliation($input: CompleteCcdaReconciliationInput) {
  completeCcdaReconciliation(input: $input) {
    messages
    user
  }
}
```
