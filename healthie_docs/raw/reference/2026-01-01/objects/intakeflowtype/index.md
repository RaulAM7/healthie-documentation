---
title: IntakeFlowType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/intakeflowtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/intakeflowtype/index.md
---

Intake Flow

## Fields

[`all_forms` ](#field-all-forms)· [`[IntakeFlowItem!]` ](/reference/2026-01-01/objects/intakeflowitem)· All forms in the intake flow

[`completed_skipped` ](#field-completed-skipped)· [`[IntakeFlowItem!]` ](/reference/2026-01-01/objects/intakeflowitem)· Completed and skipped forms in the intake flow

[`forms` ](#field-forms)· [`[IntakeFlowItem!]` ](/reference/2026-01-01/objects/intakeflowitem)· Forms in the intake flow

[`intake_flows` ](#field-intake-flows)· [`[IntakeFlowItem!]` ](/reference/2026-01-01/objects/intakeflowitem)· Intake flows

[`not_started_incomplete` ](#field-not-started-incomplete)· [`[IntakeFlowItem!]` ](/reference/2026-01-01/objects/intakeflowitem)· Not started and incomplete forms in the intake flow

[`requested` ](#field-requested)· [`[IntakeFlowItem!]` ](/reference/2026-01-01/objects/intakeflowitem)· Requested forms in the intake flow

## Used By

[`Query.intakeFlow`](/reference/2026-01-01/queries/intakeflow)

## Definition

```
"""
Intake Flow
"""
type IntakeFlowType {
  """
  All forms in the intake flow
  """
  all_forms: [IntakeFlowItem!]


  """
  Completed and skipped forms in the intake flow
  """
  completed_skipped: [IntakeFlowItem!]


  """
  Forms in the intake flow
  """
  forms: [IntakeFlowItem!]


  """
  Intake flows
  """
  intake_flows: [IntakeFlowItem!]


  """
  Not started and incomplete forms in the intake flow
  """
  not_started_incomplete: [IntakeFlowItem!]


  """
  Requested forms in the intake flow
  """
  requested: [IntakeFlowItem!]
}
```
