import pandas as pd

def load_data():
    df = pd.read_csv("Data/uber_rides_cleaned.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Parse datetime (single source of truth)
    df["Datetime"] = pd.to_datetime(
        df["Date_Time"],
        format="%Y-%m-%d %H:%M:%S",
        errors="coerce"
    )

    # Drop rows with invalid datetime (optional but recommended)
    df = df.dropna(subset=["Datetime"])

    # Time-based features
    df["Date"] = df["Datetime"].dt.date
    df["Hour"] = df["Datetime"].dt.hour
    df["Weekday"] = df["Datetime"].dt.day_name()
    df["Month"] = df["Datetime"].dt.month_name()
    df["Month_Num"] = df["Datetime"].dt.month

    return df


def filter_data(df, start_date, end_date):
    if start_date and end_date:
        start = pd.to_datetime(start_date)
        end = pd.to_datetime(end_date)
        return df[(df["Datetime"] >= start) & (df["Datetime"] <= end)]
    return df