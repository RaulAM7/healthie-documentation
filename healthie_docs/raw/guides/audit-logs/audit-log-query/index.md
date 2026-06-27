---
title: Querying the Audit Log | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/audit-logs/audit-log-query/index
  md: https://docs.gethealthie.com/guides/audit-logs/audit-log-query/index.md
---

This example demonstrates how to fetch audit log entries from the API using the `auditLog` query. You can filter by user, resource, event type, and date range, and paginate through results.

Steps necessary to implement this automation:

* Use the `auditLog` GraphQL query
* (Optionally) Filter by user, resource, event type, or date range
* Paginate results using `first`, `endCursor`, and `hasNextPage`

### Implementation

```
query auditLogExample {
  auditLog(
    acting_user_id: "12345",         # (Optional) Only show actions performed by this user ID
    resource_name: USER,             # (Optional) ex. FormAnswerGroup, BillingItem, Appointment
    resource_id: "543",            # (Optional) Filter by a specific resource ID
    event_type: CREATE,              # (Optional) Filter by event type: CREATE, UPDATE, or DESTROY
    occurred_after: "2024-01-01T00:00:00Z",  # (Optional) Only events after this date (ISO8601 format)
    occurred_before: "2024-06-01T00:00:00Z" # (Optional) Only events before this date (ISO8601 format)
  ) {
        occurred_at        # Timestamp of when the event occurred
        resource_name      # Name/type of the resource affected
        resource_id        # ID of the resource affected
        cursor
  }
}
```

> **Variables:** (replace with your own filter values as needed)

### Argument Explanations

| Argument            | Type       | Description                                                         |
| ------------------- | ---------- | ------------------------------------------------------------------- |
| `acting_user_id`    | `String`   | Only return audit events performed by this user                     |
| `resource_name`     | `Enum`     | Filter events by the type of resource affected (e.g., USER, POLICY) |
| `resource_id`       | `String`   | Filter events for a specific resource instance                      |
| `event_type`        | `Enum`     | Filter by the type of event: CREATE, UPDATE, DESTROY                |
| `occurred_after`    | `String`   | Only events after this date, inclusive (ISO8601 format)             |
| `occurred_before`   | `String`   | Only events before this date, inclusive (ISO8601 format)            |
