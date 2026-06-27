---
title: UserGroupOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/usergrouporderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/usergrouporderkeys/index.md
---

UserGroup sorting enum

## Used By

[`Document.shareable_user_groups`](/reference/2026-01-01/objects/document)

[`Folder.shareable_user_groups`](/reference/2026-01-01/objects/folder)

[`Query.userGroups`](/reference/2026-01-01/queries/usergroups)

## Definition

```
"""
UserGroup sorting enum
"""
enum UserGroupOrderKeys {
  INVITE_CODE_ASC
  INVITE_CODE_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  NAME_ASC
  NAME_DESC
  USERS_COUNT_ASC
  USERS_COUNT_DESC
}
```
