#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm> // For min/max functions

// Initialize the MPI environment and set up basic MPI file I/O for timing measurements of different algorithmic growths.
// The code distributes algorithmic tasks across MPI processes and measures execution time, writing the results to a file.
// If a task is predicted to exceed a certain threshold, it is skipped to prevent long execution times.

// Linear Growth: O(n)
// Increases linearly with the size of the input.
void linear_growth(int n) {
    int sum = 0;
    for(int i = 0; i < n; i++) {
        sum += i;
    }
}

// Quadratic Growth: O(n^2)
// Increases quadratically with the size of the input.
void quadratic_growth(int n) {
    int sum = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            sum += i + j;
        }
    }
}

// Polynomial Growth (cubic): O(n^3)
// Increases cubically with the size of the input.
void polynomial_growth(int n) {
    int sum = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            for(int k = 0; k < n; k++) {
                sum += i + j + k;
            } 
        }
    }
}

// Exponential Growth: O(2^n)
// Increases exponentially with the size of the input.
int exponential_growth(int n) {
    if(n == 0) return 1;
    return exponential_growth(n - 1) + exponential_growth(n - 1);
}

// Factorial Growth: O(n!)
// Increases factorially with the size of the input.
int factorial_growth(int n) {
    if(n == 0) return 1;
    return n * factorial_growth(n - 1);
}

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);
    int world_size, world_rank, name_len;
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Get_processor_name(processor_name, &name_len);

    MPI_File fh;
    char file_name[] = "timings.txt";
    MPI_File_open(MPI_COMM_WORLD, file_name, MPI_MODE_CREATE | MPI_MODE_WRONLY, MPI_INFO_NULL, &fh);

    char* algorithm_names[] = {"Linear", "Quadratic", "Polynomial", "Exponential", "Factorial"};
    
    // Iterate over a fixed set of sizes to measure the performance of each algorithm.
    for(int iteration = 1; iteration <= 10; iteration++) {
        int n = iteration * 2; // Adjust n for each iteration to manage execution time.
        double start = MPI_Wtime();
        char* algorithm_name = "";

        // Select an algorithm based on the rank modulo the number of algorithms.
        switch(world_rank % 5) {
            case 0: linear_growth(n); algorithm_name = algorithm_names[0]; break;
            case 1: quadratic_growth(n); algorithm_name = algorithm_names[1]; break;
            case 2: polynomial_growth(n); algorithm_name = algorithm_names[2]; break;
            case 3: 
                if(n > 10) { // Skip exponential growth for n > 10 to avoid long computation times.
                    printf("Skipping exponential growth for n=%d due to expected long computation time.\n", n);
                    MPI_Finalize();
                    return 0;
                }
                exponential_growth(n); algorithm_name = algorithm_names[3]; break;
            case 4: 
                if(n > 6) { // Skip factorial growth for n > 6 to avoid long computation times.
                    printf("Skipping factorial growth for n=%d due to expected long computation time.\n", n);
                    MPI_Finalize();
                    return 0;
                }
                factorial_growth(n); algorithm_name = algorithm_names[4]; break;
        }

        double end = MPI_Wtime();
        double time_microseconds = (end - start) * 1000000;

        // Construct the output string with timing information.
        char output[200];
        snprintf(output, sizeof(output), "Processor %s, Rank %d, Algorithm %s, Input Value %d, Time %f microseconds\n",
                 processor_name, world_rank, algorithm_name, n, time_microseconds);

        // Write the output to the file at a calculated offset to avoid write conflicts.
        MPI_Offset offset = world_rank * 10 * sizeof(output) + (iteration - 1) * sizeof(output);
        MPI_File_write_at(fh, offset, output, strlen(output), MPI_CHAR, MPI_STATUS_IGNORE);
    }

    MPI_File_close(&fh);
    MPI_Finalize();
    return 0;
}
