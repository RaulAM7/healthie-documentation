---
title: Documents | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/documents/index
  md: https://docs.gethealthie.com/guides/documents/index.md
---

# Documents

## The Document Object

```
{
  "id": "1",
  "display_name": "dummy.pdf",
  "file_content_type": "application/pdf",
  "owner": {
    "id": "1"
  }
}
```

Documents are `Document` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/document).

## Listing Documents

```
query documents(
  $offset: Int
  $keywords: String
  $folder_id: String
  $file_types: [String]
  $file_type: String
  $sort_by: String
  $private_user_id: String
  $viewable_user_id: String
  $consolidated_user_id: String
  $filter: String
  $should_paginate: Boolean
  $for_template_use: Boolean
  $provider_id: ID
) {
  documents(
    offset: $offset
    keywords: $keywords
    folder_id: $folder_id
    file_types: $file_types
    file_type: $file_type
    sort_by: $sort_by
    private_user_id: $private_user_id
    viewable_user_id: $viewable_user_id
    consolidated_user_id: $consolidated_user_id
    filter: $filter
    should_paginate: $should_paginate
    for_template_use: $for_template_use
    provider_id: $provider_id
  ) {
    id
    display_name
    file_content_type
    opens {
      id
    }
    owner {
      id
      email
    }
    users {
      id
      email
    }
  }
}
```

Listing Documents is done via the `documents` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/documents#arguments).

| Input       | Info                                                                                                                                                       |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort_by`   | Optional. Valid options are:- `oldestfirst`
- `newestfirst`
- `namedesc`
- `nameaesc` (default                                                             |
| `keywords`  | Optional. Keywords to search by. Documents can be searched by the name, description or file name.                                                          |
| `file_type` | Optional. Can be either: Valid options are:- `all`
- `other` - this will return all files that are not: pdf, image, text, video, spreadsheet, presentation |
| `folder_id` | Optional. ID of the Folder containing files to retrieve.                                                                                                   |

Returns a list of [`Document`](/reference/2024-06-01/objects/document) objects.

## Retrieving a Document

```
query document($id: ID, $course_id: ID, $custom_module_id: ID, $care_plan_id: ID) {
  document(id: $id, course_id: $course_id, custom_module_id: $custom_module_id, care_plan_id: $care_plan_id) {
    id
    display_name
    file_content_type
    opens {
      id
    }
    owner {
      id
      email
    }
    users {
      id
      email
    }
  }
}
```

Retrieving a specific Document is done via the `document` query.

| Input              | Info                                                                         |
| ------------------ | ---------------------------------------------------------------------------- |
| `id`               | ID of the Document to query.                                                 |
| `course_id`        | Optional. Find Document by the Program it’s associated with.                 |
| `custom_module_id` | Optional. Find Document by the specific Program Module it’s associated with. |
| `care_plan_id`     | Optional. Find Document by the Care Plan it’s associated with.               |

Returns a [`Document`](/reference/2024-06-01/objects/document) object.

## Creating a Document

```
mutation createDocument($file: Upload, $display_name: String, $folder_id: String) {
  createDocument(input: { file: $file, display_name: $display_name, folder_id: $folder_id }) {
    document {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createdocumentinput).

| Input          | Info                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `file`         | **Required**. This is the uploaded file as a `multipart/form-data`. Please refer to the [File Uploads](/guides/api-concepts/file-uploads/) section for more information. |
| `display_name` | Optional. If not provided, will use the original file name as a display name.                                                                                            |
| `folder_id`    | Optional. ID of the Folder to place the new Document in.                                                                                                                 |

Returns a [`createDocumentPayload`](/reference/2024-06-01/objects/createdocumentpayload) object.

## Updating a Document

```
mutation updateDocument($id: ID, $display_name: String, $folder_id: String) {
  updateDocument(input: { id: $id, display_name: $display_name, folder_id: $folder_id }) {
    document {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatedocumentinput).

Note

Please note that it’s not allowed to change the file contents. If you want to re-upload your Document, please [create a new one](/guides/documents/#creating-a-document).

The `updateDocument` mutation shares many common inputs with [`createDocument`](/guides/documents/#creating-a-document) and those inputs (e.g `display_name` or `folder_id` work the same in both places).

| Input | Info                                            |
| ----- | ----------------------------------------------- |
| `id`  | **Required**. The ID of the Document to update. |

Returns an [`updateDocumentPayload`](/reference/2024-06-01/objects/updatedocumentpayload) object.

## Deleting a Document

Documents can be deleted by authorized providers and staff members via the `deleteDocument` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletedocumentinput).

```
mutation deleteDocument($id: ID) {
  deleteDocument(input: { id: $id }) {
    document {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteDocument` mutation is called from an authenticated provider/staff account.

| Input | Info                                        |
| ----- | ------------------------------------------- |
| `id`  | **Required**. ID of the Document to delete. |

Returns a [`deleteDocumentPayload`](/reference/2024-06-01/objects/deletedocumentpayload) object.
