---
title: Insurance Payments Tracking | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/billing/insurance-payments/index
  md: https://docs.gethealthie.com/guides/billing/insurance-payments/index.md
---

The Insurance Payments API provides centralized tracking of insurance payments, aggregating Electronic Remittance Advice (ERA) data from Claim.MD alongside manual payment entries.

Insurance payments come from two sources:

| Source        | Description                     | Operations                      |
| ------------- | ------------------------------- | ------------------------------- |
| **Automatic** | Created from ERA data ingestion | Read-only (status updates only) |
| **Manual**    | User-created entries            | Full CRUD                       |

## Authorization

Access to insurance payments requires the following permissions on the provider’s organization membership:

| Permission         | Required | Description                                           |
| ------------------ | -------- | ----------------------------------------------------- |
| `can_see_billing`  | Yes      | Allows viewing billing information                    |
| `sees_all_billing` | Yes      | Allows viewing billing across the entire organization |

Requests from providers without these permissions will return an `Unauthorized` error.

## The InsurancePayment Object

```
type InsurancePayment {
  id: ID!
  organization_id: ID!
  paid_date: ISO8601Date!
  paid_amount: Float!
  deposit_status: InsurancePaymentsDepositStatusEnum!
  source: String!
  payer_name: String!
  npi: String
  ach_check_number: String
  era_id: ID
  created_by_id: ID
  created_at: ISO8601DateTime!
  updated_at: ISO8601DateTime!
}
```

| Field              | Description                                             |
| ------------------ | ------------------------------------------------------- |
| `paid_amount`      | Payment amount as a decimal (e.g., `150.00`)            |
| `paid_date`        | Date the payment was made                               |
| `payer_name`       | Name of the insurance payer                             |
| `npi`              | National Provider Identifier (exactly 10 digits)        |
| `ach_check_number` | Check number or ACH identifier                          |
| `deposit_status`   | Status of the deposit, e.g. `PENDING` or `DEPOSITED`    |
| `source`           | `automatic` (ERA) or `manual`                           |
| `era_id`           | Associated ERA record ID (automatic payments only)      |
| `created_by_id`    | Provider who created the payment (manual payments only) |

## Querying Insurance Payments

```
query insurancePayments(
  $start_paid_date: ISO8601Date
  $end_paid_date: ISO8601Date
  $order_by: InsurancePaymentsOrderKeys
  $keywords: String
  $deposit_status: InsurancePaymentsDepositStatusEnum
  $payer: String
  $first: Int
  $after: String
) {
  insurancePayments(
    start_paid_date: $start_paid_date
    end_paid_date: $end_paid_date
    order_by: $order_by
    keywords: $keywords
    deposit_status: $deposit_status
    payer: $payer
    first: $first
    after: $after
  ) {
    page_info {
      has_next_page
      end_cursor
    }
    total_count
    nodes {
      id
      paid_date
      paid_amount
      payer_name
      npi
      ach_check_number
      deposit_status
      source
      era_id
    }
  }
}
```

| Argument          | Type                                 | Description                                       |
| ----------------- | ------------------------------------ | ------------------------------------------------- |
| `start_paid_date` | `ISO8601Date`                        | Filter payments on or after this date             |
| `end_paid_date`   | `ISO8601Date`                        | Filter payments on or before this date            |
| `order_by`        | `InsurancePaymentsOrderKeys`         | Sort order (default: `PAID_DATE_DESC`)            |
| `keywords`        | `String`                             | Search NPI, ACH check number, or payer name       |
| `deposit_status`  | `InsurancePaymentsDepositStatusEnum` | Filter by `PENDING` or `DEPOSITED`                |
| `payer`           | `String`                             | Filter by exact payer name                        |
| `first`           | `Int`                                | Number of records to return (forward pagination)  |
| `after`           | `String`                             | Cursor for fetching the next page of results      |
| `last`            | `Int`                                | Number of records to return (backward pagination) |
| `before`          | `String`                             | Cursor for fetching the previous page of results  |

