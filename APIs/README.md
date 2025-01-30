# Weather Dashboard for BYU Locations

## Overview
This Streamlit application provides weather insights for various BYU locations. Users can explore weather metrics, compare locations, and visualize key performance indicators (KPIs) and other weather variables. The app integrates with the Open-Meteo Weather API to fetch real-time and historical weather data.

### Features
1. **Single Location Weather:** View temperature data for a selected BYU location.
2. **Compare Locations & KPIs:** Compare weather metrics like temperature across BYU Idaho, BYU Hawaii, and BYU Provo.
3. **Variable Selection & Timezone:** Analyze multiple weather variables (e.g., Temperature, Wind Speed, Relative Humidity) with timezone options.
4. **Summary Metrics Across Cities:** View combined metrics and boxplots for weather variables across cities.

---

## Technologies Used
- **Streamlit**: Frontend interface for interactivity.
- **Polars**: High-performance dataframe library for data manipulation.
- **Requests**: Fetches weather data from the Open-Meteo API.
- **Matplotlib**: Visualizes weather trends and comparisons.

---

## Setup and Installation
Follow the steps below to get the app running locally:

### 1. Prerequisites
Ensure the following are installed:
- Python 3.8 or higher
- pip (Python package manager)

### 2. Clone the Repository
```bash
git clone <repository-link>
cd <repository-folder>
```

### 3. Install Dependencies
Run the following command to install required Python packages:
```bash
pip install -r requirements.txt
```
**Note**: Ensure `streamlit`, `polars`, `matplotlib`, and `requests` are included in your `requirements.txt`.

### 4. Project Directory Structure
The app assumes the following directory structure:
```
project-folder/
|└── APIs/
|└── pages/
|   |└── single_location.py
|   |└── compare_locations.py
|   |└── variable_selection.py
|   |└── summary_metrics.py
|└── screenshots/
|└── utils/
|   |└── weather_api.py
|└── streamlit_app.py
|└── requirements.txt
|└── README.md
|└── docker-compose.yaml
|└── Dockerfile
```

### 5. Run the Application
Launch the app using Streamlit:
```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Usage Instructions
### Sidebar Navigation
The sidebar allows you to navigate between different app sections:
- **Single Location Weather**: Select a BYU location and view temperature data.
- **Compare Locations & KPIs**: Compare weather metrics across multiple locations.
- **Variable Selection & Timezone**: Analyze weather variables like temperature, wind speed, and humidity.
- **Summary Metrics Across Cities**: View combined metrics and visualizations.

### Input Parameters
- **Date Range**: Select a start and end date for fetching weather data.
- **Locations**: Choose from predefined BYU locations (Provo, Hawaii, Idaho).
- **Timezone Selection**: For variable analysis, choose between `America/Denver` or `Pacific/Honolulu`.

---

## API Details
- **Source**: [Open-Meteo API](https://open-meteo.com/)
- **Endpoint**: `https://api.open-meteo.com/v1/forecast`
- **Variables Supported**: Temperature, Wind Speed, Relative Humidity

---

## Screenshots
### Single Location Weather
![Single Location](screenshots/single_location.png)

### Compare Locations
![Compare Locations](screenshots/compare_locations.png)

### Variable Selection
![Variable Selection](screenshots/variable_selection.png)

### Summary Metrics
![Summary Metrics](screenshots/summary_metrics.png)

---

## Author
Christian Landaverde

---

## Acknowledgements
- Open-Meteo API for weather data.
- Streamlit for the interactive dashboard.
