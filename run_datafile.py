"""
This script is to build a OSeMOSYS data file where you have many locations/countries.
The script is user defined in the geographical, technology, year, timeslice dimesions, which makes the script very flexible.

__author__ = "Nandi Moksnes, Sebastian Moksnes"
__copyright__ = "Nandi Moksnes"
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


param_file = '/osemosys_shell_param.txt'

###############################
##    Reset all values      ##
##############################

## functions to run
##arguments from CMD are below

paths = (os.getcwd() + '\data')
path = os.getcwd()
file_object= os.getcwd() + r'\results\GIS.txt'
#####################################

dict_df = load_csvs(paths)
outPutFile = make_outputfile(path, param_file)
outPutFile = functions_to_run(dict_df,outPutFile)

#write data file
write_to_file(file_object, outPutFile)