### Sort Options

The `order_by` argument accepts:

| Option                  | Description                          |
| ----------------------- | ------------------------------------ |
| `PAID_DATE_DESC`        | Payment date, newest first (default) |
| `PAID_DATE_ASC`         | Payment date, oldest first           |
| `PAID_AMOUNT_DESC`      | Amount, highest first                |
| `PAID_AMOUNT_ASC`       | Amount, lowest first                 |
| `PAYER_NAME_DESC`       | Payer name, Z-A                      |
| `PAYER_NAME_ASC`        | Payer name, A-Z                      |
| `NPI_DESC`              | NPI, descending                      |
| `NPI_ASC`               | NPI, ascending                       |
| `ACH_CHECK_NUMBER_DESC` | Check/ACH number, descending         |
| `ACH_CHECK_NUMBER_ASC`  | Check/ACH number, ascending          |
| `SOURCE_DESC`           | Source, descending                   |
| `SOURCE_ASC`            | Source, ascending                    |
| `CREATED_AT_DESC`       | Created date, newest first           |
| `CREATED_AT_ASC`        | Created date, oldest first           |
| `UPDATED_AT_DESC`       | Updated date, newest first           |
| `UPDATED_AT_ASC`        | Updated date, oldest first           |

### Pagination

The `insurancePayments` query uses cursor-based pagination and returns an `InsurancePaymentConnection` type with the following structure:

| Field                     | Type                 | Description                                  |
| ------------------------- | -------------------- | -------------------------------------------- |
| `nodes`                   | `[InsurancePayment]` | Array of insurance payment records           |
| `page_info`               | `PageInfo`           | Pagination metadata                          |
| `page_info.has_next_page` | `Boolean`            | Whether more results are available           |
| `page_info.end_cursor`    | `String`             | Cursor for the next page                     |
| `total_count`             | `Int`                | Total number of records matching the filters |

#### Fetching the First Page

To fetch the first 20 payments:

```
query {
  insurancePayments(
    first: 20
    order_by: PAID_DATE_DESC
  ) {
    page_info {
      has_next_page
      end_cursor
    }
    total_count
    nodes {
      id
      paid_date
      paid_amount
      payer_name
      deposit_status
    }
  }
}
```

#### Fetching Subsequent Pages

Use the `end_cursor` from the previous response to fetch the next page:

```
query {
  insurancePayments(
    first: 20
    after: "eyJpZCI6MTIzNDV9"
    order_by: PAID_DATE_DESC
  ) {
    page_info {
      has_next_page
      end_cursor
    }
    nodes {
      id
      paid_date
      paid_amount
    }
  }
}
```

Continue fetching pages while `has_next_page` is `true`.

