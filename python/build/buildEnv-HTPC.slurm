#!/bin/bash
#SBATCH -p compute
#SBATCH -t 10:00
#SBATCH -c 1
#SBATCH --mem=8G

module load python/3.11.4

python -m venv ./../env

./../env/Scripts/python3 -m pip install --upgrade pip

./../env/Scripts/pip3 install -r requirements.txt

source ./../env/bin/activate
