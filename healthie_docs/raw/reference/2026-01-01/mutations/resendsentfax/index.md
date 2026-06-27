---
title: resendSentFax | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/resendsentfax/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/resendsentfax/index.md
---

resend Sent Fax

## Arguments

[`input` ](#argument-input)· [`resendSentFaxInput` ](/reference/2026-01-01/input-objects/resendsentfaxinput)· Parameters for resendSentFax

## Returns

[`resendSentFaxPayload`](/reference/2026-01-01/objects/resendsentfaxpayload)

## Example

```
mutation resendSentFax($input: resendSentFaxInput) {
  resendSentFax(input: $input) {
    messages
    sent_fax
  }
}
```
