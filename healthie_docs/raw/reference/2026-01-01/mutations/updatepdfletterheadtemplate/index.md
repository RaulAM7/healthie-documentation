---
title: updatePdfLetterheadTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatepdfletterheadtemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatepdfletterheadtemplate/index.md
---

Update \`PdfLetterheadTemplate\`

## Arguments

[`input` ](#argument-input)· [`updatePdfLetterheadTemplateInput` ](/reference/2026-01-01/input-objects/updatepdfletterheadtemplateinput)· Parameters for updatePdfLetterheadTemplate

## Returns

[`updatePdfLetterheadTemplatePayload`](/reference/2026-01-01/objects/updatepdfletterheadtemplatepayload)

## Example

```
mutation updatePdfLetterheadTemplate($input: updatePdfLetterheadTemplateInput) {
  updatePdfLetterheadTemplate(input: $input) {
    messages
    organization
    pdf_letterhead_template
  }
}
```
