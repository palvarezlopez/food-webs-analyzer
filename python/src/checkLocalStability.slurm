#!/bin/bash
#SBATCH -p compute
#SBATCH -t 10:00
#SBATCH -c 1
#SBATCH --mem=64G

python foodwebDynamics.py --checkLocalStability
