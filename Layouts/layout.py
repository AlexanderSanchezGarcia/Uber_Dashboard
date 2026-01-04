from dash import html, dcc, dash_table

def create_overall_analysis_content():
    return html.Div([
        # Top section with header and controls
        html.Div([
            # Left: Header with logo and title
            html.Div([
                html.Div([
                    html.Img(src="/assets/uber_logo.png", className="header-logo"),
                    html.Div([
                        html.H1("Uber Analytics Dashboard", className="title"),
                        html.H2("Overall Analysis", className="subtitle")
                    ], className="title-container")
                ], className="header-container"),
            ], className="header-section"),
            
            # Right: Filters and KPI
            html.Div([
                html.Div([
                    dcc.DatePickerRange(
                        id="date-filter",
                        start_date="2024-01-01",
                        end_date="2024-12-31",
                        min_date_allowed="2024-01-01",
                        max_date_allowed="2024-12-31",
                        start_date_placeholder_text="Start Date",
                        end_date_placeholder_text="End Date"
                    )
                ], className="filter-container"),
                
                html.Div([
                    html.Div([
                        html.H4("Total Bookings"),
                        html.H2(id="total-bookings")
                    ], className="kpi-card")
                ], className="kpi-container")
            ], className="controls-container")
        ], className="top-section"),

        # Charts Row 1
        html.Div([
            dcc.Graph(id="booking-status-pie"),
            dcc.Graph(id="rides-over-time")
        ], className="chart-row"),

        # Charts Row 2
        html.Div([
            dcc.Graph(id="vehicle-type-bar"),
            dcc.Graph(id="payment-method-bar")
        ], className="chart-row")
    ], className="page-content")

def create_cancellations_content():
    return html.Div([
        # Top section with header and controls
        html.Div([
            # Left: Header with logo and title
            html.Div([
                html.Div([
                    html.Img(src="/assets/uber_logo.png", className="header-logo"),
                    html.Div([
                        html.H1("Uber Analytics Dashboard", className="title"),
                        html.H2("Cancellations", className="subtitle")
                    ], className="title-container")
                ], className="header-container"),
            ], className="header-section"),
            
            # Right: Filters and KPIs
            html.Div([
                html.Div([
                    dcc.DatePickerRange(
                        id="cancellation-date-filter",
                        start_date="2024-01-01",
                        end_date="2024-12-31",
                        min_date_allowed="2024-01-01",
                        max_date_allowed="2024-12-31",
                        start_date_placeholder_text="Start Date",
                        end_date_placeholder_text="End Date"
                    )
                ], className="filter-container"),
                
                html.Div([
                    html.Div([
                        html.H4("Total Bookings"),
                        html.H2(id="cancellation-total-bookings")
                    ], className="kpi-card"),
                    html.Div([
                        html.H4("Cancelled Bookings"),
                        html.H2(id="total-cancellations")
                    ], className="kpi-card"),
                    html.Div([
                        html.H4("Cancellation Rate"),
                        html.H2(id="cancellation-rate")
                    ], className="kpi-card"),
                    html.Div([
                        html.H4("Customer Cancellations"),
                        html.H2(id="customer-cancellations-kpi")
                    ], className="kpi-card"),
                    html.Div([
                        html.H4("Driver Cancellations"),
                        html.H2(id="driver-cancellations-kpi")
                    ], className="kpi-card")
                ], className="kpi-container")
            ], className="controls-container")
        ], className="top-section"),

        # Charts Row 1
        html.Div([
            dcc.Graph(id="cancelled-by-customers-pie"),
            dcc.Graph(id="cancelled-by-drivers-pie")
        ], className="chart-row")
    ], className="page-content")

