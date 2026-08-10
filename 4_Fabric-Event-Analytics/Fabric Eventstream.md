# Microsoft Fabric Eventstream — Interview & DP-700 Notes

---

# 1. What is Eventstream?

**Eventstream** is a real-time data ingestion and processing capability in Microsoft Fabric.

It allows you to:

- Ingest streaming events
- Transform streaming data
- Filter events
- Aggregate events
- Route events
- Send processed events to destinations

### Basic Flow

```text
Source
   ↓
Eventstream
   ↓
Transform / Filter / Aggregate
   ↓
Destination
```

### Important

Eventstream is mainly used for **real-time event ingestion and processing**.

---

# 2. Eventstream Architecture

```text
                    EVENTSTREAM
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Source 1       Source 2       Source 3
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  Event Processing
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Filter         Aggregate      Manage Fields
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  Derived Stream
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Eventhouse      Lakehouse      Other Destination
```

---

# 3. Sources

A source is where streaming events originate.

Common Eventstream sources can include:

- Azure Event Hubs
- Azure IoT Hub
- Apache Kafka
- Azure Service Bus
- Fabric events
- Sample data
- Custom applications
- Other supported real-time event sources

### Purpose

Sources continuously produce or provide events to Eventstream.

Examples:

```text
IoT Device
    ↓
Eventstream
```

```text
Website Clicks
    ↓
Eventstream
```

```text
Application Logs
    ↓
Eventstream
```

---

# 4. Event

An event is an individual piece of streaming data.

Example:

```json
{
  "DeviceId": 1001,
  "Temperature": 30,
  "Timestamp": "2026-08-10T10:00:00"
}
```

Another event may arrive:

```json
{
  "DeviceId": 1002,
  "Temperature": 35,
  "Timestamp": "2026-08-10T10:00:05"
}
```

A continuous stream is simply a continuous sequence of events.

---

# 5. Event Processing

Event processing allows streaming data to be transformed before it reaches a destination.

Common transformations include:

- Manage Fields
- Filter
- Aggregate
- Group By
- Join
- Union
- Expand
- Derived Stream

---

# 6. Manage Fields

Manage Fields is used to modify the fields of incoming events.

Common operations include:

- Select fields
- Remove fields
- Rename fields

Example:

Input:

```text
DeviceId | Temp | Humidity
```

Rename:

```text
Temp → Temperature
```

Output:

```text
DeviceId | Temperature | Humidity
```

---

# 7. Filter

Filter keeps only events that satisfy a condition.

Example:

```text
Temperature > 50
```

Input:

```text
Temperature
30
55
70
40
```

Output:

```text
55
70
```

### Common Uses

- Remove unwanted events
- Filter invalid records
- Process only high-value events
- Create alert streams

---

# 8. Aggregate

Aggregate performs calculations over streaming data.

Common functions include:

- Count
- Sum
- Average
- Minimum
- Maximum

Example:

```text
Average Temperature
per 5-minute window
```

```text
Events
   ↓
5 Minute Window
   ↓
Average Temperature
```

Aggregation generally works together with **windowing** when calculating metrics over a continuous stream.

---

# 9. Group By

Group By groups streaming events based on one or more fields.

Example:

```text
Count Orders by Region
```

Input:

```text
Region
North
South
North
East
South
```

Result:

```text
North → 2
South → 2
East  → 1
```

Group By is commonly used with aggregations.

---

# 10. Join

Join combines related data from two streams or supported data sources based on matching fields.

Example:

```text
Order Stream
     +
Customer Stream
     ↓
Combined Result
```

Example:

```text
Order.CustomerID = Customer.CustomerID
```

Use cases:

- Enrich events
- Combine related event information
- Add customer information to orders

---

# 11. Union

Union combines multiple streams with compatible schemas into one stream.

Example:

```text
Region A Stream
       +
Region B Stream
       +
Region C Stream
       ↓
Combined Stream
```

### Important

Union combines streams; it does not match records like a Join.

---

# 12. Expand

Expand is used to flatten nested or array data structures where supported.

Example input:

```json
{
  "Device": {
    "Id": 1001,
    "Temperature": 28
  }
}
```

After expansion, fields can be exposed as separate fields such as:

