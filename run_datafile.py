<<<<<<< HEAD
<<<<<<< Updated upstream
"""
This script is to build a OSeMOSYS data file where you have many locations/countries.
The script is user defined in the geographical, technology, year, timeslice dimesions, which makes the script very flexible.

__author__ = "Nandi Moksnes, Sebastian Moksnes"
__copyright__ = "Nandi Moksnes, nandi@kth.se"
__licence__ = "mit"
"""

import pandas as pd
import numpy as np
import os
import argparse
import sys
import logging
from datetime import datetime
from build_data_file import *

#CMD line read from https://github.com/willu47/lcoe/blob/master/src/lcoe/lcoe.py author Will Usher

# _logger = logging.getLogger(__name__)
#
# def parse_args(args):
#     """Parse command line parameters
#     Args:
#       args ([str]): command line parameters as list of strings
#     Returns:
#       :obj:`argparse.Namespace`: command line parameters namespace
#     """
#     parser = argparse.ArgumentParser(
#         description="Location specific OSeMOSYS datafile generator")
#     parser.add_argument(
#         "--version",
#         action="version",
#         version="lcoe {ver}".format(ver=__version__))
#     parser.add_argument(
#         dest="capital_cost",
#         help="Capital cost of the plant in $/kWh",
#         type=float,
#         metavar="FLOAT")
#     parser.add_argument(
#         dest="annual_output",
#         help="Annual output of the plant in kWh",
#         type=float,
#         metavar="FLOAT")
#     parser.add_argument(
#         dest="annual_operating_cost",
#         help="Annual operating cost of the plant in $",
#         type=float,
#         metavar="FLOAT")
#     parser.add_argument(
#         dest="discount_rate",
#         help="Discount rate x where 0 <= x < 1",
#         type=float,
#         metavar="FLOAT")
#     parser.add_argument(
#         dest="lifetime",
#         help="Lifetime of the plant in years",
#         type=int,
#         metavar="INT")
#
#     return parser.parse_args(args)
#
# def main(args):
#     """Main entry point allowing external calls
#     Args:
#       args ([str]): command line parameter list
#     """
#     args = parse_args(args)
#     _logger.debug("Starting location specific calculations...")
#     print("LCOE is {}".format(
#         lcoe(args.annual_output,
#              args.capital_cost,
#              args.annual_operating_cost,
#              args.discount_rate,
#              args.lifetime)
#         ))
#     _logger.info("Script ends here")
#
#
# def run():
#     """Entry point for console_scripts
#     """
#     main(sys.argv[1:])
#
#
# if __name__ == "__main__":
#     run()
#

# def main(filepath, configuration_file):
#    """Generate spatially disaggregated values"""
#    # Read input data
#    with open(os.path.join(filepath, "data.csv", 'r') as datafile:
#       data = datafile.readlines()


#### ADD Validation of type of file that is imported


#PV_MG_CF = [0.12, 0.14,0.155,0.17,0.20]
#PV_SA_CF = [0.13,0.15, 0.16,0.18, 0.21]
#Wind_CF = [0.48,0.47,0.45,0.44,0.41,0.37,0.31,0.25,0.19,0.125]
#Battery = [8,13]

startyear = 2012
endyear = 2040
modeofoperation = [1, 2, 3]
region = "Kenya"
param_file = '/osemosys_shell_param.txt'

###############################
##    Reset all values      ##
##############################

## functions to run
##arguments from CMD are below
paths = (os.getcwd() + '\data')
path = os.getcwd()
file_object= os.getcwd() + '/GIS.txt'
#####################################

dict_df = load_csvs(paths)
outPutFile = make_outputfile(path, param_file)
outPutFile = functions_to_run(dict_df,outPutFile, startyear, endyear, region, modeofoperation)

#write data file
write_to_file(file_object, outPutFile)

=======
"""
This script is to build a OSeMOSYS data file where you have many locations/countries.
The script is user defined in the geographical, technology, year, timeslice dimesions, which makes the script very flexible.
=======
"""
This script is to build a OSeMOSYS data file where you have many locations/countries.
The script is user defined in the geographical, technology, year, timeslice dimesions, which makes the script very flexible.
"""
>>>>>>> master

__author__ = "Nandi Moksnes, Sebastian Moksnes"
__copyright__ = "Nandi Moksnes, nandi@kth.se"
__licence__ = "mit"
<<<<<<< HEAD
"""
=======
>>>>>>> master

import pandas as pd
import numpy as np
import os
import argparse
import sys
import logging
from datetime import datetime
from build_data_file import *

