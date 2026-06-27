---
title: Medications | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/medications/index
  md: https://docs.gethealthie.com/guides/medications/index.md
---

# Medications

For more information on the Medication History feature in general, visit our [help center](https://help.gethealthie.com/article/790-client-medication-history).

## The Medication object

```
{
  "id": "232132",
  "active": true,
  "comment": "Only when necessary",
  "directions": "Inhale and hold",
  "dosage": "55 mcg/inh",
  "name": "Nasal spray"
}
```

Medications are `Medication` objects.

You can view the full list of available fields [here](/schema/medicationtype.doc).

## Listing Medications

```
query medications($active: Boolean, $patient_id: ID) {
  medications(active: $active, patient_id: $patient_id) {
    id
    name
    active
    directions
    dosage
    code
    start_date
    end_date
  }
}
```

Listing Medications is done via the `medications` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/medications#arguments).

| Input        | Info                                                                                                            |
| ------------ | --------------------------------------------------------------------------------------------------------------- |
| `active`     | Optional. Fetch only active Medications.                                                                        |
| `patient_id` | Optional. ID of the Patient to fetch Medications for. If omitted, will return Medications for the current User. |

Returns a list of [Medication](/reference/2024-06-01/objects/medication) objects.

## Creating a Medication

```
mutation createMedication(
  $active: Boolean
  $comment: String
  $directions: String
  $dosage: String
  $end_date: String
  $name: String
  $start_date: String
  $user_id: String
) {
  createMedication(
    input: {
      active: $active
      comment: $comment
      directions: $directions
      dosage: $dosage
      end_date: $end_date
      name: $name
      start_date: $start_date
      user_id: $user_id
    }
  ) {
    medication {
      id
      name
      dosage
      comment
    }
    messages {
      field
      message
    }
  }
}
```

To add a Medication to a Patient, use `createMedication` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createmedicationinput).

| Input        | Info                                                                                                                    |
| ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `user_id`    | **Required**. ID of the Patient.                                                                                        |
| `name`       | **Required**. Name of the Medication.                                                                                   |
| `active`     | Optional. Whether the Patient still takes the Medication.                                                               |
| `dosage`     | Optional. Medication dosage.                                                                                            |
| `comment`    | Optional. Additional comment.                                                                                           |
| `start_date` | Optional. Start date of taking the Medication. For example: `July 16, 2023`.                                            |
| `end_date`   | Optional. End date of taking the Medication. For example: `July 16, 2023`. Does not apply if `active` is set to `true`. |

Returns a [`createMedicationPayload`](/reference/2024-06-01/objects/createmedicationpayload) object.

## Updating a Medication

```
mutation updateMedication(
  $id: ID
  $active: Boolean
  $comment: String
  $directions: String
  $dosage: String
  $end_date: String
  $name: String
  $start_date: String
) {
  updateMedication(
    input: {
      id: $id
      active: $active
      comment: $comment
      directions: $directions
      dosage: $dosage
      end_date: $end_date
      name: $name
      start_date: $start_date
    }
  ) {
    medication {
      id
      name
      dosage
      comment
    }
    messages {
      field
      message
    }
  }
}
```

The `updateMedication` has a very similar behavior to [`createMedication`](#creating-a-medication) mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatemedicationinput).

| Input | Info                                              |
| ----- | ------------------------------------------------- |
| `id`  | **Required**. The ID of the Medication to update. |

Returns an [`updateMedicationPayload`](/reference/2024-06-01/objects/updatemedicationpayload) object.

## Deleting a Medication

Medications can be deleted via the `deleteMedication` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/destroymedicationinput).

```
mutation deleteMedication($id: ID) {
  deleteMedication(input: { id: $id }) {
    medication {
      id
    }


    messages {
      field
      message
    }
  }
}
```

| Input | Info                                          |
| ----- | --------------------------------------------- |
| `id`  | **Required**. ID of the Medication to delete. |

Returns a [`destroyMedicationPayload`](/reference/2024-06-01/objects/destroymedicationpayload) object.
