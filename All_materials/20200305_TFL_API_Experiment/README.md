> [!NOTE]  
> The following was a project from the [ONS Data Science Accelerator programme]( https://www.gov.uk/government/publications/data-science-accelerator-programme/introduction-to-the-data-science-accelerator-programme) which started in late February 2020. The project was subsequently paused and subsequently abandoned due to the Covid 19 pandemic.

# Fairness of hospital transportation in London

## Aim
The problem concerns fairness in public transportation to hospitals. I will look at the reliability of public transport to hospitals in terms of areas of deprivation and disability. For example, patients with low incomes or with disability will be dependent on buses even though faster transport systems like London Underground are available. Therefore, it is vital to assess public transport reliability in terms of daily punctuality for specific demographics. The information can be used to infer possible explanation for patients being late or not attending their appointments.

The objective will be to develop an application programming interface (API), using inputs of patients’ residence, transportation restriction such as minimal interchange or step free access and hospital location. The API will output the punctuality of the route from live arrivals for a given time interval. The API will be applied to each derivation district in London and consider different modes of transport.

## Approach

With the proposed API, I expect outputs of statistics of punctualities from a set of journeys. I hope to use API to find the punctualities for each deprivation district (Lower Layer Super Output Area) for journeys to the nearest hospital. I will also consider different types of journeys constraint by disability of the user.

The key methods will be data linkage, data visualization and spatial analysis. I would need to link journeys from TFL to geographical data from hospitals and indices of deprivation. In addition, I would need to implement data visualization methods to show the punctualities on different deprivation districts. Finally, I would need spatial analysis tools to link the closest hospital to a deprivation district.

## Data
The sources of data are listed as follows:
- TFL open source data - https://tfl.gov.uk/info-for/open-data-users/ 
- Indices of deprivation - https://dclgapps.communities.gov.uk/imd/iod_index.html 
- Locations of Hospitals in London - https://digital.nhs.uk/services/organisation-data-service/data-downloads/other-nhs-organisations 

