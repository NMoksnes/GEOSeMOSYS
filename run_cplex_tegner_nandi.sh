#!/bin/bash

# Set the allocation to be charged for this job
#SBATCH -A 2019-62

# The name of the script is myjob
#SBATCH -J myjob

# 10 hour wall-clock time will be given to this job
#SBATCH -t 23:00:00

# Number of nodes
#SBATCH --nodes=1
# Number of MPI processes per node
#SBATCH --ntasks-per-node=24

#SBATCH --mail-type=ALL

#SBATCH -e error_file_ref.e
#SBATCH -o output_file_ref.o

############### Here finished the SLURM commands #############

# Load the glpk mode which includes glpsol
module add glpk/4.65-update

# Set the path to cplex
export PATH=/cfs/klemming/nobackup/n/nandi/cplex/bin/x86-64_linux/:$PATH

# filename is the name of DD file and lpName is the name of the output from glpsol
lpName=Kenya_BIG_ALL_REF11_8.lp

# this command starts glpsol (GNU Mathprog)
# Only generate the .lp file using flag --check

glpsol -m OSeMOSYS_fast.txt -d Kenya_BIG_ALL_REF11.txt --wlp Kenya_BIG_ALL_REF11.lp --check

# break mean make a new empty file for mycplexcommands
rm -f mycplexcommands
touch mycplexcommands

# echo writes each line to mycplexcommands that I want to execute in CPLEX

echo "read Kenya_BIG_ALL_REF11.lp" >> mycplexcommands
echo "set simplex tolerances optimality 1e-04" >>mycplexcommands
echo "set simplex dgradient 5" >>mycplexcommands
echo "set output clonelog 1" >>mycplexcommands
echo "set threads 24"       >> mycplexcommands
echo "optimize"             >> mycplexcommands
echo "write"                >> mycplexcommands
echo "Kenya_BIG_ALL_REF11.sol"    >> mycplexcommands
echo "quit"                 >> mycplexcommands


# executes the cplex script written above
# Should set the path to CPLEX
cplex < mycplexcommands

# the sol file is input to transform python script
#
python transform_updated.py Kenya_BIG_ALL_REF11.sol Kenya_BIG_ALL_solved_REF11.txt


