#!/bin/bash
#SBATCH --job-name=collatz_mpi_%j
#SBATCH --output=3x1_res_%j.log
#SBATCH --error=3x1_err_%j.err
#SBATCH --time=30:00

module load python39
module load openmpi

mpirun python 3xplus1_mpi.py > collatz_pairs_${SLURM_JOB_ID}.csv

echo "Pairs of initial numbers and iterations are stored in collatz_pairs.csv"

