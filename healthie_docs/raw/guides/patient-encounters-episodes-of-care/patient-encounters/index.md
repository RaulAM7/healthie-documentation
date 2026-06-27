---
title: Patient Encounters | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/patient-encounters-episodes-of-care/patient-encounters/index
  md: https://docs.gethealthie.com/guides/patient-encounters-episodes-of-care/patient-encounters/index.md
---

# Overview

Patient Encounters in Healthie provide a structured way to track individual interactions between patients and healthcare providers where medical services are rendered. These encounters automatically capture and connect appointments, documentation, billing forms, and invoices in a unified structure, streamlining both clinical workflows and billing processes.

## What is a Patient Encounter?

A Patient Encounter represents a specific interaction between a patient and healthcare provider where medical services are rendered. This could include office visits, procedures, consultations, or any billable service event.

Patient Encounters are automatically generated when an appointment is marked as “Occurred” and serve as a central hub that connects several important healthcare workflow elements.

Historical Patient Encounters have been backfilled for appointments since 2025 - for more details see the [Healthie Help Center](https://help.gethealthie.com/article/1318-encounters-and-episodes-of-care).

### The Patient Encounter Object

```
{
  "appointment": {
    "id": "123"
  },
  "charting_notes": [
    {
      "id": "456"
    }
  ],
  "cms1500": {
    "id": "789"
  },
  "patient": {
    "id": "101"
  },
  "requested_payments": [
    {
      "id": "111"
    }
  ]
}
```

Patient Encounters are `PatientEncounter` objects that connect appointments, documentation, billing forms, and invoices in a single structure.

You can view the full list of available fields [here](/reference/2024-06-01/objects/patientencounter).

### Key Components of Patient Encounters

Patient Encounters serve as a central hub that connects several important healthcare workflow elements:

* **Appointment**: The scheduled visit associated with the encounter
* **Charting Notes**: Clinical documentation recorded during the encounter
* **CMS1500**: Insurance billing forms associated with the encounter
* **Patient**: The patient who received services during the encounter
* **Requested Payments**: Invoices and billing items related to the encounter

## Working with Patient Encounters

### Retrieving a Patient Encounter

```
query patientEncounter($id: ID, $appointment_id: ID, $patient_id: ID) {
  patientEncounter(id: $id, appointment_id: $appointment_id, patient_id: $patient_id) {
    appointment {
      id
      date
      start_time
    }
    charting_notes {
      id
      form_id
    }
    cms1500 {
      id
      claim_number
    }
    patient {
      id
      first_name
      last_name
    }
    requested_payments {
      id
      price
      status
    }
  }
}
```

You can retrieve a Patient Encounter by either querying via the `id` directly or using a combination of the `appointment_id` and `patient_id`:

| Input            | Info                                                    |
| ---------------- | ------------------------------------------------------- |
| `id`             | The unique identifier of the Patient Encounter          |
| `appointment_id` | The ID of the appointment associated with the encounter |
| `patient_id`     | The ID of the patient to retrieve encounters for        |

At least one of these sets of parameters (i.e. `id` or `appointment_id` and `patient_id`) must be provided.

Returns a [`PatientEncounter`](/reference/2024-06-01/objects/patientencounter) object.

### How Patient Encounters are Generated

Patient Encounters are automatically created when you mark an appointment as “Occurred”. Here’s how to update an appointment status:

```
mutation updateAppointment(
  $id: ID!
  $pm_status: String!
) {
  updateAppointment(
    input: {
      id: $id
      pm_status: $pm_status
    }
  ) {
    appointment {
      id
      pm_status
      pm_status_changed_at
    }
    messages {
      field
      message
    }
  }
}
```

To mark an appointment as occurred, set `pm_status` to `"Occurred"`. Valid appointment statuses include:

* `"Occurred"`
* `"No-Show"`
* `"Re-Scheduled"`
* `"Cancelled"`
* `"Late Cancellation"` (if enabled)
* `"Checked-In"` (if enabled)

When an appointment is marked as “Occurred”, Healthie automatically generates a corresponding Patient Encounter that links the appointment to any associated documentation and billing.

For more information about appointments and scheduling, see the [Appointments guide](/guides/scheduling/appointments/).

## Use Cases for Patient Encounters

Patient Encounters help healthcare providers:

* **Centralize Documentation**: Link all aspects of a patient visit in one place
* **Streamline Billing**: Connect services rendered to appropriate billing forms and invoices
* **Track Care History**: Maintain a clear record of patient interactions and associated documentation
* **Support Compliance**: Ensure proper documentation is linked to billable services
* **Facilitate Reporting**: Generate comprehensive reports on patient interactions and associated revenue

## Patient Encounters and Care Coordination

While Patient Encounters track individual visits and services, they can also be organized into broader care coordination structures. For complex cases requiring coordinated care across multiple visits, Patient Encounters can be linked to Episodes of Care.

Episodes of Care provide a way to group related encounters around specific diagnoses or treatment plans, enabling comprehensive care coordination and outcome tracking over extended periods.

**Next Steps**: Learn about [Episodes of Care](/guides/billing/episodes-of-care/) to understand how to coordinate care across multiple patient encounters.