#CMD line read from https://github.com/willu47/lcoe/blob/master/src/lcoe/lcoe.py author Will Usher

# _logger = logging.getLogger(__name__)
#
# def parse_args(args):
#     """Parse command line parameters
#     Args:
#       args ([str]): command line parameters as list of strings
#     Returns:
#       :obj:`argparse.Namespace`: command line parameters namespace
#     """
#     parser = argparse.ArgumentParser(
#         description="Location specific OSeMOSYS datafile generator")
#     parser.add_argument(
#         "--version",
#         action="version",
#         version="lcoe {ver}".format(ver=__version__))
#     parser.add_argument(
#         dest="capital_cost",
#         help="Capital cost of the plant in $/kWh",
#         type=float,
#         metavar="FLOAT")
#     parser.add_argument(
#         dest="annual_output",
#         help="Annual output of the plant in kWh",
#         type=float,
#         metavar="FLOAT")
#     parser.add_argument(
#         dest="annual_operating_cost",
#         help="Annual operating cost of the plant in $",
#         type=float,
#         metavar="FLOAT")
#     parser.add_argument(
#         dest="discount_rate",
#         help="Discount rate x where 0 <= x < 1",
#         type=float,
#         metavar="FLOAT")
#     parser.add_argument(
#         dest="lifetime",
#         help="Lifetime of the plant in years",
#         type=int,
#         metavar="INT")
#
#     return parser.parse_args(args)
#
# def main(args):
#     """Main entry point allowing external calls
#     Args:
#       args ([str]): command line parameter list
#     """
#     args = parse_args(args)
#     _logger.debug("Starting location specific calculations...")
#     print("LCOE is {}".format(
#         lcoe(args.annual_output,
#              args.capital_cost,
#              args.annual_operating_cost,
#              args.discount_rate,
#              args.lifetime)
#         ))
#     _logger.info("Script ends here")
#
#
# def run():
#     """Entry point for console_scripts
#     """
#     main(sys.argv[1:])
#
#
# if __name__ == "__main__":
#     run()
#

# def main(filepath, configuration_file):
#    """Generate spatially disaggregated values"""
#    # Read input data
#    with open(os.path.join(filepath, "data.csv", 'r') as datafile:
#       data = datafile.readlines()

<<<<<<< HEAD

#### ADD Validation of type of file that is imported


#PV_MG_CF = [0.12, 0.14,0.155,0.17,0.20]
#PV_SA_CF = [0.13,0.15, 0.16,0.18, 0.21]
#Wind_CF = [0.48,0.47,0.45,0.44,0.41,0.37,0.31,0.25,0.19,0.125]
#Battery = [8,13]

startyear = 2012
endyear = 2040
modeofoperation = [1, 2, 3]
region = "Kenya"
param_file = '/osemosys_shell_param.txt'
=======
cd = os.getcwd()
df = pd.read_csv(cd +'/data/GIS_data.csv')
inputFileName = cd +'/osemosys_shell_param.txt'
file_object = cd +'/GIS.txt'
life = pd.read_csv(cd +'/data/operational_life.csv')

trade = pd.read_csv(cd +'/data/capacitytoactivity.csv')
inputactivity = pd.read_csv(cd +'/data/inputactivity.csv', index_col=0)
demand = pd.read_csv(cd +'/data/demand.csv', index_col=0, header=0)
demand_urban = pd.read_csv(cd +'/data/demandprofile.csv', index_col=0, header=0)
demand_rural = pd.read_csv(cd +'/data/demandprofile_rural.csv', index_col=0, header=0)
capacityfactor_wind = pd.read_csv(cd +'/data/capacityfactor_wind.csv',index_col=None)
capacityfactor_wind['date'] = pd.to_datetime(capacityfactor_wind['date'],errors='coerce', format='%Y/%m/%d %H:%M')
capacityfactor_wind.index = capacityfactor_wind['date']
capacityfactor_wind = capacityfactor_wind.drop(columns=['date'])
capacityfactor_wind.columns = pd.to_numeric(capacityfactor_wind.columns)
capacityfactor_solar = pd.read_csv(cd +'/data/capacityfactor_solar.csv', index_col=None)
capacityfactor_solar['0'] = pd.to_datetime(capacityfactor_solar['0'], errors='coerce', format='%Y/%m/%d %H:%M')
#capacityfactor_solar = capacityfactor_solar.drop(columns=['date'])
capacityfactor_solar.columns = pd.to_numeric(capacityfactor_solar.columns)
capacityfactor_solar = pd.read_csv(cd +'/data/capacityfactor_solar.csv', header=0)
capitalcost_RET = pd.read_csv(cd +'/data/capitalcost_RET.csv', index_col=0, header=0)
capitalcost_RET.index = capitalcost_RET['CF']
trade_cost = pd.read_csv(cd +'/data/capitalcost.csv')

