# Microsoft Fabric Data Pipeline — Complete Notes

---

# 1. Data Pipeline

## Definition

A **Data Pipeline** is used to orchestrate, schedule, automate, and monitor data workflows.

A pipeline coordinates different activities and controls the order in which they execute.

```text
Data Pipeline
│
├── Copy Activity
├── Notebook Activity
├── Dataflow Gen2 Activity
├── Stored Procedure Activity
├── Lookup Activity
├── Get Metadata Activity
├── Set Variable Activity
├── Append Variable Activity
├── If Condition Activity
├── Switch Activity
├── ForEach Activity
├── Until Activity
├── Wait Activity
├── Execute Pipeline Activity
└── Web Activity
```

## Simple Mental Model

```text
Pipeline
   ↓
Control + Orchestrate
   ↓
Activities
   ↓
Data Movement
   ↓
Transformation
   ↓
Validation
   ↓
Destination
```

---

# 2. Data Movement Activities

## Copy Activity

Copy Activity is primarily used to **move or copy data from a source to a destination**.

### Examples

```text
SQL Server
    ↓
Copy Activity
    ↓
Lakehouse
```

```text
ADLS Gen2
    ↓
Copy Activity
    ↓
Lakehouse
```

```text
API
    ↓
Copy Activity
    ↓
Lakehouse
```

## Common Uses

- SQL Server → Lakehouse
- Azure SQL → Lakehouse
- ADLS → Lakehouse
- Files → Lakehouse
- Source Database → Warehouse
- API → Data Storage

## Important

```text
Copy Activity = Data Movement
Pipeline      = Orchestration
```

---

# 3. Data Transformation Activities

## Notebook Activity

Notebook Activity is used to execute a Fabric notebook from a pipeline.

Notebooks can use:

- PySpark
- Spark SQL
- Python
- DataFrame operations
- Business logic

### Common Uses

- Data Transformation
- Data Cleansing
- Joins
- Aggregations
- Deduplication
- Null Handling
- Delta Table Creation
- Business Logic
- Complex Data Processing

Example:

```text
Pipeline
   ↓
Notebook Activity
   ↓
PySpark
   ↓
Transform Data
   ↓
Silver / Gold
```

---

# 4. Dataflow Gen2 Activity

Dataflow Gen2 provides **low-code data ingestion and transformation** using Power Query.

### Common Transformations

- Filtering
- Joins
- Derived Columns
- Aggregations
- Data Cleaning
- Data Type Conversion
- Column Renaming
- Removing Duplicates

Example:

```text
Pipeline
   ↓
Dataflow Gen2 Activity
   ↓
Power Query
   ↓
Transform Data
   ↓
Lakehouse / Warehouse
```

## Simple Difference

```text
Notebook
   ↓
Code-based transformation
   ↓
PySpark / Spark

Dataflow Gen2
   ↓
Low-code transformation
   ↓
Power Query
```

---

# 5. Stored Procedure Activity

Stored Procedure Activity is used to execute a stored procedure in a supported database/data source.

### Common Uses

- Insert Data
- Update Data
- Delete Data
- Merge Operations
- Audit Updates
- Database Business Logic

Example:

```text
Pipeline
   ↓
Stored Procedure Activity
   ↓
EXEC UpdateCustomerData
```

## Example Stored Procedure

```sql
EXEC UpdateCustomerData;
```

## Important

Stored Procedure Activity is useful when existing database logic needs to be executed as part of a pipeline workflow.

---

# 6. Metadata and Validation Activities

## Lookup Activity

Lookup Activity is used to retrieve data from a supported source and make the result available to subsequent pipeline activities.

### Common Use Cases

- Read Watermark Value
- Read Control Table
- Read Configuration Table
- Read Parameters
- Retrieve a query result
- Drive pipeline logic

Example:

```text
Control Table
     ↓
Lookup Activity
     ↓
LastProcessedDate
     ↓
Pipeline
```

### Incremental Load Example

```text
Lookup Activity
       ↓
Read LastWatermark
       ↓
Copy Activity
       ↓
Load New Records
```

