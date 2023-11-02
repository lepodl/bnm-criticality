# -*- coding: utf-8 -*- 
# @Time : 2023/10/20 15:20 
# @Author : lepold
# @File : config.py


# Absolute path of repository
base_path = r"E:\PycarmProjects2\bnm-criticality"
# Place to store simulations
data_path = r"E:\PycarmProjects2\bnm-criticality\results"
# Template for job scripts
jobscript_template = '''
# Instruction for the queuing system

mpirun python {base_path}/run_simulation.py {label}'''

"""
Here is an example for the Slurm queueing system:

# jobscript_template = '''#!/bin/bash
# #SBATCH --job-name MAM
# #SBATCH -o {sim_dir}/{label}.%j.o
# #SBATCH -e {sim_dir}/{label}.%j.e
# #SBATCH --mem=120G
# #SBATCH --time=06:00:00
# #SBATCH --exclusive
# #SBATCH --cpus-per-task={local_num_threads}
# #SBATCH --ntasks={num_processes}
# mpirun python {base_path}/run_simulation.py {label} {network_label}'''
"""

# Command to submit jobs on the local cluster
submit_cmd = None
