---
title: Episodes of Care | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/patient-encounters-episodes-of-care/episodes-of-care/index
  md: https://docs.gethealthie.com/guides/patient-encounters-episodes-of-care/episodes-of-care/index.md
---

# Overview

Episodes of Care in Healthie provide a powerful framework for coordinating healthcare services across multiple patient encounters. Unlike individual Patient Encounters that track single interactions, Episodes of Care organize related encounters into a structured patient journey around specific diagnoses or treatment plans, enabling comprehensive care coordination and outcome tracking over extended periods.

## What is an Episode of Care?

An Episode of Care represents a broader period of coordinated healthcare services provided to a patient for a specific diagnosis or health condition. Episodes of Care group related encounters into a structured patient journey, providing a comprehensive view of treatment over time.

**Important Implementation Notes:**

* Episodes of Care are never automatically created in Healthie - they must be manually created through the API
* There is currently no user interface for Episodes of Care in Healthie’s web application, so they can only be managed and viewed via API calls
* Episodes of Care are primarily designed for custom integrations, third-party applications, and backend care coordination systems

### The Episode of Care Object

```
{
  "id": "1",
  "diagnosis": {
    "id": "456",
    "code": "E11.9"
  },
  "start_date": "2024-01-15",
  "end_date": "2024-06-15",
  "patient": {
    "id": "101"
  },
  "provider": {
    "id": "202"
  },
  "patient_encounters": [
    {
      "appointment": {
        "id": "123"
      }
    }
  ]
}
```

Episodes of Care are `EpisodeOfCare` objects that organize multiple patient encounters around a specific diagnosis or treatment plan.

You can view the full list of available fields [here](/reference/2024-06-01/objects/episodeofcare).

### Key Components of Episodes of Care

Episodes of Care provide structure for coordinated care by connecting:

* **Diagnosis**: The specific medical condition being treated during the episode
* **Start/End Dates**: The timeframe during which coordinated care was provided
* **Patient**: The patient receiving coordinated care
* **Provider**: The primary provider responsible for coordinating care
* **Patient Encounters**: All individual interactions that occurred during the episode

## Working with Episodes of Care

### Listing Episodes of Care

```
query episodesOfCare(
  $first: Int
  $after: String
  $patient_id: ID
  $provider_id: ID
  $ids: [ID!]
) {
  episodesOfCare(
    first: $first
    after: $after
    patient_id: $patient_id
    provider_id: $provider_id
    ids: $ids
  ) {
    nodes {
      id
      diagnosis {
        id
        code
        description
      }
      start_date
      end_date
      patient {
        id
        first_name
        last_name
      }
      provider {
        id
        first_name
        last_name
      }
    }
    page_info {
      has_next_page
      end_cursor
    }
  }
}
```

| Input         | Info                                                    |
| ------------- | ------------------------------------------------------- |
| `first`       | Optional. Number of episodes to return (for pagination) |
| `after`       | Optional. Cursor for pagination                         |
| `patient_id`  | Optional. Filter episodes for a specific patient        |
| `provider_id` | Optional. Filter episodes for a specific provider       |
| `ids`         | Optional. Retrieve specific episodes by their IDs       |

Returns an [`EpisodeOfCareConnection`](/reference/2024-06-01/objects/episodeofcareconnection) object.

### Creating an Episode of Care

```
mutation createEpisodeOfCare(
  $patient_id: ID!
  $provider_id: ID!
  $diagnosis_id: ID!
  $start_date: ISO8601Date!
  $end_date: ISO8601Date
) {
  createEpisodeOfCare(
    input: {
      patient_id: $patient_id
      provider_id: $provider_id
      diagnosis_id: $diagnosis_id
      start_date: $start_date
      end_date: $end_date
    }
  ) {
    episode_of_care {
      id
      start_date
      end_date
    }
    messages {
      field
      message
    }
  }
}
```

| Input          | Info                                                               |
| -------------- | ------------------------------------------------------------------ |
| `patient_id`   | **Required**. ID of the patient for this episode                   |
| `provider_id`  | **Required**. ID of the provider coordinating care                 |
| `diagnosis_id` | **Required**. ID of the diagnosis associated with this episode     |
| `start_date`   | **Required**. Start date for the episode (must be present or past) |
| `end_date`     | Optional. End date when the episode concluded                      |

Returns a [`createEpisodeOfCarePayload`](/reference/2024-06-01/objects/createepisodeofcarepayload) object.

### Updating an Episode of Care

```
mutation updateEpisodeOfCare(
  $id: ID!
  $patient_id: ID!
  $provider_id: ID!
  $diagnosis_id: ID!
  $start_date: ISO8601Date!
  $end_date: ISO8601Date
) {
  updateEpisodeOfCare(
    input: {
      id: $id
      patient_id: $patient_id
      provider_id: $provider_id
      diagnosis_id: $diagnosis_id
      start_date: $start_date
      end_date: $end_date
    }
  ) {
    episode_of_care {
      id
      start_date
      end_date
    }
    messages {
      field
      message
    }
  }
}
```

