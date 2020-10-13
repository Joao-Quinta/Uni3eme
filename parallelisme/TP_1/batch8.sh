#!/bin/sh

#SBATCH --cpus-per-task=1
#SBATCH --job-name=bCast
#SBATCH --ntasks=8
#SBATCH --time=0-00:03:00
#SBATCH --mail-user=Joao.Costa@etu.unige.ch
#SBATCH --partition=debug-EL7
#SBATCH --output=outBcast8.out
#SBATCH --constraint=E5-2660V0

srun ./hello
