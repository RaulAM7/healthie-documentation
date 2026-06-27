---
title: pdfLetterheadTemplatePreview | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/pdfletterheadtemplatepreview/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/pdfletterheadtemplatepreview/index.md
---

PDF Letterhead HTML String. Falls back to the system default template unless \`pdf\_letterhead\_template\_id\` is given

## Arguments

[`pdf_letterhead_template_id` ](#argument-pdf-letterhead-template-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`patient_id` ](#argument-patient-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query pdfLetterheadTemplatePreview(
  $pdf_letterhead_template_id: ID
  $patient_id: ID
) {
  pdfLetterheadTemplatePreview(
    pdf_letterhead_template_id: $pdf_letterhead_template_id
    patient_id: $patient_id
  )
}
```
