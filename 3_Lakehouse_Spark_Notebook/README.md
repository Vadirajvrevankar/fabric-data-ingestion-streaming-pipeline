# Fabric Lakehouse & Spark Notebook Pipeline

## Project Overview

This project demonstrates hands-on data engineering using Microsoft Fabric Lakehouse and Apache Spark.

The project covers:

- Creating and attaching a Fabric Lakehouse to a Notebook
- Reading CSV data using PySpark
- Creating a Spark DataFrame
- Writing raw data as Parquet to Lakehouse Files
- Creating a managed Delta table
- Querying the Delta table using the SQL Analytics Endpoint
- Chaining notebooks using `mssparkutils.notebook.run()`

---

## Project Flow

```text
Sample CSV
    ↓
Spark DataFrame
    ├──→ Raw Parquet → Lakehouse Files
    │
    └──→ Managed Delta Table
                  ↓
          SQL Analytics Endpoint

Parent Notebook
       ↓
mssparkutils.notebook.run()
       ↓
Child Notebook