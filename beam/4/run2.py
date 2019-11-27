#!/usr/bin/env python

import apache_beam as beam


def myprint(l):
    print(l)
    return l

project = "astute-cumulus-230103"
p = beam.Pipeline(argv=[
    f"--project={project}"
])

(p
 | beam.io.Read(beam.io.BigQuerySource(
     project=project,
     query="select * from `horikoshi_work.temp_20191127_stayhome_sample`",
     use_standard_sql=True))
 | beam.Map(myprint)
 | beam.io.Write(beam.io.BigQuerySink(
     table="temp_20191127_2",
     dataset="horikoshi_work",
     project=project,
     schema=",".join(["uuid:STRING",
                      "latitude:FLOAT",
                      "longitude:FLOAT",
                      "accuracy:FLOAT",
                      "timestamp:INTEGER",
                      "datetime_jst:DATETIME"])))
)
 
p.run().wait_until_finish()
