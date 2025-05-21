# Solar Data Explorer Dashboard

A Streamlit-based interactive dashboard for exploring and comparing solar potential across Benin, Sierra Leone, and Togo. The dashboard provides comprehensive visualizations and statistical analysis of key solar metrics including GHI (Global Horizontal Irradiance), DNI (Direct Normal Irradiance), and DHI (Diffuse Horizontal Irradiance).

## Features

- **Interactive Country Selection**: Compare solar data across multiple countries simultaneously
- **Multiple Visualization Types**:
  - Box plots showing distribution of solar metrics
  - Maps for geographical comparison
  - Bar charts for metric ranking
  - Statistical summary tables
- **Dynamic Metric Selection**: Switch between GHI, DNI, and DHI metrics
- **Responsive Design**: Clean, card-based layout with consistent color themes
- **Real-time Updates**: All visualizations update automatically based on user selections

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Setup

1. Clone the repository:
```bash
git clone https://github.com/shaloms4/solar-challenge-week1
cd solar-challenge-week1
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix/MacOS
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
cd app
streamlit run main.py
```

2. The dashboard will open in your default web browser at `http://localhost:8501`

3. Using the Dashboard:
   - Use the sidebar to select countries for comparison
   - Choose a solar metric (GHI, DNI, or DHI) to visualize
   - Interact with the visualizations:
     - Use the toolbar to zoom or download plots
     - Click on legend items to show/hide specific data series

## Development Process

1. **Data Processing**:
   - Clean and preprocess country-specific solar data

2. **Visualization Development**:
   - Create consistent color themes and styling
   - Implement interactive plots using Plotly
   - Add responsive layout with Streamlit containers

3. **User Interface**:
   - Design intuitive sidebar controls
   - Implement card-based layout for visualizations


