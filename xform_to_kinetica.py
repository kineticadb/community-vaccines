import csv
from time import sleep


# https://openflights.org/data.html#route
INPUT_FILE_AIRPORTS = "data/airports.csv"
INPUT_FILE_ROUTES = "data/routes.csv"
# https://docs.kinetica.com/7.1/graph_solver/network_graph_solver/
OUTPUT_FILE_NODES = "out_nodes.csv"
OUTPUT_FILE_EDGES = "out_edges.csv"

FIELDS_NODES = ["NODE_ID",
                "NODE_X",
                "NODE_Y",
                "NODE_NAME",
                "NODE_WKTPOINT",
                "NODE_LABEL",
                "IATA",
                "ICAO",
                "CITY",
                "COUNTRY"]

FIELDS_EDGES = ["EDGE_ID",
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

# Helper function to simplify strings
def cleanse(in_str):
    out_str = in_str
    out_str.replace(",", "")
    out_str.replace("'", "")
    return out_str

# TODO: this is just a rough measure, a stand-in for now
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
def rough_distance(slon, slat, dlon, dlat):
    from math import sin, cos, sqrt, atan2, radians
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(float(slat))
    lon1 = radians(float(slon))
    lat2 = radians(float(dlat))
    lon2 = radians(float(dlon))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance    

def main():

    lookup_airport = {}
    airport_nodes = []

    input_file = csv.DictReader(open(INPUT_FILE_AIRPORTS))
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
    
        if row['AIRPORT_ID'] == "\\N":
            continue
        nlon = row['LONGITUDE']
        nlat = row['LATITUDE']
        if row['IATA']=="\\N":
            row['IATA']=None
            nodename = f"{row['ICAO']}: {cleanse(row['NAME'])}"
            nodelabel = f"{row['ICAO']}: {cleanse(row['NAME'])}; {cleanse(row['CITY'])}, {cleanse(row['COUNTRY'])}"
        else:
            nodename = f"{row['IATA']}: {cleanse(row['NAME'])}"
            nodelabel = f"{row['IATA']}: {cleanse(row['NAME'])}; {cleanse(row['CITY'])}, {cleanse(row['COUNTRY'])}"

        persistable = {
            "NODE_ID": row['AIRPORT_ID'],
            "NODE_X": nlon,
            "NODE_Y": nlat,
            "NODE_NAME": nodename,
            "NODE_WKTPOINT": f"POINT({nlon} {nlat})",
            "NODE_LABEL": nodelabel,
            "IATA": row['IATA'],
            "ICAO": row['ICAO'],
            "CITY": cleanse(row['CITY']),
            "COUNTRY": cleanse(row['COUNTRY'])
        }
        airport_nodes.append(persistable)
        print(f"Adding node {persistable['NODE_LABEL']}")

    print(f"Writing {len(airport_nodes)} rows")

    with open('out_nodes.csv', 'w', newline='\n') as csvfile:        
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS_NODES)
        writer.writeheader()
        for n in airport_nodes:
            writer.writerow(n)









    inter_airport_network_edges = []
    edge_id = 10000

    input_file = csv.DictReader(open(INPUT_FILE_ROUTES))
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
        if lookup_airport[row['SOURCE_AIRPORT_ID']]['COUNTRY'] == lookup_airport[row['DEST_AIRPORT_ID']]['COUNTRY']:
            # skipping domestic flight
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
            "EDGE_WEIGHT_VALUESPECIFIED": rough_distance(slon, slat, dlon, dlat)
        }
        inter_airport_network_edges.append(persistable)
        print(f"Adding edge {persistable['EDGE_LABEL']}")

    print(f"Writing {len(inter_airport_network_edges)} rows")

    with open('out_edges.csv', 'w', newline='\n') as csvfile:        
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS_EDGES)
        writer.writeheader()
        for i in inter_airport_network_edges:
            writer.writerow(i)
            
        
if __name__ == "__main__":
    main()
    