---

# 7. Get Metadata Activity

Get Metadata Activity retrieves metadata information about data in a supported data store.

It is commonly used to check information such as:

- File existence
- File size
- File name
- Last modified information
- Child items
- Other available metadata

### Example

```text
File
 ↓
Get Metadata Activity
 ↓
Check File Exists
 ↓
If Condition
 ↓
Process File
```

## Common Use Case

Before processing a file:

```text
Check whether file exists
        ↓
      Exists?
      /     \
    Yes      No
    ↓         ↓
Process     Skip / Alert
```

---

# 8. Variable Activities

Variables store temporary values during pipeline execution.

## Set Variable Activity

Set Variable Activity assigns a value to a pipeline variable.

### Example

```text
Status = "Success"
FileCount = 10
```

Variables can store values such as:

- String
- Integer
- Boolean
- Array

### Example

```text
Set Variable
     ↓
FileCount = 10
```

---

# 9. Append Variable Activity

Append Variable Activity adds a value to an **array variable**.

Example:

```text
ProcessedFiles = []

Append:
    customer.csv
    product.csv
    sales.csv
```

Result:

```text
ProcessedFiles
[
    "customer.csv",
    "product.csv",
    "sales.csv"
]
```

## Common Use

Useful when collecting multiple values during a pipeline execution.

---

# 10. Conditional Activities

Conditional activities allow a pipeline to make decisions.

---

## If Condition Activity

If Condition Activity executes different logic based on whether a condition is true or false.

Example:

```text
File Exists?
    │
 ┌──┴───┐
Yes     No
 ↓       ↓
Process  Skip
File     File
```

### Example

```text
@equals(variables('Status'), 'Success')
```

If the condition is true:

```text
Continue Processing
```

If false:

```text
Stop / Alert / Alternative Path
```

---

# 11. Switch Activity

Switch Activity is used when there are **multiple possible conditions or cases**.

Example:

```text
Source Type
    │
    ├── SQL
    │     ↓
    │  Pipeline A
    │
    ├── CSV
    │     ↓
    │  Pipeline B
    │
    └── JSON
          ↓
       Pipeline C
```

## Simple Difference

```text
If Condition
     ↓
Usually True / False decision

Switch
     ↓
Multiple possible cases
```

---

# 12. Looping Activities

Looping activities allow a pipeline to repeat operations.

---

## ForEach Activity

ForEach Activity processes each item in a collection.

It can process items sequentially or in parallel, depending on the configuration.

Example:

```text
Files
[
  customer.csv
  product.csv
  sales.csv
]
       ↓
   ForEach
       ↓
 ┌─────┼─────┐
 ↓     ↓     ↓
File  File  File
 1     2     3
```

### Common Uses

- Process multiple files
- Process multiple tables
- Process multiple folders
- Execute the same activity for many items

### Example

```text
ForEach File
    ↓
Copy File
    ↓
Transform File
    ↓
Load File
```

---

# 13. Until Activity

Until Activity repeats activities until a specified condition becomes true.

Example:

```text
Start
  ↓
Check File
  ↓
File Available?
  ↓
No
  ↓
Wait
  ↓
Check Again
  ↓
File Available?
  ↓
Yes
  ↓
Continue
```

### Example Use Case

Wait until a file arrives:

```text
Until File Arrives
      ↓
Check File
      ↓
Wait
      ↓
Check Again
```

---

# 14. Wait Activity

Wait Activity pauses pipeline execution for a specified amount of time.

Example:

```text
Activity A
    ↓
Wait 5 Minutes
    ↓
Activity B
```

### Common Uses

- Wait before retrying
- Delay execution
- Give an external process time to complete
- Polling scenarios

---

# 15. Execute Pipeline Activity

Execute Pipeline Activity is used to execute another pipeline from a parent pipeline.

This supports **parent-child pipeline architecture**.

## Example

```text
Parent Pipeline
      ↓
Execute Pipeline Activity
      ↓
Child Pipeline
```

### Master Pipeline Example

```text
Master Pipeline
│
├── Customer Pipeline
├── Product Pipeline
└── Sales Pipeline
```

