from mpi4py import MPI

def main():
    # Initialize the MPI environment
    MPI.Init()
    
    # Get the size of the MPI world
    world_size = MPI.COMM_WORLD.Get_size()
    
    # Get the rank of the current process
    world_rank = MPI.COMM_WORLD.Get_rank()
    
    # Get the name of the processor
    processor_name = MPI.Get_processor_name()
    
    # Print a hello message from the processor
    print(f"Hello world from processor {processor_name}, rank {world_rank} out of {world_size} processors")
    
    # Finalize the MPI environment
    MPI.Finalize()

if __name__ == "__main__":
    main()