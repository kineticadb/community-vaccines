CREATE MATERIALIZED EXTERNAL TABLE "DEMO_Vaccine_Distro"."map_iata_to_country_iso"
(
   "ident" VARCHAR (8) NOT NULL,
   "type" VARCHAR (16, dict) NOT NULL,
   "name" VARCHAR (128) NOT NULL,
   "elevation_ft" SMALLINT,
   "continent" VARCHAR (2) NOT NULL,
   "iso_country" VARCHAR (2) NOT NULL,
   "iso_region" VARCHAR (8, dict) NOT NULL,
   "municipality" VARCHAR (64),
   "gps_code" VARCHAR (4),
   "iata_code" VARCHAR (4),
   "local_code" VARCHAR (8),
   "coordinates" VARCHAR (64) NOT NULL
)
FILE PATHS '/mnt/data/persist/airport-to-country-map.csv'
FORMAT DELIMITED TEXT;