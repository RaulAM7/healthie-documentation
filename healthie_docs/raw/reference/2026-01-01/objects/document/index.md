---
title: Document | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/document/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/document/index.md
---

A document file that contains an attachment and information about the attachment

## Fields

[`can_only_share` ](#field-can-only-share)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the user cannot adjust settings for the document besides sharing.

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the document was made available to the given client

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the document

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The display name of the document

[`email_on_welcome` ](#field-email-on-welcome)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Include the file in new clients welcome email

[`expiring_url` ](#field-expiring-url)· [`String` ](/reference/2026-01-01/scalars/string)· A URL to download the file, good for 10 seconds

[`extension` ](#field-extension)· [`String` ](/reference/2026-01-01/scalars/string)· The extension of the document

[`file_content_type` ](#field-file-content-type)· [`String` ](/reference/2026-01-01/scalars/string)· The file type of the document

[`form_answer_groups` ](#field-form-answer-groups)· [`[FormAnswerGroup!]` ](/reference/2026-01-01/objects/formanswergroup)· The form answer groups associated with this document

[`friendly_type` ](#field-friendly-type)· [`String` ](/reference/2026-01-01/scalars/string)· The file extension in human-readable format e.g.: 'Video'/'Audio'/'Excel' etc

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique idenitifer of the document

[`include_in_charting` ](#field-include-in-charting)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Include the document within the private charts section

[`internal_notes` ](#field-internal-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Notes on the document (not visible to the client)

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000. Only accessible by staff and providers

[`opens` ](#field-opens)· [`[DocumentViewing!]` ](/reference/2026-01-01/objects/documentviewing)· Instances of the document being viewed/opened

[`owner` ](#field-owner)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this document

[`rel_user` ](#field-rel-user)· [`User` ](/reference/2026-01-01/objects/user)· In the case of a private document, the user that this document is for

[`rel_user_id` ](#field-rel-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the assigned client

[`shareable_org_members` ](#field-shareable-org-members)· [`UserConnection` ](/reference/2026-01-01/objects/userconnection)· The organization members who may have access to the shareable record

[`shareable_patients` ](#field-shareable-patients)· [`UserConnection` ](/reference/2026-01-01/objects/userconnection)· The patients who may have access to the shareable record

[`shareable_user_groups` ](#field-shareable-user-groups)· [`UserGroupPaginationConnection` ](/reference/2026-01-01/objects/usergrouppaginationconnection)· The user groups that may have access to the shareable record

[`shared` ](#field-shared)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The document shared

[`shared_on_welcome` ](#field-shared-on-welcome)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Share the file with new clients automatically

[`shared_user_groups_count` ](#field-shared-user-groups-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of user groups who the document is shared

[`shared_users_count` ](#field-shared-users-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of users who the document is directly shared with (not through groups)

[`shared_with_dietitians` ](#field-shared-with-dietitians)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Share with all members of the organization

[`unshared_patients_count` ](#field-unshared-patients-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · The number of patients who do not have this item shared with them

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the document was updated

[`user_groups` ](#field-user-groups)· [`[UserGroup!]!` ](/reference/2026-01-01/objects/usergroup)· required · The user groups who have access to this document

[`users` ](#field-users)· [`UserConnection!` ](/reference/2026-01-01/objects/userconnection)· required · The users who have access to this document

## Used By

[`CarePlan.documents`](/reference/2026-01-01/objects/careplan)

[`ChartingItemType.document`](/reference/2026-01-01/objects/chartingitemtype)

[`DocumentEdge.node`](/reference/2026-01-01/objects/documentedge)

[`DocumentPaginationConnection.nodes`](/reference/2026-01-01/objects/documentpaginationconnection)

[`FormAnswerGroup.documents`](/reference/2026-01-01/objects/formanswergroup)

[`LabOrder.document`](/reference/2026-01-01/objects/laborder)

[`LabOrder.pdf_document`](/reference/2026-01-01/objects/laborder)

[`LabOrder.requisition_document`](/reference/2026-01-01/objects/laborder)

[`LabResult.document`](/reference/2026-01-01/objects/labresult)

[`SentDirectMessage.attachments`](/reference/2026-01-01/objects/sentdirectmessage)

[`createDocumentPayload.document`](/reference/2026-01-01/objects/createdocumentpayload)

[`deleteDocumentPayload.document`](/reference/2026-01-01/objects/deletedocumentpayload)

[`shareAnswersAsDocumentPayload.document`](/reference/2026-01-01/objects/shareanswersasdocumentpayload)

[`updateDocumentPayload.document`](/reference/2026-01-01/objects/updatedocumentpayload)

[`Query.document`](/reference/2026-01-01/queries/document)

## Definition

```
"""
A document file that contains an attachment and information about the attachment
"""
type Document {
  """
  When true, the user cannot adjust settings for the document besides sharing.
  """
  can_only_share: Boolean


  """
  The date the document was made available to the given client
  """
  created_at(
    """
    The custom ID of viewable user (default: current user)
    """
    viewable_user_id: String
  ): ISO8601DateTime!


  """
  The description of the document
  """
  description: String


  """
  The display name of the document
  """
  display_name: String


  """
  Include the file in new clients welcome email
  """
  email_on_welcome: Boolean!


  """
  A URL to download the file, good for 10 seconds
  """
  expiring_url: String


  """
  The extension of the document
  """
  extension: String


  """
  The file type of the document
  """
  file_content_type: String


  """
  The form answer groups associated with this document
  """
  form_answer_groups: [FormAnswerGroup!]


  """
  The file extension in human-readable format e.g.: 'Video'/'Audio'/'Excel' etc
  """
  friendly_type: String


  """
  The unique idenitifer of the document
  """
  id: ID!


  """
  Include the document within the private charts section
  """
  include_in_charting: Boolean!


  """
  Notes on the document (not visible to the client)
  """
  internal_notes: String


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000. Only accessible by staff and providers
  """
  metadata: String


  """
  Instances of the document being viewed/opened
  """
  opens: [DocumentViewing!]


  """
  Owner of this document
  """
  owner: User


  """
  In the case of a private document, the user that this document is for
  """
  rel_user: User


  """
  ID of the assigned client
  """
  rel_user_id: ID


  """
  The organization members who may have access to the shareable record
  """
  shareable_org_members(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int


    """
    Search patients by name, identifiers, email, DOB, or NPI
    """
    keywords: String
    order_by: UserOrderKeys = LAST_NAME_ASC


    """
    Filter on organization members that are either already shared or unshared
    """
    shared: Boolean
  ): UserConnection


  """
  The patients who may have access to the shareable record
  """
  shareable_patients(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int


    """
    Search patients by name, identifiers, email, or DOB
    """
    keywords: String
    order_by: UserOrderKeys = LAST_NAME_ASC


    """
    Filter on patients that are either already shared or unshared
    """
    shared: Boolean
  ): UserConnection


  """
  The user groups that may have access to the shareable record
  """
  shareable_user_groups(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int


    """
    Search user groups by name
    """
    keywords: String
    order_by: UserGroupOrderKeys = NAME_ASC


    """
    Filter on user groups that are either already shared or unshared
    """
    shared: Boolean
  ): UserGroupPaginationConnection


  """
  The document shared
  """
  shared: Boolean


  """
  Share the file with new clients automatically
  """
  shared_on_welcome: Boolean!


  """
  The number of user groups who the document is shared
  """
  shared_user_groups_count: Int


  """
  The number of users who the document is directly shared with (not through groups)
  """
  shared_users_count: Int


  """
  Share with all members of the organization
  """
  shared_with_dietitians: Boolean!


  """
  The number of patients who do not have this item shared with them
  """
  unshared_patients_count: Int!


  """
  The date the document was updated
  """
  updated_at: ISO8601DateTime!


  """
  The user groups who have access to this document
  """
  user_groups: [UserGroup!]!


  """
  The users who have access to this document
  """
  users(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
    order_by: UserOrderKeys = LAST_NAME_ASC
  ): UserConnection!
}
```
