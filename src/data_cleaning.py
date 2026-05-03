import pandas as pd
import os

# Get project root dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned")

def load_data():
    apr = pd.read_csv(os.path.join(RAW_DATA_PATH, "uber-raw-data-apr14.csv"))
    may = pd.read_csv(os.path.join(RAW_DATA_PATH, "uber-raw-data-may14.csv"))
    df = pd.concat([apr, may], ignore_index = True)
    return df

def clean_data(df):
    # Convert datetime
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    
    # Feature Engineering
    df['hour'] = df['Date/Time'].dt.hour
    df['day'] = df['Date/Time'].dt.day
    df['weekday'] = df['Date/Time'].dt.day_name()
    
    return df

def save_cleaned_data(df):
    os.makedirs(CLEANED_DATA_PATH, exist_ok = True)
    output_path = os.path.join(CLEANED_DATA_PATH, "uber_cleaned.csv")
    df.to_csv(output_path, index = False)

def main():
    df = load_data()
    df = clean_data(df)
    save_cleaned_data(df)
    print("Data cleaned and saved successfully!")

if __name__ == "__main__":
    main()