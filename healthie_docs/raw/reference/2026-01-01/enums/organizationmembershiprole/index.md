---
title: OrganizationMembershipRole | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/organizationmembershiprole/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/organizationmembershiprole/index.md
---

Roles that a user can have in an organization

## Used By

[`UpdateUiConfigurationInput.role`](/reference/2026-01-01/input-objects/updateuiconfigurationinput)

## Definition

```
"""
Roles that a user can have in an organization
"""
enum OrganizationMembershipRole {
  """
  The user is a standard member of the organization (includes providers)
  """
  STANDARD


  """
  The user is a support member of the organization
  """
  SUPPORT
}
```
