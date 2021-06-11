LOAD DATA INTO DEMO_Vaccine_Distro.airport_routes
FROM FILE PATHS '/mnt/data/persist/out_edges.csv'
FORMAT TEXT (INCLUDES HEADER = true)
WITH OPTIONS (INGESTION MODE = TYPE INFERENCE) 