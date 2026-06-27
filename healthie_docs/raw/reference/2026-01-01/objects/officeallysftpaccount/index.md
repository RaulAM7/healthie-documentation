---
title: OfficeallySftpAccount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/officeallysftpaccount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/officeallysftpaccount/index.md
---

Info on SFTP connection to OfficeAlly

## Fields

[`ftp_url` ](#field-ftp-url)· [`String` ](/reference/2026-01-01/scalars/string)· The OfficeAlly SFTP URL

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connection

[`is_enabled` ](#field-is-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the SFTP connection is turned by user

[`is_valid` ](#field-is-valid)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the SFTP connection is working

[`last_imported_from` ](#field-last-imported-from)· [`String` ](/reference/2026-01-01/scalars/string)· The last time we imported from the SFTP

[`username` ](#field-username)· [`String` ](/reference/2026-01-01/scalars/string)· The SFTP OfficeAlly Username

## Used By

[`Query.officeallySftpAccount`](/reference/2026-01-01/queries/officeallysftpaccount)

[`createOfficeallySftpAccountPayload.officeally_sftp_account`](/reference/2026-01-01/objects/createofficeallysftpaccountpayload)

[`updateOfficeallySftpAccountPayload.officeally_sftp_account`](/reference/2026-01-01/objects/updateofficeallysftpaccountpayload)

## Definition

```
"""
Info on SFTP connection to OfficeAlly
"""
type OfficeallySftpAccount {
  """
  The OfficeAlly SFTP URL
  """
  ftp_url: String


  """
  The unique identifier of the connection
  """
  id: ID!


  """
  True if the SFTP connection is turned by user
  """
  is_enabled: Boolean


  """
  True if the SFTP connection is working
  """
  is_valid: Boolean


  """
  The last time we imported from the SFTP
  """
  last_imported_from: String


  """
  The SFTP OfficeAlly Username
  """
  username: String
}
```
