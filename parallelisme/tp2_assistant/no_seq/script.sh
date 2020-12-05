#!/bin/sh 
#SBATCH --cpus-per-task=1
#SBATCH --job-name=laplace
#SBATCH --ntasks=1
#SBATCH --time=0-00:20:00
#SBATCH --mail-user=Joao.Costa@etu.unige.ch
#SBATCH --mail-type=END
#SBATCH --partition=debug
#SBATCH --clusters=baobab
#SBATCH --output=slurm-%J.out


srun your_binary
