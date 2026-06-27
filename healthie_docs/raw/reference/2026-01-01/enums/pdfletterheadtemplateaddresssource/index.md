---
title: PdfLetterheadTemplateAddressSource | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplateaddresssource/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplateaddresssource/index.md
---

The source used to populate the address shown on the letterhead.

## Used By

[`PdfLetterheadTemplate.address_source`](/reference/2026-01-01/objects/pdfletterheadtemplate)

[`createPdfLetterheadTemplateInput.address_source`](/reference/2026-01-01/input-objects/createpdfletterheadtemplateinput)

[`updatePdfLetterheadTemplateInput.address_source`](/reference/2026-01-01/input-objects/updatepdfletterheadtemplateinput)

## Definition

```
"""
The source used to populate the address shown on the letterhead.
"""
enum PdfLetterheadTemplateAddressSource {
  ORGANIZATION
  CURRENT_USER
  PRIMARY_PROVIDER
  OTHER
}
```
