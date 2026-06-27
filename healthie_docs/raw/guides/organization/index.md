---
title: Organization Management | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/organization/index
  md: https://docs.gethealthie.com/guides/organization/index.md
---

# Organization Management

## The Organization Object

```
 # Some Example Fields


 "organization": {
      "id": "9900",
      "name": "Healthie",
      "phone_number": "555-444-2244",
      "tax_id": "123456789",
      "tax_id_type": "EIN",
      "npi": "1234567890",
      "location": {
        "city": "New York",
        "country": "US"
      }
    }
```

Organizations are `Organization` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/organization).

## Retrieving an Organization

```
query getOrganization($id: ID) {
  organization(id: $id) {
    id
    name
    location {
      city
      country
    }
  }
}
```

| Input          | Info                                                                               |
| -------------- | ---------------------------------------------------------------------------------- |
| `id`           | Organization ID, if none provided, will retutrn the current user’s Organization    |
| `provider_id`  | Find Organization by Provider ID                                                   |
| `provider_ids` | Find Organization by multiple Provider IDs                                         |
| `email`        | Email address of the User associated with the Organization                         |
| `for_client`   | Use `true` to find the Organization for the currently logged-in end User (Patient) |

## Adding an Organization Member

In order to create a new Organization Member, you should use the `createOrganizationMembership` mutation.

```
mutation createOrganizationMembership(
  $first_name: String
  $last_name: String
  $email: String
  $password: String
  $title: String
  $org_role: String
  $send_invite_email: Boolean
  $phone_number: String
  $dont_send_welcome: Boolean
  $organization_id: ID
  $timezone: String
) {
  createOrganizationMembership(
    input: {
      first_name: $first_name
      last_name: $last_name
      email: $email
      password: $password
      title: $title
      org_role: $org_role
      send_invite_email: $send_invite_email
      phone_number: $phone_number
      dont_send_welcome: $dont_send_welcome
      organization_id: $organization_id
      timezone: $timezone
    }
  ) {
    organizationMembership {
      user {
        id
      }
      org_role
      can_see_calendar
      can_edit_forms
    }


    messages {
      field
      message
    }
  }
}
```

The `createOrganizationMembership` mutation is called from an authenticated Super Admin account or by an Organization Member with `can_add_members` permission.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createorganizationmembershipinput).

| Input               | Info                                                                                                                                                                                                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`   | Required. Specifies to which organization to invite the user.                                                                                                                                                                                                         |
| `first_name`        | Required.                                                                                                                                                                                                                                                             |
| `last_name`         | Required.                                                                                                                                                                                                                                                             |
| `email`             | Required.                                                                                                                                                                                                                                                             |
| `title`             | Optional. Used for additional metadata about the membership. Not used in Healthie UI.                                                                                                                                                                                 |
| `org_role`          | Optional. Either `"Standard"` (default) or `"Support"`.                                                                                                                                                                                                               |
| `password`          | Optional. Sets the default password for the invited user. If provided, needs to be a minimum of 8 chars, and meet a calculated strength requirement. Healthie uses [StrongPassword](https://github.com/bdmac/strong_password) Ruby gem to calculate password strength |
| `send_invite_email` | Optional. Whether to send an invite email.                                                                                                                                                                                                                            |

The `createOrganizationMembership` mutation returns an `OrganizationMembership` object, which describes a list of the new member’s permissions. You can view a full list of potential return properties [here](/reference/2024-06-01/objects/organizationmembership).

## Listing Providers / Organization Members

You can retrieve a list of your organization’s providers and support members using the `organizationMembers` query.

You can view a full list of potential inputs in our [API Explorer](https://docs.gethealthie.com/docs/explorer.html).

```
query getOrganizationMembers(
  $offset: Int
  $page_size: Int
  $keywords: String
  $sort_by: String
  $licensed_in_state: String
  $conversation_id: ID
) {
  organizationMembers(
    offset: $offset
    page_size: $page_size
    keywords: $keywords
    sort_by: $sort_by
    licensed_in_state: $licensed_in_state
    conversation_id: $conversation_id
  ) {
    id
    first_name
    last_name
    email
    has_api_access
  }
}
```

| Input               | Info                                                                                                                                                                                                                                                                                                                              |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort_by`           | Default value is `last_name`. Other options are `email`, `first_name_asc`, `first_name_desc`, `last_name_asc`, `last_name_desc`, `created_at_desc`, `created_at_asc`, `updated_at_desc`, `updated_at_asc`, `group_name_asc`, `group_name_desc`, `provider_name_asc`, `provider_name_desc`, `next_appt_asc`, and `next_appt_desc`. |
| `licensed_in_state` | Two letter state abbreviation (e.g. “CA”, “NY”)                                                                                                                                                                                                                                                                                   |
| `conversation_id`   | Can be used to filter org members by a Conversation ID                                                                                                                                                                                                                                                                            |
| `offset`            | Optional. Offset for pagination                                                                                                                                                                                                                                                                                                   |
| `page_size`         | Defaults to 10. The number of records to return                                                                                                                                                                                                                                                                                   |

