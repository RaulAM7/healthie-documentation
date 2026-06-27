---
title: Lab Orders | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/lab_orders/index
  md: https://docs.gethealthie.com/guides/lab_orders/index.md
---

# Lab Orders

For more information on the Lab Orders feature in general, view our [help articles here](https://help.gethealthie.com/category/543-e-labs).

## The Lab Order object

```
{
  "id": "334455",
  "status": "completed",
  "lab": "Example test",
  "lab_company": "ACME Labs",
  "integration": "lab_testing_api",
  "normalized_status": "completed"
}
```

Lab Orders are `LabOrder` objects in Healthie.

You can view the full list of available fields [here](/reference/2024-06-01/objects/laborder).

## Listing Lab Orders

```
query labOrders(
  $client_filter: String
  $client_id: ID
  $keywords: String
  $lab_filter: String
  $provider_filter: String
  $recent_orders: Boolean
  $offset: Int
  $sort_by: String
  $status_filter: String
) {
  labOrders(
    client_filter: $client_filter
    client_id: $client_id
    keywords: $keywords
    lab_filter: $lab_filter
    provider_filter: $provider_filter
    recent_orders: $recent_orders
    offset: $offset
    sort_by: $sort_by
    status_filter: $status_filter
  ) {
    id
    integration
    lab
    lab_company
    patient {
      id
      full_name
    }
    orderer {
      id
      full_name
    }
    status
    normalized_status
    test_date
    lab_results {
      id
      lab_observation_requests {
        id
        lab_analyte
        lab_observation_results {
          id
          units
          reference_range
          qualitative_result
          quantitative_result
          abnormal_flag
        }
      }
    }
  }
}
```

Listing Lab Orders is done via the `labOrders` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/laborders#arguments).

| Input             | Info                                                                                                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`       | Optional. ID of the Patient to filter by.                                                                                                                                                                                                         |
| `client_filter`   | Optional. A comma-separeted list of Patient IDs to filter Lab Orders by.                                                                                                                                                                          |
| `lab_filter`      | Optional. A comma-separated list of Labs to filter the results by. You can obtain a list of possible values by using the `labFiltersData` query.                                                                                                  |
| `keywords`        | Optional. Can be searched by Patient’s or Orderer’s first and last name, as well as ID, lab or status.                                                                                                                                            |
| `provider_filter` | Optional. A comma-separeted list of Provider IDs to filter Lab Orders by.                                                                                                                                                                         |
| `status_filter`   | Optional. Filters Labs by status.                                                                                                                                                                                                                 |
| `recent_orders`   | Optional. If provided, will return 10 most recent Lab Orders.                                                                                                                                                                                     |
| `sort_by`         | Optional. Valid options are:- `updated_at_asc`
- `updated_at_desc` (default)
- `name_asc`
- `name_desc`
- `lab_asc`
- `lab_desc`
- `appt_asc`
- `appt_desc`
- `client_name_asc`
- `client_name_desc`
- `provider_name_asc`
- `provider_name_desc` |

Returns a list of [`LabOrder`](/reference/2024-06-01/objects/laborder) objects.

## Retrieving a Lab Order

```
query labOrder($id: ID) {
  labOrder(id: $id) {
    id
    integration
    lab
    lab_company
    patient {
      id
      full_name
    }
    orderer {
      id
      full_name
    }
    status
    normalized_status
    test_date
    lab_results {
      id
      lab_observation_requests {
        id
        lab_analyte
        lab_observation_results {
          id
          units
          reference_range
          qualitative_result
          quantitative_result
          abnormal_flag
        }
      }
    }
  }
}
```

Retrieving a specific Lab Order is done via the `labOrder` query.

| Input | Info                          |
| ----- | ----------------------------- |
| `id`  | ID of the Lab Order to query. |

Returns a [`LabOrder`](/reference/2024-06-01/objects/laborder) object.

## Creating a Lab Order

```
mutation createLabOrder($document_id: ID, $lab: String, $lab_company: String, $orderer_id: ID, $patient_id: ID) {
  createLabOrder(
    input: {
      document_id: $document_id
      lab: $lab
      lab_company: $lab_company
      orderer_id: $orderer_id
      patient_id: $patient_id
    }
  ) {
    labOrder {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createlaborderinput).

| Input         | Info                                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `document_id` | **Required**. The ID of the document containing the lab results. Needs to be pre-created and have a rel\_user\_id matching the patient ID. |
| `lab`         | **Required**. The Lab panel that was ordered.                                                                                              |
| `lab_company` | **Required**. The Lab Company who processed the Order.                                                                                     |
| `orderer_id`  | **Required**. The ID of the User in Healthie who ordered the Lab.                                                                          |
| `patient_id`  | **Required**. The ID of the Patient.                                                                                                       |

Returns a [`createLabOrderPayload`](/reference/2024-06-01/objects/createlaborderpayload) object.

## Creating a Rupa Lab Order

```
mutation createRupaOrder($document_id: ID, $lab: String, $lab_company: String, $orderer_id: ID, $patient_id: ID) {
  createRupaOrder(
    input: {
      document_id: $document_id
      lab: $lab
      lab_company: $lab_company
      orderer_id: $orderer_id
      patient_id: $patient_id
    }
  ) {
    rupa_order_url


    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createrupaorderinput).

| Input       | Info                                                     |
| ----------- | -------------------------------------------------------- |
| `client_id` | **Required**. ID of the Patient to create the Order for. |

Returns a [`createRupaOrderPayload`](/reference/2024-06-01/objects/createrupaorderpayload) object.

The `rupa_order_url` field returned is the URL to which the user should be redirected (or opened in a modal) in order to proceed on the Rupa side.

## Updating a Lab Order

```
mutation updateLabOrder($id: ID, $appt_confirmation_code: String, $patient_id: ID) {
  updateLabOrder(input: { id: $id, appt_confirmation_code: $appt_confirmation_code, patient_id: $patient_id }) {
    labOrder {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatelaborderinput).

| Input                    | Info                                                 |
| ------------------------ | ---------------------------------------------------- |
| `id`                     | **Required**. The ID of the Lab Order to update.     |
| `appt_confirmation_code` | Optional. Confirmation code for the Lab Appointment. |
| `patient_id`             | **Required**. The ID of the Patient.                 |

Returns an [`updateLabOrderPayload`](/reference/2024-06-01/objects/updatelaborderpayload) object.