```text
Device.Id
Device.Temperature
```

This makes nested data easier to process.

---

# 13. Derived Stream

A Derived Stream is a new stream created from processed event data.

Example:

```text
Source
   ↓
Filter
   ↓
Derived Stream
```

A derived stream can be used as a reusable output for downstream processing or destinations.

Example:

```text
Source
   ↓
Filter
   ↓
Derived Stream
      ├── Eventhouse
      └── Lakehouse
```

### Important

A derived stream represents the output of processing and can help route transformed data to multiple destinations.

---

# 14. Windowing

Streaming data is continuous and does not naturally have a beginning or end.

**Windowing** creates a time boundary so that operations such as counting, summing, and averaging can be performed over a defined period.

Example:

```text
Continuous Stream
       ↓
Window
       ↓
Aggregation
```

Common window types include:

- Tumbling Window
- Hopping / Sliding Window
- Session Window

---

# 15. Tumbling Window

A Tumbling Window divides events into **fixed-size, non-overlapping time periods**.

Example:

```text
10:00 - 10:05
10:05 - 10:10
10:10 - 10:15
```

### Characteristics

- Fixed duration
- No overlap
- Each event belongs to one window

### Use Cases

- Sales count every 5 minutes
- Orders per hour
- Number of events per minute

### Easy Memory

```text
Tumbling = Fixed + No Overlap
```

---

# 16. Hopping / Sliding Window

A Hopping Window uses a fixed window size but moves forward by a smaller hop/slide interval, causing overlap.

Example:

```text
Window Size = 10 minutes
Hop = 5 minutes

10:00 - 10:10
10:05 - 10:15
10:10 - 10:20
```

### Characteristics

- Fixed-size window
- Overlapping windows
- Events may belong to multiple windows

### Use Cases

- Rolling averages
- Trend analysis
- Monitoring
- Moving metrics

### Easy Memory

```text
Hopping = Fixed + Overlap
```

---

# 17. Session Window

A Session Window groups events based on periods of user activity.

The session closes when there is no activity for a configured period.

Example:

```text
10:00 Click
10:01 Click
10:03 Click

No activity
      ↓
Session closes

10:35 Click
```

Result:

```text
Session 1
10:00 - 10:03

Session 2
10:35
```

### Use Cases

- User activity tracking
- Website analytics
- Customer journeys
- Application sessions

### Easy Memory

```text
Session = Activity + Inactivity Gap
```

---

# 18. Window Comparison

| Window | Overlap | Main Use |
|---|---|---|
| Tumbling | No | Fixed-period aggregation |
| Hopping / Sliding | Yes | Rolling / trend analysis |
| Session | Activity-based | User sessions |

### Important DP-700 Memory

```text
Tumbling → Fixed + Non-overlapping

Hopping → Fixed + Overlapping

Session → Activity + Inactivity
```

---

# 19. Destinations

A destination defines where Eventstream sends processed events.

Depending on the Eventstream configuration and supported destinations, streaming data can be routed to destinations such as:

- Eventhouse
- Lakehouse
- Activator
- Custom endpoints
- Other supported Fabric destinations

---

# 20. Eventhouse

Eventhouse is designed for storing and analyzing large volumes of real-time event data.

It is commonly used for:

- Log Analytics
- Monitoring
- Telemetry
- Clickstream Analysis
- Real-Time Analytics

It uses **KQL databases**.

### Example

```text
Eventstream
    ↓
Eventhouse
    ↓
KQL Database
    ↓
KQL Query
```

### Best For

```text
Real-Time Analytics
Operational Monitoring
Telemetry
Logs
Events
```

---

# 21. Lakehouse Destination

A Lakehouse can be used as a destination for streaming data.

It is useful for:

- Long-term storage
- Historical analysis
- Data Engineering
- BI
- Data Science
- Combining streaming and batch data

Example:

```text
Eventstream
     ↓
Lakehouse
     ↓
Delta Tables
     ↓
Historical Analytics
```

---

# 22. Activator

Activator is used to detect conditions in data and trigger actions.

Example:

```text
Temperature > 80
       ↓
Condition Detected
       ↓
Activator
       ↓
Action
```

Possible actions can include supported notifications or workflow actions.

### Example

