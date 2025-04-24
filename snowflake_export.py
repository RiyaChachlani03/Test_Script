import snowflake.connector
import csv
from datetime import datetime

conn = snowflake.connector.connect(
    account = "XQEFMFM-HAKKODAINC_PARTNER",
    user = "RIYA_CHACHLANI@HAKKODA.IO",
    password = "Rr@0303200203",
    role = "DATA_ENGINEER",
    warehouse = "COMPUTE_WH",
    database = "CASE_STUDY_TEAMB",
    schema = "REFINED_TEAMB"
)

sql_command = "SELECT * FROM STG_CRYPTO"

cursor = conn.cursor()
cursor.execute(sql_command)

columns = [desc[0] for desc in cursor.description]
rows = cursor.fetchall()

filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(rows)

print(f"✅ CSV file saved as {filename}")

cursor.close()
conn.close()
