import os
import sys
import csv

## ------------------------------------------------------------------------
## Execution parameters

# https://covid.cdc.gov/covid-data-tracker/#vaccinations
INPUT_FILE_SUPPLY = "data/covid19_vaccinations_in_the_united_states.csv"
OUTPUT_FILE_SUPPLY = "out_supply.csv"
## ------------------------------------------------------------------------

def main():

    with open(INPUT_FILE_SUPPLY) as f:
        lines = f.readlines()
    lines.pop(0) # remove line 1: COVID-19 Vaccinations in the United States
    lines.pop(0) # remove line 2: Date generated: Fri Jun 11 2021 09:21:54 GMT-0400 (Eastern Daylight Time)

    lines[0] = lines[0].replace("+","plus")
    lines[0] = lines[0].replace("-","_")
    lines[0] = lines[0].replace(" ","_")
    lines[0] = lines[0].replace("/","_")

    with open(OUTPUT_FILE_SUPPLY, 'w') as filehandle:
        filehandle.writelines(d.replace("N/A","") for d in lines)
            
        
if __name__ == "__main__":
    main()
    

