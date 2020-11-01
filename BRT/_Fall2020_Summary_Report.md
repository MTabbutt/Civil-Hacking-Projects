# Fall 2020 work on BRT - Report Summary

Author: Megan Tabbutt


## 1. Madison Metro Summary:

![SystemMap](PaperFigures/SystemMap.png)

Figure 1: A plot showing all of the bus routes in the City of Madison. A greater opaqueness dipicts overlapping routes, and greater service for that area. 

</br>

## 2. Route Stop Spacing Summary:

![Quartiles_allTrips_Weekdays](PaperFigures/Quartiles_allTrips_Weekdays.png)
![Quartiles_allTrips_Weekdays_zoom](PaperFigures/Quartiles_allTrips_Weekdays_zoom.png)

Figure 2: Distribution of stop spacing by route. Three quartiles are shown: top 25%, middle 50%, bottom 25%. The overall system average is also show. Routes with a very high top 25% stop spacing most likely have a limited stop zone on the route. These limited stop zones increase route speed by having a section that does not stop at all, and typically cover larger distances across the city. 

</br>

## 3. Route Frequency:

![FrequencyHeatMap](PaperFigures/FrequencyHeatMap.png)

Figure 3: A Summary of the frequency of service for bus routes during the weekday. 

</br>

## 4. Demographics vs Route Characteristics:

<p float="left">
  <img src="PaperFigures/CarOwnershipVSfrequency6am.png" alt="drawing" width="450"/>
  <img src="PaperFigures/CarOwnershipVSfrequency12pm.png" alt="drawing" width="450"/>
</p>

Figure 4: Heatmap of the cars per capita. Route frequency is denoted by opaqueness of the lines. More opaque and connected lines have more buses during the 6am hour. 

</br>
</br>
</br>
***

## Old Work: 

### About:
 Listed below are some of the interesting plots and finds from work during the 2020 semester with CaSP and more groups. 
 
 

## Route Spacing - Route Balancing Considerations

### Data is based on weekday regular routes (not weekend, not holiday)
 
## Initial tinkering with spacing: 

Process: Look at all weekday routes possible: "92_WKDX' where X are different perameters specified by Madison Metro. For every route, look at every possible trip during the week. For each trip find all of the distances between stops. Create one, massive, array with all of these distances. Then plot the mean, and quartiles as seen below.

### Mean of all Weekday Trips:
![Means_allTrips_Weekdays_zoom](Figures/Means_allTrips_Weekdays_zoom.png)

### Mean, Farthest 25%, Shortest 25% of all Weekday Trips:
![Quartiles_allTrips_Weekdays](Figures/Quartiles_allTrips_Weekdays.png)

### Mean, Farthest 25%, Shortest 25% of all Weekday Trips - ZOOM:
![Quartiles_allTrips_Weekdays_zoom](Figures/Quartiles_allTrips_Weekdays_zoom.png)


## Finding Routes to Rebalance:

Wanted to look at correlation between average speed the bus goes, average ridership for that route and average stop spacing. No correlation seems to exist. 

### Ridership vs Spacing (no 80):
![Ridership vs Spacing](Figures/Correlation_Ridership_Stop-Spacing_no80.png)

### Ridership vs Spacing - Zoom:
![Ridership vs Spacing zoom](Figures/Lowest_ridership_closest_stop_spacing.png)

### Ridership vs speed (no 80):
![Ridership vs Speed](Figures/Correlation__Ridership_Speed_no80.png)




## Four Routes I Suggest We Rebalance:

These are the four routes with the lowest riders but the shortest stop spacing. Exclding special routes: 80, 81, 82, 36. 

### Data explanation: 
- Average spacing for a specific route: Take all possible weekday trips and for each trip find the stop spacing, get an average for each trip, average those together for a route specific average spacing. 
- Average spacing across all routes: take the above average for each route and average it together. 

</br>

- Percent of daily riders for a specific route: Take all riders of the route at all stops and divide by the total riders across all routes (for weekday only). 
- Percent of daily riders across all routes: Average the above percentages together for all routes.

</br>

- Average speed for a specific route: For ever trip possible for a specific route, take the total distance travelled dividided by the total trip time. Average these trips together for each route. 
- Average speed across all routes: Average the above averages together for all routes.

</br>

> _Average Ridership Overall: 1.36%     Average Speed Overall: 16.19 MPH     Average Stop Spacing Overall: .26 Miles_
### Route 27:
![Route_characterstics_27](Figures/Route_characterstics_27.png)

> _Average Ridership Overall: 1.36%     Average Speed Overall: 16.19 MPH     Average Stop Spacing Overall: .26 Miles_
### Route 32:
![Route_characterstics_32](Figures/Route_characterstics_32.png)

> _Average Ridership Overall: 1.36%     Average Speed Overall: 16.19 MPH     Average Stop Spacing Overall: .26 Miles_
### Route 44:
![Route_characterstics_44](Figures/Route_characterstics_44.png)

> _Average Ridership Overall: 1.36%     Average Speed Overall: 16.19 MPH     Average Stop Spacing Overall: .26 Miles_
### Route 51:
![Route_characterstics_51](Figures/Route_characterstics_51.png)