emissions = pd.read_csv(cd +'/data/emissions.csv', header=0)
variable_cost = pd.read_csv(cd +'/data/variable_cost.csv', header=0)
fixed_cost = pd.read_csv(cd +'/data/fixed_cost.csv', header=0)

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
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
startyear = 2012
endyear = 2040
modeofoperation = [1,2,3]
region = "Kenya"
>>>>>>> master

###############################
##    Reset all values      ##
##############################
<<<<<<< HEAD

## functions to run
##arguments from CMD are below
paths = (os.getcwd() + '\data')
path = os.getcwd()
file_object= os.getcwd() + '/GIS.txt'
#####################################

dict_df = load_csvs(paths)
outPutFile = make_outputfile(path, param_file)
outPutFile = functions_to_run(dict_df,outPutFile, startyear, endyear, region, modeofoperation)
=======
allLinesFromKenyaXy = ""
with open(inputFileName, "r") as inputFile:
   allLinesFromKenyaXy = inputFile.read()

outPutFile = allLinesFromKenyaXy

## functions to run
outPutFile = operational_life(df, outPutFile, region, life)
outPutFile = emissionactivity(df, outPutFile, startyear, endyear, region, emissions, modeofoperation)
outPutFile = variblecost(df, outPutFile, startyear, endyear, region, variable_cost, modeofoperation)
outPutFile = fixedcost(df, outPutFile, startyear, endyear, region, fixed_cost)



outPutFile = capitalcost_dynamic(df, outPutFile, elec, capitalcost_RET, trade_cost, wind_power, solar_power, capacityfactor_wind, capacityfactor_solar, startyear, endyear, region, modeofoperation)

outPutFile = capitalcost(df, outPutFile, trade_cost, startyear, endyear,region, modeofoperation)
outPutFile = capacityfactor_solar_battery8h(elec, outPutFile, df, capacityfactor_wind, capacityfactor_solar,
                                            solar_power, wind_power,
                                            timesliceDN, timesliceDE, timesliceED, timesliceEN, timesliceNE,
                                            timesliceND, batteryCF,
                                            battery13h, battery8h, startyear, endyear, months,region, modeofoperation)
outPutFile = capacityfactor_solar_battery13h(elec, outPutFile, df, capacityfactor_wind, capacityfactor_solar, solar_power, wind_power, timesliceDN, timesliceDE, timesliceED, timesliceEN, timesliceNE, timesliceND, batteryCF, battery13h, battery8h, startyear, endyear, months,region, modeofoperation)
outPutFile = capacityfactor_PV(elec, outPutFile, df, capacityfactor_wind, capacityfactor_solar, solar_power, wind_power, timesliceDN, timesliceDE, timesliceED, timesliceEN, timesliceNE, timesliceND, batteryCF, battery13h, battery8h, startyear, endyear, months,region, modeofoperation)
outPutFile = capacityfactor_wi(elec, outPutFile, df, capacityfactor_wind, capacityfactor_solar, solar_power, wind_power, timesliceDN, timesliceDE, timesliceED, timesliceEN, timesliceNE, timesliceND, batteryCF, battery13h, battery8h, startyear, endyear, months,region, modeofoperation)
outPutFile = capacityfactor(elec, outPutFile, df, capacityfactor_wind, capacityfactor_solar, solar_power, wind_power, timesliceDN, timesliceDE, timesliceED, timesliceEN, timesliceNE, timesliceND, batteryCF, battery13h, battery8h, startyear, endyear,region, modeofoperation)
outPutFile = capacitytoactivity(trade,outPutFile,region, modeofoperation)
outPutFile = totaltechnologyannualactivityupperlimit(df, outPutFile, startyear, endyear,region, modeofoperation)
outPutFile = SpecifiedDemandProfile(outPutFile, demand, demand_urban, demand_rural,startyear, endyear,region, modeofoperation)
outPutFile = inputact(outPutFile, inputactivity, startyear, endyearregion, modeofoperation)
outPutFile = specifiedannualdemand(outPutFile, demandregion, modeofoperation)
>>>>>>> master

#write data file
write_to_file(file_object, outPutFile)

<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> master