This approach helps divide a large workflow into smaller reusable pipelines.

---

# 16. Web Activity

Web Activity is used to call a web endpoint or REST API from a pipeline.

### Common Use Cases

- Call REST API
- Trigger external application
- Invoke web service
- Send HTTP request
- Integrate with external systems

Example:

```text
Pipeline
   ↓
Web Activity
   ↓
REST API
   ↓
External Application
```

---

# 17. Pipeline Parameters

## Definition

Parameters are values passed into a pipeline when the pipeline is executed.

They make pipelines reusable and configurable.

### Example

Parameter:

```text
FileName = customer.csv
```

Expression:

```text
@pipeline().parameters.FileName
```

### Example

```text
Pipeline Parameter
       ↓
FileName
       ↓
customer.csv
       ↓
Copy Activity
```

## Important Characteristics

- Input to the pipeline
- Passed at runtime
- Can be used throughout the pipeline
- Useful for creating reusable pipelines
- Pipeline parameters are not changed during pipeline execution

---

# 18. Variables

Variables store values during pipeline execution.

## Common Variable Types

- String
- Integer
- Boolean
- Array

## Characteristics

- Used inside the pipeline
- Can be modified during execution
- Store intermediate values
- Useful for maintaining state during execution

### Example

```text
Variable:
FileCount = 10
```

Later:

```text
Set Variable
FileCount = 20
```

---

# 19. Parameters vs Variables

This is an important interview and DP-700 concept.

| Parameter | Variable |
|---|---|
| Input to pipeline | Value stored during execution |
| Usually provided at runtime | Created/used inside pipeline |
| Used for configuration | Used for temporary/intermediate values |
| Not modified during pipeline execution | Can be modified |
| Helps make pipeline reusable | Helps maintain execution state |

## Easy Memory Trick

```text
Parameter = Input

Variable = Runtime Value
```

---

# 20. Dynamic Content

Dynamic Content allows values to be generated or referenced dynamically at runtime.

Examples:

```text
@utcNow()
```

```text
@pipeline().parameters.FileName
```

```text
@variables('FileCount')
```

## Common Uses

- Dynamic File Names
- Dynamic Folder Names
- Dynamic Queries
- Dynamic Paths
- Dynamic Filters
- Dynamic Dates
- Dynamic Parameters

### Example

Instead of hardcoding:

```text
customer.csv
```

Use:

```text
@pipeline().parameters.FileName
```

Now the same pipeline can process:

```text
customer.csv
product.csv
sales.csv
```

---

# 21. Full Load

## Definition

A Full Load loads the entire dataset from the source into the destination.

Example:

```text
Source
  ↓
Read ALL Records
  ↓
Destination
```

Suppose a table contains:

```text
1,000,000 records
```

Every run loads all 1,000,000 records.

## Advantages

- Simple
- Easy to implement
- Easy to understand

## Disadvantages

- More data movement
- More processing
- More time
- Higher resource usage
- Not efficient for very large datasets

---

# 22. Incremental Load

## Definition

Incremental Load loads only **new or modified records** instead of loading the entire dataset.

Example:

```text
Source
  ↓
Only New / Updated Records
  ↓
Destination
```

Suppose:

```text
Total Records = 1,000,000

New Records = 5,000
Updated Records = 2,000
```

Instead of processing all 1,000,000 records:

```text
Process only 7,000 records
```

This improves efficiency.

---

# 23. Full Load vs Incremental Load

| Full Load | Incremental Load |
|---|---|
| Loads entire dataset | Loads only new/changed data |
| Simple | More complex |
| More data movement | Less data movement |
| More processing | Less processing |
| Suitable for small datasets | Suitable for large datasets |
| Can be slower | Usually faster |

## Easy Memory Trick

```text
Full Load
    ↓
Everything

Incremental Load
    ↓
Only Changes
```

---

# 24. Watermark

## Definition

A Watermark stores the value representing the **last successfully processed point** in an incremental data load.

It allows the next pipeline run to identify which records are new or changed.

### Common Watermark Columns

