import plotly.express as px

# KPI
def total_bookings(df):
    return f"{len(df):,.0f}"

# PIE — Booking Status
def booking_status_pie(df):
    fig = px.pie(
        df,
        names="Booking Status",
        title="Booking Status Breakdown",
        hole=0.4
    )
    fig.update_traces(textinfo="percent+label")
    return fig

# LINE — Ride Volume Over Time
def rides_over_time(df):
    grouped = (
        df.groupby(["Month", "Month_Num"])
        .size()
        .reset_index(name="Bookings")
        .sort_values("Month_Num")
    )

    fig = px.line(
        grouped,
        x="Month",
        y="Bookings",
        markers=True,
        title="Ride Volume Over Time"
    )
    return fig

# BAR — Vehicle Type
def vehicle_type_bar(df):
    vc = (
        df["Vehicle Type"]
        .value_counts()
        .reset_index(name="Bookings")
        .rename(columns={"index": "Vehicle Type"})
    )

    fig = px.bar(
        vc,
        x="Vehicle Type",
        y="Bookings",
        title="Bookings by Vehicle Type"
    )

    return fig

# BAR — Payment Method
def payment_method_bar(df):
    vc = (
        df["Payment Method"]
        .value_counts()
        .reset_index(name="Count")
        .rename(columns={"index": "Payment Method"})
    )

    fig = px.bar(
        vc,
        x="Payment Method",
        y="Count",
        title="Payment Method Distribution"
    )

    return fig