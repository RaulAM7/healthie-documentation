---
title: GoalHistoryActionTypeEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/goalhistoryactiontypeenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/goalhistoryactiontypeenum/index.md
---

The type of action that created this goal history record

## Used By

[`GoalHistory.action`](/reference/2026-01-01/objects/goalhistory)

[`createGoalHistoryInput.action`](/reference/2026-01-01/input-objects/creategoalhistoryinput)

## Definition

```
"""
The type of action that created this goal history record
"""
enum GoalHistoryActionTypeEnum {
  """
  Goal history was created
  """
  CREATED


  """
  Goal was marked as completed
  """
  COMPLETED


  """
  Goal was marked as incomplete
  """
  MARKED_INCOMPLETE


  """
  Goal was activated
  """
  ACTIVE


  """
  Goal was deactivated
  """
  INACTIVE


  """
  Goal was updated
  """
  UPDATED
}
```
