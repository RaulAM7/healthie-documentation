---
title: PermissionTemplateType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/permissiontemplatetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/permissiontemplatetype/index.md
---

An permission templateType

## Fields

[`allow_group_level_actions` ](#field-allow-group-level-actions)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Can initiate group level actions (e.g. create group conversations in chat, assign groups to course modules, request form completions from a group)

[`allow_self_scheduling_in_care_team` ](#field-allow-self-scheduling-in-care-team)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, clients who this org member has been added as a care team member will be able to schedule appointments with them.

[`auto_create_convo_for_care_team` ](#field-auto-create-convo-for-care-team)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, clients who this org member has been added as a care team member for will automatically see a Chat conversation with this org member.

[`can_access_calendar_quick_share` ](#field-can-access-calendar-quick-share)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can access calendar quick share

[`can_access_to_members_chat` ](#field-can-access-to-members-chat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user should be able to access other active organization members conversations

[`can_add_clients` ](#field-can-add-clients)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can add new clients

[`can_add_members` ](#field-can-add-members)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can add new people to the organization

[`can_add_members_to_chat` ](#field-can-add-members-to-chat)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user should be able to add other active organization members to chat

[`can_add_others_appointments` ](#field-can-add-others-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can add appointments on other providers' calendars

[`can_add_own_appointments` ](#field-can-add-own-appointments)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can add appointments on their own calendar

[`can_assign_tasks_to_all_org_members` ](#field-can-assign-tasks-to-all-org-members)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user should be able to assign a task to any member of their organization

[`can_autogenerate_charting_notes_from_zoom_calls` ](#field-can-autogenerate-charting-notes-from-zoom-calls)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can autogenerate charting notes by AI Scribe

[`can_be_care_team_member` ](#field-can-be-care-team-member)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can be added to the care team members list for a client

[`can_be_edited` ](#field-can-be-edited)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the current user can modify this permission template

[`can_charge_clients` ](#field-can-charge-clients)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can charge clients

[`can_create_tags` ](#field-can-create-tags)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can create tags

[`can_delete_automations` ](#field-can-delete-automations)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can delete automations

[`can_delete_charting_notes` ](#field-can-delete-charting-notes)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, user сan delete charting notes

[`can_delete_faxes` ](#field-can-delete-faxes)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can delete faxes

[`can_delete_recordings` ](#field-can-delete-recordings)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can delete appointment recordings and transcripts

[`can_edit_appointment_types` ](#field-can-edit-appointment-types)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can edit appointment types

[`can_edit_automations` ](#field-can-edit-automations)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can create and edit automations

[`can_edit_calendar` ](#field-can-edit-calendar)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can edit calendar

[`can_edit_credit` ](#field-can-edit-credit)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can edit client credit

[`can_edit_docs` ](#field-can-edit-docs)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can edit documents

[`can_edit_education` ](#field-can-edit-education)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can edit education content

[`can_edit_forms` ](#field-can-edit-forms)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can edit forms

[`can_edit_members` ](#field-can-edit-members)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can manage the people and roles in the organization

[`can_edit_packages` ](#field-can-edit-packages)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can edit client packages

[`can_edit_products` ](#field-can-edit-products)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can add, edit and delete products

[`can_edit_settings` ](#field-can-edit-settings)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can edit settings

[`can_enroll_clients_to_programs` ](#field-can-enroll-clients-to-programs)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can enroll and remove clients from programs

[`can_lock_others_charting_notes` ](#field-can-lock-others-charting-notes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can lock charting notes other providers created

[`can_lock_own_charting_notes` ](#field-can-lock-own-charting-notes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can lock charting notes they created

[`can_manage_care_plan_templates` ](#field-can-manage-care-plan-templates)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user should be able to manage care plan templates

[`can_manage_others_availability` ](#field-can-manage-others-availability)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can manage other members' availability

[`can_manage_others_blocks` ](#field-can-manage-others-blocks)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can manage other members' blocks

[`can_manage_own_availability` ](#field-can-manage-own-availability)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can manage their own availability

[`can_manage_own_blocks` ](#field-can-manage-own-blocks)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can manage their own blocks

[`can_mark_assigned_tasks_to_other_org_members_as_completed` ](#field-can-mark-assigned-tasks-to-other-org-members-as-completed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, can mark tasks complete that are assigned to other org members

[`can_merge_clients` ](#field-can-merge-clients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can merge clients

[`can_order_labs` ](#field-can-order-labs)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, view labs page and view patient lab results

[`can_remove_client` ](#field-can-remove-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can remove clients

[`can_remove_org_member_signatures` ](#field-can-remove-org-member-signatures)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, can remove other org members' signatures from charting notes

[`can_rename_and_delete_tags` ](#field-can-rename-and-delete-tags)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user should be able to rename or delete tags

[`can_restrict_clients` ](#field-can-restrict-clients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, can restrict client

[`can_see_billing` ](#field-can-see-billing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can view the billing tab

[`can_see_calendar` ](#field-can-see-calendar)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can see all calendars in the organization

[`can_see_clients` ](#field-can-see-clients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can see all clients in the organization

[`can_see_docs` ](#field-can-see-docs)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can see documents within the entire org

[`can_see_faxes` ](#field-can-see-faxes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can see incoming faxes

[`can_see_fullscript_tab` ](#field-can-see-fullscript-tab)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true user should be able to see fullscript tab in client profile and view fullscript box in homepage

[`can_see_sent_faxes` ](#field-can-see-sent-faxes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can see sent faxes

[`can_see_transfers` ](#field-can-see-transfers)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can see transfers tab in billing page

[`can_set_client_password` ](#field-can-set-client-password)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, user can set client passwords

[`can_share_documents_and_folders_with_org_members` ](#field-can-share-documents-and-folders-with-org-members)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can share documents and folders with organizations members

[`can_sign_others_charting_notes` ](#field-can-sign-others-charting-notes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can sign charting notes other providers created

[`can_sign_own_charting_notes` ](#field-can-sign-own-charting-notes)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can sign charting notes they created

[`can_submit_cms_1500s_to_office_ally` ](#field-can-submit-cms-1500s-to-office-ally)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can submit CMS 1500s to Office Ally

[`can_unlink_chart_note_from_appointment` ](#field-can-unlink-chart-note-from-appointment)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can unlink chart notes from appointments

[`can_unlock_charting_notes` ](#field-can-unlock-charting-notes)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can unlock charting notes

[`can_view_all_org_members_tasks` ](#field-can-view-all-org-members-tasks)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, it will return all organization tasks for current user

[`can_view_audit_log` ](#field-can-view-audit-log)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can access the audit log API query.

[`can_view_automations` ](#field-can-view-automations)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true, the user can view automations

[`can_view_cms1500s` ](#field-can-view-cms1500s)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can view/edit cms1500s

[`can_view_goal_templates` ](#field-can-view-goal-templates)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true can use goal favorites that are shared from other members of the organization

[`can_view_labs` ](#field-can-view-labs)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can edit appointment types

[`can_view_org_dashboard` ](#field-can-view-org-dashboard)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can view org dashboard

[`can_view_recordings` ](#field-can-view-recordings)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can view appointment recordings and transcripts

[`can_view_reports` ](#field-can-view-reports)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can view organization-level reports

[`can_view_super_bills` ](#field-can-view-super-bills)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can view/edit super bills

[`can_write_org_addendums` ](#field-can-write-org-addendums)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can write addendums for other org members charting notes

[`create_chat_when_assigned` ](#field-create-chat-when-assigned)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, a chat conversation will be automatically created when a client is assigned to the member

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date of creation

[`gets_failed_fax_notif` ](#field-gets-failed-fax-notif)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user will receive notif about failed notif

[`gets_fax_notif` ](#field-gets-fax-notif)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user will receive a fax notif

[`has_own_branding` ](#field-has-own-branding)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true the user will have their own branding

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the template

[`is_admin` ](#field-is-admin)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user has been noted as being an admin

[`is_developer` ](#field-is-developer)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the user is a developer

[`is_provider` ](#field-is-provider)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the user is a provider in the organization

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of template

[`notify_any_client_activity` ](#field-notify-any-client-activity)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user is notified when any client activity including intake forms, journal entries, programs, documents

[`notify_on_book` ](#field-notify-on-book)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true the user is notified when any appointment is booked within the org

[`notify_on_cancel` ](#field-notify-on-cancel)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true the user is notified when any appointment is cancelled within the org

[`notify_on_payment_failure` ](#field-notify-on-payment-failure)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, user will notified about all failed payments

[`org_role` ](#field-org-role)· [`String` ](/reference/2026-01-01/scalars/string)· The organization role

[`request_eligibility_checks` ](#field-request-eligibility-checks)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user can request eligibility checks

[`sees_all_billing` ](#field-sees-all-billing)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user will see all org billing, not just individual

[`sees_all_clients` ](#field-sees-all-clients)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user will see all org clients, not just individual on clients list page

[`send_email_on_intake_flow_complete` ](#field-send-email-on-intake-flow-complete)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user receive email notification when any client in the organization completes an intake flow

[`send_email_on_intake_flow_start` ](#field-send-email-on-intake-flow-start)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user receive email notification when any client in the organization starts an intake flow

[`share_appointment_types` ](#field-share-appointment-types)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user will share appointment types with the entire org

[`share_custom_metrics` ](#field-share-custom-metrics)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user shares custom metrics with entire org

[`share_fullscript` ](#field-share-fullscript)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true user should uses the same API access token for Fullscript

[`share_goal_templates` ](#field-share-goal-templates)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true has their goal favorites available to other members of the organization

[`share_packages` ](#field-share-packages)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the user shares packages with entire org

[`share_smart_phrases` ](#field-share-smart-phrases)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, all active organization members will see shared smart phrases

[`share_user_groups` ](#field-share-user-groups)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true the user will share user groups with the entire org

[`show_availability_first` ](#field-show-availability-first)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Show availability in the calendar by default

[`show_org_tab` ](#field-show-org-tab)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, show org link on left hand side

[`start_conversation_with` ](#field-start-conversation-with)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true the clients are able to start a new conversation with the member

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date when record was last updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The user attached to the organization membership

## Used By

[`Organization.permission_templates`](/reference/2026-01-01/objects/organization)

[`OrganizationMembership.permission_template`](/reference/2026-01-01/objects/organizationmembership)

[`PermissionTemplateTypeEdge.node`](/reference/2026-01-01/objects/permissiontemplatetypeedge)

[`PermissionTemplateTypePaginationConnection.nodes`](/reference/2026-01-01/objects/permissiontemplatetypepaginationconnection)

[`createPermissionTemplatePayload.newPermissionTemplate`](/reference/2026-01-01/objects/createpermissiontemplatepayload)

[`deletePermissionTemplatePayload.permission_template`](/reference/2026-01-01/objects/deletepermissiontemplatepayload)

[`updatePermissionTemplatePayload.permissionTemplate`](/reference/2026-01-01/objects/updatepermissiontemplatepayload)

[`Query.permissionTemplate`](/reference/2026-01-01/queries/permissiontemplate)

## Definition

```
"""
An permission templateType
"""
type PermissionTemplateType {
  """
  Can initiate group level actions (e.g. create group conversations in chat, assign groups to course modules, request form completions from a group)
  """
  allow_group_level_actions: Boolean!


  """
  If true, clients who this org member has been added as a care team member will be able to schedule appointments with them.
  """
  allow_self_scheduling_in_care_team: Boolean


  """
  If true, clients who this org member has been added as a care team member for will automatically see a Chat conversation with this org member.
  """
  auto_create_convo_for_care_team: Boolean


  """
  If true, the user can access calendar quick share
  """
  can_access_calendar_quick_share: Boolean!


  """
  If true, the user should be able to access other active organization members conversations
  """
  can_access_to_members_chat: Boolean


  """
  If true, the user can add new clients
  """
  can_add_clients: Boolean!


  """
  If true, the user can add new people to the organization
  """
  can_add_members: Boolean!


  """
  If true, the user should be able to add other active organization members to chat
  """
  can_add_members_to_chat: Boolean


  """
  If true, the user can add appointments on other providers' calendars
  """
  can_add_others_appointments: Boolean


  """
  If true, the user can add appointments on their own calendar
  """
  can_add_own_appointments: Boolean


  """
  If true, the user should be able to assign a task to any member of their organization
  """
  can_assign_tasks_to_all_org_members: Boolean


  """
  If true, the user can autogenerate charting notes by AI Scribe
  """
  can_autogenerate_charting_notes_from_zoom_calls: Boolean


  """
  If true, the user can be added to the care team members list for a client
  """
  can_be_care_team_member: Boolean!


  """
  If true, the current user can modify this permission template
  """
  can_be_edited: Boolean!


  """
  If true, the user can charge clients
  """
  can_charge_clients: Boolean!


  """
  If true, the user can create tags
  """
  can_create_tags: Boolean


  """
  If true, the user can delete automations
  """
  can_delete_automations: Boolean!


  """
  If true, user сan delete charting notes
  """
  can_delete_charting_notes: Boolean!


  """
  If true, the user can delete faxes
  """
  can_delete_faxes: Boolean!


  """
  If true, the user can delete appointment recordings and transcripts
  """
  can_delete_recordings: Boolean


  """
  If true, the user can edit appointment types
  """
  can_edit_appointment_types: Boolean!


  """
  If true, the user can create and edit automations
  """
  can_edit_automations: Boolean!


  """
  If true, the user can edit calendar
  """
  can_edit_calendar: Boolean


  """
  If true, the user can edit client credit
  """
  can_edit_credit: Boolean


  """
  If true, the user can edit documents
  """
  can_edit_docs: Boolean


  """
  If true, the user can edit education content
  """
  can_edit_education: Boolean


  """
  If true, the user can edit forms
  """
  can_edit_forms: Boolean


  """
  If true, the user can manage the people and roles in the organization
  """
  can_edit_members: Boolean


  """
  If true, the user can edit client packages
  """
  can_edit_packages: Boolean


  """
  If true, the user can add, edit and delete products
  """
  can_edit_products: Boolean


  """
  If true, the user can edit settings
  """
  can_edit_settings: Boolean


  """
  If true, the user can enroll and remove clients from programs
  """
  can_enroll_clients_to_programs: Boolean


  """
  If true, the user can lock charting notes other providers created
  """
  can_lock_others_charting_notes: Boolean


  """
  If true, the user can lock charting notes they created
  """
  can_lock_own_charting_notes: Boolean


  """
  If true, the user should be able to manage care plan templates
  """
  can_manage_care_plan_templates: Boolean


  """
  If true, the user can manage other members' availability
  """
  can_manage_others_availability: Boolean


  """
  If true, the user can manage other members' blocks
  """
  can_manage_others_blocks: Boolean


  """
  If true, the user can manage their own availability
  """
  can_manage_own_availability: Boolean


  """
  If true, the user can manage their own blocks
  """
  can_manage_own_blocks: Boolean


  """
  If true, can mark tasks complete that are assigned to other org members
  """
  can_mark_assigned_tasks_to_other_org_members_as_completed: Boolean


  """
  If true, the user can merge clients
  """
  can_merge_clients: Boolean


  """
  If true, view labs page and view patient lab results
  """
  can_order_labs: Boolean


  """
  If true, the user can remove clients
  """
  can_remove_client: Boolean


  """
  If true, can remove other org members' signatures from charting notes
  """
  can_remove_org_member_signatures: Boolean


  """
  If true, the user should be able to rename or delete tags
  """
  can_rename_and_delete_tags: Boolean


  """
  If true, can restrict client
  """
  can_restrict_clients: Boolean


  """
  If true, the user can view the billing tab
  """
  can_see_billing: Boolean


  """
  If true, the user can see all calendars in the organization
  """
  can_see_calendar: Boolean


  """
  If true, the user can see all clients in the organization
  """
  can_see_clients: Boolean


  """
  If true, the user can see documents within the entire org
  """
  can_see_docs: Boolean


  """
  If true, the user can see incoming faxes
  """
  can_see_faxes: Boolean


  """
  If true user should be able to see fullscript tab in client profile and view fullscript box in homepage
  """
  can_see_fullscript_tab: Boolean


  """
  If true, the user can see sent faxes
  """
  can_see_sent_faxes: Boolean


  """
  If true, the user can see transfers tab in billing page
  """
  can_see_transfers: Boolean


  """
  If true, user can set client passwords
  """
  can_set_client_password: Boolean


  """
  If true, the user can share documents and folders with organizations members
  """
  can_share_documents_and_folders_with_org_members: Boolean


  """
  If true, the user can sign charting notes other providers created
  """
  can_sign_others_charting_notes: Boolean


  """
  If true, the user can sign charting notes they created
  """
  can_sign_own_charting_notes: Boolean


  """
  If true, the user can submit CMS 1500s to Office Ally
  """
  can_submit_cms_1500s_to_office_ally: Boolean


  """
  If true, the user can unlink chart notes from appointments
  """
  can_unlink_chart_note_from_appointment: Boolean!


  """
  If true, the user can unlock charting notes
  """
  can_unlock_charting_notes: Boolean!


  """
  If true, it will return all organization tasks for current user
  """
  can_view_all_org_members_tasks: Boolean


  """
  If true, the user can access the audit log API query.
  """
  can_view_audit_log: Boolean


  """
  If true, the user can view automations
  """
  can_view_automations: Boolean!


  """
  If true, the user can view/edit cms1500s
  """
  can_view_cms1500s: Boolean


  """
  If true can use goal favorites that are shared from other members of the organization
  """
  can_view_goal_templates: Boolean


  """
  If true, the user can edit appointment types
  """
  can_view_labs: Boolean


  """
  If true, the user can view org dashboard
  """
  can_view_org_dashboard: Boolean


  """
  If true, the user can view appointment recordings and transcripts
  """
  can_view_recordings: Boolean


  """
  If true, the user can view organization-level reports
  """
  can_view_reports: Boolean


  """
  If true, the user can view/edit super bills
  """
  can_view_super_bills: Boolean


  """
  If true, the user can write addendums for other org members charting notes
  """
  can_write_org_addendums: Boolean


  """
  If true, a chat conversation will be automatically created when a client is assigned to the member
  """
  create_chat_when_assigned: Boolean


  """
  The date of creation
  """
  created_at: ISO8601DateTime!


  """
  If true, the user will receive notif about failed notif
  """
  gets_failed_fax_notif: Boolean


  """
  If true, the user will receive a fax notif
  """
  gets_fax_notif: Boolean


  """
  If true the user will have their own branding
  """
  has_own_branding: Boolean


  """
  The unique identifier of the template
  """
  id: ID!


  """
  If true, the user has been noted as being an admin
  """
  is_admin: Boolean


  """
  Whether the user is a developer
  """
  is_developer: Boolean


  """
  Whether the user is a provider in the organization
  """
  is_provider: Boolean


  """
  Name of template
  """
  name: String


  """
  If true, the user is notified when any client activity including intake forms, journal entries, programs, documents
  """
  notify_any_client_activity: Boolean


  """
  If true the user is notified when any appointment is booked within the org
  """
  notify_on_book: Boolean


  """
  If true the user is notified when any appointment is cancelled within the org
  """
  notify_on_cancel: Boolean


  """
  If true, user will notified about all failed payments
  """
  notify_on_payment_failure: Boolean


  """
  The organization role
  """
  org_role: String


  """
  If true, the user can request eligibility checks
  """
  request_eligibility_checks: Boolean


  """
  If true, the user will see all org billing, not just individual
  """
  sees_all_billing: Boolean


  """
  If true, the user will see all org clients, not just individual on clients list page
  """
  sees_all_clients: Boolean


  """
  If true, the user receive email notification when any client in the organization completes an intake flow
  """
  send_email_on_intake_flow_complete: Boolean


  """
  If true, the user receive email notification when any client in the organization starts an intake flow
  """
  send_email_on_intake_flow_start: Boolean


  """
  If true, the user will share appointment types with the entire org
  """
  share_appointment_types: Boolean


  """
  If true, the user shares custom metrics with entire org
  """
  share_custom_metrics: Boolean


  """
  If true user should uses the same API access token for Fullscript
  """
  share_fullscript: Boolean


  """
  If true has their goal favorites available to other members of the organization
  """
  share_goal_templates: Boolean


  """
  If true, the user shares packages with entire org
  """
  share_packages: Boolean


  """
  If true, all active organization members will see shared smart phrases
  """
  share_smart_phrases: Boolean


  """
  If true the user will share user groups with the entire org
  """
  share_user_groups: Boolean


  """
  Show availability in the calendar by default
  """
  show_availability_first: Boolean


  """
  If true, show org link on left hand side
  """
  show_org_tab: Boolean


  """
  If true the clients are able to start a new conversation with the member
  """
  start_conversation_with: Boolean


  """
  Date when record was last updated
  """
  updated_at: ISO8601DateTime


  """
  The user attached to the organization membership
  """
  user: User
}
```
