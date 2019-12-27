#standardSQL

select jslibs.h3.ST_H3(
  ST_GeogPoint(-3.7038,40.4168), 8
)  


-- +-----------------+
-- |       f0_       |
-- +-----------------+
-- | 88390cb1b1fffff |
-- +-----------------+
