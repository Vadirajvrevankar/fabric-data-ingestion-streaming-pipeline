# Dataflow Gen2 Ingestion

## Objective
Build an end-to-end data ingestion and transformation solution
using Microsoft Fabric Dataflow Gen2 and Lakehouse.

## Architecture

CSV Files
    ↓
Lakehouse Files
    ↓
Dataflow Gen2
    ↓
Power Query
    ↓
Lakehouse Tables

## Sources
- customers.csv
- products.csv
- orders.csv

## Transformations
### Customers
- Promote headers
- Replace blank city with Unknown
- Rename customer_segment → segment
- signup_date → Date
- Remove duplicate customer_id

### Products
- Promote headers
- Missing category → Unknown
- unit_price → Decimal number
- stock_qty → Whole number
- Filter active products
- Remove duplicate product_id

### Orders
- Promote headers
- Verify data types
- Filter Completed orders
- Remove duplicate order_id

## Destination
Lakehouse: LH_Ecommerce_Lakehouse

Tables:
- dbo.customers
- dbo.products
- dbo.orders

## Pipeline
Dataflow Gen2 embedded in Pipeline and executed successfully.

## Result
End-to-end ingestion and transformation completed successfully.
