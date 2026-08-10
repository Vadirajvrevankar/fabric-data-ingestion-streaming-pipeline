# Microsoft Fabric — Data Engineering Complete Notes

---

# 1. Sources

Data can come from multiple sources.

## Batch Sources

- SQL Server
- Azure SQL Database
- Oracle
- SAP
- APIs
- CSV Files
- Excel Files
- JSON Files
- ADLS Gen2
- Azure Blob Storage
- Amazon S3
- SharePoint
- Dataverse

## Streaming / Real-Time Sources

- Azure Event Hubs
- Apache Kafka
- IoT Devices
- Streaming Sources
- Event Sources

---

# 2. Ingestion

Data is ingested into Microsoft Fabric using different tools.

## Main Ingestion Tools

### Data Pipeline

Used mainly for:

- Orchestration
- Workflow management
- Scheduling
- Coordinating multiple activities

### Copy Activity

Used mainly for:

- Moving data
- Copying data from source to destination

### Dataflow Gen2

Used for:

- Low-code data ingestion
- Data transformation
- Power Query-based transformations

### Notebook

Used for:

- Code-based ingestion
- PySpark
- Spark
- Complex transformations

### Eventstream

Used for:

- Real-time data ingestion
- Streaming data processing
- Filtering
- Transformation
- Routing events

## Important

```text
Pipeline = Orchestration

Copy Activity = Data Movement
```

Example:

```text
SQL Server
    ↓
Data Pipeline
    ↓
Copy Activity
    ↓
Lakehouse
```

---

# 3. Transformation

Transformation means cleaning, changing, combining, and preparing data for analytics.

## Transformation Tools

- PySpark
- Spark SQL
- Dataflow Gen2
- Notebook
- SQL
- Eventstream transformations

## Common Transformations

- Filtering
- Selecting columns
- Renaming columns
- Joining
- Aggregation
- Deduplication
- Null handling
- Data type conversion
- Standardization
- Sorting
- Business rules

Example:

```text
Bronze
   ↓
Filtering
   ↓
Deduplication
   ↓
Null Handling
   ↓
Standardization
   ↓
Silver
```

---

# 4. OneLake

## Definition

OneLake is the unified logical data lake for Microsoft Fabric.

It provides a centralized way to store and access organizational data across Fabric workloads.

```text
Microsoft Fabric
       ↓
     OneLake
       ↓
 ┌─────┼──────────────┐
 ↓     ↓              ↓
Lakehouse Warehouse  Other Fabric
                     Workloads
```

## Important

OneLake is built into Microsoft Fabric and provides a unified data lake experience.

Do not simply say:

> All Fabric items store data in OneLake.

Instead remember:

> OneLake is the unified logical data lake for Microsoft Fabric, and Fabric workloads can store and access data through OneLake.

---

# 5. Lakehouse

## Definition

A Lakehouse is used for storing, processing, and analyzing data.

It combines the flexibility of a data lake with structured analytics capabilities.

```text
Lakehouse
│
├── Files
│
└── Tables
```

---

# 6. Lakehouse Files

Files provide flexible file-based storage.

## Files can contain

- CSV
- JSON
- Parquet
- Text files
- Other supported formats

## Common Uses

Files are commonly used for:

- Raw Data
- Semi-Structured Data
- Landing Zone
- Intermediate Data
- Source Data

Example:

```text
Files/
│
├── raw/
│   ├── customer.csv
│   └── orders.json
│
├── processed/
│   └── customer.parquet
│
└── intermediate/
```

---

# 7. Lakehouse Tables

Tables provide a structured tabular interface for analytics.

Fabric Lakehouse tables are typically Delta Lake tables.

Example:

```text
Tables
│
├── Customer
├── Product
├── Orders
└── Sales
```

## Tables are used for

- Analytics
- Reporting
- Data Processing
- Business Consumption

---

# 8. Delta Lake

A Lakehouse table uses the Delta Lake table format.

A Delta table generally consists of:

```text
Delta Table
     │
     ├── Parquet Data Files
     │
     └── _delta_log
```

