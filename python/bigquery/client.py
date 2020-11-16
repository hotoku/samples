from google.cloud import bigquery

"""
https://googleapis.dev/python/bigquery/latest/index.html

## credentialの場所
~/.config/gcloud/legacy_credentials/<user-id>

## credentialの指定
- GOOGLE_APPLICATION_CREDENTIALS環境変数に指定
- bigquery.Clientに渡す
"""

client = bigquery.Client(
    project="dtws-user-yasunori-horikoshi",
    location="US"
)


sql = """
select * from `bigquery-public-data.samples.gsod`
where station_number = 803150 and year = 1966
"""


ret = client.query(sql)
df = ret.to_dataframe()
