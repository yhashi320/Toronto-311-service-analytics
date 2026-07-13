import os
import pandas as pd

# Build path relative to this script's location so it works on any machine
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
file_path = os.path.join(project_root, 'data', 'raw', 'sr2025.csv')

df = pd.read_csv(
    file_path,
    engine="python",
    encoding="latin1",
    on_bad_lines="skip"
)

print(df.columns)

df['Creation Date'] = pd.to_datetime(df['Creation Date'], errors='coerce')
df['Year'] = df['Creation Date'].dt.year
df['Month'] = df['Creation Date'].dt.month

print(df['Creation Date'].head())
print(f"Rows with invalid/missing Creation Date: {df['Creation Date'].isna().sum()}")
