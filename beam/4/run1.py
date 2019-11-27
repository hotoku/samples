#!/usr/bin/env python

import apache_beam as beam



project = "astute-cumulus-230103"
p = beam.Pipeline(argv=[
    f"--project={project}"
])

(p
 | beam.io.Read(beam.io.BigQuerySource(
     project=project,
     query="select * from `horikoshi_work.temp_20191127_stayhome_sample`",
     use_standard_sql=True))
 | beam.FlatMap(print)
)
 
p.run().wait_until_finish()
