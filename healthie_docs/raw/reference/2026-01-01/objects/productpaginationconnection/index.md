---
title: ProductPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/productpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/productpaginationconnection/index.md
---

The connection type for Product.

## Fields

[`edges` ](#field-edges)· [`[ProductEdge]` ](/reference/2026-01-01/objects/productedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Product]` ](/reference/2026-01-01/objects/product)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.products`](/reference/2026-01-01/queries/products)

## Definition

```
"""
The connection type for Product.
"""
type ProductPaginationConnection {
  """
  A list of edges.
  """
  edges: [ProductEdge]


  """
  A list of nodes.
  """
  nodes: [Product]


  """
  Information to aid in pagination.
  """
  page_info: PageInfo!


  """
  Total count of items.
  """
  total_count: Int!
}
```
