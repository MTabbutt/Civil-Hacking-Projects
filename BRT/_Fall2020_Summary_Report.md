# Fall 2020 work on BRT - Report Summary

Author: Megan Tabbutt

### About:
 Listed below are some of the interesting plots and finds from work during the 2020 semester with CaSP and more groups. 
 
 
## Route Spacing - Route Balancing Considerations
 
## Initial tinkering with spacing: 

Process: Look at all weekday routes possible: "92_WKDX' where X are different perameters specified by Madison Metro. For every route, look at every possible trip during the week. For each trip find all of the distances between stops. Create one, massive, array with all of these distances. Then plot the mean, and quartiles as seen below.

### Mean of all Weekday Trips:
![Means_allTrips_Weekdays_zoom](Means_allTrips_Weekdays_zoom.png)

### Mean, Farthest 25%, Shortest 25% of all Weekday Trips:
![Quartiles_allTrips_Weekdays](Quartiles_allTrips_Weekdays.png)

### Mean, Farthest 25%, Shortest 25% of all Weekday Trips - ZOOM:
![Quartiles_allTrips_Weekdays_zoom](Quartiles_allTrips_Weekdays_zoom.png)


## Finding Routes to Rebalance:

Wanted to look at correlation between average speed the bus goes, average ridership for that route and average stop spacing. No correlation seems to exist. 

### Ridership vs Spacing (no 80):
![Ridership vs Spacing](Correlation_Ridership_Stop-Spacing_no80.png)

### Ridership vs Spacing - Zoom:
![Ridership vs Spacing zoom](Lowest_ridership_closest_stop_spacing.png)

### Ridership vs speed (no 80):
![Ridership vs Speed](Correlation__Ridership_Speed_no80.png)