| Input          | Info                                                           |
| -------------- | -------------------------------------------------------------- |
| `id`           | **Required**. ID of the episode to update                      |
| `patient_id`   | **Required**. ID of the patient for this episode               |
| `provider_id`  | **Required**. ID of the provider coordinating care             |
| `diagnosis_id` | **Required**. ID of the diagnosis associated with this episode |
| `start_date`   | **Required**. Start date for the episode                       |
| `end_date`     | Optional. End date when the episode concluded                  |

Returns an [`updateEpisodeOfCarePayload`](/reference/2024-06-01/objects/updateepisodeofcarepayload) object.

### Deleting an Episode of Care

```
mutation deleteEpisodeOfCare($id: ID!) {
  deleteEpisodeOfCare(input: { id: $id }) {
    episode_of_care {
      id
    }
    messages {
      field
      message
    }
  }
}
```

| Input | Info                                      |
| ----- | ----------------------------------------- |
| `id`  | **Required**. ID of the episode to delete |

Returns a [`deleteEpisodeOfCarePayload`](/reference/2024-06-01/objects/deleteepisodeofcarepayload) object.

## Linking Patient Encounters to Episodes of Care

The true power of Episodes of Care comes from linking Patient Encounters to create a comprehensive view of coordinated care delivery. This enables you to group individual appointments and services under broader treatment episodes.

### Linking Encounters to an Episode

```
mutation linkEncounterToEpisodeOfCare(
  $encounter_ids: [ID]!
  $episode_of_care_id: ID!
) {
  linkEncounterToEpisodeOfCare(
    input: {
      encounter_ids: $encounter_ids
      episode_of_care_id: $episode_of_care_id
    }
  ) {
    results {
      patient_encounter_id
      episode_of_care_id
      success
      failed_reason
    }
    messages {
      field
      message
    }
  }
}
```

| Input                | Info                                                          |
| -------------------- | ------------------------------------------------------------- |
| `encounter_ids`      | **Required**. Array of Patient Encounter IDs to link          |
| `episode_of_care_id` | **Required**. ID of the Episode of Care to link encounters to |

Returns a [`linkEncounterToEpisodeOfCarePayload`](/reference/2024-06-01/objects/linkencountertoepisodeofcarepayload) object.

### Unlinking Encounters from an Episode

```
mutation unlinkEncounterToEpisodeOfCare(
  $encounter_ids: [ID]!
  $episode_of_care_id: ID!
) {
  unlinkEncounterToEpisodeOfCare(
    input: {
      encounter_ids: $encounter_ids
      episode_of_care_id: $episode_of_care_id
    }
  ) {
    results {
      patient_encounter_id
      episode_of_care_id
      success
      failed_reason
    }
    messages {
      field
      message
    }
  }
}
```

| Input                | Info                                                              |
| -------------------- | ----------------------------------------------------------------- |
| `encounter_ids`      | **Required**. Array of Patient Encounter IDs to unlink            |
| `episode_of_care_id` | **Required**. ID of the Episode of Care to unlink encounters from |

Returns an [`unlinkEncounterToEpisodeOfCarePayload`](/reference/2024-06-01/objects/unlinkencountertoepisodeofcarepayload) object.

## Use Cases for Episodes of Care

Episodes of Care enable healthcare providers to:

* **Coordinate Complex Care**: Organize multiple encounters around specific diagnoses or treatment plans
* **Track Treatment Outcomes and Longitudinal Patient Progress**: Monitor treatment progress and outcomes across multiple visits for chronic conditions
* **Optimize Resource Allocation**: Understand the full scope of care provided for specific health conditions
* **Support Value-Based Care**: Group related services for alternative payment models
* **Enhance Care Transitions**: Ensure continuity when patients move between different providers or care settings
* **Facilitate Population Health**: Analyze patterns of care delivery across similar patient populations

**Since Episodes of Care currently have no web UI in Healthie**, they are primarily useful for:

* Custom reporting and analytics through API integrations
* Third-party applications that need to track coordinated care periods
* Backend systems that manage care coordination workflows

## Best Practices

### When to Use Episodes of Care

**Use Episodes of Care when:**

* Coordinating care for chronic conditions requiring multiple visits
* Managing treatment plans that span weeks or months
* Implementing value-based care contracts
* Tracking outcomes for specific diagnoses across time
* Coordinating care among multiple providers

### Workflow Integration

1. **Create Episode of Care** first when beginning coordinated treatment for a specific diagnosis
2. **Generate Patient Encounters** through normal appointment workflows (marking appointments as “Occurred”)
3. **Link Encounters to Episodes** to maintain the relationship between individual services and overall care coordination
4. **Update Episode end dates** when coordinated care concludes
5. **Use linked data** for comprehensive reporting and outcome tracking

## Relationship to Patient Encounters

Episodes of Care work in conjunction with [Patient Encounters](/guides/billing/patient-encounters/), which track individual patient visits and services. While Patient Encounters are automatically generated when appointments are marked as “Occurred”, Episodes of Care must be manually created and managed to organize these encounters into meaningful care coordination periods.

By leveraging both Patient Encounters and Episodes of Care, healthcare providers can maintain detailed records of individual patient interactions while also organizing care delivery around specific health conditions and treatment goals.