## Parquet Files

Parquet stores the actual table data in a columnar format.

## _delta_log

The Delta transaction log keeps track of table changes, transactions, and versions.

## Delta Table Features

- ACID Transactions
- Schema Enforcement
- Schema Evolution
- Time Travel
- Reliable Updates
- Reliable Deletes
- Version History
- Better Performance for Analytical Workloads

## Important

Do not think:

```text
Delta Table = One Parquet File
```

Instead:

```text
Delta Table
     ↓
Delta Lake Format
     ↓
Parquet Data Files
+
Delta Transaction Log
     ↓
Stored in OneLake
```

---

# 9. Medallion Architecture

Medallion Architecture organizes data into three main layers:

```text
Bronze
   ↓
Silver
   ↓
Gold
```

---

## Bronze Layer

Bronze contains raw or minimally transformed data.

### Characteristics

- Raw Data
- Source Copy
- Minimal Transformation
- Preserve Original Data
- Historical Data

Example:

```text
SQL Server
    ↓
Copy Activity
    ↓
Bronze
```

---

## Silver Layer

Silver contains cleaned, standardized, and integrated data.

### Common Transformations

- Joins
- Filtering
- Null Handling
- Deduplication
- Standardization
- Data Type Conversion
- Data Validation

Example:

```text
Bronze
   ↓
Clean
   ↓
Standardize
   ↓
Deduplicate
   ↓
Join
   ↓
Silver
```

---

## Gold Layer

Gold contains business-ready data.

### Characteristics

- Business Logic
- Aggregated Data
- KPIs
- Reporting Data
- Analytics-Ready Data

Example:

```text
Silver
   ↓
Business Logic
   ↓
Aggregation
   ↓
Gold
```

## Gold Layer Consumers

- Power BI
- Semantic Models
- SQL Users
- Business Users
- Data Analysts
- Analytics Teams
- Management

---

# 10. Data Access

Data in a Fabric Lakehouse can be accessed through:

- Files
- Tables
- SQL Analytics Endpoint
- Spark
- Notebooks

---

# 11. File Access

## Relative Path

Example:

```text
Files/Customer/customer.parquet
```

## PySpark

```python
df = spark.read.parquet("Files/Customer/customer.parquet")
```

---

# 12. ABFSS Path

ABFSS is commonly used to access Azure Data Lake Storage Gen2 data.

## General Format

```text
abfss://container@storageaccount.dfs.core.windows.net/path/file.parquet
```

## PySpark Example

```python
df = spark.read.parquet(
    "abfss://container@storageaccount.dfs.core.windows.net/path/file.parquet"
)
```

## Important

In Fabric, you will often work with OneLake, Lakehouse paths, and Shortcuts rather than manually constructing long external storage paths.

---

# 13. Table Access

## SQL

```sql
SELECT *
FROM Customer;
```

## PySpark

```python
df = spark.read.table("Customer")
```

Tables provide a structured way to work with data.

---

# 14. SQL Analytics Endpoint

A Fabric Lakehouse provides a SQL Analytics Endpoint for querying Lakehouse tables using SQL.

```text
Lakehouse
│
├── Files
│
├── Tables
│
└── SQL Analytics Endpoint
```

Example:

```sql
SELECT
    CustomerID,
    CustomerName
FROM Customer;
```

## Important

The SQL Analytics Endpoint is mainly used for querying Lakehouse tables using SQL.

---

# 15. Shortcuts

## Definition

Shortcuts provide access to data without physically copying the data into the destination.

## Supported Sources Can Include

- Another Lakehouse
- ADLS Gen2
- Amazon S3
- Other supported OneLake locations

## Normal Copy

```text
Source
   ↓
Copy Data
   ↓
Fabric
```

Data is duplicated.

## Shortcut

```text
External Data
      ↑
      │
   Shortcut
      │
      ↓
  Lakehouse
```

The data remains in the source location while Fabric provides logical access to it.

## Benefits

- No unnecessary data duplication
- Reduced storage requirements
- Centralized Access
- Single Logical View
- Easier Data Sharing

