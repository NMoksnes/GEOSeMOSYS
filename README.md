# GEOSeMOSYS

# Usecase
This code is to help build location specific parameters in OSeMOSYS to a text file to run in GNU MathProg.

# What the code builds
Parameters that are built for each location are:

- SpecifiedAnnualDemand
- VariableCost
- OperationalCost
- FixedCost
- Emissionactivity
- TotalTechnologyAnnualActivity
- InputActivity
- OutputActivity
- SpecifiedDemandProfile
- CapitalCost which is dynamic for renewable technologies based on Capacity Factor
- CaptialCost which is static over time
- CapacitytoActivity
- CapacityFactor

The run_datafile.py calls the functions in build_data_file.py the OSeMOSYS file for your locations with a base OSeMOSYS file which contains all parameters (osemosys_shell_param.txt).

# How to run the file
The file should be run from the command prompt.
You need to specify which folder your "Folder containing CSV data files", "Path to the OSeMOSYS template" and "Name and path of the output file"

# python run_datafile.py data osemosys_shell_param.txt results/GIS.txt

The data file structure needs to follow the same naminig and structure as in test/data. However you don't need to run all parameters, the code will check what files are present and only run those parameters.