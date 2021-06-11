CREATE OR REPLACE materialized VIEW DEMO_Vaccine_Distro.vaccine_demand_intl refresh ON change AS
(
SELECT iso_code,
              location,
              countrymap.ISO_ALPHA_2 as country_iso2,
              countrymap.ISO_ALPHA_3 as country_iso3,
              int(population) as "total_population",
              int(people_fully_vaccinated) as "fully_vaccinated_population",
              int(new_cases_per_million) as "new_cases_per_1mm",
              int(total_deaths_per_million) as "total_deaths_per_1mm",
              int(population-people_fully_vaccinated) AS "unvaccinated",
              int(100*(population-people_fully_vaccinated)/population) AS "unvaccinated_pct",
              (select int(avg(100*(population-people_fully_vaccinated)/population)) from DEMO_Vaccine_Distro.global_covid_statistics) as "avg_global_unvaccinated_pct",
              if (people_fully_vaccinated , int(population-people_fully_vaccinated), int(0.92 * population) ) AS "vaccinate_doses_required"
       FROM   DEMO_Vaccine_Distro.global_covid_statistics gstat,
              DEMO_Vaccine_Distro.map_iso_alpha23 countrymap
       WHERE  date='2021-06-01'
       AND    trim(countrymap.ISO_ALPHA_3) = trim(iso_code)

) 