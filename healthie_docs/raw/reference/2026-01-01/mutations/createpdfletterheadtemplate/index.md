---
title: createPdfLetterheadTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpdfletterheadtemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpdfletterheadtemplate/index.md
---

Create \`PdfLetterheadTemplate\`

## Arguments

[`input` ](#argument-input)· [`createPdfLetterheadTemplateInput` ](/reference/2026-01-01/input-objects/createpdfletterheadtemplateinput)· Parameters for createPdfLetterheadTemplate

## Returns

[`createPdfLetterheadTemplatePayload`](/reference/2026-01-01/objects/createpdfletterheadtemplatepayload)

## Example

```
mutation createPdfLetterheadTemplate($input: createPdfLetterheadTemplateInput) {
  createPdfLetterheadTemplate(input: $input) {
    messages
    organization
    pdf_letterhead_template
  }
}
```
