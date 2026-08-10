# Microsoft Fabric Notebooks — Interview & DP-700 Quick Notes

---

# 1. Notebook Basics

## Notebook

A **Fabric Notebook** is an interactive development environment used to write and execute code for data engineering, analytics, and data science.

Common languages include:

- PySpark / Python
- Spark SQL
- Scala
- R

### Common Uses

- Data ingestion
- Data transformation
- Data cleansing
- Data analysis
- ETL / ELT
- Delta Lake operations
- Data quality checks
- Advanced data processing

---

# 2. Notebook Cell

A **cell** is an individual executable block inside a notebook.

Cells can contain:

- Code
- SQL
- Markdown

Example:

```text id="q6i9u7"
Notebook
│
├── Markdown Cell
├── PySpark Cell
├── SQL Cell
└── PySpark Cell
```

Cells can be executed individually or as part of the notebook workflow.

---

# 3. Spark Session

`spark` represents the Spark session used by the notebook.

It provides the entry point for performing Spark operations.

Example:

```python id="n6dq9m"
df = spark.read.csv("Files/customer.csv", header=True)
```

Common Spark operations include:

- Reading data
- Writing data
- Creating DataFrames
- Running SQL
- Transforming data
- Managing Spark jobs

### Interview One-Liner

> **Spark Session = Entry point for Spark operations in a notebook.**

---

# 4. Spark Compute

Fabric Notebooks use Spark compute to execute Spark workloads.

Spark compute provides the resources required to:

- Execute PySpark code
- Read data
- Transform data
- Write data
- Run Spark SQL
- Process large datasets

### Important

Do not think of a Spark pool simply as "the notebook."

```text id="d2a8w8"
Notebook
   ↓
Spark Session
   ↓
Spark Compute
   ↓
Execute Spark Workload
```

Fabric manages the Spark environment used by notebooks and Spark jobs.

---

# 5. Language Selection / Magics

Fabric Notebooks support different languages.

Common language magic examples include:

```text id="8u0j6g"
%%pyspark
```

Execute PySpark code.

```text id="q1f24k"
%%sql
```

Execute Spark SQL.

```text id="k3o4yw"
%%scala
```

Execute Scala.

```text id="1l4e3m"
%%sparkr
```

Execute R.

### Important

Language magics allow you to specify the language used by a notebook cell where supported.

---

# 6. Reading Data

Spark can read different file formats.

---

## CSV

```python id="6u0y1t"
df = spark.read.csv(
    "Files/customer.csv",
    header=True,
    inferSchema=True
)
```

---

## Parquet

```python id="xk4z91"
df = spark.read.parquet(
    "Files/customer.parquet"
)
```

---

## JSON

```python id="7ez1ry"
df = spark.read.json(
    "Files/customer.json"
)
```

---

## Delta

```python id="7d7v1k"
df = spark.read.format("delta").load(
    "Tables/Customer"
)
```

---

# 7. Reading ADLS Gen2 Data

ADLS Gen2 data can be accessed using an ABFSS path when appropriate authentication and permissions are configured.

General format:

```text id="5c1w4k"
abfss://container@storageaccount.dfs.core.windows.net/path/file.parquet
```

Example:

```python id="h7w3bd"
df = spark.read.parquet(
    "abfss://container@storageaccount.dfs.core.windows.net/path/file.parquet"
)
```

### Important

In Fabric, you will often use:

- OneLake paths
- Lakehouse Files
- Lakehouse Tables
- Shortcuts

instead of manually working with long external storage paths.

---

# 8. Authentication

When accessing external resources, authentication and authorization are required.

Common approaches include:

- SAS
- Service Principal
- Managed Identity
- OAuth / Microsoft Entra-based authentication

---

## SAS Token

SAS provides delegated, time-limited access to Azure Storage resources.

### Characteristics

- Temporary access
- Permission-based
- Can have an expiration time
- Useful for specific access scenarios

### Important

Avoid hardcoding SAS tokens in notebooks.

---

# 9. Service Principal

A Service Principal represents an application identity in Microsoft Entra ID.

Common information includes:

- Tenant ID
- Client ID
- Client Secret or certificate

### Common Uses

- Automation
- Application-to-application authentication
- Pipelines
- Automated data access

### Important

Secrets should be stored securely rather than hardcoded in notebooks.

---

# 10. Managed Identity

Managed Identity provides an Azure-managed identity without requiring developers to manage passwords or client secrets.

### Benefits

- No hardcoded passwords
- No client secret management
- Azure-managed identity
- Suitable for automation
- Strong security option

### Important

Managed Identity is generally preferred when the service and target resource support it.

---

# 11. Writing Data

Spark can write data in different formats.

---

## Write CSV

```python id="ryy2fi"
df.write.csv(
    "Files/output/customer"
)
```