## Updating an Organization Membership

```
mutation updateOrganizationMembership(
  $first_name: String
  $last_name: String
  $email: String
  $password: String
  $title: String
  $org_role: String
  $send_invite_email: Boolean
  $phone_number: String
  $dont_send_welcome: Boolean
  $organization_id: ID
  $timezone: String
  $action_for_appointments: String
  $active: Boolean
  $allow_group_level_actions: Boolean
  $allow_self_scheduling_in_care_team: Boolean
  $auto_create_convo_for_care_team: Boolean
  $can_access_calendar_quick_share: Boolean
  $can_access_to_members_chat: Boolean
  $can_access_zus: Boolean
  $can_add_clients: Boolean
  $can_add_members: Boolean
  $can_add_members_to_chat: Boolean
  $can_assign_tasks_to_all_org_members: Boolean
  $can_autogenerate_charting_notes_from_zoom_calls: Boolean
  $can_be_care_team_member: Boolean
  $can_charge_clients: Boolean
  $can_create_tags: Boolean
  $can_delete_charting_notes: Boolean
  $can_delete_faxes: Boolean
  $can_edit_appointment_types: Boolean
  $can_edit_calendar: Boolean
  $can_edit_credit: Boolean
  $can_edit_docs: Boolean
  $can_edit_education: Boolean
  $can_edit_members: Boolean
  $can_edit_packages: Boolean
  $can_edit_products: Boolean
  $can_edit_settings: Boolean
  $can_enroll_clients_to_programs: Boolean
  $can_lock_form_answer_groups: Boolean
  $can_lock_others_charting_notes: Boolean
  $can_lock_own_charting_notes: Boolean
  $can_manage_care_plan_templates: Boolean
  $can_mark_assigned_tasks_to_other_org_members_as_completed: Boolean
  $can_merge_clients: Boolean
  $can_order_labs: Boolean
  $can_remove_client: Boolean
  $can_remove_org_member_signatures: Boolean
  $can_rename_and_delete_tags: Boolean
  $can_restrict_clients: Boolean
  $can_see_billing: Boolean
  $can_see_clients: Boolean
  $can_see_docs: Boolean
  $can_see_faxes: Boolean
  $can_see_fullscript_tab: Boolean
  $can_see_option_to_use_erx_dosespot: Boolean
  $can_see_sent_faxes: Boolean
  $can_see_transfers: Boolean
  $can_set_client_password: Boolean
  $can_share_documents_and_folders_with_org_members: Boolean
  $can_sign_others_charting_notes: Boolean
  $can_sign_own_charting_notes: Boolean
  $can_submit_cms_1500s_to_change_health: Boolean
  $can_submit_cms_1500s_to_office_ally: Boolean
  $can_unlock_charting_notes: Boolean
  $can_view_audit_log: Boolean
  $can_view_all_org_members_tasks: Boolean
  $can_view_cms1500s: Boolean
  $can_view_goal_templates: Boolean
  $can_view_labs: Boolean
  $can_view_org_dashboard: Boolean
  $can_view_reports: Boolean
  $can_view_super_bills: Boolean
  $can_write_org_addendums: Boolean
  $erx_dosespot_role: String
  $fullscript_practitioner_id: String
  $gets_failed_fax_notif: Boolean
  $gets_fax_notif: Boolean
  $has_own_branding: Boolean
  $hide_calendar_tab: Boolean
  $id: ID
  $is_admin: Boolean
  $is_developer: Boolean
  $is_provider: Boolean
  $notify_any_client_activity: Boolean
  $notify_on_book: Boolean
  $notify_on_cancel: Boolean
  $notify_on_payment_failure: Boolean
  $permission_template_id: ID
  $permission_template_applied: Boolean
  $position: Int
  $professions: [ProfessionsInput]
  $provider_to_receive_clients: ID
  $qualifications: String
  $request_eligibility_checks: Boolean
  $scheduling_priority: String
  $sees_all_billing: Boolean
  $sees_all_clients: Boolean
  $selected_licensed_in_filter: [String]
  $selected_locations_filter: [String]
  $selected_statuses_filter: [String]
  $selected_tags_filter: [String]
  $send_email_on_intake_flow_complete: Boolean
  $send_email_on_intake_flow_start: Boolean
  $share_appointment_types: Boolean
  $share_custom_metrics: Boolean
  $share_fullscript: Boolean
  $share_goal_templates: Boolean
  $share_packages: Boolean
  $share_smart_phrases: Boolean
  $share_user_groups: Boolean
  $show_availability_first: Boolean
  $show_org_tab: Boolean
  $specialties: [SpecialtiesInput]
  $start_conversation_with: Boolean
) {
  updateOrganizationMembership(
    input: {
      first_name: $first_name
      last_name: $last_name
      email: $email
      password: $password
      title: $title
      org_role: $org_role
      send_invite_email: $send_invite_email
      phone_number: $phone_number
      dont_send_welcome: $dont_send_welcome
      organization_id: $organization_id
      timezone: $timezone
      # ...
      # any other variables that are passed in from above
      # ...
    }
  ) {
    organizationMembership {
      user {
        id
      }
      org_role
      can_see_calendar
      can_edit_forms
    }


    messages {
      field
      message
    }
  }
}
```

