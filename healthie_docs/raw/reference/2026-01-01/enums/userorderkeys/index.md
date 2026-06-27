---
title: UserOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/userorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/userorderkeys/index.md
---

User sorting enum

## Used By

[`Document.shareable_org_members`](/reference/2026-01-01/objects/document)

[`Document.shareable_patients`](/reference/2026-01-01/objects/document)

[`Document.users`](/reference/2026-01-01/objects/document)

[`Folder.shareable_org_members`](/reference/2026-01-01/objects/folder)

[`Folder.shareable_patients`](/reference/2026-01-01/objects/folder)

[`Folder.users`](/reference/2026-01-01/objects/folder)

[`Organization.providers`](/reference/2026-01-01/objects/organization)

[`Task.assignees`](/reference/2026-01-01/objects/task)

[`Query.organizationMembers`](/reference/2026-01-01/queries/organizationmembers)

[`Query.users`](/reference/2026-01-01/queries/users)

## Definition

```
"""
User sorting enum
"""
enum UserOrderKeys {
  EMAIL_ASC
  EMAIL_DESC
  FIRST_NAME_ASC
  FIRST_NAME_DESC
  LAST_NAME_DESC
  LAST_NAME_ASC
  CREATED_AT_DESC
  CREATED_AT_ASC
  UPDATED_AT_DESC
  UPDATED_AT_ASC
  GROUP_NAME_ASC
  GROUP_NAME_DESC
  PROVIDER_NAME_ASC
  PROVIDER_NAME_DESC
  NEXT_APPT_DATE_ASC
  NEXT_APPT_DATE_DESC
}
```
