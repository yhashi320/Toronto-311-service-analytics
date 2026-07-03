import pandas as pd
import os

# Load
df = pd.read_csv(
    "~/desktop/toronto-311-analytics/Data/Raw/sr2025.csv",
    engine="python",
    encoding="latin1",
    on_bad_lines="skip"
)
print(f"Loaded: {len(df):,} rows")

# Parse dates
df['Creation Date'] = pd.to_datetime(df['Creation Date'])

# Drop duplicates
df = df.drop_duplicates()
print(f"After dedup: {len(df):,} rows")

# Drop intersection columns (83% null, not useful)
df = df.drop(columns=['Intersection Street 1', 'Intersection Street 2'])

# Group service types into categories
def categorize_service(row):
    division = row['Division']
    section = str(row['Section']) if pd.notna(row['Section']) else ''
    
    if 'Animal' in section:
        return 'Animal Services'
    elif division == 'Municipal Licensing & Standards':
        return 'Licensing & Standards'
    elif division == 'Solid Waste Management Services':
        return 'Waste Management'
    elif division == 'Toronto Water':
        return 'Water Services'
    elif division == 'Transportation Services':
        return 'Transportation'
    elif division == 'Parks, Forestry & Recreation':
        return 'Parks & Recreation'
    else:
        return 'Other'

df['Service Category'] = df.apply(categorize_service, axis=1)

# Save
os.makedirs('../data/processed', exist_ok=True)
df.to_csv('../data/processed/sr2025_cleaned.csv', index=False)

print(f"\nSaved: {len(df):,} rows, {len(df.columns)} columns")
print("\nService Category breakdown:")
print(df['Service Category'].value_counts())