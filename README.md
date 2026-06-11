# Schiphol Airflow BI

ETL Pipeline using Apache Airflow, Python and Power BI with Schiphol Airport API.

---

## Architecture

```
Schiphol API
      │
      ▼
Extract
      │
      ▼
Bronze Layer
      │
      ▼
Transform
      │
      ▼
Silver Layer
      │
      ▼
Load
      │
      ▼
Gold Layer
      │
      ▼
Power BI Dashboard
```

---

## Technologies

- Python
- Apache Airflow
- Docker
- Pandas
- Power BI
- Git
- GitHub

---

## Data Architecture

### Bronze

Raw API data.

### Silver

Cleaned and standardized data.

### Gold

Analytics-ready data.

---

## Project Structure

```
dags/
src/
data/
dashboard/
docs/
```

---

## Dashboard Features

- Total Flights
- Arrivals vs Departures
- Flights by Hour
- Top Airlines
- Flight Status
- Operational Table

---

## Pipeline Flow

```
start
   ↓
extract_flights
   ↓
transform_flights
   ↓
load_gold
   ↓
end
```