## Important

```text
Copy     = Data Movement

Shortcut = Data Access Without Copying
```

---

# 16. Lakehouse vs Warehouse

## Lakehouse

Best suited for:

- Data Engineering
- Spark
- PySpark
- Data Lake Architecture
- Files + Tables
- Semi-Structured Data
- Large-scale Data Processing

```text
Lakehouse
│
├── Files
├── Tables
└── Spark
```

## Warehouse

Best suited for:

- SQL
- Relational Data
- Data Warehousing
- BI
- Reporting
- T-SQL-based Analytics

```text
Warehouse
    ↓
Structured Tables
    ↓
SQL
    ↓
Analytics / BI
```

## Simple Difference

```text
Lakehouse → Spark + Files + Tables

Warehouse → SQL + Structured Tables
```

---

# 17. Data Pipeline and Orchestration

Orchestration means controlling and coordinating different data activities.

Example:

```text
Pipeline
   ↓
Schedule
   ↓
Copy Activity
   ↓
Bronze
   ↓
Notebook
   ↓
Silver
   ↓
Notebook
   ↓
Gold
   ↓
Power BI
```

A pipeline can coordinate multiple activities and control their execution order.

---

# 18. Pipeline Monitoring

After creating a pipeline, its execution can be monitored.

## Important Monitoring Concepts

- Pipeline Run
- Activity Run
- Success
- Failure
- Retry
- Error Details
- Execution Duration
- Run History

Example:

```text
Pipeline
   ↓
Run
   ↓
Monitor
   ↓
Success / Failure
   ↓
Troubleshoot
```

---

# 19. Choosing the Right Fabric Tool

| Requirement | Recommended Tool |
|---|---|
| Move data | Copy Activity |
| Orchestrate workflow | Data Pipeline |
| Low-code transformation | Dataflow Gen2 |
| Complex transformation | Notebook / PySpark |
| Spark processing | Notebook |
| SQL processing | SQL / Spark SQL |
| Real-time ingestion | Eventstream |
| Store lake data | Lakehouse |
| SQL-first analytics | Warehouse |
| Query Lakehouse tables | SQL Analytics Endpoint |
| Access external data without copying | Shortcut |
| BI Reporting | Power BI |

## Easy Memory Trick

```text
Move Data        → Copy Activity
Control Workflow → Pipeline
Low-Code ETL     → Dataflow Gen2
Code ETL         → Notebook / PySpark
Real-Time        → Eventstream
Store Data       → Lakehouse / Warehouse
BI               → Power BI
```

---

# 20. Real-Time Intelligence

Fabric also supports real-time data processing.

## Basic Architecture

```text
Real-Time Source
       ↓
   Eventstream
       ↓
 Transform / Filter
       ↓
   Eventhouse
       ↓
      KQL
       ↓
Real-Time Analytics
```

## Example Sources

- IoT Devices
- Event Hubs
- Kafka
- Applications
- Streaming Events

---

# 21. Eventstream

Eventstream is used to ingest, transform, and route real-time event data.

## Common Operations

- Filter
- Transform
- Aggregate
- Manage Fields
- Route Events
- Multiple Destinations

Example:

```text
IoT Events
    ↓
Eventstream
    ↓
Filter
    ↓
Aggregate
    ↓
Eventhouse
```

---

# 22. Eventhouse

Eventhouse is designed for storing and analyzing real-time data.

It uses KQL databases and is optimized for high-volume event data and real-time analytics.

Example:

```text
Eventstream
     ↓
Eventhouse
     ↓
KQL Database
     ↓
KQL Query
```

---

# 23. KQL

KQL stands for Kusto Query Language.

It is used to query and analyze real-time data, such as data stored in Eventhouse.

Example:

```kusto
SalesEvents
| where Amount > 1000
| summarize TotalSales = sum(Amount)
```

---

# 24. Consumption Layer

The Consumption Layer is where prepared data is consumed by users and analytics tools.

```text
Bronze
   ↓
Silver
   ↓
Gold
   ↓
Consumption
```

