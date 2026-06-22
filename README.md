# Fuel Price ETL Pipeline with Apache Airflow

This project is an end-to-end ETL pipeline built using Apache Airflow and PostgreSQL.

The pipeline extracts gas price data from an external API, transform the data into a
structured format, and load it into a PostgreSQL database for analysis and reporting.

## Architecture

External API
|
v
Extract Task
|
v
Transform Task
|
v
Load Task
|
v
PostgreSQL

The Airflow DAG orchestrates the workflow:

extract -> transform -> load

## Setup

### Clone Repository

```bash
git clone https://github.com/sirsona/gas-price-etl.git

cd gas-price-etl
```

### Create Environment

`uv sync`

### Configure Environment Variables

Create a `.env` file:

```bash
API_KEY=your_api_key
API_URL=your_api_url

DB_HOST=localhost
DB_PORT=5432
DB_NAME=gasprice
DB_USER=postgres
DB_PASSWORD=password
```

### Initialize Airflow

`airflow standalone`

### Run The DAG

1. Open Airflow UI
2. Enable the DAG
3. Trigger a DAG run
