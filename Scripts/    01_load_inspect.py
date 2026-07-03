import pandas as pd

df = pd.read_csv(
    "../Data/Raw/sr2025.csv",
    engine="python",
    encoding="latin1",
    on_bad_lines="skip"
)

print(df.columns) 

df['Creation Date'] = pd.to_datetime(df["Creation Date"], errors = 'coerce')
df['Year'] = df["Creation Date"].dt.year
df['Month'] = df['Creation Date'].dt.month

print(df["Creation Date"].head())
print(df["Creation Date"].isna().sum())