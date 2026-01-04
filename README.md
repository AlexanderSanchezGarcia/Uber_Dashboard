# Uber Analytics Dashboard

A comprehensive interactive web-based analytics dashboard built with **Dash** and **Plotly** to analyze Uber ride data. This project provides visual insights into booking patterns, cancellations, ratings, and ride metrics through an intuitive multi-page interface.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Pages & Visualizations](#pages--visualizations)
- [Data](#data)
- [Technologies](#technologies)
- [Configuration](#configuration)

## ✨ Features

- **Interactive Dashboard**: Multi-page application with dynamic filtering
- **Date Range Filtering**: Analyze data for specific time periods
- **Real-time KPIs**: Key Performance Indicators including total bookings, cancellation rates, and average ratings
- **Comprehensive Visualizations**:
  - Booking status breakdowns
  - Ride volume trends over time
  - Vehicle type analysis
  - Payment method distribution
  - Cancellation reasons and patterns
  - Rating distribution and trends
- **Responsive Design**: Clean, professional UI with sidebar navigation
- **Raw Data Viewer**: Browse complete dataset with filtering capabilities
- **Mobile-Friendly**: Toggleable sidebar for better mobile experience

## 📁 Project Structure

```
Uber_Dashboard/
├── app.py                           # Main Dash application entry point
├── README.md                        # Project documentation
├── requeriments.txt                # Python dependencies
├── Data/
│   └── uber_rides_cleaned.csv      # Dataset with cleaned Uber ride data
├── Assets/
│   └── style.css                   # Custom styling for dashboard
├── Layouts/
│   └── layout.py                   # Page layouts and UI components
├── Callbacks/
│   └── callbacks.py                # Interactive callbacks for dashboard
├── Figures/
│   └── charts.py                   # Chart and visualization functions
└── Utils/
    └── preprocessing.py            # Data loading and preprocessing utilities
```

## 📦 Requirements

- Python 3.7+
- Dash 2.0+
- Plotly
- Pandas
- Gunicorn (for deployment)

## 🚀 Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd Uber_Dashboard
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requeriments.txt
   ```

## 🎯 Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Open in browser**:
   Navigate to `http://127.0.0.1:8050` (default Dash port)

3. **Navigate the dashboard**:
   - Use the sidebar menu to switch between different analysis pages
   - Use date pickers to filter data by time range
   - Hover over charts for detailed information
   - Toggle the sidebar on mobile using the floating button

## 📊 Pages & Visualizations

### 1. **Overall Analysis** (Home)
   - **Total Bookings KPI**: Count of all rides in the selected period
   - **Booking Status Breakdown**: Donut chart showing completed vs. cancelled rides
   - **Ride Volume Over Time**: Line chart tracking bookings trends by month
   - **Vehicle Type Distribution**: Bar chart comparing bookings by vehicle type
   - **Payment Method Analysis**: Bar chart showing payment method preferences

### 2. **Cancellations**
   - **Total Bookings & Cancelled Rides**: Summary KPIs
   - **Cancellation Rate**: Percentage of cancelled bookings
   - **Customer vs. Driver Cancellations**: KPI comparison
   - **Cancellation Reasons**: Breakdown of why rides were cancelled
   - **Cancellations Over Time**: Trend analysis of cancellation frequency
   - **Cancellations by Vehicle Type**: Vehicle-specific cancellation patterns

### 3. **Ratings**
   - **Average Rating KPI**: Overall ride rating metric
   - **Rating Distribution**: Histogram or pie chart of rating categories
   - **Ratings Over Time**: Trend analysis of average ratings
   - **Ratings by Vehicle Type**: Performance comparison across vehicle types
   - **Ratings by Payment Method**: Analysis of ratings by payment type

### 4. **Raw Data**
   - Complete dataset viewer with sortable and filterable columns
   - Download capability for data export
   - Search and filter functionality

## 📈 Data

### Data Source
The dashboard uses `Data/uber_rides_cleaned.csv`, a pre-processed Uber rides dataset containing:

**Key Columns**:
- `Date_Time`: Timestamp of the ride
- `Booking Status`: Completed or Cancelled
- `Vehicle Type`: Type of vehicle (UberX, Uber Black, etc.)
- `Payment Method`: Payment type used
- `Cancellation Reason`: Reason for cancellation (if applicable)
- `Rating`: Passenger rating (1-5 scale)

**Data Processing**:
- Datetime parsing and validation
- Automatic extraction of temporal features (date, hour, weekday, month)
- Date-range filtering for analysis

## 🛠️ Technologies

| Technology | Purpose |
|-----------|---------|
| **Dash** | Web framework for interactive dashboards |
| **Plotly** | Interactive visualization library |
| **Pandas** | Data manipulation and analysis |
| **Python** | Backend programming language |
| **CSS** | Custom styling and responsive design |
| **Gunicorn** | WSGI server for production deployment |

## ⚙️ Configuration

### Modifying Styles
Edit `Assets/style.css` to customize:
- Colors and themes
- Layout spacing and dimensions
- Font sizes and typography
- Responsive breakpoints

### Adding New Visualizations
1. Create chart functions in `Figures/charts.py`
2. Add layout components in `Layouts/layout.py`
3. Register callbacks in `Callbacks/callbacks.py`
4. Update routing in `app.py` if needed

### Extending Filters
Date filters can be easily extended by:
1. Modifying the date range in `Layouts/layout.py`
2. Adding new filter components and callbacks in `Callbacks/callbacks.py`
3. Updating filtering logic in `Utils/preprocessing.py`

## 📝 Notes

- The dashboard expects data in `Data/uber_rides_cleaned.csv`
- Ensure datetime column is named `Date_Time` for proper parsing
- For production deployment, use Gunicorn with a reverse proxy (Nginx/Apache)
- The `suppress_callback_exceptions=True` flag allows multi-page routing

## 🔗 Deployment

To deploy this application:

1. **Using Gunicorn**:
   ```bash
   gunicorn app:server
   ```

2. **Using Docker** (optional):
   Create a Dockerfile and docker-compose configuration for containerized deployment

3. **Cloud Platforms**: Can be deployed to Heroku, AWS, or other cloud services that support Python applications

---

**Created**: January 2026  
**Last Updated**: January 4, 2026