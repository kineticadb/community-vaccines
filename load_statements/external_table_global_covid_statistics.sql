LOAD DATA INTO DEMO_Vaccine_Distro.global_covid_statistics
FROM FILE PATHS '/mnt/data/persist/owid-covid-data.csv'
FORMAT TEXT (INCLUDES HEADER = true)
WITH OPTIONS (INGESTION MODE = TYPE INFERENCE)