import os
import pandas as pd

# Build path relative to this script's location so it works on any machine
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
raw_path = os.path.join(project_root, 'data', 'raw', 'sr2025.csv')
processed_dir = os.path.join(project_root, 'data', 'processed')
processed_path = os.path.join(processed_dir, 'sr2025_cleaned.csv')

# Load
df = pd.read_csv(
    raw_path,
    engine="python",
    encoding="latin1",
    on_bad_lines="skip"
)
print(f"Loaded: {len(df):,} rows")

# Parse dates
df['Creation Date'] = pd.to_datetime(df['Creation Date'], errors='coerce')

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
os.makedirs(processed_dir, exist_ok=True)
df.to_csv(processed_path, index=False)

print(f"\nSaved: {len(df):,} rows, {len(df.columns)} columns")
print("\nService Category breakdown:")
print(df['Service Category'].value_counts())

# Flag how much fell into 'Other' so it doesn't get lost silently
other_pct = (df['Service Category'] == 'Other').mean() * 100
print(f"\n'Other' category share: {other_pct:.1f}%")
