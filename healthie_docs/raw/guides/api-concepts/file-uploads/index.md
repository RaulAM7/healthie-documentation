---
title: File Uploads | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/file-uploads/index
  md: https://docs.gethealthie.com/guides/api-concepts/file-uploads/index.md
---

Some Healthie API mutations provide support for uploading files. While it’s not natively supported by the Apollo Client, it can be achieved by using third-party libraries like [apollo-upload-client](https://www.npmjs.com/package/apollo-upload-client).

Alternatively, here’s a curl command to upload the image as a base64 string:

Terminal window

```
curl --request POST \
  --url https://staging-api.gethealthie.com/graphql \
  --header 'Authorization: Basic API_KEY' \
  --header 'AuthorizationSource: API' \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "mutation createDocument($file: String) {
      createDocument(input: {
        rel_user_id: "10",
        share_with_rel: true,
        file_string: $file,
        display_name: "example.pdf"
      }) {
        document {
          id
        }
      }
    }",
    "variables": {
      "file": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
    },
    "operationName": "createDocument"
  }'
```

Healthie API uses the [`Upload`](/reference/2024-06-01/scalars/upload) type for fields that support file uploads.

For implementation details, please refer to the documentation of the GraphQL upload library of your choice.
