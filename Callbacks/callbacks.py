from dash import Input, Output, State
from Utils.preprocessing import load_data, filter_data
from Figures.charts import (
    total_bookings,
    booking_status_pie,
    rides_over_time,
    vehicle_type_bar,
    payment_method_bar
)

df = load_data()

def register_callbacks(app):

    @app.callback(
        Output("sidebar", "className"),
        Output("floating-toggle-btn", "style"),
        Input("sidebar-toggle-btn", "n_clicks"),
        Input("floating-toggle-btn", "n_clicks"),
        State("sidebar", "className"),
        prevent_initial_call=True
    )
    def toggle_sidebar(sidebar_n_clicks, float_n_clicks, current_class):
        # Total clicks from both buttons
        total_clicks = (sidebar_n_clicks or 0) + (float_n_clicks or 0)
        
        # Determine if sidebar should be open (odd clicks = open)
        if total_clicks % 2 == 1:
            # Sidebar is open, hide floating button
            return "sidebar open", {"display": "none"}
        else:
            # Sidebar is closed, show floating button
            return "sidebar", {"display": "block"}

    @app.callback(
        Output("total-bookings", "children"),
        Output("booking-status-pie", "figure"),
        Output("rides-over-time", "figure"),
        Output("vehicle-type-bar", "figure"),
        Output("payment-method-bar", "figure"),
        Input("date-filter", "start_date"),
        Input("date-filter", "end_date"),
        Input("url", "pathname")
    )
    def update_dashboard(start_date, end_date, pathname):
        # Only update when on the Overall Analysis page
        if pathname != "/" and pathname != "":
            return tuple([None] * 5)

        filtered = filter_data(df, start_date, end_date)

        return (
            total_bookings(filtered),
            booking_status_pie(filtered),
            rides_over_time(filtered),
            vehicle_type_bar(filtered),
            payment_method_bar(filtered)
        )

    @app.callback(
        Output("cancellation-total-bookings", "children"),
        Output("total-cancellations", "children"),
        Output("cancellation-rate", "children"),
        Output("customer-cancellations-kpi", "children"),
        Output("driver-cancellations-kpi", "children"),
        Output("cancelled-by-customers-pie", "figure"),
        Output("cancelled-by-drivers-pie", "figure"),
        Input("cancellation-date-filter", "start_date"),
        Input("cancellation-date-filter", "end_date"),
        Input("url", "pathname")
    )
    def update_cancellations(start_date, end_date, pathname):
        import plotly.express as px
        
        # Only update when on the Cancellations page
        if pathname != "/cancellations":
            return tuple([None] * 7)

        filtered = filter_data(df, start_date, end_date)
        
        total_bookings_count = len(filtered)
        
        # Count cancellations
        customer_cancelled = filtered["Cancelled Rides by Customer"].sum() if "Cancelled Rides by Customer" in filtered.columns else 0
        driver_cancelled = filtered["Cancelled Rides by Driver"].sum() if "Cancelled Rides by Driver" in filtered.columns else 0
        total_cancelled = customer_cancelled + driver_cancelled
        
        cancellation_rate = (total_cancelled / total_bookings_count * 100) if total_bookings_count > 0 else 0
        
        # Pie chart for customer cancellations
        customer_cancel_count = int(customer_cancelled)
        customer_complete = total_bookings_count - customer_cancel_count
        fig_customer = px.pie(
            values=[customer_complete, customer_cancel_count],
            names=["Completed", "Cancelled by Customer"],
            title="Cancelled Rides by Customers",
            color_discrete_sequence=["#4CAF50", "#FF6B6B"]
        )
        
        # Pie chart for driver cancellations
        driver_cancel_count = int(driver_cancelled)
        driver_complete = total_bookings_count - driver_cancel_count
        fig_driver = px.pie(
            values=[driver_complete, driver_cancel_count],
            names=["Completed", "Cancelled by Driver"],
            title="Cancelled Rides by Drivers",
            color_discrete_sequence=["#4CAF50", "#FF9800"]
        )
        
        # Reasons chart (placeholder - will need actual reason data)
        fig_reasons = {}
        fig_timeline = {}
        
        return (
            f"{total_bookings_count:,.0f}",
            f"{int(total_cancelled):,.0f}",
            f"{cancellation_rate:.1f}%",
            f"{customer_cancel_count:,.0f}",
            f"{driver_cancel_count:,.0f}",
            fig_customer,
            fig_driver
        )

    @app.callback(
        Output("total-records", "children"),
        Output("raw-data-table", "data"),
        Output("raw-data-table", "columns"),
        Input("rawdata-date-filter", "start_date"),
        Input("rawdata-date-filter", "end_date"),
        Input("url", "pathname")
    )
    def update_raw_data(start_date, end_date, pathname):
        # Only update when on the Raw Data page
        if pathname != "/raw-data":
            return None, [], []

        filtered = filter_data(df, start_date, end_date)
        
        # Prepare table data
        table_data = filtered.to_dict('records')
        columns = [{"name": i, "id": i} for i in filtered.columns]
        
        return f"{len(filtered):,.0f}", table_data, columns

    @app.callback(
        Output("avg-rating", "children"),
        Output("five-star-count", "children"),
        Output("total-revenue", "children"),
        Output("rating-distribution", "figure"),
        Output("ratings-by-vehicle-type", "figure"),
        Output("revenue-over-time", "figure"),
        Output("top-customers-table", "data"),
        Output("top-customers-table", "columns"),
        Input("ratings-date-filter", "start_date"),
        Input("ratings-date-filter", "end_date"),
        Input("url", "pathname")
    )
    def update_ratings(start_date, end_date, pathname):
        import plotly.express as px
        
        # Only update when on the Ratings page
        if pathname != "/ratings":
            return tuple([None] * 8)

        filtered = filter_data(df, start_date, end_date)
        
        # Calculate KPIs
        avg_rating = filtered["Customer Rating"].mean() if "Customer Rating" in filtered.columns else 0
        five_star_count = len(filtered[filtered["Customer Rating"] == 5]) if "Customer Rating" in filtered.columns else 0
        total_revenue = filtered["Booking Value"].sum() if "Booking Value" in filtered.columns else 0
        
        # Rating distribution chart
        rating_dist = filtered["Customer Rating"].value_counts().sort_index() if "Customer Rating" in filtered.columns else {}
        fig_rating_dist = px.bar(
            x=rating_dist.index,
            y=rating_dist.values,
            title="Rating Distribution",
            labels={"x": "Rating", "y": "Count"},
            color_discrete_sequence=["#2196F3"]
        ) if len(rating_dist) > 0 else {}
        
        # Ratings by vehicle type
        if "Vehicle Type" in filtered.columns and "Customer Rating" in filtered.columns:
            rating_by_vehicle = filtered.groupby("Vehicle Type")["Customer Rating"].mean().reset_index()
            fig_by_vehicle = px.bar(
                rating_by_vehicle,
                x="Vehicle Type",
                y="Customer Rating",
                title="Average Ratings by Vehicle Type",
                color_discrete_sequence=["#4CAF50"]
            )
        else:
            fig_by_vehicle = {}
        
        # Revenue over time
        if "Datetime" in filtered.columns and "Booking Value" in filtered.columns:
            filtered_copy = filtered.copy()
            filtered_copy["Date"] = filtered_copy["Datetime"].dt.date
            revenue_daily = filtered_copy.groupby("Date")["Booking Value"].sum().reset_index()
            fig_revenue = px.line(
                revenue_daily,
                x="Date",
                y="Booking Value",
                title="Revenue Over Time",
                markers=True,
                color_discrete_sequence=["#FF9800"]
            )
        else:
            fig_revenue = {}
        
        # Top 5 customers
        if "Customer ID" in filtered.columns:
            top_5_customers = filtered["Customer ID"].value_counts().head(5).reset_index()
            top_5_customers.columns = ["Customer ID", "Number of Bookings"]
            table_data = top_5_customers.to_dict('records')
            columns = [{"name": i, "id": i} for i in top_5_customers.columns]
        else:
            table_data = []
            columns = []
        
        return (
            f"{avg_rating:.2f}",
            f"{five_star_count:,.0f}",
            f"${total_revenue:,.0f}",
            fig_rating_dist,
            fig_by_vehicle,
            fig_revenue,
            table_data,
            columns
        )