---

## Write Parquet

```python id="g4e8lq"
df.write.parquet(
    "Files/output/customer"
)
```

---

## Write Delta

```python id="l9m55t"
df.write.format("delta").save(
    "Files/output/customer"
)
```

---

## Save as Table

```python id="6e3ax8"
df.write.saveAsTable("Customer")
```

A managed Lakehouse table can then be queried using SQL.

---

# 12. Write Modes

Common Spark write modes include:

```text id="5jyx5f"
append
overwrite
ignore
error / errorifexists
```

Example:

```python id="2u9b5n"
df.write \
  .mode("append") \
  .format("delta") \
  .save("Tables/Sales")
```

### Important

```text
append    → Add new data
overwrite → Replace existing data
ignore    → Do nothing if destination exists
error     → Fail if destination exists
```

---

# 13. Files vs Delta Tables

## Files

Files are stored in the Lakehouse **Files** area.

Examples:

- CSV
- JSON
- Parquet

Common uses:

- Raw data
- Landing data
- Intermediate data
- Source files

Example:

```text id="6v5l8k"
Lakehouse
│
└── Files
    ├── raw
    ├── processed
    └── intermediate
```

---

## Delta Tables

Lakehouse tables use the Delta Lake format.

They provide:

- Structured table access
- ACID transactions
- Schema enforcement
- Schema evolution
- Time travel
- Updates
- Deletes
- Merge / Upsert
- Reliable data management

Example:

```text id="aj1l7w"
Lakehouse
│
└── Tables
    ├── Customer
    ├── Product
    └── Sales
```

---

# 14. Files vs Tables — Important Correction

Do not memorize:

> Files = No metadata  
> Delta Tables = Metadata

That is too simplistic.

Instead remember:

```text id="cqk52x"
Files
 ↓
File-based storage
 ↓
CSV / JSON / Parquet
 ↓
Flexible storage

Tables
 ↓
Structured table abstraction
 ↓
Typically Delta Lake
 ↓
SQL / Spark analytics
```

Files can also contain metadata depending on the format and how they are managed.

---

# 15. Bronze, Silver, Gold in Notebooks

Notebooks are commonly used to implement transformations between Medallion layers.

```text id="e8zj4s"
Bronze
  ↓
Notebook
  ↓
Clean / Transform
  ↓
Silver
  ↓
Notebook
  ↓
Business Logic
  ↓
Gold
```

### Bronze

- Raw data
- Minimal transformation

### Silver

- Cleaned data
- Deduplicated data
- Standardized data
- Joined data

### Gold

- Business-ready data
- Aggregated data
- Reporting data

---

# 16. mssparkutils

`mssparkutils` is a Microsoft Fabric utility library used from notebooks for common utility operations.

Depending on the Fabric environment and supported APIs, it can help with:

- File operations
- Notebook execution
- Workspace-related utilities
- Secret-related operations
- Other Fabric/Spark utility tasks

---

## File Operations

Common examples include:

```text id="myv3ph"
ls()
cp()
rm()
mkdirs()
```

Example concept:

```python id="qg6jpj"
mssparkutils.fs.ls("Files/")
```

---

## Run Another Notebook

Notebook utilities can be used to execute another notebook where supported.

Conceptually:

```text id="z2d7i9"
Notebook A
    ↓
Run Notebook B
```

### Important

Use the current Fabric-supported `mssparkutils` APIs/documentation when implementing these operations because available methods can vary by workload/runtime.

---

# 17. Partitioning

Partitioning divides data into separate directory partitions based on one or more columns.

Example:

```text id="mbb7y6"
sales/
│
├── year=2024/
├── year=2025/
└── year=2026/
```

Another example:

```text id="rj5f3t"
sales/
│
├── year=2026/
│   ├── month=01/
│   ├── month=02/
│   └── month=03/
```

---

# 18. Benefits of Partitioning

Partitioning can provide:

- Partition pruning
- Less data scanning
- Better query performance
- Improved processing efficiency
- Reduced compute requirements in suitable workloads

### Important

Partitioning is **not automatically faster**.

Poor partition choices can create:

- Too many small files
- Too many partitions
- Uneven data distribution
- Metadata overhead

Therefore, choose partition columns based on query patterns and data volume.

---

# 19. Common Partition Columns

Common examples:

- Year
- Month
- Date
- Region
- Country

Good partition columns generally have:

- Appropriate cardinality
- Frequent filtering in queries
- Sufficient data per partition

---

# 20. Why Parquet?

Parquet is a columnar storage format.

### Advantages

- Columnar storage
- Compression
- Efficient analytical reads
- Reads only required columns
- Better performance than many row-oriented formats for analytics

Example:

```text id="kz4nkg"
CSV
 ↓
Row-based text format
 ↓
Larger / slower for analytics

Parquet
 ↓
Columnar format
 ↓
Compressed
 ↓
Efficient analytics
```

---

# 21. Why Delta Lake?

Delta Lake builds additional reliability and data-management capabilities on top of Parquet.

### Delta Features

- ACID Transactions
- Schema Enforcement
- Schema Evolution
- Time Travel
- MERGE / Upsert
- UPDATE
- DELETE
- Transaction Log
- Reliable Data Management

### Simple Comparison

```text id="j56j8y"
CSV
 ↓
Text-based
 ↓
Simple
 ↓
Not ideal for large-scale analytics

Parquet
 ↓
Columnar
 ↓
Compressed
 ↓
Fast analytical reads

Delta
 ↓
Parquet
+
Transaction Log
 ↓
ACID + Schema + Time Travel + MERGE
```

---

# 22. Delta MERGE / UPSERT

Delta supports `MERGE` operations for updating existing records and inserting new records.

Conceptually:

```sql id="k0l7g6"
MERGE INTO target
USING source
ON target.CustomerID = source.CustomerID

WHEN MATCHED THEN
    UPDATE SET *

WHEN NOT MATCHED THEN
    INSERT *;
```

### Common Uses

- Incremental loads
- Upserts
- Synchronizing source and target
- Slowly Changing Dimensions
- Data lakehouse pipelines

---

# 23. Copy Activity vs Dataflow Gen2 vs Notebook

This is an important DP-700 concept.

## Copy Activity

Used mainly for:

- Moving data
- Source → Destination
- Fast ingestion
- Minimal transformation

Example:

```text id="09qg2k"
SQL Server
    ↓
Copy Activity
    ↓
Lakehouse
```

---

## Dataflow Gen2

Used for:

- Low-code transformations
- Filtering
- Joining
- Renaming
- Cleaning
- Derived columns
- Aggregations

Ideal when Power Query provides sufficient transformation capabilities.

---

## Notebook

Used for:

- Complex transformations
- PySpark
- Spark SQL
- Advanced ETL
- Large-scale processing
- Custom business logic
- Advanced data engineering
- Data science / ML workloads where appropriate

Example:

```text id="5h4f8b"
Source
  ↓
Notebook
  ↓
PySpark
  ↓
Complex Transformation
  ↓
Delta Table
```

---

# 24. Simple Tool Selection

```text id="v1y0pb"
Need to MOVE data?
        ↓
   Copy Activity

Need LOW-CODE transformation?
        ↓
   Dataflow Gen2

Need COMPLEX / CODE-BASED transformation?
        ↓
   Notebook / PySpark

Need REAL-TIME processing?
        ↓
   Eventstream
```

---

# 25. Notebook with DataFrame

A DataFrame is a distributed table-like data structure used by Spark.

Example:

```python id="1b2t4w"
df = spark.read.parquet("Files/customer.parquet")
```

Select columns:

```python id="82g1v4"
df.select("CustomerID", "CustomerName")
```

Filter:

```python id="w8v8ko"
df.filter(df.Country == "India")
```

Group and aggregate:

```python id="7h2v0p"
df.groupBy("Country").count()
```

Write:

```python id="z6h7ye"
df.write.format("delta").mode("overwrite").save(
    "Tables/Customer"
)
```

---

# 26. Notebook Transformation Flow

```text id="e5f9c3"
Read Data
   ↓
DataFrame
   ↓
Filter
   ↓
Select
   ↓
Join
   ↓
Aggregate
   ↓
Deduplicate
   ↓
Handle Nulls
   ↓
Write Delta
   ↓
Silver / Gold
```

---

# 27. Notebook and Pipeline Integration

A Notebook can be executed as part of a Data Pipeline.

```text id="7am1ql"
Data Pipeline
      ↓
Notebook Activity
      ↓
Fabric Notebook
      ↓
PySpark
      ↓
Transformation
      ↓
Lakehouse
```

This allows notebooks to become part of automated ETL/ELT workflows.

---

# 28. Notebook Parameters

Notebook parameters can be used to make notebooks reusable.

Example concept:

```text id="7o0i7x"
Pipeline
   ↓
Notebook Activity
   ↓
Parameters
   ├── SourcePath
   ├── TargetTable
   └── LoadDate
   ↓
Notebook
```

Instead of hardcoding:

```python id="g7a0qj"
source = "Files/customer.csv"
```

the notebook can receive a runtime value.

This makes the same notebook reusable for multiple datasets.

---

# 29. Notebook Performance — Important Points

For large datasets, remember:

### Avoid

- Collecting huge datasets to the driver
- Excessive `collect()`
- Excessive `toPandas()`
- Too many small files
- Unnecessary shuffles
- Poor partitioning
- Repeated expensive transformations

