import csv
from time import sleep



print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

# https://docs.kinetica.com/7.1/graph_solver/network_graph_solver/
# https://openflights.org/data.html#route


def cleanse(in_str):
    out_str = in_str
    out_str.replace(",", "")
    out_str.replace("'", "")
    return out_str

def main():

    lookup_airport = {}

    input_file = csv.DictReader(open("data/airports.csv"))
    for row in input_file:
        lookup_airport[row['AIRPORT_ID']] = {
            'AIRPORT_ID': row['AIRPORT_ID'],
            'NAME': cleanse(row['NAME']),
            'CITY': cleanse(row['CITY']),
            'COUNTRY': cleanse(row['COUNTRY']),
            'IATA': row['IATA'],
            'ICAO': row['ICAO'],
            'LATITUDE': row['LATITUDE'],
            'LONGITUDE': row['LONGITUDE']
        }

    #print(lookup_airport)


    inter_airport_network_edges = []
    edge_id = 10000

    input_file = csv.DictReader(open("data/routes.csv"))
    for row in input_file:
        edge_id = edge_id + 1
        if row['SOURCE_AIRPORT_ID'] == "\\N":
            print(f"Warn source airport {row['SOURCE_AIRPORT_ID']} is Null, skipping...")
            continue
        if row['DEST_AIRPORT_ID'] == "\\N":
            print(f"Warn source airport {row['DEST_AIRPORT_ID']} is Null, skipping...")
            continue
        if str(row['SOURCE_AIRPORT_ID']) not in lookup_airport:
            print(f"Warn source airport {row['SOURCE_AIRPORT_ID']} not found in Airports lookup table, skipping...")
            continue
        if str(row['DEST_AIRPORT_ID']) not in lookup_airport:
            print(f"Warn {row['SOURCE_AIRPORT_ID']} not found in Airports lookup table, skipping...")
            continue
        slon = lookup_airport[row['SOURCE_AIRPORT_ID']]['LONGITUDE']
        slat = lookup_airport[row['SOURCE_AIRPORT_ID']]['LATITUDE']
        dlon = lookup_airport[row['DEST_AIRPORT_ID']]['LONGITUDE']
        dlat = lookup_airport[row['DEST_AIRPORT_ID']]['LATITUDE']
        persistable = {
            "EDGE_ID": edge_id,
            "EDGE_NODE1_ID": row['SOURCE_AIRPORT_ID'],
            "EDGE_NODE2_ID": row['DEST_AIRPORT_ID'],
            "EDGE_WKTLINE": f"LINESTRING({slon} {slat}, {dlon} {dlat})",
            "EDGE_NODE1_X": slon,
            "EDGE_NODE1_Y": slat,
            "EDGE_NODE2_X": dlon,
            "EDGE_NODE2_Y": dlat,
            "EDGE_NODE1_WKTPOINT": f"POINT({slon} {slat})",
            "EDGE_NODE2_WKTPOINT": f"POINT({dlon} {dlat})",
            "EDGE_NODE1_NAME": f"{lookup_airport[row['SOURCE_AIRPORT_ID']]['IATA']}: {lookup_airport[row['SOURCE_AIRPORT_ID']]['NAME']}",
            "EDGE_NODE2_NAME": f"{lookup_airport[row['DEST_AIRPORT_ID']]['IATA']}: {lookup_airport[row['DEST_AIRPORT_ID']]['NAME']}",
            "EDGE_DIRECTION": "0",
            "EDGE_LABEL": f"'{row['AIRLINE']} {row['AIRLINE_ID']} from {lookup_airport[row['SOURCE_AIRPORT_ID']]['IATA']} --> {lookup_airport[row['DEST_AIRPORT_ID']]['IATA']}'",
            "EDGE_WEIGHT_VALUESPECIFIED": 1
        }
        inter_airport_network_edges.append(persistable)
        print(f"Adding edge {persistable['EDGE_LABEL']}")

    print(f"Writing {len(inter_airport_network_edges)} rows")

    with open('out_edges.csv', 'w', newline='\n') as csvfile:
        fieldnames = ["EDGE_ID",
            "EDGE_NODE1_ID",
            "EDGE_NODE2_ID",
            "EDGE_WKTLINE",
            "EDGE_NODE1_X",
            "EDGE_NODE1_Y",
            "EDGE_NODE2_X",
            "EDGE_NODE2_Y",
            "EDGE_NODE1_WKTPOINT",
            "EDGE_NODE2_WKTPOINT",
            "EDGE_NODE1_NAME",
            "EDGE_NODE2_NAME",
            "EDGE_DIRECTION",
            "EDGE_LABEL",
            "EDGE_WEIGHT_VALUESPECIFIED"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in inter_airport_network_edges:
            writer.writerow(i)
            
        
if __name__ == "__main__":
    main()
    

