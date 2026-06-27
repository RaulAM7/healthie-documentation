---
title: PdfLetterheadTemplateBrandLogoSource | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplatebrandlogosource/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplatebrandlogosource/index.md
---

The source used to populate the brand logo shown on the letterhead.

## Used By

[`PdfLetterheadTemplate.brand_logo_source`](/reference/2026-01-01/objects/pdfletterheadtemplate)

[`createPdfLetterheadTemplateInput.brand_logo_source`](/reference/2026-01-01/input-objects/createpdfletterheadtemplateinput)

[`updatePdfLetterheadTemplateInput.brand_logo_source`](/reference/2026-01-01/input-objects/updatepdfletterheadtemplateinput)

## Definition

```
"""
The source used to populate the brand logo shown on the letterhead.
"""
enum PdfLetterheadTemplateBrandLogoSource {
  ORGANIZATION
  CURRENT_USER
  PRIMARY_PROVIDER
}
```
