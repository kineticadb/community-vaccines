LOAD DATA INTO DEMO_Vaccine_Distro.vaccine_utilization_usa
FROM FILE PATHS '/mnt/data/persist/supply.csv'
FORMAT TEXT (INCLUDES HEADER = true)
WITH OPTIONS (INGESTION MODE = TYPE INFERENCE)