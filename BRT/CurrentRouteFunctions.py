import numpy as np


def convertArrivalTimes():
    
    arrivalTimesArray = np.array(stop_times_df['arrival_time'])

    arrivalTimesArrayFixed = []
    for time in arrivalTimesArray:
        timeList = time.split(":")
        timeList = [int(time) for time in timeList]
        if timeList[0] < 24:
            dateTime = datetime.datetime(2000, 1, 1, timeList[0], timeList[1], timeList[2])
        else:
            dateTime = datetime.datetime(2000, 1, 2, timeList[0]-24, timeList[1], timeList[2])
        arrivalTimesArrayFixed.append(dateTime)
    
    stop_times_df['arrival_time'] = arrivalTimesArrayFixed