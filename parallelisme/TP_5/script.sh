#!/bin/sh
#SBATCH --cpus-per-task=1
#SBATCH --job-name=mpi_simple
#SBATCH --ntasks=1
#SBATCH --time=0-01:00:00
#SBATCH --mail-user=Joao.Costa@etu.unige.ch
#SBATCH --mail-type=END
#SBATCH --partition=debug-EL7
#SBATCH --clusters=baobab
#SBATCH --output=t.out


srun mpiRun -np 1 ./julia_mpi_simple -2 -2 2 2 -0.8 0.156 100 600 600 4 teste.pgm
