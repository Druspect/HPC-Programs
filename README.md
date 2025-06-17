# HPC Programs

This repository contains a collection of small experiments and test programs for exploring high performance computing concepts.  Code is written in Python, C, and shell scripts.  Examples include MPI "hello world", Collatz calculations, algorithmic timing tests and small Monte‑Carlo demonstrations.

## Prerequisites

* Python 3.8+ with `mpi4py` for the MPI Python examples
* An MPI implementation such as MPICH or OpenMPI to compile and run the C and Python MPI programs
* Optional utilities: `dos2unix` for line‑ending conversion

## Building and Running

### Compile the C example

```bash
mpicc test_mpi.c -o test_mpi
mpirun -np 4 ./test_mpi
```

### Run the MPI Python example

```bash
mpirun -np 4 python py_mpi_test.py
```

### Run the Collatz scripts

Sequential version:

```bash
bash 3xrun.sh
```

MPI version:

```bash
bash 3xrun_mpi.sh
```

### Other utilities

* `HPC_eff.py` – measures how different algorithmic complexities scale with input size
* `single_monte.py` – simple Monte‑Carlo Pi estimation
* `MpiAlg.py` – MPI based timing of several sorting algorithms (work in progress)

Output logs and generated CSV files are ignored via `.gitignore`.

## License

This project is released under the MIT License.
