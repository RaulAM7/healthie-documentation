---
title: Forms | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/forms/index
  md: https://docs.gethealthie.com/guides/forms/index.md
---

Healthie supports two types of forms:

* [Form Templates (Forms)](#form-templates)
* [Onboarding Flows (Intake Flows)](#onboarding-flows)

For more information on the feature in general, view our help articles [here](https://help.gethealthie.com/category/261-intake-forms).

## Form Templates

Form Templates are considered public to view. All mutations can be performed only by an authenticated provider/staff account.

### The Form Template Object

```
{
  "id": "1",
  "name": "Health History",
  "has_matrix_field": true,
  "prefill": false,
  "is_video": false,
  "use_for_charting": false,
  "use_for_program": false,
  "has_non_readonly_modules": true,
  "custom_modules": [
    // An array of CustomModule objects
  ]
}
```

Forms are `CustomModuleForm` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/custommoduleform).

### Listing all Forms

```
query formTemplates(
  $include_default_templates: Boolean
  $active_status: Boolean
  $should_paginate: Boolean
  $category: String
  $keywords: String
  $offset: Int
  $sortBy: String
) {
  customModuleForms(
    include_default_templates: $include_default_templates
    active_status: $active_status
    should_paginate: $should_paginate
    category: $category
    keywords: $keywords
    offset: $offset
    sort_by: $sortBy
  ) {
    id
    is_video
    name
    prefill
    uploaded_by_healthie_team
  }
}
```

A list of Form Templates can be retrieved via the `customModuleForms` query. This query is considered public.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/custommoduleforms#arguments).

We will go over some of them below.

| Input           | Info                                                                                                                                                                          |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `category`      | Optional. Valid options are:- `all` (default)
- `charting`
- `program`
- `intake`                                                                                             |
| `active_status` | Optional. Whether to fetch archived forms, `false` by default.                                                                                                                |
| `keywords`      | Optional. A term to search Forms by. Can be searched by form name.                                                                                                            |
| `sort_by`       | Optional. Valid options are:- `last_updated_asc`
- `last_updated_desc` (default)
- `created_by_asc`
- `created_by_desc`
- `type_asc`
- `type_desc`
- `name_asc`
- `name_desc` |

Returns an array of [`CustomModuleForm`](/reference/2024-06-01/objects/custommoduleform) objects.

### Retrieving a Form

```
query form($id: ID) {
  customModuleForm(id: $id) {
    id
    has_matrix_field
    has_non_readonly_modules
    is_video
    name
    prefill
    use_for_charting
    use_for_program


    custom_modules {
      id
      hipaa_name
      mod_type
      options
      # ...
    }
  }
}
```

Retrieving a specific Form Template is done via the `customModuleForm` query. This query is considered public.

The `customModuleForm` query accepts the following arguments:

| Input | Info                                      |
| ----- | ----------------------------------------- |
| `id`  | **Required**. The ID of the Form Template |

Returns a [`CustomModuleForm`](/reference/2024-06-01/objects/custommoduleform) object.

### Creating a Form

```
mutation createCustomModuleForm($name: String, $use_for_charting: Boolean, $use_for_program: Boolean) {
  createCustomModuleForm(
    input: { name: $name, use_for_charting: $use_for_charting, use_for_program: $use_for_program }
  ) {
    customModuleForm {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `createCustomModuleForm` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createcustommoduleforminput).

| Input              | Info                                                  |
| ------------------ | ----------------------------------------------------- |
| `name`             | **Required**. Form name.                              |
| `use_for_charting` | Optional. Set to `true` to use the Form for charting  |
| `use_for_program`  | Optional. Set to `true` to use the Form for a program |

Note

To create an Intake Form, set both `use_for_charting` and `use_for_program` to `false`.

Returns [`createCustomModuleFormPayload`](/reference/2024-06-01/objects/createcustommoduleformpayload).

### Updating a Form

```
mutation updateCustomModuleForm($id: ID, $name: String, $is_archived: Boolean) {
  updateCustomModuleForm(input: { id: $id, name: $name, is_archived: $is_archived }) {
    customModuleForm {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateCustomModuleForm` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatecustommoduleforminput).

| Input              | Info                                                  |
| ------------------ | ----------------------------------------------------- |
| `id`               | **Required**. The ID of the Form to update.           |
| `name`             | Optional. New name for the Form.                      |
| `is_archived`      | Optional. Set to `true` to archive the Form.          |
| `use_for_charting` | Optional. Set to `true` to use the Form for charting  |
| `use_for_program`  | Optional. Set to `true` to use the Form for a program |

Returns [`updateCustomModuleFormPayload`](/reference/2024-06-01/objects/updatecustommoduleformpayload).

### Deleting a Form

```
mutation deleteCustomModuleForm($id: ID) {
  deleteCustomModuleForm(input: { id: $id }) {
    customModuleForm {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `deleteCustomModuleForm` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletecustommoduleforminput).

| Input | Info                                        |
| ----- | ------------------------------------------- |
| `id`  | **Required**. The ID of the Form to delete. |

Returns [`updateCustomModuleFormPayload`](/reference/2024-06-01/objects/updatecustommoduleformpayload).

### Copying a Form

```
mutation copyCustomModuleForm($id: ID, $id_list: String, $user_id: String) {
  copyCustomModuleForm(input: { id: $id, id_list: $id_list, user_id: $user_id }) {
    customModuleForm {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can clone a Form Template by using the `copyCustomModuleForm` mutation.

The full input definition can be found [here](/reference/2024-06-01/input-objects/copycustommoduleforminput).

| Input     | Info                                                                                                                         |
| --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `id`      | The ID of the Form to copy. Either this or `id_list` is required.                                                            |
| `id_list` | A comma-separated string with IDs of the Forms to copy. Required if `id` is not present. Example: `"1,2,3"`.                 |
| `user_id` | The ID of the owner of newly created Forms. Available only to super admins, otherwise will copy to the current user’s forms. |

Returns [`copyCustomModuleFormPayload`](/reference/2024-06-01/objects/copycustommoduleformpayload).

### Sharing a Form

```
mutation shareCustomModuleForm($id: ID, $form_share_recipient: String) {
  shareCustomModuleForm(input: { id: $id, form_share_recipient: $form_share_recipient }) {
    customModuleForm {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can share a Form with another Healthie member. The recipient needs to be specified with an email address. They will receive their own independent copy of the form.

This mutation will trigger a notification email to the recipient.

You can clone a Form Template by using the `shareCustomModuleForm` mutation.

The full input definition can be found [here](/reference/2024-06-01/input-objects/sharecustommoduleforminput).

| Input                  | Info                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| `id`                   | **Required**. The ID of the Form to share.                                                                  |
| `form_share_recipient` | **Required**. Email address of the recipient. Must be a valid email address of an existing Healthie member. |

Returns [`shareCustomModuleFormPayload`](/reference/2024-06-01/objects/sharecustommoduleformpayload).

## Onboarding Flows

### The Onboarding Flow Object

```
{
  "id": "1",
  "name": "Intake flow",
  "has_forms_after_welcome": true,
  "is_multiple_providers": true,
  "onboarding_items": [
    // an array of OnboardingItem documents
  ]
}
```

Onboarding Flows are `OnboardingFlow` objects. Onboarding Flows can be associated with zero or more [User Groups](/guides/patient/#user-groups).

Onboarding Flows consist of `OnboardingItem` documents.

You can view the full list of available fields [here](/reference/2024-06-01/objects/custommoduleform).

### Listing Onboarding Flows

```
query onboardingFlows($offset: Int, $keywords: String, $sort_by: String, $should_paginate: Boolean) {
  onboardingFlows(offset: $offset, keywords: $keywords, sort_by: $sort_by, should_paginate: $should_paginate) {
    id
    name
    is_multiple_providers
    has_forms_after_welcome
  }
}
```

A list of Onboarding Flows can be retrieved via the `onboardingFlows` query. This query is available to authenticated provider/staff accounts.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/onboardingflows#arguments).

We will go over some of them below.

| Input      | Info                                                                                                                                                                             |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keywords` | Optional. A term to search by. Can be searched by the flow name.                                                                                                                 |
| `sort_by`  | Optional. Valid options are:- `onboarding_flow_name_asc` (default)
- `onboarding_flow_name_desc`
- `created_at_asc`
- `created_at_desc`
- `forms_count_asc`
- `forms_count_desc` |

Returns an array of [`OnboardingFlow`](/reference/2024-06-01/objects/onboardingflow) objects.

### Retrieving a Flow

```
query onboardingFlow($id: ID, $user_id: ID) {
  onboardingFlow(id: $id, user_id: $user_id) {
    id
    name
    is_multiple_providers
    has_forms_after_welcome
  }
}
```

Retrieving a specific Onboarding Flow is done via the `onboardingFlow` query. This can be done either via the ID of the Flow or for a specific Patient.

You can view a full list of all potential arguments [here](/reference/2024-06-01/queries/onboardingflow#arguments).

| Input     | Info                                                                                |
| --------- | ----------------------------------------------------------------------------------- |
| `id`      | ID of the Flow. Either this or `user_id` needs to be provided.                      |
| `user_id` | Patient’s ID. This argument is ignored if querying as a non-staff/provider account. |

Returns an [`OnboardingFlow`](/reference/2024-06-01/objects/onboardingflow) object.

### Creating a Flow

```
mutation createOnboardingFlow($name: String, $groups_to_use_onboarding_flow: String) {
  createOnboardingFlow(input: { name: $name, groups_to_use_onboarding_flow: $groups_to_use_onboarding_flow }) {
    onboardingFlow {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `createOnboardingFlow` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createonboardingflowinput).

| Input                           | Info                                                                                                  |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `name`                          | **Required**. Onboarding Flow name.                                                                   |
| `groups_to_use_onboarding_flow` | Optional. A comma-separated list of User Groups to attach the Onboarding Flow to. Example: `"1,2,3"`. |

Returns [`createOnboardingFlowPayload`](/reference/2024-06-01/input-objects/createonboardingflowinput).

### Updating a Flow

```
mutation updateOnboardingFlow($id: ID, $name: String, $groups_to_use_onboarding_flow: String) {
  updateOnboardingFlow(input: { id: $id, name: $name, groups_to_use_onboarding_flow: $groups_to_use_onboarding_flow }) {
    onboardingFlow {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Onboarding Flows are deleted via the `updateOnboardingFlow` mutation. The `updateOnboardingFlow` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateonboardingflowinput).

| Input                           | Info                                                                                                  |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                            | **Required**. The ID of the Onboarding Flow to update.                                                |
| `name`                          | Optional. A new name for the Onboarding Flow.                                                         |
| `groups_to_use_onboarding_flow` | Optional. A comma-separated list of User Groups to attach the Onboarding Flow to. Example: `"1,2,3"`. |

Returns [`updateOnboardingFlowPayload`](/reference/2024-06-01/input-objects/updateonboardingflowinput).

### Deleting a Flow

```
mutation deleteOnboardingFlow($id: ID, $flow_to_receive_groups: ID) {
  deleteOnboardingFlow(input: { id: $id, name: $name, flow_to_receive_groups: $flow_to_receive_groups }) {
    onboardingFlow {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Onboarding Flows are deleted via the `deleteOnboardingFlow` mutation. The `deleteOnboardingFlow` mutation is called from an authenticated provider/staff account.

When deleting an Onboarding Flow, you can automatically reassign the User Groups to another Flow by using the `flow_to_receive_groups` argument.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleteonboardingflowinput).

| Input                    | Info                                                                    |
| ------------------------ | ----------------------------------------------------------------------- |
| `id`                     | **Required**. The ID of the Onboarding Flow to delete.                  |
| `flow_to_receive_groups` | Optional. Provide the ID of a Flow that should inherit the User Groups. |

Returns [`deleteOnboardingFlowPayload`](/reference/2024-06-01/objects/deleteonboardingflowpayload).

## Onboarding Items

Onboarding Items are used to associate Forms with Intake Flows.

### The Onboarding Item Object

```
{
  "id": "1980",
  "item_type": "Insurance Form",
  "display_name": "Insurance Form",
  "is_skippable": true,
  "onboarding_flow": {
    "id": "170"
  }
}
```

Onboarding Items are `OnboardingItem` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/onboardingitem).

### Retrieving an Onboarding Item

```
query getOnboardingItem($id: ID) {
  onboardingItem(id: $id) {
    id
    item_type
    display_name
    is_skippable
    onboarding_flow {
      id
    }
  }
}
```

Retrieving a specific Onboarding Item is done via the `onboardingItem` query. This query is considered public.

| Input | Info                                   |
| ----- | -------------------------------------- |
| `id`  | ID of the Onboarding Item to retrieve. |

Returns an [`OnboardingItem`](/reference/2024-06-01/objects/onboardingitem) object.

### Creating an Onboarding Item

```
mutation createOnboardingItem($onboarding_flow_id: String, $item_type: String, $is_skippable: Boolean) {
  createOnboardingItem(
    input: { onboarding_flow_id: $onboarding_flow_id, item_type: $item_type, is_skippable: $is_skippable }
  ) {
    onboardingItem {
      id
    }


    messages {
      field
      message
    }
  }
}
```

Onboarding Items are created via the `createOnboardingItem` mutation. This mutation is called from an authenticated account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createonboardingiteminput).

| Input                | Info                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `onboarding_flow_id` | **Required**. ID of the Onboarding Flow to attach the Item to                                                                                                                                                                                                                                                                               |
| `item_type`          | **Required**. A stringified JSON array containing object(s) of the following structure.- `type` - Onboarding Item type (see below)
- `id` - ID of the related ItemYou can obtain the list of available Item types using the [Listing Available Item Types](#listing-available-item-types) query. Example: `{"type":"Module Form","id":"1"}` |
| `is_skippable`       | **Required**. Set to `false` if this Onboarding Item is mandatory                                                                                                                                                                                                                                                                           |

Returns a [`createOnboardingItemPayload`](/reference/2024-06-01/objects/createonboardingitempayload) object.

### Updating an Onboarding Item

```
mutation updateOnboardingItem(
  $id: ID
  $onboarding_flow_id: String
  $item_type: String
  $item_id: String
  $is_skippable: Boolean
  $row_order: Int
) {
  updateOnboardingItem(
    input: {
      id: $id
      onboarding_flow_id: $onboarding_flow_id
      item_type: $item_type
      item_id: $item_id
      is_skippable: $is_skippable
      row_order: $row_order
    }
  ) {
    onboardingItem {
      id
    }


    messages {
      field
      message
    }
  }
}
```

Onboarding Items are updated via the `updateOnboardingItem` mutation. This mutation is called from an authenticated account.

Note

Please note that the `item_type` and `item_id` fields work differently than in the [`createOnboardingItem` mutation](#creating-an-onboarding-item).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateonboardingiteminput).

| Input       | Info                                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `id`        | **Required**. The ID of the Onboarding Item to update                                                                         |
| `item_type` | Optional. Type of the Item. Please check [Listing Available Item Types](#listing-available-item-types) to get possible values |
| `item_id`   | Optional. ID of the related Item                                                                                              |
| `row_order` | Optional. Use this to reorder the Item inside of the Onboarding Flow                                                          |

Returns an [`updateOnboardingItemPayload`](/reference/2024-06-01/objects/updateonboardingitempayload) object.

### Deleting an Onboarding Item

Onboarding Items can be deleted via the `deleteOnboardingItem` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleteonboardingiteminput).

```
mutation deleteOnboardingItem($id: ID) {
  deleteOnboardingItem(input: { id: $id }) {
    onboardingItem {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteOnboardingItem` mutation is called from an authenticated provider/staff account.

| Input | Info                                               |
| ----- | -------------------------------------------------- |
| `id`  | **Required**. ID of the Onboarding Item to delete. |

Returns a [`deleteOnboardingItemPayload`](/reference/2024-06-01/objects/deleteonboardingitempayload) object.

### Listing Available Item Types

```
query getAvailableItemTypes($onboarding_flow_id: String) {
  availableItemTypes(onboarding_flow_id: $onboarding_flow_id)
}
```

| Input                | Info                                                              |
| -------------------- | ----------------------------------------------------------------- |
| `onboarding_flow_id` | Optional. ID of the Onboarding Flow to return available types for |

This query returns a serialized JSON string containing a list of available types. Each type object has an `id` and `name` field, for example: `{"id":"1","name":"Financial Agreement"}`.

### Listing Unassociated Completed Onboarding Items

```
query getUnassociatedCompletedOnboardingItems($user_id: String) {
  unassociatedCompletedOnboardingItems(user_id: $user_id) {
    id
    item_type
    item_id
    onboarding_item_id
    skipped
    user {
      id
    }
  }
}
```

The `unassociatedCompletedOnboardingItems` query returns a list of user completed Onboarding Items, that are not part of the User’s current flow.

| Input     | Info                                          |
| --------- | --------------------------------------------- |
| `user_id` | Optional. ID of the User to get the Items for |

Returns a [`CompletedOnboardingItem`](/reference/2024-06-01/objects/completedonboardingitem) object.

### Creating a Completed Onboarding Item

```
mutation createCompletedOnboardingItem($onboarding_item_id: ID, $user_id: ID, $skipped: Boolean) {
  createCompletedOnboardingItem(
    input: { onboarding_item_id: $onboarding_item_id, user_id: $user_id, skipped: $skipped }
  ) {
    completed_onboarding_item {
      id
    }
  }
}
```

To mark an Onboarding Item completed by a User, use the `createCompletedOnboardingItem` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createcompletedonboardingiteminput).

| Input                | Info                                                                      |
| -------------------- | ------------------------------------------------------------------------- |
| `onboarding_item_id` | **Required**. ID of the Onboarding Item to mark as complete               |
| `skipped`            | **Required**. If set to `true`, will mark this Onboarding Item as skipped |
| `user_id`            | Optional. If not provided, will apply to the current User                 |

Returns a [`createCompletedOnboardingItemPayload`](/reference/2024-06-01/objects/createcompletedonboardingitempayload) object.

## Form Completion Requests

### Form Completion Request Object

```
{
  "id": 1,
  "custom_module_form": {
    "id": 1
  },
  "item_type": "cmf",
  "recipient": {
    "id": 200,
    "email": "patient@example.com"
  },
  "form_answer_group": {
    // FormAnswerGroup object
  },
  "sender": {
    "id": 1
  },
  "status": "Open"
}
```

When you want to send Patient a Form to complete, you create a Form Completion Request.

Within the API, Form Completion Requests are known as `RequestedFormCompletion` objects.

### Listing all Form Completion Requests

```
query requestedFormCompletions($userId: ID, $keywords: String, $status: String) {
  requestedFormCompletions(user_id: $userId, keywords: $keywords, status: $status) {
    id
    item_type
  }
}
```

A list of Form Completion Requests can be retrieved via the `requestedFormCompletions` query. This query is available to authenticated provider/staff accounts.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/requestedformcompletions#arguments).

We will go over some of them below.

| Input      | Info                                                                           |
| ---------- | ------------------------------------------------------------------------------ |
| `user_id`  | Optional. ID of the Form recipient.                                            |
| `status`   | Optional. Can be either `Open` or `Incomplete`.                                |
| `keywords` | Optional. A term to search Requests by. Can be searched by Form Template name. |

Returns an array of [`RequestedFormCompletion`](/reference/2024-06-01/objects/requestedformcompletion) objects.

### Creating a Form Completion Request

```
mutation createRequestedFormCompletion(
  $recipient_ids: String
  $form: String
  $is_recurring: Boolean
  $frequency: String
  $period: String
  $minute: String
  $hour: String
  $weekday: String
  $monthday: String
  $recurrence_ends: Boolean
  $ends_on: String
) {
  createRequestedFormCompletion(
    input: {
      recipient_ids: $recipient_ids
      form: $form
      is_recurring: $is_recurring
      frequency: $frequency
      period: $period
      minute: $minute
      hour: $hour
      weekday: $weekday
      monthday: $monthday
      recurrence_ends: $recurrence_ends
      ends_on: $ends_on
    }
  ) {
    requestedFormCompletion {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `createRequestedFormCompletion` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createrequestedforminput).

| Input             | Info                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| `recipient_ids`   | **Required**. Array of User IDs that should receive the Form Completion Request.                |
| `form`            | **Required**. ID of the Form.                                                                   |
| `is_recurring`    | Optional. Set to `true` if the Form completion should be recurring.                             |
| `frequency`       | Required if `is_recurring` is set to `true`. Valid options are:- `Daily`
- `Weekly`
- `Monthly` |
| `period`          | `AM` or `PM`.                                                                                   |
| `minute`          | For instance, if you want to trigger the completion request at 1:05 PM, use `"5"`.              |
| `hour`            | For instance, if you want to trigger the completion request at 1:05 PM, use `"1"`.              |
| `weekday`         | Use the full weekday name, e.g. `"Monday"`.                                                     |
| `monthday`        | Number of the day of month, e.g. `"27th"`.                                                      |
| `recurrence_ends` | Set to true if the recurrence should have an end date.                                          |
| `ends_on`         | Recurrence end date in the `YYYY-MM-DD` format.                                                 |

Returns [`createRequestedFormPayload`](/reference/2024-06-01/objects/createrequestedformpayload).

### Deleting a Form Completion Request

```
mutation deleteRequestedFormCompletion($id: ID, $recurringFormId: ID) {
  deleteRequestedFormCompletion(input: { id: $id, recurringFormId: $recurringFormId }) {
    requestedFormCompletion {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteRequestedFormCompletion` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleterequestedforminput).

| Input             | Info                                                                         |
| ----------------- | ---------------------------------------------------------------------------- |
| `id`              | **Required**. The ID of the Form Completion Request to delete.               |
| `recurringFormId` | Optional. Provide if you also want to delete the recurring form (if exists). |

Returns [`deleteRequestedFormPayload`](/reference/2024-06-01/objects/deleterequestedformpayload).
