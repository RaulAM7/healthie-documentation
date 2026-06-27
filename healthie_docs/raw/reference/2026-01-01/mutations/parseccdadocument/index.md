---
title: parseCcdaDocument | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/parseccdadocument/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/parseccdadocument/index.md
---

Import client from a CCDA file

## Arguments

[`input` ](#argument-input)· [`parseCcdaDocumentInput` ](/reference/2026-01-01/input-objects/parseccdadocumentinput)· Parameters for parseCcdaDocument

## Returns

[`parseCcdaDocumentPayload`](/reference/2026-01-01/objects/parseccdadocumentpayload)

## Example

```
mutation parseCcdaDocument($input: parseCcdaDocumentInput) {
  parseCcdaDocument(input: $input) {
    current_provider_has_access
    is_new_patient
    messages
    user
    xml_file_name
  }
}
```
