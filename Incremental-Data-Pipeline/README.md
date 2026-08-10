# Incremental Data Pipeline

## Project Overview

This project demonstrates a parameterized, scheduled, and watermark-based incremental data ingestion pipeline built using Microsoft Fabric.

The project demonstrates:

- Loading order data from a CSV file stored in a Fabric Lakehouse
- Using pipeline parameters and Dynamic Content
- Scheduling pipeline execution
- Creating and using a watermark/control table
- Using a Lookup activity to retrieve the last processed date
- Filtering source data using the watermark
- Loading only new records into a destination Lakehouse table

---

## Architecture

```text
Microsoft Fabric Lakehouse
│
├── Files
│   └── orders.csv
│
│        ↓
│
├── Pipeline Parameter
│   └── SourceFilePath
│
│        ↓
│
├── Schedule Trigger
│
│        ↓
│
├── Lookup_Watermark
│   └── Reads LastProcessedDate
│
│        ↓
│
├── Copy_New_Orders
│   └── Filters records using order_date
│
│        ↓
│
└── Tables
    ├── dbo.orders
    ├── dbo.orders_incremental
    ├── dbo.orders_incremental_v2
    └── dbo.watermark