def create_ratings_content():
    return html.Div([
        # Top section with header and controls
        html.Div([
            # Left: Header with logo and title
            html.Div([
                html.Div([
                    html.Img(src="/assets/uber_logo.png", className="header-logo"),
                    html.Div([
                        html.H1("Uber Analytics Dashboard", className="title"),
                        html.H2("Ratings", className="subtitle")
                    ], className="title-container")
                ], className="header-container"),
            ], className="header-section"),
            
            # Right: Filters and KPIs
            html.Div([
                html.Div([
                    dcc.DatePickerRange(
                        id="ratings-date-filter",
                        start_date="2024-01-01",
                        end_date="2024-12-31",
                        min_date_allowed="2024-01-01",
                        max_date_allowed="2024-12-31",
                        start_date_placeholder_text="Start Date",
                        end_date_placeholder_text="End Date"
                    )
                ], className="filter-container"),
                
                html.Div([
                    html.Div([
                        html.H4("Average Rating"),
                        html.H2(id="avg-rating")
                    ], className="kpi-card"),
                    html.Div([
                        html.H4("5-Star Ratings"),
                        html.H2(id="five-star-count")
                    ], className="kpi-card"),
                    html.Div([
                        html.H4("Total Revenue"),
                        html.H2(id="total-revenue")
                    ], className="kpi-card")
                ], className="kpi-container")
            ], className="controls-container")
        ], className="top-section"),

        # Charts Row 1
        html.Div([
            dcc.Graph(id="rating-distribution"),
            dcc.Graph(id="ratings-by-vehicle-type")
        ], className="chart-row"),

        # Charts Row 2
        html.Div([
            dcc.Graph(id="revenue-over-time")
        ], className="chart-row"),
        
        # Top 5 Customers Table
        html.Div([
            html.H3("Top 5 Customers by Bookings", style={"marginBottom": "20px"}),
            dash_table.DataTable(
                id="top-customers-table",
                style_cell={'textAlign': 'left', 'padding': '10px'},
                style_header={'backgroundColor': '#2a2a2a', 'color': 'white', 'fontWeight': 'bold'},
                style_data={'backgroundColor': '#f4f4f4'}
            )
        ], className="table-container")
    ], className="page-content")

def create_raw_data_content():
    return html.Div([
        # Top section with header and controls
        html.Div([
            # Left: Header with logo and title
            html.Div([
                html.Div([
                    html.Img(src="/assets/uber_logo.png", className="header-logo"),
                    html.Div([
                        html.H1("Uber Analytics Dashboard", className="title"),
                        html.H2("Raw Data", className="subtitle")
                    ], className="title-container")
                ], className="header-container"),
            ], className="header-section"),
            
            # Right: Filters and KPI
            html.Div([
                html.Div([
                    dcc.DatePickerRange(
                        id="rawdata-date-filter",
                        start_date="2024-01-01",
                        end_date="2024-01-31",
                        min_date_allowed="2024-01-01",
                        max_date_allowed="2024-12-31",
                        start_date_placeholder_text="Start Date",
                        end_date_placeholder_text="End Date"
                    )
                ], className="filter-container"),
                
                html.Div([
                    html.Div([
                        html.H4("Total Records"),
                        html.H2(id="total-records")
                    ], className="kpi-card")
                ], className="kpi-container")
            ], className="controls-container")
        ], className="top-section"),
        
        # Data Table
        html.Div([
            dash_table.DataTable(
                id="raw-data-table",
                style_cell={'textAlign': 'left', 'padding': '10px'},
                style_header={'backgroundColor': '#2a2a2a', 'color': 'white', 'fontWeight': 'bold'},
                style_data={'backgroundColor': '#f4f4f4'},
                page_size=20
            )
        ], className="table-container")
    ], className="page-content")

def create_layout():
    return html.Div([
        dcc.Location(id="url", refresh=False),
        
        # Sidebar
        html.Div([
            html.Div([
                html.Button("☰", id="sidebar-toggle-btn", className="sidebar-toggle-btn"),
                html.H3("Navigation", className="sidebar-title")
            ], className="sidebar-header"),
            
            html.Div([
                dcc.Link(html.Button("Overall Analysis", className="sidebar-btn"), href="/"),
                dcc.Link(html.Button("Cancellations", className="sidebar-btn"), href="/cancellations"),
                dcc.Link(html.Button("Ratings", className="sidebar-btn"), href="/ratings"),
                dcc.Link(html.Button("Raw Data", className="sidebar-btn"), href="/raw-data")
            ], className="sidebar-buttons")
        ], id="sidebar", className="sidebar open"),
        
        # Main content
        html.Div([
            html.Button("☰", id="floating-toggle-btn", className="floating-toggle-btn", style={"display": "none"}),
            html.Div(id="page-content", className="dashboard-container")
        ], className="main-content")
    ], className="app-container")