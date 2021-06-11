SELECT DISTINCT 
    a.node_id, 
    a.iata, 
    a.city, 
    a.country, 
    count(*) as "Flights" 
FROM
    DEMO_Vaccine_Distro.airport_routes r,
    DEMO_Vaccine_Distro.airport_nodes a
WHERE 
    r.edge_node1_id=a.node_id
    and a.country='United States'
GROUP BY a.node_id, a.iata, a.city, a.country
ORDER BY Flights DESC