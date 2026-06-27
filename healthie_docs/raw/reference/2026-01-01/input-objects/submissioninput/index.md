---
title: SubmissionInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/submissioninput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/submissioninput/index.md
---

If included, Healthie will attempt to submit an order. This must be enabled for your organization.

## Fields

[`tests` ](#field-tests)· [`[TestInput]` ](/reference/2026-01-01/input-objects/testinput)· DEPRECATED. Requested lab test options

deprecated

Use lab\_option\_ids to submit tests

[`lab_option_ids` ](#field-lab-option-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· List of Lab Option IDs for tests being ordered

[`activate_by` ](#field-activate-by)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· An optional future date to process the order

[`physician_id` ](#field-physician-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Healthie ID of the physician who will review this order. If left empty default provider network will be used.

[`billing_type` ](#field-billing-type)· [`LabOrderBilling` ](/reference/2026-01-01/enums/laborderbilling)· The billing type for this order. If missing, the provider will be billed.

[`icd_code_ids` ](#field-icd-code-ids)· [`[ID]` ](/reference/2026-01-01/scalars/id)· List of ICD-10 code ids for this order

[`form_answer_group_id` ](#field-form-answer-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Chart note ID associated with this lab order, group charting notes are not accepted, chart note should not be signed or locked Make sure the \`OrganizationType.can\_link\_labs\_to\_chart\_notes\` setting is enabled for your organization before using this arg.

## Used By

[`createLabOrderInput.submission`](/reference/2026-01-01/input-objects/createlaborderinput)

## Definition

```
"""
If included, Healthie will attempt to submit an order. This must be enabled for your organization.
"""
input SubmissionInput {
  """
  DEPRECATED. Requested lab test options
  """
  tests: [TestInput] @deprecated(reason: "Use lab_option_ids to submit tests")


  """
  List of Lab Option IDs for tests being ordered
  """
  lab_option_ids: [ID]


  """
  An optional future date to process the order
  """
  activate_by: ISO8601DateTime


  """
  Healthie ID of the physician who will review this order. If left empty default provider network will be used.
  """
  physician_id: ID


  """
  The billing type for this order. If missing, the provider will be billed.
  """
  billing_type: LabOrderBilling = PROVIDER


  """
  List of ICD-10 code ids for this order
  """
  icd_code_ids: [ID]


  """
  Chart note ID associated with this lab order, group charting notes are not accepted, chart note should not be signed or locked Make sure the `OrganizationType.can_link_labs_to_chart_notes` setting is enabled for your organization before using this arg.
  """
  form_answer_group_id: ID
}
```
