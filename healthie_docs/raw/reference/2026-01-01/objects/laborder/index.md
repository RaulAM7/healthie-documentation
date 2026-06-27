---
title: LabOrder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/laborder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/laborder/index.md
---

Lab Order Object

## Fields

[`abnormal` ](#field-abnormal)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· abnormality in results

[`appt_confirmation_code` ](#field-appt-confirmation-code)· [`String` ](/reference/2026-01-01/scalars/string)· Confirmation Code of Scheduled Appointment

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date Lab Order was Placed

[`document` ](#field-document)· [`Document` ](/reference/2026-01-01/objects/document)· Get result document

[`external_identifier` ](#field-external-identifier)· [`ID` ](/reference/2026-01-01/scalars/id)· The order id for the lab vendor

[`form_answer_group` ](#field-form-answer-group)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· Associated chart note

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the order

[`integration` ](#field-integration)· [`LabOrderIntegration!` ](/reference/2026-01-01/enums/laborderintegration)· required · Order integration (lab\_testing\_api, evexia, rupa, vital)

[`interpretation` ](#field-interpretation)· [`LabOrderInterpretation!` ](/reference/2026-01-01/enums/laborderinterpretation)· required · The highest level interpretation of the lab results

[`lab` ](#field-lab)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the lab

[`lab_company` ](#field-lab-company)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the lab

[`lab_options` ](#field-lab-options)· [`[LabOption!]!` ](/reference/2026-01-01/objects/laboption)· required · Lab options included in lab order

[`lab_results` ](#field-lab-results)· [`[LabResult!]!` ](/reference/2026-01-01/objects/labresult)· required · Lab results

[`latest_result_received_at` ](#field-latest-result-received-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Timestamp for recording when lab order last received results, if applicable

[`lta_id` ](#field-lta-id)· [`String` ](/reference/2026-01-01/scalars/string)· Order ID

[`normalized_status` ](#field-normalized-status)· [`String` ](/reference/2026-01-01/scalars/string)· The normalized status of the order

[`orderer` ](#field-orderer)· [`User` ](/reference/2026-01-01/objects/user)· Provider who ordered lab order

[`patient` ](#field-patient)· [`User` ](/reference/2026-01-01/objects/user)· Patient for lab order

[`pdf_document` ](#field-pdf-document)· [`Document` ](/reference/2026-01-01/objects/document)· Get most recent pdf document

[`requisition_document` ](#field-requisition-document)· [`Document` ](/reference/2026-01-01/objects/document)· The requisition of the order. Contact support for more info.

[`reviewing_provider` ](#field-reviewing-provider)· [`User` ](/reference/2026-01-01/objects/user)· Provider for review of lab order

[`rupa_order_id` ](#field-rupa-order-id)· [`String` ](/reference/2026-01-01/scalars/string)· Order ID on the rupa health

[`show_pdf_messages` ](#field-show-pdf-messages)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Show lab result with PDF document

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· Status of the Lab Order

[`test_date` ](#field-test-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· Date of Test

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date Lab Order was updated

[`view_rupa_order_url` ](#field-view-rupa-order-url)· [`String` ](/reference/2026-01-01/scalars/string)· Link to view the rupa order

## Used By

[`FormAnswerGroup.lab_orders`](/reference/2026-01-01/objects/formanswergroup)

[`LabOrderEdge.node`](/reference/2026-01-01/objects/laborderedge)

[`LabOrderPaginationConnection.nodes`](/reference/2026-01-01/objects/laborderpaginationconnection)

[`createLabOrderPayload.lab_order`](/reference/2026-01-01/objects/createlaborderpayload)

[`updateLabOrderPayload.lab_order`](/reference/2026-01-01/objects/updatelaborderpayload)

[`Query.labOrder`](/reference/2026-01-01/queries/laborder)

## Definition

```
"""
Lab Order Object
"""
type LabOrder {
  """
  abnormality in results
  """
  abnormal: Boolean


  """
  Confirmation Code of Scheduled Appointment
  """
  appt_confirmation_code: String


  """
  Date Lab Order was Placed
  """
  created_at: ISO8601DateTime!


  """
  Get result document
  """
  document: Document


  """
  The order id for the lab vendor
  """
  external_identifier: ID


  """
  Associated chart note
  """
  form_answer_group: FormAnswerGroup


  """
  The unique identifier of the order
  """
  id: ID!


  """
  Order integration (lab_testing_api, evexia, rupa, vital)
  """
  integration: LabOrderIntegration!


  """
  The highest level interpretation of the lab results
  """
  interpretation: LabOrderInterpretation!


  """
  Name of the lab
  """
  lab: String


  """
  Name of the lab
  """
  lab_company: String


  """
  Lab options included in lab order
  """
  lab_options: [LabOption!]!


  """
  Lab results
  """
  lab_results: [LabResult!]!


  """
  Timestamp for recording when lab order last received results, if applicable
  """
  latest_result_received_at: ISO8601DateTime


  """
  Order ID
  """
  lta_id: String


  """
  The normalized status of the order
  """
  normalized_status: String


  """
  Provider who ordered lab order
  """
  orderer: User


  """
  Patient for lab order
  """
  patient: User


  """
  Get most recent pdf document
  """
  pdf_document: Document


  """
  The requisition of the order. Contact support for more info.
  """
  requisition_document: Document


  """
  Provider for review of lab order
  """
  reviewing_provider: User


  """
  Order ID on the rupa health
  """
  rupa_order_id: String


  """
  Show lab result with PDF document
  """
  show_pdf_messages: Boolean


  """
  Status of the Lab Order
  """
  status: String


  """
  Date of Test
  """
  test_date: ISO8601Date


  """
  Date Lab Order was updated
  """
  updated_at: ISO8601DateTime!


  """
  Link to view the rupa order
  """
  view_rupa_order_url: String
}
```
