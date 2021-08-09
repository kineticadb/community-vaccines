<!-- LOGO -->
<br />
<h1>
<p align="center">
  <img src="https://2wz2rk1b7g6s3mm3mk3dj0lh-wpengine.netdna-ssl.com/wp-content/uploads/2018/08/kinetica_logo.svg" alt="Logo" width="140" height="110">
  <br>Vaccine Excess Supply Delivery
</h1>
  <p align="center">
    Exploring logistics in the context of COVID vaccinations.
    <br />
    </p>
</p>

<p align="center"> 
![caption](images/routes.png)
</p>                                                                                                                             
                                                                                                                                                      
## About The Project
We've all heard of the Traveling Salesperson Problem(1), it is one of the most common Graph problems and has numerous implementations. In the practice, however, problems are much more complicated. In the world of logistics, a more realistic setup is typicall the Multiple Supply Demand Chain Optimization (MSDO), where there are multiple sources and sinks and we're looking for the most optimal delivery routes. A generic overview can be seen here: https://www.kinetica.com/blog/kinetica-graph-analytics-multiple-supply-demand-chain-optimization-msdo-graph-solver/

To demonstrate Multiple Supply Demand Chain Optimization (MSDO) with an immediate challenge we face globally, we've modeled the challenge of vaccine donations. The US has excess vaccine supply which expires over time. If supply is expiring, it is better to donate it abroad before expiration, as quickly as possible. The White House has been doing this(2). But can it be done more efficiently?

This is a complex problem:

    We have multiple supply sites (each state or region) which can feed into major international airports
    We have multiple demand sites (many nations), many of which desperately require more vaccine supply
    We have time constraints since accumulation, transport, and distribution need to be faster than expiration timelines
    Everything above is dynamic -- the supply and demand constantly changes with broad usage and infection trends

We have a Multiple Supply Demand Chain Optimization (MSDO) problem! We've modeled the supply, demand, routes, and have everything ready to run on a database (to respond to daily changes in global supply and demand.) The setup documentation can be seen at https://docs.kinetica.com/7.1/guides/match_graph_dc_multi_supply_demand/ but it will be more instructive to run it yourself below. Everything below will run on the Developer Edition (https://www.kinetica.com/try/) or on Kinetica Cloud (https://www.kinetica.com/kinetica-as-a-service-on-azure/)



## Importing

Import from GitHub:
```py
git@github.com:kineticadb/community-vaccines.git
jupyter notebook
```

## Credits
- Kaan Karamete; Saif Ahmed; Matt Brown; Kyle Suttom; Chad Meley (info@kinetica.com)
