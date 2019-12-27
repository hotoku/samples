#standardSQL

select
  jslibs.h3.ST_H3_POLYFILLFROMGEOG(tract_geom, 11)
from
  `bigquery-public-data.geo_census_tracts.census_tracts_new_york`
limit 1  




-- ["8b2a1072d604fff","8b2a1072d631fff","8b2a1072d606fff","8b2a1072d600fff","8b2a1072d605fff","8b2a1072d623fff","8b2a1072d622fff","8b2a1072d635fff","8b2a1072d630fff","8b2a1072d633fff","8b2a1072d615fff","8b2a1072d602fff","8b2a1072d603fff","8b2a1072d601fff","8b2a1072d62afff","8b2a1072d62efff","8b2a1072d621fff","8b2a1072d620fff","8b2a1072d626fff","8b2a1072d71bfff","8b2a1072d634fff","8b2a1072d636fff","8b2a1072d632fff","8b2a1072d614fff","8b2a1072d610fff","8b2a1072d611fff","8b2a1072d61cfff","8b2a1072d60efff","8b2a1072d60cfff","8b2a1072d62bfff","8b2a1072d628fff","8b2a1072d62cfff","8b2a1072d752fff","8b2a1072d625fff","8b2a1072d624fff","8b2a1072d719fff","8b2a1072d718fff","8b2a1072d71afff","8b2a1072d7a9fff","8b2a1072d7abfff","8b2a1072d78dfff","8b2a1072d789fff","8b2a1072d616fff","8b2a1072d612fff","8b2a1072d613fff","8b2a1072d61efff","8b2a1072d60dfff","8b2a1072d676fff","8b2a1072d629fff","8b2a1072d62dfff","8b2a1072d753fff","8b2a1072d750fff","8b2a1072d756fff","8b2a1072d70bfff","8b2a1072d70afff","8b2a1072d71dfff","8b2a1072d71cfff","8b2a1072d71efff","8b2a1072d7adfff","8b2a1072d7a8fff","8b2a1072d7aafff","8b2a1072d78cfff","8b2a1072d788fff","8b2a1072d78bfff","8b2a1072d6a5fff","8b2a1072d6a1fff","8b2a1072d670fff","8b2a1072d674fff","8b2a1072d75afff","8b2a1072d75efff","8b2a1072d751fff","8b2a1072d755fff","8b2a1072d754fff","8b2a1072d709fff","8b2a1072d708fff","8b2a1072d70efff","8b2a1072d703fff","8b2a1072d702fff","8b2a1072d711fff","8b2a1072d713fff","8b2a1072d7acfff","8b2a1072d7aefff","8b2a1072d673fff","8b2a1072d671fff","8b2a1072d675fff","8b2a1072d75bfff","8b2a1072d773fff","8b2a1072d772fff","8b2a1072d70dfff","8b2a1072d710fff","8b2a1072d712fff","8b2a1072d7a1fff","8b2a1072d644fff","8b2a1072d662fff","8b2a1072d7a5fff"]
