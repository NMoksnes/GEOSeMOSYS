# GEOSeMOSYS
Python code to build location specific OSeMOSYS data file to run in GNU MathProg. 
The code is built on the /data/GIS_data.csv which then builds all the spatially distributed technologies for the different parameters.

The run_datafile.py calls the functions in build_data_file.py the OSeMOSYS file for all 376 locations with a base OSeMOSYS file which contains all paramaters and central grid data which is not handled in the location specific iteration.

/data contains specific data for Kenya.

The run_cplex_tegner_REF.sh is the bash file for running the script on PDC/Tegner.
