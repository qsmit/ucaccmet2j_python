# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:41:46 2018

@author: Quirine
"""
# Station code for Seattle is: GHCND:US1WAKG0038

total_year =  []        #This is the list that the monthly totals will be added to

month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']  #This is a list of all the month options
import json

with open('precipitation.json') as file_json:
    data = json.load(file_json)
    for month_from_list in month_list:
        monthly_rain = []           #The empty list to which the daily totals per month are added
        for item in data:
            station_code = item['station']              # Making a varibale to be able to select the variable
            if station_code == 'GHCND:US1WAKG0038':     # If the station code corresponds with Seattle, then add it to the list
                month_from_data = item['date'][5:7]                   # To select for month
                if month_from_data == month_from_list:
                    monthly_rain.append(item['value'])
        total_year.append(sum(monthly_rain))            # Adding the monthly totals to the list of the year

with open('yearly_precipitation.json', 'w') as file:      
    json.dump(total_year, file)

