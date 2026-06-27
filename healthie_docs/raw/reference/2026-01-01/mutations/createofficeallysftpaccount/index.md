---
title: createOfficeallySftpAccount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createofficeallysftpaccount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createofficeallysftpaccount/index.md
---

create OfficeallySftpAccount

## Arguments

[`input` ](#argument-input)· [`createOfficeallySftpAccountInput` ](/reference/2026-01-01/input-objects/createofficeallysftpaccountinput)· Parameters for createOfficeallySftpAccount

## Returns

[`createOfficeallySftpAccountPayload`](/reference/2026-01-01/objects/createofficeallysftpaccountpayload)

## Example

```
mutation createOfficeallySftpAccount($input: createOfficeallySftpAccountInput) {
  createOfficeallySftpAccount(input: $input) {
    messages
    officeally_sftp_account
  }
}
```