For more information, refer to the [Connection-based Cursor Pagination](/guides/api-concepts/pagination/#connection-based-cursor-pagination)

## Creating a Manual Payment

```
mutation createInsurancePayment(
  $paid_date: ISO8601Date!
  $npi: String!
  $paid_amount: Float!
  $deposit_status: InsurancePaymentsDepositStatusEnum!
  $payer_name: String!
  $ach_check_number: String
) {
  createInsurancePayment(
    input: {
      paid_date: $paid_date
      npi: $npi
      paid_amount: $paid_amount
      deposit_status: $deposit_status
      payer_name: $payer_name
      ach_check_number: $ach_check_number
    }
  ) {
    insurance_payment {
      id
      paid_amount
      payer_name
      source
    }
    messages {
      field
      message
    }
  }
}
```

| Input              | Required | Description                                      |
| ------------------ | -------- | ------------------------------------------------ |
| `paid_date`        | Yes      | Date of the payment (`YYYY-MM-DD`)               |
| `npi`              | Yes      | National Provider Identifier (exactly 10 digits) |
| `paid_amount`      | Yes      | Payment amount (must be > 0)                     |
| `deposit_status`   | Yes      | `PENDING` or `DEPOSITED`                         |
| `payer_name`       | Yes      | Insurance payer name                             |
| `ach_check_number` | No       | Check or ACH identifier                          |

### Example

```
{
  "paid_date": "2024-01-20",
  "npi": "1234567890",
  "paid_amount": 150.00,
  "deposit_status": "PENDING",
  "payer_name": "Blue Cross Blue Shield",
  "ach_check_number": "CHK-789012"
}
```

## Updating a Manual Payment

Use `updateManualInsurancePayment` to modify manual payments. This mutation cannot modify automatic (ERA) payments.

```
mutation updateManualInsurancePayment(
  $payment_id: ID!
  $paid_date: ISO8601Date
  $npi: String
  $ach_check_number: String
  $paid_amount: Float
  $deposit_status: InsurancePaymentsDepositStatusEnum
) {
  updateManualInsurancePayment(
    input: {
      payment_id: $payment_id
      paid_date: $paid_date
      npi: $npi
      ach_check_number: $ach_check_number
      paid_amount: $paid_amount
      deposit_status: $deposit_status
    }
  ) {
    insurance_payment {
      id
      paid_amount
      deposit_status
      updated_at
    }
    messages {
      field
      message
    }
  }
}
```

## Updating Deposit Status

Use `updateInsurancePaymentDepositStatus` to change the deposit status of any payment, including automatic payments.

```
mutation updateInsurancePaymentDepositStatus(
  $payment_id: ID!
  $deposit_status: InsurancePaymentsDepositStatusEnum!
) {
  updateInsurancePaymentDepositStatus(
    input: {
      payment_id: $payment_id
      deposit_status: $deposit_status
    }
  ) {
    insurance_payment {
      id
      deposit_status
      updated_at
    }
    messages {
      field
      message
    }
  }
}
```

## Deleting a Manual Payment

Use `deleteManualInsurancePayment` to soft-delete a manual payment. Automatic payments cannot be deleted.

```
mutation deleteManualInsurancePayment($payment_id: ID!) {
  deleteManualInsurancePayment(input: { payment_id: $payment_id }) {
    insurance_payment {
      id
    }
    messages {
      field
      message
    }
  }
}
```

## Common Workflows

### Reconciling ERA Payments

Query pending payments within a date range to reconcile with bank deposits:

```
query {
  insurancePayments(
    start_paid_date: "2024-01-01"
    end_paid_date: "2024-01-31"
    deposit_status: PENDING
    first: 50
  ) {
    total_count
    nodes {
      id
      paid_amount
      paid_date
      payer_name
      ach_check_number
      era_id
    }
  }
}
```

### Marking Payments as Deposited

After reconciling with bank deposits, update the status:

```
mutation {
  updateInsurancePaymentDepositStatus(
    input: {
      payment_id: "123"
      deposit_status: DEPOSITED
    }
  ) {
    insurance_payment {
      id
      deposit_status
    }
  }
}
```

### Searching Payment History

```
query {
  insurancePayments(
    keywords: "Blue Cross"
    order_by: PAID_DATE_DESC
    first: 20
  ) {
    total_count
    nodes {
      id
      paid_amount
      paid_date
      payer_name
      npi
      ach_check_number
      source
      deposit_status
    }
  }
}
```

## Error Handling

### Source Validation

Attempting to update or delete an automatic payment (or a non-existent payment) returns:

```
{
  "data": {
    "updateManualInsurancePayment": {
      "insurance_payment": null,
      "messages": [
        {
          "field": null,
          "message": "Payment not found"
        }
      ]
    }
  }
}
```

### Duplicate ERA Prevention

The system prevents duplicate ERA payments using the unique `era_id` constraint.

## Related

* [Insurance](/guides/insurance/) - Insurance policy management
* [Insurance Auto-Billing](/guides/billing/insurance-auto-billing/) - Automatic patient billing
* [Billing Items](/guides/billing/billing-items/) - Billing item management
