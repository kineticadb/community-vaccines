LOAD DATA INTO DEMO_Vaccine_Distro.airport_metadata_usa
FROM FILE PATHS '/mnt/data/persist/airport_metadata.csv'
FORMAT TEXT (INCLUDES HEADER = true)
WITH OPTIONS (INGESTION MODE = TYPE INFERENCE)