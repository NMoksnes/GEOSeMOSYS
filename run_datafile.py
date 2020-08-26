import pandas as pd
import numpy as np
import os
from datetime import datetime
from build_data_file import *

##############################
##       Input data      ##
#############################
## Excelfiles import##
#datafile = 'Kenya_data_input_ALL.xlsx'
#df = pd.read_csv(datafile, 'GIS_data')
#elec = pd.read_excel(datafile, 'elec')
#trade = pd.read_excel(datafile, 'capacitytoactivity')
#inputactivity = pd.read_excel(datafile, 'inputactivity', index_col=0)
#demand = pd.read_excel(datafile, 'demand', index_col=0, header=0)
#demand_urban = pd.read_excel(datafile, 'demandprofile', index_col=0, header=0)
#demand_rural = pd.read_excel(datafile, 'demandprofile_rural', index_col=0, header=0)
#capacityfactor_wind = pd.read_excel(datafile, 'capacityfactor_wind', header=0)
#capacityfactor_wind = pd.read_excel('capacityfactor_wind.xlsx', header=0)
#capacityfactor_wind['date'] = pd.to_datetime(capacityfactor_wind['date'], format='%d/%m/%Y %H:%M')
#capacityfactor_wind.index = capacityfactor_wind['date']
#capacityfactor_solar = pd.read_excel(datafile, 'capacityfactor_solar', header=0)
#capacityfactor_solar = pd.read_excel('capacityfactor_solar.xlsx', header=0)
#capitalcost_RET = pd.read_excel(datafile, 'capitalcost_RET', index_col=0, header=0)
#capitalcost_RET.index = capitalcost_RET['CF']

### Making csv files instead to make the read more efficient
cd = os.getcwd()
df = pd.read_csv(cd +'/data/GIS_data.csv')
inputFileName = "Kenya_BIG_ALL_REF_200622_revB.txt"
file_object = 'Kenya_BIG_ALL_REF_200622_revC.txt'
elec = pd.read_csv(cd +'/data/elec.csv')
trade = pd.read_csv(cd +'/data/capacitytoactivity.csv')
inputactivity = pd.read_csv(cd +'/data/inputactivity.csv', index_col=0)
demand = pd.read_csv(cd +'/data/demand.csv', index_col=0, header=0)
demand_urban = pd.read_csv(cd +'/data/demandprofile.csv', index_col=0, header=0)
demand_rural = pd.read_csv(cd +'/data/demandprofile_rural.csv', index_col=0, header=0)
capacityfactor_wind = pd.read_csv(cd +'/data/capacityfactor_wind.csv')
#capacityfactor_wind = pd.read_excel('capacityfactor_wind.xlsx', header=0)
capacityfactor_wind['date'] = pd.to_datetime(capacityfactor_wind['date'], format='%d/%m/%Y %H:%M')
capacityfactor_wind.index = capacityfactor_wind['date']
print(capacityfactor_wind)
capacityfactor_solar = pd.read_csv(cd +'/data/capacityfactor_solar.csv', header=0)
#capacityfactor_solar = pd.read_excel('capacityfactor_solar.xlsx', header=0)
capitalcost_RET = pd.read_csv(cd +'/data/capitalcost_RET.csv', index_col=0, header=0)
capitalcost_RET.index = capitalcost_RET['CF']
trade_cost = pd.read_csv(cd +'/data/capitalcost.csv')

wind_power = 600      #600 kW from renewable ninja
solar_power = 1000  #1000W
batteryCF = 900  #900W
battery13h = 13  #hours that the battery is operational
battery8h = 8 #hours that the battery is operational

timesliceDN = '06:00'
timesliceDE = '17:00'
timesliceED = '18:00'
timesliceEN = '22:00'
timesliceNE = '23:00'
timesliceND = '05:00'

startyear = 2012
endyear = 2040

###############################
##    Reset all values      ##
##############################
allLinesFromKenyaXy = ""
with open(inputFileName, "r") as inputFile:
   allLinesFromKenyaXy = inputFile.read()

outPutFile = allLinesFromKenyaXy

## functions to run
#outPutFile = capitalcost(df, outPutFile, elec, capitalcost_RET, trade_cost, wind_power, solar_power, capacityfactor_wind, capacityfactor_solar, startyear, endyear)
#outPutFile = capacityfactor(elec, outPutFile, df, capacityfactor_wind, capacityfactor_solar, solar_power, wind_power, timesliceDN, timesliceDE, timesliceED, timesliceEN, timesliceNE, timesliceND, batteryCF, battery13h, battery8h, startyear, endyear)
outPutFile = operational_life(df, elec, outPutFile)
#outPutFile = capacitytoactivity(trade,outPutFile)
#outPutFile = emissionactivity(df, outPutFile, startyear, endyear)
#outPutFile = variablecost(outPutFile, df, elec, startyear, endyear)
#outPutFile = totaltechnologyannualactivityupperlimit(df, outPutFile, startyear, endyear)
#outPutFile = inputactivity(outPutFile, inputactivity, startyear, endyear)




#write data file
write_to_file(file_object, outPutFile)

