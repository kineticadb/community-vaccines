CREATE MATERIALIZED EXTERNAL TABLE "DEMO_Vaccine_Distro"."airport_metadata_usa"
(
   "id" INTEGER,
   "ident" VARCHAR (8),
   "type" VARCHAR (16, dict),
   "name" VARCHAR (128),
   "latitude_deg" DOUBLE,
   "longitude_deg" DOUBLE,
   "elevation_ft" SMALLINT,
   "continent" VARCHAR (2),
   "country_name" VARCHAR (16, dict),
   "iso_country" VARCHAR (2),
   "region_name" VARCHAR (32, dict),
   "iso_region" VARCHAR (8, dict),
   "local_region" VARCHAR (2),
   "municipality" VARCHAR (64),
   "scheduled_service" TINYINT,
   "gps_code" VARCHAR (4),
   "iata_code" VARCHAR (4),
   "local_code" VARCHAR (8),
   "home_link" VARCHAR (128),
   "wikipedia_link" VARCHAR (128),
   "keywords" VARCHAR (256),
   "score" INTEGER,
   "last_updated" VARCHAR (32)
)
FILE PATHS '/mnt/data/persist/airport_metadata.csv'
FORMAT DELIMITED TEXT;