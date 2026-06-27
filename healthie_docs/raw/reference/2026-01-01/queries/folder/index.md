---
title: folder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/folder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/folder/index.md
---

fetch a folder by id

## Arguments

[`custom_module_id` ](#argument-custom-module-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`id` ](#argument-id)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`Folder`](/reference/2026-01-01/objects/folder)

## Example

```
query folder($custom_module_id: ID, $id: String) {
  folder(custom_module_id: $custom_module_id, id: $id) {
    can_only_share
    created_at
    current_user_can_edit
    description
    documents_count
    email_on_welcome
    folder_id
    folder_path
    id
    name
    owner
    parent_folder
    rel_user
    rel_user_id
    shareable_org_members
    shareable_patients
    shareable_user_groups
    shared
    shared_on_welcome
    shared_user_groups_count
    shared_users_count
    shared_with_dietitians
    subfolders_count
    system_generated
    unshared_patients_count
    user_groups
    users
  }
}
```