```text
Temperature > 80
       ↓
Trigger Alert
       ↓
Notify Team
```

---

# 23. Custom Endpoint

A custom endpoint can be used to send streaming data to an external system or application through a supported endpoint.

Example:

```text
Eventstream
    ↓
Custom Endpoint
    ↓
External Application
```

Use cases:

- External applications
- Custom processing systems
- Third-party integrations

---

# 24. Eventhouse vs Lakehouse

## Eventhouse

Used mainly for:

- Real-time analytics
- Event monitoring
- Logs
- Telemetry
- High-volume event analysis

Query Language:

```text
KQL
```

Examples:

```text
Application Logs
Website Clicks
IoT Telemetry
Security Events
```

---

## Lakehouse

Used mainly for:

- Historical analytics
- Data Engineering
- Reporting
- Data Science
- Long-term analytical storage

Common technologies:

```text
SQL
PySpark
Spark SQL
```

Examples:

```text
Sales Analytics
Customer Analytics
Business Reporting
Historical Data
```

### Easy Memory

```text
Eventhouse → Real-Time + KQL

Lakehouse  → Historical + Spark / SQL
```

---

# 25. Checkpointing

Checkpointing stores processing progress so a streaming workload can recover after a failure.

Conceptually:

```text
Process Events
      ↓
Checkpoint
      ↓
More Events
      ↓
Failure
      ↓
Restart
      ↓
Recover Processing State
```

### Benefits

- Fault tolerance
- Recovery
- Maintaining processing state
- Reducing unnecessary reprocessing

### Important

Checkpointing is primarily a **stream-processing reliability concept**. Do not treat it as simply "a location where all streaming data is stored."

---

# 26. Late-Arriving Events

An event may arrive later than the time at which it was generated.

Example:

```text
Event Time:   10:00 AM
Arrival Time: 10:05 AM
```

Streaming systems may use **event time** and windowing/watermark concepts to handle events that arrive later than expected.

### Important Terms

```text
Event Time
    ↓
When the event actually happened

Arrival / Processing Time
    ↓
When the system receives/processes it
```

Late-arriving event handling depends on the streaming engine and configuration.

---

# 27. Schema

Schema defines the structure of event data.

Example:

```json
{
  "DeviceId": 1001,
  "Temperature": 30,
  "Timestamp": "2026-08-10T10:00:00"
}
```

Schema describes:

```text
DeviceId    → Integer
Temperature → Number
Timestamp   → DateTime
```

### Benefits

- Consistent structure
- Easier processing
- Easier querying
- Better data quality
- Easier downstream analytics

---

# 28. Real-Time vs Batch Processing

## Real-Time Processing

Data is processed continuously or with very low latency as events arrive.

Examples:

- Fraud Detection
- IoT Monitoring
- Live Dashboards
- Alerting
- Application Monitoring
- Real-Time Recommendations

```text
Event
 ↓
Process Immediately
 ↓
Action / Analytics
```

---

## Batch Processing

Data is collected and processed periodically.

Examples:

- Daily Data Loads
- Monthly Reporting
- Payroll Processing
- Scheduled ETL

```text
Data
 ↓
Collect
 ↓
Wait
 ↓
Process Batch
```

---

# 29. KQL vs SQL vs PySpark

## SQL

Used for:

- Structured data
- Relational queries
- Lakehouse tables
- Warehouses
- BI workloads

Example:

```sql
SELECT *
FROM Sales;
```

---

## KQL

KQL stands for **Kusto Query Language**.

Used mainly for:

- Logs
- Telemetry
- Events
- Monitoring
- Real-time analytics

Example:

```kusto
Events
| summarize count()
```

---

## PySpark

Used for:

- Large-scale data processing
- ETL / ELT
- Complex transformations
- Data Engineering
- Data Science / ML workloads

Example:

```python
df = spark.read.parquet("Files/sales.parquet")
```

### Easy Memory

```text
SQL     → Structured / Relational Analytics

KQL     → Logs / Events / Real-Time Analytics

PySpark → Large-Scale Data Processing
```

---

# 30. Typical Real-Time Analytics Architecture

## Eventhouse Architecture

```text
IoT Devices / Applications / Kafka
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
                 ↓
              Power BI
```

---

# 31. Eventstream → Lakehouse Architecture