## Consumers

- Power BI
- Semantic Models
- SQL
- Notebooks
- Data Analysts
- Business Users
- Applications
- Management

## Power BI Flow

```text
Gold Tables
     ↓
Semantic Model
     ↓
Power BI
     ↓
Reports
     ↓
Dashboards
     ↓
Business Decisions
```

---

# 25. Complete Microsoft Fabric Data Flow

```text
                         DATA SOURCES
                              │
          ┌───────────────────┼───────────────────┐
          ↓                   ↓                   ↓
        SQL                 Files                APIs
      Oracle                CSV/JSON             SAP
      Azure SQL             Excel                S3
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ↓
                         INGESTION
                              │
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
           Pipeline       Dataflow Gen2    Notebook
           Copy Activity                     PySpark
              │               │               │
              └───────────────┼───────────────┘
                              ↓
                           ONELAKE
                              │
                          LAKEHOUSE
                              │
                    ┌─────────┴─────────┐
                    ↓                   ↓
                  Files               Tables
              CSV/JSON/Parquet        Delta
                    │                   │
                    └─────────┬─────────┘
                              ↓
                     MEDALLION ARCHITECTURE
                              │
                    Bronze → Silver → Gold
                              │
                              ↓
                         CONSUMPTION
                              │
                ┌─────────────┼─────────────┐
                ↓             ↓             ↓
             Power BI        SQL        Notebooks
                │
         Semantic Model
                │
             Reports
```

---

# 26. Real-Time Fabric Data Flow

```text
IoT / Event Source / Kafka / Event Hub
                  ↓
              Eventstream
                  ↓
        Filter / Transform
                  ↓
              Eventhouse
                  ↓
                 KQL
                  ↓
        Real-Time Analytics
```

---

# 27. Most Important Points to Remember

## OneLake

> OneLake is the unified logical data lake for Microsoft Fabric.

## Lakehouse

> A Lakehouse combines data lake flexibility with structured analytics capabilities.

## Files

> Files provide flexible file-based storage such as CSV, JSON, and Parquet.

## Tables

> Lakehouse tables provide a structured interface and are typically Delta Lake tables.

## Delta Lake

> Delta Lake provides reliable table management using Parquet data files and a transaction log.

## Pipeline

> Pipeline is used for orchestration and workflow management.

## Copy Activity

> Copy Activity is primarily used for moving/copying data.

## Dataflow Gen2

> Dataflow Gen2 provides low-code data ingestion and transformation.

## Notebook

> Notebook is used for code-based data processing using Spark/PySpark.

## Eventstream

> Eventstream is used for real-time event ingestion, transformation, and routing.

## Eventhouse

> Eventhouse is used for storing and analyzing real-time event data.

## Shortcut

> Shortcut provides access to data without physically copying it.

## Bronze

> Bronze contains raw or minimally transformed data.

## Silver

> Silver contains cleaned, standardized, and integrated data.

## Gold

> Gold contains business-ready and analytics-ready data.

## SQL Analytics Endpoint

> SQL Analytics Endpoint allows SQL querying of Lakehouse tables.

## Warehouse

> Warehouse is a SQL-first relational analytics and data warehousing workload.

---

# 28. Final Mental Model

## Batch / Data Engineering

```text
SOURCE
   ↓
INGEST
   ↓
ONELAKE
   ↓
LAKEHOUSE
   ↓
FILES / TABLES
   ↓
BRONZE
   ↓
SILVER
   ↓
GOLD
   ↓
SEMANTIC MODEL
   ↓
POWER BI
   ↓
BUSINESS DECISIONS
```

## Real-Time

```text
EVENT SOURCE
   ↓
EVENTSTREAM
   ↓
EVENTHOUSE
   ↓
KQL
   ↓
REAL-TIME ANALYTICS
```

# ⭐ One-Line Memory

```text
Source → Ingest → OneLake → Lakehouse → Bronze → Silver → Gold → Semantic Model → Power BI
```

```text
Real-Time:
Source → Eventstream → Eventhouse → KQL
```