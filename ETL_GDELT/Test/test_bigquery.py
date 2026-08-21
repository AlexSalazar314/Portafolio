from google.cloud import bigquery

client = bigquery.Client(project="prueba-505900")

query = """
SELECT
    GLOBALEVENTID,
    SQLDATE,
    Actor1Name,
    Actor2Name,
    EventCode,
    GoldsteinScale
FROM `gdelt-bq.gdeltv2.events_partitioned`
WHERE _PARTITIONTIME >= TIMESTAMP('2026-08-16')
  AND _PARTITIONTIME < TIMESTAMP('2026-08-17')
LIMIT 10
"""

df = client.query(query).to_dataframe()

print(df)