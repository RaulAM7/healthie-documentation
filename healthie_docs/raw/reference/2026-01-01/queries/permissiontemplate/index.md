---
title: permissionTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/permissiontemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/permissiontemplate/index.md
---

Fetch permission template

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`PermissionTemplateType`](/reference/2026-01-01/objects/permissiontemplatetype)

## Example

```
query permissionTemplate($id: ID) {
  permissionTemplate(id: $id) {
    allow_group_level_actions
    allow_self_scheduling_in_care_team
    auto_create_convo_for_care_team
    can_access_calendar_quick_share
    can_access_to_members_chat
    can_add_clients
    can_add_members
    can_add_members_to_chat
    can_add_others_appointments
    can_add_own_appointments
    can_assign_tasks_to_all_org_members
    can_autogenerate_charting_notes_from_zoom_calls
    can_be_care_team_member
    can_be_edited
    can_charge_clients
    can_create_tags
    can_delete_automations
    can_delete_charting_notes
    can_delete_faxes
    can_delete_recordings
    can_edit_appointment_types
    can_edit_automations
    can_edit_calendar
    can_edit_credit
    can_edit_docs
    can_edit_education
    can_edit_forms
    can_edit_members
    can_edit_packages
    can_edit_products
    can_edit_settings
    can_enroll_clients_to_programs
    can_lock_others_charting_notes
    can_lock_own_charting_notes
    can_manage_care_plan_templates
    can_manage_others_availability
    can_manage_others_blocks
    can_manage_own_availability
    can_manage_own_blocks
    can_mark_assigned_tasks_to_other_org_members_as_completed
    can_merge_clients
    can_order_labs
    can_remove_client
    can_remove_org_member_signatures
    can_rename_and_delete_tags
    can_restrict_clients
    can_see_billing
    can_see_calendar
    can_see_clients
    can_see_docs
    can_see_faxes
    can_see_fullscript_tab
    can_see_sent_faxes
    can_see_transfers
    can_set_client_password
    can_share_documents_and_folders_with_org_members
    can_sign_others_charting_notes
    can_sign_own_charting_notes
    can_submit_cms_1500s_to_office_ally
    can_unlink_chart_note_from_appointment
    can_unlock_charting_notes
    can_view_all_org_members_tasks
    can_view_audit_log
    can_view_automations
    can_view_cms1500s
    can_view_goal_templates
    can_view_labs
    can_view_org_dashboard
    can_view_recordings
    can_view_reports
    can_view_super_bills
    can_write_org_addendums
    create_chat_when_assigned
    created_at
    gets_failed_fax_notif
    gets_fax_notif
    has_own_branding
    id
    is_admin
    is_developer
    is_provider
    name
    notify_any_client_activity
    notify_on_book
    notify_on_cancel
    notify_on_payment_failure
    org_role
    request_eligibility_checks
    sees_all_billing
    sees_all_clients
    send_email_on_intake_flow_complete
    send_email_on_intake_flow_start
    share_appointment_types
    share_custom_metrics
    share_fullscript
    share_goal_templates
    share_packages
    share_smart_phrases
    share_user_groups
    show_availability_first
    show_org_tab
    start_conversation_with
    updated_at
    user
  }
}
```