- ModifiedDate
- UpdatedDate
- CreatedDate
- Increasing ID
- Timestamp
- Version Number

---

# 25. Watermark Example

Suppose the source table contains:

```text
ID    ModifiedDate
1     2026-08-01
2     2026-08-02
3     2026-08-03
4     2026-08-04
5     2026-08-05
```

The previous successful pipeline run processed:

```text
Watermark = 2026-08-03
```

The next run can load:

```text
ModifiedDate > 2026-08-03
```

Therefore:

```text
ID 4
ID 5
```

are processed.

---

# 26. Watermark with a Control Table

A control table can store the last successfully processed watermark.

Example:

```text
Control Table
─────────────────────────
PipelineName
LastWatermark
Status
LastRunTime
─────────────────────────
CustomerLoad
2026-08-03
Success
2026-08-10
```

Pipeline flow:

```text
Control Table
      ↓
Lookup Activity
      ↓
Read Last Watermark
      ↓
Copy Activity
      ↓
Load New / Modified Data
      ↓
Successful?
      ↓
Update Watermark
```

---

# 27. Complete Incremental Load Flow

```text
                 SOURCE
                    ↓
             Control Table
                    ↓
              Lookup Activity
                    ↓
          Read Last Watermark
                    ↓
              Copy Activity
                    ↓
        Filter New / Updated Records
                    ↓
                Lakehouse
                    ↓
             Transformation
                    ↓
              Load Successful?
                 /       \
               Yes        No
                ↓          ↓
        Update Watermark   Do Not
                ↓          Update
             Control Table
```

## Very Important

Update the watermark **only after the data load has successfully completed**.

If the pipeline fails, the watermark should not incorrectly move forward.

---

# 28. Incremental Load Using a Date Filter

Example source query:

```sql
SELECT *
FROM Customer
WHERE ModifiedDate > '2026-08-03';
```

In a dynamic pipeline, the watermark can be supplied dynamically.

Conceptually:

```text
LastWatermark
      ↓
Dynamic Query
      ↓
Only New / Modified Records
```

---

# 29. Control Table

A Control Table stores configuration and execution information used by data pipelines.

It can contain:

```text
PipelineName
SourceTable
TargetTable
WatermarkColumn
LastWatermark
LoadType
Status
LastRunTime
```

Example:

```text
CustomerLoad
Source: Customer
Target: Customer
WatermarkColumn: ModifiedDate
LastWatermark: 2026-08-03
LoadType: Incremental
Status: Success
```

## Why Control Tables Matter

They help create metadata-driven pipelines.

Instead of creating a separate hardcoded pipeline for every table, configuration can be stored in a control table.

---

# 30. Metadata-Driven Pipeline

A metadata-driven pipeline uses configuration information to dynamically control processing.

Example:

```text
Control Table
      ↓
Lookup
      ↓
Read Configuration
      ↓
ForEach
      ↓
Process Multiple Tables
```

Example control table:

```text
SourceTable    TargetTable    LoadType
Customer       Customer       Incremental
Product        Product        Full
Sales          Sales          Incremental
```

The same pipeline can use this configuration to process multiple tables.

---

# 31. Pipeline Retry and Error Handling

Pipelines can be designed to handle failures.

Example:

```text
Copy Activity
      ↓
Success?
   /       \
 Yes        No
 ↓          ↓
Continue   Retry
              ↓
           Failed?
           /    \
         Yes     No
          ↓       ↓
       Alert    Continue
```

Common approaches include:

- Retry
- Failure paths
- Conditional logic
- Logging
- Notifications
- Monitoring

---

# 32. Complete Data Pipeline Example

A real-world customer ingestion pipeline could look like this:

```text
SQL Server
    ↓
Pipeline
    ↓
Lookup Activity
    ↓
Read Watermark
    ↓
Copy Activity
    ↓
Load New / Modified Customers
    ↓
Lakehouse Bronze
    ↓
Notebook Activity
    ↓
Clean + Deduplicate
    ↓
Lakehouse Silver
    ↓
Notebook / Dataflow Gen2
    ↓
Business Transformation
    ↓
Lakehouse Gold
    ↓
Update Watermark
    ↓
Power BI
```

