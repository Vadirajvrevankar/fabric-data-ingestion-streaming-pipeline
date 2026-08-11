# Real-Time Data Streaming with Microsoft Fabric

## Overview

Built a real-time streaming pipeline using **Python and Microsoft Fabric Eventstream**.

Python generates simulated meter data and sends it to a **Fabric Custom Endpoint** using SAS authentication. The data is ingested into Eventstream and processed using the **Manage Fields** transformation.

## Architecture

Python → Fabric Custom Endpoint → Eventstream → Manage Fields → Output

## Technologies

- Python
- Microsoft Fabric Eventstream
- Fabric Custom Endpoint
- Azure Event Hubs SDK
- SAS Authentication

## Implemented

- ✅ Python real-time event producer
- ✅ Fabric Custom Endpoint
- ✅ Real-time Eventstream ingestion
- ✅ Manage Fields transformation

## Screenshots

### Eventstream Input
![Eventstream Input](images/Eventstream_Input.png)

### Manage Fields Output
![Manage Fields Output](images/Manage_Fields_Output.png)