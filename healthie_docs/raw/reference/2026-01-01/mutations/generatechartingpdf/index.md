---
title: generateChartingPdf | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/generatechartingpdf/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/generatechartingpdf/index.md
---

Generate a PDF of charting notes for a client

## Arguments

[`input` ](#argument-input)· [`generateChartingPdfInput` ](/reference/2026-01-01/input-objects/generatechartingpdfinput)· Parameters for generateChartingPdf

## Returns

[`generateChartingPdfPayload`](/reference/2026-01-01/objects/generatechartingpdfpayload)

## Example

```
mutation generateChartingPdf($input: generateChartingPdfInput) {
  generateChartingPdf(input: $input) {
    messages
    user
  }
}
```
