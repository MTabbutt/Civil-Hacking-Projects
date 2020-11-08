# Fall 2020 work on BRT - Report Summary

Author: Megan Tabbutt


## 1. Madison Metro Summary:

![PopDenstiyRoutes](PaperFigures/PopDenstiyRoutes.png)

Figure 1: Population density on a log scale for the city of Madison. Value is based on survey responses/sq mile. Madison Metro bus system map is shown in white overlaid. 

</br>


## 2. Route Comparison:

Overall Averages of Statistics not Including Route 80:

_Ridership: 1.36%     Speed: 16.19 MPH     Farthest Distance: 8.06 Miles     Spacing: 0.26 Miles     Std Dev. of Spacing: 0.22 Miles_

![PopDenstiyRoutes](PaperFigures/Route_27.png)
Route 27 is an of a route that needs to be re-balanced: too close on part of the route, several stops are .1miles or less apart. 

</br>

![PopDenstiyRoutes](PaperFigures/Route_23.png)
Route 23 is an example of a very specialized route. It was created to take people from the capitol (and a couple places on E Washington Ave) to American Family Center (employment center).

</br>

![PopDenstiyRoutes](PaperFigures/Route_67.png)
Route 67 is an example of a well balanced route. 

</br>

![PopDenstiyRoutes](PaperFigures/Route_31.png)
Route 31 is an example of a limited stop zone route. It goes far, fast and has good spacing. 

</br>

## 2. Route Stop Spacing Summary:

![Quartiles_allTrips_Weekdays](PaperFigures/Quartiles_allTrips_Weekdays.png)
![Quartiles_allTrips_Weekdays_zoom](PaperFigures/Quartiles_allTrips_Weekdays_zoom.png)

Figure 2: Distribution of stop spacing by route. Three quartiles are shown: top 25%, middle 50%, bottom 25%. The overall system average is also show. Routes with a very high top 25% stop spacing most likely have a limited stop zone on the route. These limited stop zones increase route speed by having a section that does not stop at all, and typically cover larger distances across the city. 

</br>

## 3. Route Frequency:

![FrequencyHeatMap](PaperFigures/FrequencyHeatMap.png)

Figure 3: A Summary of the frequency of service for bus routes during the weekday. Since the specific time a bus comes depends on the stop, the middle stop of each route is chosen for this figure. 

</br>


## 3. Route Frequency:

![FrequencyHeatMap](PaperFigures/FrequencyHeatMap.png)

Figure 3: A Summary of the frequency of service for bus routes during the weekday. Since the specific time a bus comes depends on the stop, the middle stop of each route is chosen for this figure. 

</br>

## 5. Demographics vs Departure time for Work:

![WeightFactorRaces](PaperFigures/WeightFactorRaces.png)

How to read this graph: If there are 50 Black workers and 50 White workers, then at any given hour 50% of the people leaving should be Black if there is a fair distribution of work time (not depending on race). Then we ask who is actually leaving at 10pm. It turns out to be 75 Black people and 25 White people. So a Black person is 1.5 times more likely to leave for work at 10pm than a White person. And a White person is .5 times more likely to leave to work at 10pm than a Black person. This is the factor that is plotted on the y axis. Given this graph. If it is 10pm in Wisconsin, Hispanic people are 1.25 times more likely to be working than what would be fair or unbiased, and Blacks are 1.75 times more likely. 

Routes to look at more closely based on the plot above. 7am is the peak for most commuters. Also more likely to be White than Black or Hispanic. 10pm is the most disproportionately Black workers. 2am is the most disproportionately Hispanic workers. 2pm is the second peak on the distribution of workers, also disproportionately higher for Black and Hispanic, and also maybe the easiest for Metro to fix and add more “off-peak” service during the day. 

<p float="left">
  <img src="PaperFigures/CarOwnershipVSfrequency2am.png" alt="drawing" width="450"/>
  <img src="PaperFigures/CarOwnershipVSfrequency7am.png" alt="drawing" width="450"/>
  <img src="PaperFigures/CarOwnershipVSfrequency2pm.png" alt="drawing" width="450"/>
  <img src="PaperFigures/CarOwnershipVSfrequency10pm.png" alt="drawing" width="450"/>
</p>

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
