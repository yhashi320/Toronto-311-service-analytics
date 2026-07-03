import pandas as pd
import os
import matplotlib as plt

# Get correct file path
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
file_path = os.path.join(project_root, 'data', 'processed', 'sr2025_cleaned.csv')

# Load data 
df = pd.read_csv(file_path)
print(f"Loaded: {len(df):,} rows")

#Adding hour and day to Date features 
df["Creation Date"] = pd.to_datetime(df['Creation Date'])
df['Hour'] = df['Creation Date'].dt.hour
df['Dayofweek'] = df['Creation Date'].dt.day_name()
df['Month'] = df['Creation Date'].dt.month

#Season Mapping
def get_season(month):
    if month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return 'Spring'
    elif month in [6,7,8]:
        return 'Summer'
    else:
        return 'Fall'

df['Season'] = df['Month'].apply(get_season)

print('=' * 60)
print("KEY INSIGHTS - TORONTO 311 DATA")
print("=" * 60)

# 1. Top Service Categories
print('TOP SERVICE CATEGORIES')
top_categories = df['Service Category'].value_counts()
for cat, count in top_categories.head(10).items():
    print(f'{cat}: {count, } ({count/len(df)*100:.1f}%)')

# 2. Top Granular service types
print("\nTOP SPECIFIC SERVICE REQUESTS")
top_services = df['Service Request Type'].value_counts().head(10)
for service, count in top_services.items():
    print(f' {service}, {count:,}')

# 3. Hourly Patterns
print('\nBUSIEST HOURS')
hourly = df['Hour'].value_counts().sort_index()
busy_hours = hourly.idxmax()
print(f'Peak Hour: {busy_hours}:00 ({hourly.max():,} requests)')
print(f'Top 3 hours:')
for hour in hourly.nlargest(3).index:
    print(f'{hour}:00 {hourly[hour]:,} requests')

# 4. Day of week Pattern
print('\nBUSIEST DAYS')
daily = df['Dayofweek'].value_counts()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily = daily.reindex(day_order)
for day, count in daily.items():
    print(f' {day}: {count:,} ({count/len(df)*100:.1f}%)')

# 5. Seasonal Pattern
print("\nBUSIEST SEASON")
seasonal = df['Season'].value_counts()
for season, count in seasonal.items():
    print(f' {season}: {count:,} ({count/len(df)*100:.1f}%)')

# 6. Top ward
print('\n TOP 10 WARDS')
top_wards = df['Ward'].value_counts().head(10)
for ward, count in top_wards.items():
    print(f' {ward}: {count:,} ({count/len(df)*100:.1f}%)') 

# 7. Division Workload
print('\nDIVISON WORKLOAD')
top_division = df['Division'].value_counts()
for divison, count in top_division.items():
    print(f'{divison}: {count:,} ({count/len(df)*100:.1f}%)')

# 8. Status Breakdown
print('\nREQUEST STATUS')
status = df['Status'].value_counts()
for status, count in status.items():
    print(f'{status}: {count:,} ({count/len(df)*100:.1f}%)')
