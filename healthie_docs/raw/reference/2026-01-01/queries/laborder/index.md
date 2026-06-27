---
title: labOrder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/laborder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/laborder/index.md
---

Fetch onboarding flows collection

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`LabOrder`](/reference/2026-01-01/objects/laborder)

## Example

```
query labOrder($id: ID) {
  labOrder(id: $id) {
    abnormal
    appt_confirmation_code
    created_at
    document
    external_identifier
    form_answer_group
    id
    integration
    interpretation
    lab
    lab_company
    lab_options
    lab_results
    latest_result_received_at
    lta_id
    normalized_status
    orderer
    patient
    pdf_document
    requisition_document
    reviewing_provider
    rupa_order_id
    show_pdf_messages
    status
    test_date
    updated_at
    view_rupa_order_url
  }
}
```
