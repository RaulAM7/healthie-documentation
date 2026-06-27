---
title: OfferingImage | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringimage/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringimage/index.md
---

Offering Image

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the offering image

[`image_content_type` ](#field-image-content-type)· [`String` ](/reference/2026-01-01/scalars/string)· image content type

[`image_file_name` ](#field-image-file-name)· [`String` ](/reference/2026-01-01/scalars/string)· image file name

[`image_file_size` ](#field-image-file-size)· [`String` ](/reference/2026-01-01/scalars/string)· image file size

[`image_updated_at` ](#field-image-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· when image was updated

[`image_url` ](#field-image-url)· [`String` ](/reference/2026-01-01/scalars/string)· url for image

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of image

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

## Used By

[`Offering.offering_image`](/reference/2026-01-01/objects/offering)

[`OfferingImageEdge.node`](/reference/2026-01-01/objects/offeringimageedge)

[`OfferingImagePaginationConnection.nodes`](/reference/2026-01-01/objects/offeringimagepaginationconnection)

## Definition

```
"""
Offering Image
"""
type OfferingImage {
  """
  created at
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the offering image
  """
  id: ID!


  """
  image content type
  """
  image_content_type: String


  """
  image file name
  """
  image_file_name: String


  """
  image file size
  """
  image_file_size: String


  """
  when image was updated
  """
  image_updated_at: ISO8601DateTime


  """
  url for image
  """
  image_url: String


  """
  name of image
  """
  name: String


  """
  updated at
  """
  updated_at: ISO8601DateTime!
}
```
