CREATE OR REPLACE materialized VIEW DEMO_Vaccine_Distro.vaccine_supply_usa refresh ON change AS
(
select 
    Total_Doses_Delivered,
    Total_Doses_Administered_by_State_where_Administered,
    People_Fully_Vaccinated_by_State_of_Residence,
    People_18plus_Fully_Vaccinated_by_State_of_Residence,
    Total_Doses_Delivered - Total_Doses_Administered_by_State_where_Administered as CURRENT_VACCINE_INVENTORY,
    int(0.23 * (Total_Doses_Delivered - Total_Doses_Administered_by_State_where_Administered)) as "Donateable" /* PER BIDEN DONATION ESTIMATES */
from DEMO_Vaccine_Distro.vaccine_utilization_usa
) 