The `updateOrganizationMembership` mutation shares many common inputs with [`createOrganizationMembership`](#adding-an-organization-member) and those inputs (e.g `org_role` or `title` work the same in both places). However, the `updateOrganizationMembership` provides more granular control over the membership object.

The `updateOrganizationMembership` mutation can be called by Super Admins or Organization Members with `can_edit_members` permission.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateorganizationmembershipinput).

| Input            | Info                                                                          |
| ---------------- | ----------------------------------------------------------------------------- |
| `id`             | **Required**. ID of the Organization Membership to update                     |
| `active`         | Optional. Boolean indicating whether the Organization Member should be active |
| `timezone`       | Optional. Allows to update the timezone of the Organization Member            |
| `qualifications` | Optional. Updates the qualifications of the Organization Member               |

Additionally, the `updateOrganizationMembership` mutation accepts a set of Boolean input parameters that determine permissions of the Member.

Returns an [`updateOrganizationMembershipPayload`](/reference/2024-06-01/objects/updateorganizationmembershippayload) object.

## Removing an Organization Member

```
mutation deleteOrganizationMembership($id: ID) {
  deleteOrganizationMembership(input: { id: $id }) {
    organizationMembership {
      id
    }


    messages {
      field
      message
    }
  }
}
```

Organization Memberships can be deleted via the `deleteOrganizationMembership` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleteorganizationmembershipinput).

The `deleteOrganizationMembership` mutation can be called by Super Admins only.

| Input | Info                                          |
| ----- | --------------------------------------------- |
| `id`  | **Required**. ID of the Membership to delete. |

Returns a [`deleteOrganizationMembershipPayload`](/reference/2024-06-01/objects/deleteorganizationmembershippayload) object.
