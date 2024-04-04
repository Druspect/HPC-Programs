#!/bin/bash
#SBATCH --job-name=collatz_%j
#SBATCH --output=3x1_res_%j.log
#SBATCH --error=3x1_err_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=15:00:00

module load python39

# Create a temporary file to store the pairs
TEMP_FILE=$(mktemp)

for i in {1..100000}
do
  RANDOM_NUM=$(python -c "import random; print(random.randint(1, 100000000000))")
  ITERATIONS=$(python 3xplus1.py $RANDOM_NUM)
  # Storing the pairs (initial number and iterations) in the temporary file
  echo "$RANDOM_NUM,$ITERATIONS" >> $TEMP_FILE
done

# Moving the temporary file to a permanent location
mv $TEMP_FILE collatz_pairs_${SLURM_JOB_ID}.csv

echo "Pairs of initial numbers and iterations are stored in collatz_pairs.csv"

