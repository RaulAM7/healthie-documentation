---
title: Care Plans | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/care-plans/index
  md: https://docs.gethealthie.com/guides/care-plans/index.md
---

# Care Plans

For more information on the Care Plans feature in general, view our [help articles here](https://help.gethealthie.com/article/371-care-plans).

## The Care Plan object

```
{
  "id": "1",
  "name": "Care Plan 1",
  "description": "Example description",
  "recommendations": [
    {
      "id": "1",
      "recommendation_body": "<p>Drink 8 glasses of water a day</p>",
      "recommendation_type": "Nutrition",
      "sanitized_body": "Drink 8 glasses of water a day"
    }
  ],
  "is_active": true,
  "is_hidden": false
}
```

Care Plans are `CarePlan` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/careplan).

## Listing Care Plans

```
query carePlans(
  $patient_id: ID
  $offset: Int
  $sort_by: String
  $templates_only: Boolean
  $template_search_keywords: String
) {
  carePlans(
    patient_id: $patient_id
    offset: $offset
    sort_by: $sort_by
    templates_only: $templates_only
    template_search_keywords: $template_search_keywords
  ) {
    id
    name
    patient {
      id
    }
  }
}
```

Listing Care Plans is done via the `carePlans` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/careplans#arguments).

| Input                      | Info                                                                                                                                                                                                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort_by`                  | Optional. Valid options are:- `oldest`
- `newest` (default)
- `name_asc`
- `name_desc`
- `status_asc`
- `status_desc`
- `client_name_desc`
- `client_name_asc`
- `deactivated_desc, activated_desc`
- `deactivated_asc, activated_asc` |
| `patient_id`               | Optional. ID of the Client that is associated with the Care Plan.                                                                                                                                                                      |
| `template_search_keywords` | Optional. Can be searched by name.                                                                                                                                                                                                     |

Returns a list of [Care Plan](/reference/2024-06-01/objects/careplan) objects.

## Retrieving a Care Plan

```
query carePlan($id: ID) {
  carePlan(id: $id) {
    id
    name
    patient {
      id
    }
  }
}
```

Retrieving a specific Care Plan is done via the `carePlan` query.

| Input | Info                          |
| ----- | ----------------------------- |
| `id`  | ID of the Care Plan to query. |

Returns a [Care Plan](/reference/2024-06-01/objects/careplan) object.

## Creating a Care Plan

```
mutation createCarePlan(
  $name: String,
  $patient_id: ID,
  $is_hidden: Boolean
) {
  createCarePlan(input: {
    $name: String,
    $patient_id: ID,
    $is_hidden: Boolean,
  }) {
    carePlan {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createcareplaninput).

| Input        | Info                                                          |
| ------------ | ------------------------------------------------------------- |
| `name`       | **Required**. Name of the care plan. Not visible to Patients. |
| `patient_id` | Optional. ID of the Patient to create a Care Plan for.        |
| `is_hidden`  | Optional. Whether the Care Plan should be hidden.             |

Returns a [`createCarePlanPayload`](/reference/2024-06-01/objects/createcareplanpayload) object.

## Updating a Care Plan

```
mutation updateCarePlan(
  $id: ID
  $name: String
  $description: String
  $new_patient_id: ID
  $is_template: Boolean
  $is_hidden: Boolean
) {
  updateCarePlan(
    input: {
      id: $id
      name: $name
      description: $description
      new_patient_id: $new_patient_id
      is_template: $is_template
      is_hidden: $is_hidden
    }
  ) {
    carePlan {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatecareplaninput).

| Input            | Info                                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------------- |
| `id`             | **Required**. The ID of the Care Plan to update.                                                         |
| `description`    | Optional. A description visible to Patients.                                                             |
| `new_patient_id` | Optional. Provide a new Patient ID to move the Care Plan to another Patient.                             |
| `is_template`    | Optional. Set to `true` in order to created a Care Plan template. Should be used without a `patient_id`. |

Returns an [`updateCarePlanPayload`](/reference/2024-06-01/objects/updatecareplanpayload) object.

## Deleting a Care Plan

Care Plans can be deleted by authorized providers and staff members via the `deleteCarePlan` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletecareplaninput).

```
mutation deleteCarePlan($id: ID) {
  deleteCarePlan(input: { id: $id }) {
    carePlan {
      id
    }


    messages {
      field
      message
    }
  }
}
```

| Input | Info                                         |
| ----- | -------------------------------------------- |
| `id`  | **Required**. ID of the Care Plan to delete. |

Returns a [`deleteCarePlanPayload`](/reference/2024-06-01/objects/deletecareplanpayload) object.
