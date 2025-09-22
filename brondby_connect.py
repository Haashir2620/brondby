import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Forbind til MySQL (ret user/password hvis nødvendigt)
conn = mysql.connector.connect(
    host="localhost",
    user="admin",                
    password="AdminKode_2025!",     
    database="brondby",
    port=3306
)

# Hent 5 rækker fra matches som test
df_matches = pd.read_sql("SELECT * FROM matches LIMIT 100;", conn)

print("Data hentet fra matches:\n", df_matches)

# Gem som CSV (så kan du åbne i Power BI)
df_matches.to_csv("matches_sample.csv", index=False)

conn.close()
print("Done. Fil gemt: matches_sample.csv")
