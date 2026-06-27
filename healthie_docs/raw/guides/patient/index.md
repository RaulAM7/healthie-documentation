---
title: Patient (Client) Management | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/patient/index
  md: https://docs.gethealthie.com/guides/patient/index.md
---

## The Patient Object

```
 # Some Example Fields
 {
  "id": "9900",
  "first_name": "Jonas",
  "last_name": "Salk",
  "dob": "2010-10-10",
  "gender": "Male",
  "email": "jonas.salk@example.com",
  "phone_number": "555-444-2244",
  "next_appt_date": null
}
```

Patients are `User` objects. This is the same object type that is used for providers/staff members. Due to this, The `User` object has an immense amount of fields, many of which are not relevant for patients. With GraphQL, you select the exact fields you want returned, so you don’t need to deal with any non-relevant data.

You can view the full list of available fields [here](/reference/2024-06-01/objects/user).

If you have questions about how `legal_name` and `gender`/`gender_identity`/`sex` interact with each other, We recommend reading our general help articles [here](https://help.gethealthie.com/article/470-storing-and-modifying-client-information-in-healthie) and [here](https://help.gethealthie.com/article/683-gender-and-gender-identity).

## Creating a Patient

Patient accounts are created in three main ways.

| Method                           | Corresponding Mutation |
| -------------------------------- | ---------------------- |
| Added by a provider/staff member | `createClient`         |
| Self-Sign Up                     | `signUp`               |
| Booking and/or buying            | `completeCheckout`     |

### `createClient` Mutation

```
mutation createClient(
  $first_name: String
  $last_name: String
  $email: String
  $skipped_email: Boolean
  $phone_number: String
  $dietitian_id: String
  $user_group_id: String
  $dont_send_welcome: Boolean
) {
  createClient(
    input: {
      first_name: $first_name
      last_name: $last_name
      email: $email
      skipped_email: $skipped_email
      phone_number: $phone_number
      dietitian_id: $dietitian_id
      user_group_id: $user_group_id
      dont_send_welcome: $dont_send_welcome
    }
  ) {
    user {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `createClient` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createclientinput). We will go over some of them below.

| Input               | Info                                                                  |
| ------------------- | --------------------------------------------------------------------- |
| `first_name`        | Required                                                              |
| `last_name`         | Required                                                              |
| `email`             | Required if `skipped_email` is false                                  |
| `skipped_email`     | Optional                                                              |
| `phone_number`      | Optional                                                              |
| `dietitian_id`      | Required, ID of the provider. Defaults to the authenticated user’s ID |
| `user_group_id`     | Optional                                                              |
| `dont_send_welcome` | When true, an invite email will not be sent to the new client.        |

#### Sending a welcome email with `signup_token`

After creating a client with the `createClient` mutation, you may want to send your own welcome email to the client with the `signup_token` to allow them to set a password and activate their account. You can obtain the `signup_token` from the `set_password_link` field on the User object, by querying the client account with the `user` query.

### Patient `signUp` Mutation

```
mutation signUp(
  $timezone: String
  $first_name: String
  $last_name: String
  $email: String
  $password: String
  $phone_number: String
  $invite_code: String
  $provider_type: String
  $role: String
  $dietitian_id: String
) {
  signUp(
    input: {
      first_name: $first_name
      last_name: $last_name
      email: $email
      password: $password
      phone_number: $phone_number
      invite_code: $invite_code
      role: $role
      dietitian_id: $dietitian_id
      timezone: $timezone
    }
  ) {
    user {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `signUp` mutation is called unauthenticated.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/signupinput). We will go over the inputs relevant for new patients below.

| Input          | Info                                                                                                                                                                                                     |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `first_name`   | Required                                                                                                                                                                                                 |
| `last_name`    | Required                                                                                                                                                                                                 |
| `email`        | Required                                                                                                                                                                                                 |
| `password`     | Required. Needs to be a minimum of 8 chars, and meet a calculated strength requirement. Healthie uses [StrongPassword](https://github.com/bdmac/strong_password) Ruby gem to calculate password strength |
| `role`         | Required. Needs to be “patient”                                                                                                                                                                          |
| `phone_number` | Optional                                                                                                                                                                                                 |
| `dietitian_id` | ID of the provider. Either this or `invite_code` need to be provided. This can be provided along with a user group’s invite code                                                                         |
| `invite_code`  | Invite code for a specific provider *or* user group.                                                                                                                                                     |
| `timezone`     | Optional. Sets the timezone of the new patient’s account                                                                                                                                                 |

### `completeCheckout` Mutation

The `completeCheckout` mutation is used for a patient to book an appointment, or make a payment. It creates a new patient if the following conditions are present

* The mutation is called unauthenticated
* The given email does not exist on another patient in the provider’s account

We will go over this mutation in more depth in the Scheduling and Payments sections.

## Retrieving a Patient

```
query getUser($id: ID) {
  user(id: $id) {
    id
    first_name
    last_name
    dob
    gender
    email
    phone_number
    next_appt_date
  }
}
```

Retrieving a specific patient’s information is done via the `user` query.

| Input             | Info                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------- |
| `id`              | Either this needs to be provided, or `or_current_user` needs to be true.              |
| `clear_notifs`    | When true, existing notifications from this patient will be marked as seen.           |
| `or_current_user` | When true, the authenticated user will be returned if `id` is invalid or not present. |

## Updating a Patient

Patient account information is updated in two main ways.

| Method                                     | Corresponding Mutation |
| ------------------------------------------ | ---------------------- |
| Updated by a provider/staff member         | `updateClient`         |
| Updated in bulk by a provider/staff member | `bulkUpdateClients`    |
| Updated by the patient themselves          | `updateUser`           |

### `updateClient` Mutation

```
mutation updateClient($id: ID, $first_name: String, $last_name: String, $legal_name: String, $email: String) {
  updateClient(
    input: { id: $id, first_name: $first_name, last_name: $last_name, legal_name: $legal_name, email: $email }
  ) {
    user {
      id
      first_name
      last_name
      legal_name
      email
    }
    messages {
      field
      message
    }
  }
}
```

The `updateClient` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateclientinput).

We will go over some of the required and less clear ones below.

| Input                          | Info                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                           | Required                                                                                                                                                                                                                                                                                                                                               |
| `resend_welcome`               | When true, a new invite email will be sent to the patient.                                                                                                                                                                                                                                                                                             |
| `send_form_request_reminder`   | If this is true, `is_intake_item` or `requested_form_completion_id` must be sent in as well                                                                                                                                                                                                                                                            |
| `is_intake_item`               | When sent with `send_form_request_reminder`, will send the patient an email reminding them to complete their intake forms.                                                                                                                                                                                                                             |
| `requested_form_completion_id` | When sent with `send_form_request_reminder`, will send the patient an email reminding them to complete a specific form request.                                                                                                                                                                                                                        |
| `for_changing_groups`          | When true, the patient will be removed from their group. It is normally better to just send in a `user_group_id` of ""                                                                                                                                                                                                                                 |
| `password`                     | When passed in, this will change the password the patient uses to sign in. This is helpful if you want to set passwords for your patients. If provided, needs to be a minimum of 8 chars, and meet a calculated strength requirement. Healthie uses [StrongPassword](https://github.com/bdmac/strong_password) Ruby gem to calculate password strength |
| `gender_identity_code`         | When passed in, this will update the patient’s gender identity in the system. The acceptable values are as follows: - `MALE` - `FEMALE` - `FEMALE_TO_MALE` - `MALE_TO_FEMALE` - `GENDERQUEER` - `OTHER` - `CHOOSE_NOT_TO_DISCLOSE`                                                                                                                     |
| `sex`                          | The sex on file with client’s insurance. This field is specifically for insurance purposes and is limited to two values: `Male` and `Female`.                                                                                                                                                                                                          |

The inputs that trigger emails/reminders (`resend_welcome` through `requested_form_completion_id`) take precendece over other demographic updates you are trying to make to the patient record. For example, if you send in a new `first_name` and also `resend_welcome`, the invite email will be sent, but the patient’s name will not be updated.

### `bulkUpdateClients` Mutation

```
mutation bulkUpdateClients($ids: [ID!], $active_status: Boolean) {
  bulkUpdateClients(input: { ids: $ids, active_status: $active_status }) {
    users {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `bulkUpdateClients` mutation is called from an authenticated provider/staff account. It allows you to update multiple patients at the same time.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/bulkupdateclientsinput).

We will go over some of the common ones below.

| Input           | Info                                                                                                             |
| --------------- | ---------------------------------------------------------------------------------------------------------------- |
| `ids`           | Required                                                                                                         |
| `user_group_id` | When present, all specified patients will be moved to the specified user group.                                  |
| `active_status` | If `user_group_id` is not present, this field is required. All specified patients will have their status update. |

This mutation can only bulk update one field at a time. If `user_group_id` and `active_status` are both passed in, `active_status` will be ignored.

### Patient `updateUser` Mutation

```
mutation updateUser($first_name: String, $legal_name: String, $last_name: String, $email: String, $id: ID) {
  updateUser(
    input: { first_name: $first_name, legal_name: $legal_name, last_name: $last_name, email: $email, id: $id }
  ) {
    user {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateUser` mutation is called from an authenticated patient account or (more rarely) from an authenticated provider/staff account with access to the patient.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateuserinput).

We will go over some of the required and less clear ones below.

| Input           | Info                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| `current_email` | Email of the Patient to update. Normally better to pass `id` in instead                                      |
| `id`            | ID of the patient to update. If this is blank, the mutation will default to updating the authenticated user. |

## Deleting a Patient

Patients (and `User` objects in general) cannot be deleted via the Healthie API. Instead, you should archive the patient using the `updateClient` mutation mentioned above.

## List All Patients

```
query users(
  $offset: Int
  $keywords: String
  $sort_by: String
  $active_status: String
  $group_id: String
  $show_all_by_default: Boolean
  $should_paginate: Boolean
  $provider_id: String
  $conversation_id: ID
  $limited_to_provider: Boolean
) {
  usersCount(
    keywords: $keywords
    active_status: $active_status
    group_id: $group_id
    conversation_id: $conversation_id
    provider_id: $provider_id
    limited_to_provider: $limited_to_provider
  )
  users(
    offset: $offset
    keywords: $keywords
    sort_by: $sort_by
    active_status: $active_status
    group_id: $group_id
    conversation_id: $conversation_id
    show_all_by_default: $show_all_by_default
    should_paginate: $should_paginate
    provider_id: $provider_id
    limited_to_provider: $limited_to_provider
  ) {
    id
  }
}
```

A list of patients can be retrieved via the `users` query. This query is called from an authenticated provider/staff account.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/users#arguments).

We will go over some of them below.

| Input                 | Info                                                                                                                                      |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `should_paginate`     | Defaults to true. When false, the returned patient list is not paginated.                                                                 |
| `keywords`            | Optional. A term to search patients by. Find more about searching [here](#patient-search).                                                |
| `sort_by`             | Defaults to “last\_name\_desc”. View the query [here](/reference/2024-06-01/queries/users#argument-sort-by) to see all potential options. |
| `active_status`       | Optional. Options are \[“active”, “archived”]. When passed in, only patients of the specified active status will be returned.             |
| `group_id`            | Optional. When passed in, only patients in the specified User Group will be returned                                                      |
| `show_all_by_default` | Defaults to true. When false, no patients will be returned unless `keywords` are also provided to the query.                              |
| `provider_id`         | Defaults to the ID of the authenticated user. When passed in, only patients the specified user has access to will be returned.            |
| `limited_to_provider` | Defaults to false. When true, only patients with the specified user as a provider will be returned.                                       |
| `conversation_id`     | Optional. When passed in, returns patients in the specified conversation.                                                                 |

### Patient Search

```
query users($keywords: String) {
  users(keywords: $keywords) {
    id
  }
}
```

Patients can be searched using the `keywords` argument. The `keywords` argument can be used to search by `id`, `first_name`, `legal_name`, `last_name`, `record_identifier`, `email`, `dob`, and `npi`.

> Example variables:

```
{
  "keywords": "John Doe 2002-01-01"
}
```

You can combine multiple search terms by separating them with a space. The search will return patients who match **all the terms**. In the provided example, the search will only return patients with the first and last names “John Doe” and a date of birth 2002-01-01.

## Create Location

```
mutation createLocation(
  $user_id: String
  $name: String
  $line1: String
  $zip: String
  $city: String
  $state: String
  $npi: String
) {
  createLocation(
    input: { user_id: $user_id, name: $name, line1: $line1, zip: $zip, city: $city, state: $state, npi: $npi }
  ) {
    location {
      id
      name
      line1
      zip
    }
    messages {
      field
      message
    }
  }
}
```

You can use the `creatLocation` or `updateLocation` mutations to create update address information for patients.

## User Groups

### The User Group Object

```
 # Some Example Fields


 "userGroup": {
      "id": "9900",
      "name": "Discovery Patients",
      "users_count": "7",
      "invite_code": "fbeb7f",
      "onboarding_flow_id": 11
    }
```

Patients can be organized into groups. Groups are a powerful feature in Healthie’s API. You can trigger automations, automatically share content, restrict features, and more based on groups. You can read a full overview of the feature [here](https://help.gethealthie.com/article/157-overview-client-groups).

Groups are `UserGroup` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/usergroup).

### Creating a User Group

```
mutation createGroup($name: String) {
  createGroup(input: { name: $name }) {
    user_group {
      id
      name
    }
    messages {
      field
      message
    }
  }
}
```

User Groups are created via the `createGroup` mutation. The `createGroup` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/creategroupinput).

We will go over them below.

| Input  | Info                             |
| ------ | -------------------------------- |
| `name` | Required. The name of the group. |

### Retrieving a User Group

```
query getUserGroup($id: ID) {
  userGroup(id: $id) {
    id
    name
    users_count
    invite_code
  }
}
```

Retrieving information on a a specific group is done via the `userGroup` query.

| Input | Info      |
| ----- | --------- |
| `id`  | Required. |

### Updating a User Group

```
mutation updateUserGroup($id: ID, $name: String, $onboarding_flow_id: ID) {
  updateUserGroup(input: { id: $id, name: $name, onboarding_flow_id: $onboarding_flow_id }) {
    user_group {
      id
      name
    }
    messages {
      field
      message
    }
  }
}
```

User Groups are updated via the `updateUserGroup` mutation. The `updateUserGroup` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateusergroupinput).

We will go over them below.

| Input                | Info                                                                                          |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `id`                 | Required. The ID of the group that will be updated                                            |
| `name`               | Optional.                                                                                     |
| `onboarding_flow_id` | Optional. The ID of the Onboarding Flow that patients in the group will be asked to fill out. |

### Deleting a User Group

```
mutation deleteUserGroup($id: ID!, $group_to_receive_clients: ID) {
  deleteUserGroup(input: { id: $id, group_to_receive_clients: $group_to_receive_clients }) {
    user_group {
      id
    }
    messages {
      field
      message
    }
  }
}
```

User Groups are deleted via the `deleteUserGroup` mutation. The `deleteUserGroup` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleteusergroupinput).

We will go over them below.

| Input                      | Info                                                                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                       | Required. The ID of the group to delete.                                                                                                                           |
| `group_to_receive_clients` | Optional. The ID of a group to transfer all patients to that are currently assigned to the deleted group. When left blank, patients are not placed into any group. |

### List All User Groups

```
query userGroups($offset: Int, $keywords: String, $sort_by: String) {
  userGroupsCount(keywords: $keywords)
  userGroups(offset: $offset, keywords: $keywords, sort_by: $sort_by, should_paginate: true) {
    id
    name
    users_count
  }
}
```

A list of groups can be retrieved via the `userGroups` query. This query is called from an authenticated provider/staff account.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/usergroups#arguments).

We will go over some of them below.

| Input             | Info                                                                                                                                                                                   |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `should_paginate` | Defaults to false. When true, the returned list of groups is paginated.                                                                                                                |
| `keywords`        | Optional. A term to search groups by. Groups can be searched by `name`.                                                                                                                |
| `sort_by`         | Defaults to “name”. Options are \[“name”, “invite\_code”, “created\_at\_asc”, “created\_at\_desc”, “group\_name\_asc”, “group\_name\_desc”, “users\_count\_asc”, “users\_count\_desc”] |

## Tags

### The User Tag Object

```
{
  "id": 1,
  "name": "Tag A",
  "tagged_users": [
    {
      "id": 2,
      "first_name": "John"
    }
  ],
  "user": {
    "id": 1,
    "email": "provider@example.com"
  }
}
```

Client Tags offer an additional way (beyond Client Groups) to assign particular attributes to clients and automate specific actions based on Tags that have been established. While clients can only be assigned to one group, clients can have an unlimited number of tags.

Tags are `Tag` objects.

**Please note** that tags are unique per provider/staff account.

### Creating a Tag

```
mutation createTag($name: String, $taggable_user_id: ID) {
  createTag(input: { name: $name, taggable_user_id: $taggable_user_id }) {
    tag {
      id
      name
      tagged_users {
        id
      }
    }


    messages {
      field
      message
    }
  }
}
```

The `createTag` mutation is called from an authenticated provider/staff account.

Creating a new Tag with with the same name as another one will fail. To apply an existing Tag to other Users please check out [Applying Tags to Users](#applying-tags-to-users).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createtaginput).

| Input              | Info                                            |
| ------------------ | ----------------------------------------------- |
| `name`             | Required. Tag name.                             |
| `taggable_user_id` | Optional. The ID of the User to apply a Tag on. |

Returns [`createTagPayload`](/reference/2024-06-01/objects/createtagpayload).

### Updating a Tag

```
mutation updateTag($id: ID, $name: String) {
  updateTag(input: { id: $id, name: $name }) {
    tag {
      id
      name
    }


    messages {
      field
      message
    }
  }
}
```

Allows to change the Tag name.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatetaginput).

| Input  | Info                |
| ------ | ------------------- |
| `id`   | Required. Tag ID.   |
| `name` | Required. Tag name. |

Returns [`updateTagPayload`](/reference/2024-06-01/objects/updatetagpayload).

### Deleting a Tag

```
mutation deleteTag($id: ID) {
  deleteTag(input: { id: $id }) {
    tag {
      id
      name
    }


    messages {
      field
      message
    }
  }
}
```

Use the `deleteTag` mutation to permanently delete a Tag. It does not delete associated Users.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletetaginput).

| Input | Info                  |
| ----- | --------------------- |
| `id`  | Required. The Tag ID. |

Returns [`deleteAppliedTagPayload`](/reference/2024-06-01/objects/deletetagpayload).

### List all Tags

```
query tags {
  tags {
    id
    name
  }
}
```

Display a list of all Tags for the current User’s Organization.

Returns an array of [`Tag`](/reference/2024-06-01/objects/tag) objects.

### Applying Tags to Users

```
mutation applyTags($ids: [ID], $taggable_user_id: ID) {
  bulkApply(input: { ids: $ids, taggable_user_id: $taggable_user_id }) {
    tags {
      id
      name
    }


    messages {
      field
      message
    }
  }
}
```

You can apply multiple existing Tags at once to a single User by using `bulkApply` mutation.

Note

Please note that you can apply Tags to both Patients and Providers.

The `bulkApply` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/bulkapplyinput).

| Input              | Info                                            |
| ------------------ | ----------------------------------------------- |
| `ids`              | Required. List of Tag IDs to apply.             |
| `taggable_user_id` | Required. The ID of the User to apply a Tag on. |

Returns [`bulkApplyPayload`](/reference/2024-06-01/objects/bulkapplypayload).

### Removing Applied Tags

```
mutation removeAppliedTag($id: ID, $taggable_user_id: ID) {
  removeAppliedTag(input: { id: $id, taggable_user_id: $taggable_user_id }) {
    tag {
      id
      name
    }


    messages {
      field
      message
    }
  }
}
```

You can remove applied Tag from User by using `removeAppliedTag` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/removeappliedtaginput).

| Input              | Info                                                 |
| ------------------ | ---------------------------------------------------- |
| `id`               | Required. The Tag ID.                                |
| `taggable_user_id` | Required. The ID of the User to remove the Tag from. |

Returns [`removeAppliedTagPayload`](/reference/2024-06-01/objects/removeappliedtagpayload).