```text
IoT Devices / Applications
            ↓
        Eventstream
            ↓
      Filter / Transform
            ↓
         Lakehouse
            ↓
       Delta Tables
            ↓
    Historical Analytics
            ↓
          Power BI
```

---

# 32. Multiple Destinations

One Eventstream can route processed events to multiple destinations.

Example:

```text
                    Eventstream
                         ↓
                  Event Processing
                         ↓
                   Derived Stream
                    /          \
                   /            \
                  ↓              ↓
            Eventhouse        Lakehouse
                  ↓              ↓
               KQL          Historical Data
```

### Use Case

The same events can be used for:

- Real-time monitoring in Eventhouse
- Long-term analytics in Lakehouse

---

# 33. Eventstream vs Eventhouse

These are different.

## Eventstream

Responsible mainly for:

```text
Ingest
  ↓
Transform
  ↓
Route
```

## Eventhouse

Responsible mainly for:

```text
Store
  ↓
Query
  ↓
Analyze
```

### Easy Memory

```text
Eventstream → Move + Process

Eventhouse  → Store + Analyze
```

---

# 34. Eventstream vs Data Pipeline

Another important distinction.

## Data Pipeline

Primarily used for:

- Batch data movement
- Orchestration
- Scheduling
- Workflow automation

```text
Pipeline
   ↓
Copy
   ↓
Transform
   ↓
Load
```

## Eventstream

Primarily used for:

- Continuous event ingestion
- Real-time processing
- Event routing

```text
Events
  ↓
Eventstream
  ↓
Process
  ↓
Destination
```

### Easy Memory

```text
Pipeline   → Batch / Orchestration

Eventstream → Real-Time / Streaming
```

---

# 35. Important DP-700 Concepts

## Eventstream

> Real-time ingestion, transformation, and routing of streaming events.

## Source

> Origin of streaming events.

## Event

> Individual piece of streaming data.

## Event Processor

> Processes and transforms streaming events.

## Filter

> Keeps events that satisfy a condition.

## Aggregate

> Calculates metrics such as count, sum, average, min, and max over event data.

## Group By

> Groups events by one or more fields for processing or aggregation.

## Join

> Combines related data based on matching fields.

## Union

> Combines compatible streams into one stream.

## Derived Stream

> A processed stream created from an Eventstream transformation flow.

## Tumbling Window

> Fixed-size, non-overlapping window.

## Hopping Window

> Fixed-size, overlapping window that advances by a hop interval.

## Session Window

> Groups events based on activity separated by an inactivity gap.

## Eventhouse

> Real-time analytical store optimized for event data and queried using KQL.

## Lakehouse

> Analytical storage system for engineering, historical analytics, and BI workloads.

## Activator

> Detects conditions and triggers supported actions.

## Checkpointing

> Maintains processing state/progress to support recovery.

## Late Event

> An event that arrives after its event-time window or expected arrival point.

---

# 36. Final Mental Model

```text
                     REAL-TIME SOURCE
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
      Event Hubs         Kafka          IoT / Apps
          │                │                │
          └────────────────┼────────────────┘
                           ↓
                       EVENTSTREAM
                           │
                           ↓
                 EVENT PROCESSING
                           │
       ┌───────────────────┼───────────────────┐
       ↓                   ↓                   ↓
     Filter             Aggregate         Manage Fields
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ↓
                    Derived Stream
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
         Eventhouse     Lakehouse     Activator
              ↓            ↓
             KQL        Delta Tables
              ↓            ↓
       Real-Time       Historical
        Analytics       Analytics
```

---

# ⭐ One-Line Memory

```text
Source → Eventstream → Transform → Derived Stream → Destination
```

```text
Eventstream → Ingest + Process + Route

Eventhouse  → Real-Time Store + KQL

Lakehouse   → Historical / Analytical Storage

Tumbling    → Fixed + No Overlap

Hopping     → Fixed + Overlap

Session     → Activity + Inactivity Gap

Filter      → Keep Matching Events

Aggregate   → Calculate Metrics

Group By    → Group Events

Join        → Combine Related Data

Union       → Combine Compatible Streams

Checkpoint  → Recovery / Processing State

KQL         → Real-Time Event Analytics
```