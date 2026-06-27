---
title: FormAnswerGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroup/index.md
---

A completed form, with metadata about the completion, and the saved answers

## Fields

[`appointment` ](#field-appointment)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· The appointment the note is connected to

[`autoscored_sections` ](#field-autoscored-sections)· [`[AutoscoredSectionType!]!` ](/reference/2026-01-01/objects/autoscoredsectiontype)· required · The autoscored sections for the filled form

[`chart_note_status` ](#field-chart-note-status)· [`ChartNoteStatus` ](/reference/2026-01-01/enums/chartnotestatus)· The status of the charting note

[`charting_note_addendums` ](#field-charting-note-addendums)· [`[ChartingNoteAddendumType!]` ](/reference/2026-01-01/objects/chartingnoteaddendumtype)· The addendums added to the locked charting note

[`cms1500` ](#field-cms1500)· [`Cms1500` ](/reference/2026-01-01/objects/cms1500)· The CMS1500 created from the form answer group

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date on which the filled form was saved. If form is associated with an appointment, this is the date and time of service.

[`current_summary` ](#field-current-summary)· [`GeneratedSummary` ](/reference/2026-01-01/objects/generatedsummary)· The most recent generated summary. Null if no summary has been generated

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· The form template that was filled out

[`deleted_at` ](#field-deleted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date the form was deleted

[`documents` ](#field-documents)· [`[Document!]` ](/reference/2026-01-01/objects/document)· The documents associated with the form answer group

[`external_id` ](#field-external-id)· [`String` ](/reference/2026-01-01/scalars/string)· An external ID stored on the filled form or charting note

[`filler` ](#field-filler)· [`User` ](/reference/2026-01-01/objects/user)· The user who filled out the form

[`finished` ](#field-finished)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the filled form has been saved by the user (verse a hidden draft)

[`form_answer_group_audit_events` ](#field-form-answer-group-audit-events)· [`[FormAnswerGroupAuditEvent!]!` ](/reference/2026-01-01/objects/formanswergroupauditevent)· required · The history when a charting note was locked, unlocked or signed

[`form_answer_group_prescriptions` ](#field-form-answer-group-prescriptions)· [`[Prescription!]!` ](/reference/2026-01-01/objects/prescription)· required · A list of associated dosespot prescriptions

[`form_answer_group_signings` ](#field-form-answer-group-signings)· [`[FormAnswerGroupSigning!]!` ](/reference/2026-01-01/objects/formanswergroupsigning)· required · Signatures for the form

[`form_answer_group_users_connections` ](#field-form-answer-group-users-connections)· [`[FormAnswerGroupUserConnection!]` ](/reference/2026-01-01/objects/formanswergroupuserconnection)· A list of connections between a form\_answer\_group and group appointment users

[`form_answers` ](#field-form-answers)· [`[FormAnswer!]!` ](/reference/2026-01-01/objects/formanswer)· required · The visible answers for the filled form

[`frozen` ](#field-frozen)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· when true, the note cannot be edited

[`group_appointment_attendees` ](#field-group-appointment-attendees)· [`[User!]` ](/reference/2026-01-01/objects/user)· All patients that have attended in the related group appointment

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the group

[`individual_client_notes` ](#field-individual-client-notes)· [`[IndividualClientType!]` ](/reference/2026-01-01/objects/individualclienttype)· A collection of individual charting notes related to the main group charting note

[`individual_note` ](#field-individual-note)· [`IndividualClientType` ](/reference/2026-01-01/objects/individualclienttype)· Same as individual\_client\_notes but returns a specific instance for given user

[`is_group_appt_note` ](#field-is-group-appt-note)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicates whether the answer group is related to group appointment (charting note created for group appointment)

[`is_locked` ](#field-is-locked)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Shows whether \`FormAnswerGroup\` is locked

[`lab_orders` ](#field-lab-orders)· [`[LabOrder!]` ](/reference/2026-01-01/objects/laborder)· The lab orders associated with the form answer group

[`locked_at` ](#field-locked-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date and time when the charting note was locked

[`locked_by` ](#field-locked-by)· [`User` ](/reference/2026-01-01/objects/user)· The provider who have locked the charting note

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000. Only accessible by staff and providers

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The given name of the filled form

[`narx_checks` ](#field-narx-checks)· [`[NarxCheck!]!` ](/reference/2026-01-01/objects/narxcheck)· required · A list of associated dosespot Narx checks, sorted by timestamp ascending

[`offering_with_recommended_products` ](#field-offering-with-recommended-products)· [`Offering` ](/reference/2026-01-01/objects/offering)· If you have product recommendation algorithm enabled, this will return a package containing the products recommended by the algorithm

[`packages_with_recommended_products_purchase_url` ](#field-packages-with-recommended-products-purchase-url)· [`String` ](/reference/2026-01-01/scalars/string)· If you have product recommendation algorithm enabled, this will return a package containing a URL to purchase the products recommended by the algorithm

deprecated

Not used anywhere, will cause an error

[`provider_can_add_addendum` ](#field-provider-can-add-addendum)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether current user or given user can add addendum to this \`form\_answer\_group\`

[`provider_can_lock` ](#field-provider-can-lock)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether current user or given user can lock this \`form\_answer\_group\`

[`provider_can_sign` ](#field-provider-can-sign)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether current user or given user can sign this \`form\_answer\_group\`

[`provider_can_unlock` ](#field-provider-can-unlock)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether current user or given user can unlock this \`form\_answer\_group\`

[`record_created_at` ](#field-record-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date that the note was actually created

[`requested_form_completion` ](#field-requested-form-completion)· [`RequestedFormCompletion` ](/reference/2026-01-01/objects/requestedformcompletion)· The form request associated with the completed form

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The last updated date for the filled form

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The user the form is about

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the user

[`versioning_stream_name` ](#field-versioning-stream-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the signed stream to track changes in \`form\_answers\`

## Used By

[`Appointment.filled_embed_form`](/reference/2026-01-01/objects/appointment)

[`Appointment.form_answer_group`](/reference/2026-01-01/objects/appointment)

[`Appointment.form_answer_groups`](/reference/2026-01-01/objects/appointment)

[`ChartingItemType.form_answer_group`](/reference/2026-01-01/objects/chartingitemtype)

[`ChartingNoteAddendumType.form_answer_group`](/reference/2026-01-01/objects/chartingnoteaddendumtype)

[`CreateClientViaFormPayload.form_answer_group`](/reference/2026-01-01/objects/createclientviaformpayload)

[`CustomModuleForm.form_answer_groups`](/reference/2026-01-01/objects/custommoduleform)

[`Document.form_answer_groups`](/reference/2026-01-01/objects/document)

[`FormAnswer.form_answer_group`](/reference/2026-01-01/objects/formanswer)

[`FormAnswerGroupAuditEvent.form_answer_group`](/reference/2026-01-01/objects/formanswergroupauditevent)

[`FormAnswerGroupEdge.node`](/reference/2026-01-01/objects/formanswergroupedge)

[`FormAnswerGroupPaginationConnection.nodes`](/reference/2026-01-01/objects/formanswergrouppaginationconnection)

[`GeneratedFormAnswerGroupType.form_answer_group`](/reference/2026-01-01/objects/generatedformanswergrouptype)

[`LabOrder.form_answer_group`](/reference/2026-01-01/objects/laborder)

[`LockPayload.form_answer_group`](/reference/2026-01-01/objects/lockpayload)

[`PatientEncounter.charting_notes`](/reference/2026-01-01/objects/patientencounter)

[`RequestedFormCompletion.form_answer_group`](/reference/2026-01-01/objects/requestedformcompletion)

[`SignPayload.form_answer_group`](/reference/2026-01-01/objects/signpayload)

[`Subscription.formAnswerGroupModifiedSubscription`](/reference/2026-01-01/objects/subscription)

[`UnlockPayload.form_answer_group`](/reference/2026-01-01/objects/unlockpayload)

[`User.form_answer_groups`](/reference/2026-01-01/objects/user)

[`convertGeneratedFormAnswerGroupPayload.form_answer_group`](/reference/2026-01-01/objects/convertgeneratedformanswergrouppayload)

[`createAppointmentFormAnswerGroupConnectionPayload.form_answer_group`](/reference/2026-01-01/objects/createappointmentformanswergroupconnectionpayload)

[`createFormAnswerGroupPayload.form_answer_group`](/reference/2026-01-01/objects/createformanswergrouppayload)

[`deleteAppointmentFormAnswerGroupConnectionPayload.form_answer_group`](/reference/2026-01-01/objects/deleteappointmentformanswergroupconnectionpayload)

[`deleteFormAnswerGroupPayload.form_answer_group`](/reference/2026-01-01/objects/deleteformanswergrouppayload)

[`updateFormAnswerGroupPayload.form_answer_group`](/reference/2026-01-01/objects/updateformanswergrouppayload)

[`Query.formAnswerGroup`](/reference/2026-01-01/queries/formanswergroup)

## Definition

```
"""
A completed form, with metadata about the completion, and the saved answers
"""
type FormAnswerGroup {
  """
  The appointment the note is connected to
  """
  appointment: Appointment


  """
  The autoscored sections for the filled form
  """
  autoscored_sections: [AutoscoredSectionType!]!


  """
  The status of the charting note
  """
  chart_note_status: ChartNoteStatus


  """
  The addendums added to the locked charting note
  """
  charting_note_addendums: [ChartingNoteAddendumType!]


  """
  The CMS1500 created from the form answer group
  """
  cms1500: Cms1500


  """
  The date on which the filled form was saved. If form is associated with an appointment, this is the date and time of service.
  """
  created_at: ISO8601DateTime!


  """
  The most recent generated summary. Null if no summary has been generated
  """
  current_summary: GeneratedSummary


  """
  The form template that was filled out
  """
  custom_module_form: CustomModuleForm


  """
  The date the form was deleted
  """
  deleted_at: ISO8601DateTime


  """
  The documents associated with the form answer group
  """
  documents: [Document!]


  """
  An external ID stored on the filled form or charting note
  """
  external_id: String


  """
  The user who filled out the form
  """
  filler: User


  """
  Whether the filled form has been saved by the user (verse a hidden draft)
  """
  finished: Boolean!


  """
  The history when a charting note was locked, unlocked or signed
  """
  form_answer_group_audit_events: [FormAnswerGroupAuditEvent!]!


  """
  A list of associated dosespot prescriptions
  """
  form_answer_group_prescriptions: [Prescription!]!


  """
  Signatures for the form
  """
  form_answer_group_signings: [FormAnswerGroupSigning!]!


  """
  A list of connections between a form_answer_group and group appointment users
  """
  form_answer_group_users_connections: [FormAnswerGroupUserConnection!]


  """
  The visible answers for the filled form
  """
  form_answers(
    """
    When true, all answers (even conditionally hidden ones) are returned.
    """
    is_for_editing: Boolean = false


    """
    If provided, only answers for the given custom module ids are returned
    """
    custom_module_ids: [ID]
  ): [FormAnswer!]!


  """
  when true, the note cannot be edited
  """
  frozen: Boolean


  """
  All patients that have attended in the related group appointment
  """
  group_appointment_attendees: [User!]


  """
  The unique identifier of the group
  """
  id: ID!


  """
  A collection of individual charting notes related to the main group charting note
  """
  individual_client_notes(
    """
    Preferable sorting order
    """
    order_by: IndividualClientNoteOrderKeys


    """
    Preferable sorting order
    """
    sort_by: IndividualClientNoteSorting
      @deprecated(reason: "Use `order_by` instead")
  ): [IndividualClientType!]


  """
  Same as individual_client_notes but returns a specific instance for given user
  """
  individual_note(
    """
    The client's ID
    """
    user_id: ID
  ): IndividualClientType


  """
  Indicates whether the answer group is related to group appointment (charting note created for group appointment)
  """
  is_group_appt_note: Boolean


  """
  Shows whether `FormAnswerGroup` is locked
  """
  is_locked: Boolean!


  """
  The lab orders associated with the form answer group
  """
  lab_orders: [LabOrder!]


  """
  The date and time when the charting note was locked
  """
  locked_at: ISO8601DateTime


  """
  The provider who have locked the charting note
  """
  locked_by: User


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000. Only accessible by staff and providers
  """
  metadata: String


  """
  The given name of the filled form
  """
  name: String


  """
  A list of associated dosespot Narx checks, sorted by timestamp ascending
  """
  narx_checks: [NarxCheck!]!


  """
  If you have product recommendation algorithm enabled, this will return a package containing the products recommended by the algorithm
  """
  offering_with_recommended_products: Offering


  """
  If you have product recommendation algorithm enabled, this will return a package containing a URL to purchase the products recommended by the algorithm
  """
  packages_with_recommended_products_purchase_url: String
    @deprecated(reason: "Not used anywhere, will cause an error")


  """
  Whether current user or given user can add addendum to this `form_answer_group`
  """
  provider_can_add_addendum(
    """
    Given provider's id. Falls back to current user if not given
    """
    provider_id: ID = null
  ): Boolean!


  """
  Whether current user or given user can lock this `form_answer_group`
  """
  provider_can_lock(
    """
    Given provider's id. Falls back to current user if not given
    """
    provider_id: ID = null
  ): Boolean!


  """
  Whether current user or given user can sign this `form_answer_group`
  """
  provider_can_sign(
    """
    Given provider's id. Falls back to current user if not given
    """
    provider_id: ID = null
  ): Boolean!


  """
  Whether current user or given user can unlock this `form_answer_group`
  """
  provider_can_unlock(
    """
    Given provider's id. Falls back to current user if not given
    """
    provider_id: ID = null
  ): Boolean!


  """
  The date that the note was actually created
  """
  record_created_at: ISO8601DateTime


  """
  The form request associated with the completed form
  """
  requested_form_completion: RequestedFormCompletion


  """
  The last updated date for the filled form
  """
  updated_at: ISO8601DateTime!


  """
  The user the form is about
  """
  user: User


  """
  ID of the user
  """
  user_id: String


  """
  The name of the signed stream to track changes in `form_answers`
  """
  versioning_stream_name: String
}
```
