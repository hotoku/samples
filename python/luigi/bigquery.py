"""
usage:
$ python bigquery.py

Before running the command, set environment variable GOOGLE_APPLICATION_CREDENTIALS.
The credential file for a gcloud account is located ~/.config/gcloud/legacy_credentials/<account>/adc.json
"""

import luigi
from luigi.contrib.bigquery import BigQueryTarget
from google.cloud import bigquery
from datetime import datetime, timedelta

_PROJECT = "olm-user-yasunori-horikoshi"


class BigqueryWrapper:
    def __init__(self, proj):
        self.client = bigquery.Client(
            project=proj
        )

    def query(self, sql):
        job = self.client.query(sql)
        return job.to_dataframe()

    def dryrun(self, sql):
        job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
        query_job = self.client.query(
            sql,
            job_config=job_config,
        )
        print("This query will process {} bytes.".format(query_job.total_bytes_processed))


Bigquery = BigqueryWrapper(_PROJECT)


class T1(luigi.Task):
    day = luigi.DateParameter()

    def requires(self):
        return []

    def output(self):
        return [BigQueryTarget(
            _PROJECT,
            "temp",
            "table1_" + self.day.strftime("%Y%m%d")
        )]

    def run(self):
        ymd = self.day.strftime("%Y%m%d")
        sql = f"""
create or replace table `{_PROJECT}.temp.table1_{ymd}` as
select 1 as one
"""
        Bigquery.query(sql)


class T2(luigi.Task):
    day = luigi.DateParameter()

    def requires(self):
        return [T1(self.day)]

    def output(self):
        return [BigQueryTarget(
            _PROJECT,
            "temp",
            "table2_" + self.day.strftime("%Y%m%d")
        )]

    def run(self):
        ymd = self.day.strftime("%Y%m%d")
        sql = f"""
create or replace table `{_PROJECT}.temp.table2_{ymd}` as
select 2 as two
"""
        Bigquery.query(sql)


def main():
    day = datetime(2020, 8, 1)
    days = [
        day + timedelta(days=i) for i in range(10)
    ]
    tasks = [T2(d) for d in days]
    luigi.build(
        tasks,
        local_scheduler=True,
        workers=4
    )


if __name__ == "__main__":
    main()
