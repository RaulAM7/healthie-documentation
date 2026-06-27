---
title: updateOfficeallySftpAccount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateofficeallysftpaccount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateofficeallysftpaccount/index.md
---

update OfficeallySftpAccount

## Arguments

[`input` ](#argument-input)· [`updateOfficeallySftpAccountInput` ](/reference/2026-01-01/input-objects/updateofficeallysftpaccountinput)· Parameters for updateOfficeallySftpAccount

## Returns

[`updateOfficeallySftpAccountPayload`](/reference/2026-01-01/objects/updateofficeallysftpaccountpayload)

## Example

```
mutation updateOfficeallySftpAccount($input: updateOfficeallySftpAccountInput) {
  updateOfficeallySftpAccount(input: $input) {
    messages
    officeally_sftp_account
  }
}
```
