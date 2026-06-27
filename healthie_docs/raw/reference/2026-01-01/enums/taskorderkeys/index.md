---
title: TaskOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/taskorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/taskorderkeys/index.md
---

Task sorting enum

## Used By

[`Query.tasks`](/reference/2026-01-01/queries/tasks)

[`User.my_tasks`](/reference/2026-01-01/objects/user)

## Definition

```
"""
Task sorting enum
"""
enum TaskOrderKeys {
  TASK_ASC
  TASK_DESC
  CREATOR_ASC
  CREATOR_DESC
  ASSIGNEE_ASC
  ASSIGNEE_DESC
  CREATED_ASC
  CREATED_DESC
  PRIORITY_ASC
  PRIORITY_DESC
  DUE_DATE_ASC
  DUE_DATE_DESC


  """
  Order by client first name and last name descending
  """
  CLIENT_NAME_DESC


  """
  Order by client first name and last name ascending
  """
  CLIENT_NAME_ASC


  """
  Order by completion date ascending (earlier completed tasks first)
  """
  COMPLETED_AT_ASC


  """
  Order by completion date descending (recently completed tasks first)
  """
  COMPLETED_AT_DESC
  COMPLETED_AT_DESC_INCOMPLETE_FIRST
  UPDATED_AT_ASC
  UPDATED_AT_DESC
}
```