### Prefer

- DataFrame APIs
- Predicate filtering
- Column pruning
- Appropriate partitioning
- Efficient file formats such as Parquet/Delta
- Caching only when beneficial
- Optimized joins

---

# 30. Notebook vs Pipeline

These are different concepts.

```text id="v8q4x4"
Pipeline
   ↓
Orchestration
   ↓
Controls workflow
```

```text id="3cr8d8"
Notebook
   ↓
Data Processing
   ↓
PySpark / Spark SQL
```

They work together:

```text id="qq3lzb"
Pipeline
   ↓
Notebook Activity
   ↓
Notebook
   ↓
PySpark
   ↓
Transform Data
```

---

# 31. Notebook vs Dataflow Gen2

| Notebook | Dataflow Gen2 |
|---|---|
| Code-based | Low-code |
| PySpark / Spark | Power Query |
| Complex transformations | Standard transformations |
| Advanced processing | Business-friendly |
| Highly customizable | Easier to build |
| Suitable for complex ETL | Suitable for low-code ETL |

---

# 32. Files vs Delta Tables

| Files | Delta Tables |
|---|---|
| Flexible file storage | Structured table format |
| CSV / JSON / Parquet | Delta |
| Often used for raw data | Often used for curated data |
| Flexible access | SQL + Spark access |
| Depends on file format for capabilities | ACID transactions |
| Good for landing/intermediate data | Good for analytical workloads |

---

# 33. Most Important Interview One-Liners

```text id="tw9h3m"
Notebook
= Interactive development environment for Spark-based data processing.

Cell
= Individual executable block in a notebook.

Spark Session
= Entry point for Spark operations.

Spark Compute
= Compute resources used to execute Spark workloads.

Language Magic
= Specifies the language used by a notebook cell.

PySpark
= Python API for Apache Spark.

DataFrame
= Distributed table-like data structure in Spark.

Files
= Flexible file-based storage area in a Lakehouse.

Delta Table
= Structured table using the Delta Lake format.

Partitioning
= Organizing data into partitions to improve data skipping/pruning and query performance when used appropriately.

mssparkutils
= Fabric notebook utility library for common notebook, file, and workspace-related operations.

Managed Identity
= Azure-managed identity that avoids managing application secrets.

Copy Activity
= Data movement.

Dataflow Gen2
= Low-code transformation.

Notebook
= Code-based Spark processing.

Delta Lake
= Reliable table format with ACID transactions, schema management, time travel, and MERGE support.
```

---

# 34. Most Important DP-700 Points

## Notebook

> Interactive environment for data engineering and Spark processing.

## Cell

> Individual executable block inside a notebook.

## Spark Session

> Entry point to Spark operations.

## Spark Compute

> Compute resources used to execute Spark workloads.

## PySpark

> Python API used to work with Apache Spark.

## DataFrame

> Distributed table-like structure used to process data with Spark.

## Dataflow Gen2

> Low-code data ingestion and transformation tool.

## Copy Activity

> Data movement tool used to copy data between sources and destinations.

## Delta

> Reliable table format built around Parquet and a transaction log.

## Partitioning

> Organizes data into partitions and can improve query performance through partition pruning.

## Managed Identity

> Azure-managed identity that avoids storing application secrets.

## mssparkutils

> Fabric utility library available in notebooks for common utility operations.

---

# 35. Final Mental Model

```text id="znh4qa"
                    FABRIC NOTEBOOK
                          │
                          ↓
                    SPARK SESSION
                          │
                          ↓
                    SPARK COMPUTE
                          │
                          ↓
                      READ DATA
                          │
          ┌───────────────┼────────────────┐
          ↓               ↓                ↓
         CSV           Parquet           Delta
          │               │                │
          └───────────────┼────────────────┘
                          ↓
                       DataFrame
                          │
                          ↓
                  TRANSFORM DATA
                          │
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
      Filter             Join           Aggregate
        ↓                 ↓                 ↓
        └─────────────────┼─────────────────┘
                          ↓
                     WRITE DATA
                          │
                          ↓
                       Delta
                          │
                          ↓
                    Silver / Gold
```

---

# ⭐ One-Line Memory

```text id="xw1l0j"
Notebook = Code + Spark + Data Processing

Cell = Executable Block

Spark Session = Entry Point

Spark Compute = Runs Spark Workloads

PySpark = Python + Spark

DataFrame = Distributed Table

Copy = Move Data

Dataflow Gen2 = Low-Code Transformation

Notebook = Complex Code-Based Transformation

Files = Flexible Storage

Delta = Reliable Analytical Tables

Partitioning = Organize Data for Efficient Access

Parameter = Runtime Input

Variable = Runtime Value

Managed Identity = Secure Azure-Managed Authentication
```