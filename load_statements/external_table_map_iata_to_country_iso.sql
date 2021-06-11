LOAD DATA INTO DEMO_Vaccine_Distro.map_iata_to_country_iso
FROM FILE PATHS '/mnt/data/persist/airport-to-country-map.csv'
FORMAT TEXT (INCLUDES HEADER = true)
WITH OPTIONS (INGESTION MODE = TYPE INFERENCE)