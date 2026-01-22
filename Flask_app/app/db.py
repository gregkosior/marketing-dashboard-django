import _sqlite3
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" 
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "database.db"
conn = _sqlite3.connect(DB_PATH)

df=pd.read_csv(DATA_DIR / "processed" / "shop_clean.csv")
df.to_sql("shop_data", conn, if_exists="replace", index=False)

conn.close()
