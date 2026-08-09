\# Incremental Data Pipeline 



\## Project Overview



This project demonstrates a parameterized and scheduled data ingestion pipeline built using Microsoft Fabric.



The first milestone focuses on loading order data from a CSV file stored in a Fabric Lakehouse into a Lakehouse table.



The pipeline is designed to be reusable by using a pipeline parameter and Dynamic Content for the source file path.



\---



\## Architecture



```text

Fabric Lakehouse

│

├── Files

│   └── orders.csv

│

│        ↓

│

│   Copy Data Activity

│

│        ↓

│

└── Tables

&#x20;   └── dbo.orders\_incremental