---

# 33. Complete Pipeline Architecture

```text
                         DATA PIPELINE
                              │
        ┌─────────────────────┼──────────────────────┐
        ↓                     ↓                      ↓
 Data Movement         Transformation          Control Flow
        │                     │                      │
 Copy Activity          Notebook Activity       If Condition
                        Dataflow Gen2           Switch
                        Stored Procedure        ForEach
                                                Until
                                                Wait
        │                     │                      │
        └─────────────────────┼──────────────────────┘
                              ↓
                       Metadata / Config
                              │
                    ┌─────────┴─────────┐
                    ↓                   ↓
                 Lookup            Get Metadata
                    │                   │
                    └─────────┬─────────┘
                              ↓
                         Variables
                              │
                    Set / Append Variable
                              ↓
                       Dynamic Content
                              ↓
                         Destination
```

---

# 34. Most Important DP-700 Points

## Data Pipeline

> Used to orchestrate, schedule, automate, and monitor data workflows.

## Copy Activity

> Used primarily to move/copy data from source to destination.

## Notebook Activity

> Executes a Fabric notebook from a pipeline.

## Dataflow Gen2 Activity

> Executes a low-code Power Query-based transformation flow.

## Stored Procedure Activity

> Executes a stored procedure in a supported data source.

## Lookup Activity

> Retrieves data from a supported source for use in subsequent pipeline logic.

## Get Metadata Activity

> Retrieves available metadata about data in a supported data store.

## Set Variable

> Assigns a value to a pipeline variable.

## Append Variable

> Adds a value to an array variable.

## If Condition

> Executes different logic based on a true/false condition.

## Switch

> Selects a path from multiple possible cases.

## ForEach

> Repeats processing for each item in a collection.

## Until

> Repeats activities until a condition becomes true.

## Wait

> Pauses pipeline execution for a specified period.

## Execute Pipeline

> Executes another pipeline.

## Web Activity

> Calls a web endpoint or REST API.

## Parameter

> Input/configuration value supplied to a pipeline.

## Variable

> Runtime value that can be modified during pipeline execution.

## Dynamic Content

> Generates or references values dynamically at runtime.

## Full Load

> Loads the complete dataset.

## Incremental Load

> Loads only new or modified data.

## Watermark

> Stores the last successfully processed value used to identify new or changed records.

## Control Table

> Stores configuration and processing information used by pipelines.

---

# 35. Final Mental Model

Remember the Data Pipeline like this:

```text
                    DATA PIPELINE
                         │
                         ↓
                   ORCHESTRATION
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
   DATA MOVEMENT    TRANSFORMATION    CONTROL FLOW
        │                │                │
 Copy Activity      Notebook          If Condition
                    Dataflow Gen2     Switch
                    Stored Proc       ForEach
                                     Until
                                     Wait
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                   METADATA / CONFIG
                         │
                    Lookup / Metadata
                         ↓
                    Variables
                         ↓
                  Dynamic Content
                         ↓
                     DESTINATION
```

---

# 36. Incremental Load Mental Model

```text
SOURCE
  ↓
Lookup Watermark
  ↓
Read Last Successful Value
  ↓
Copy New / Modified Records
  ↓
Transform
  ↓
Load Destination
  ↓
SUCCESS?
  ↓
YES → Update Watermark
NO  → Keep Old Watermark
```

---

# ⭐ One-Line Memory

```text
Pipeline = Orchestrate

Copy = Move

Notebook = Code Transformation

Dataflow Gen2 = Low-Code Transformation

Lookup = Read Configuration / Watermark

Get Metadata = Read Metadata

Variable = Runtime Value

Parameter = Pipeline Input

Dynamic Content = Runtime Expression

If = Two-Way Decision

Switch = Multiple Choices

ForEach = Repeat for Every Item

Until = Repeat Until Condition

Execute Pipeline = Parent → Child

Full Load = Everything

Incremental Load = Only Changes

Watermark = Last Successfully Processed Value
```