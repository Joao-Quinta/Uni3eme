#!/bin/sh
#SBATCH --cpus-per-task=1
#SBATCH --job-name=laplace
#SBATCH --ntasks=1
#SBATCH --time=0-00:20:00
#SBATCH --mail-user=Joao.Costa@etu.unige.ch
#SBATCH --mail-type=END
#SBATCH --partition=debug-EL7
#SBATCH --clusters=baobab
#SBATCH --output=teste.out


srun ./laplace 2000 2000 500 tes
