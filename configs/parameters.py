# -*- coding: utf-8 -*- 
# @Time : 2023/10/20 15:19 
# @Author : lepold
# @File : parameters.py

"""
Single-node parameters
"""
# dictionary defining single-node parameters
single_node_params = {
    # Overall effective external input
    "I_0": 0.382,
    # Modulation of 'I_0' for excitatory, respectively, inhibitory population
    "W_e": 1.,
    "W_i": 0.7,
    # Local excitatory recurrence
    "w+": 1.4,
    # Excitatory synaptic coupling
    "J_nmda": 0.15,
    # Feedback inhibitory synaptic coupling,
    # obtained by FIC
    "J_i": None,
    # Structural connectivity matrix,
    # obtained by dwMRI tractography
    "C_ij": None,
    # Long-range excitation
    # Obtained by FC or criticality fitting
    "w_ij_lre": None,
    # Feedforward inhibition
    # Obtained by FC or criticality fitting
    "w_ij_ffi": None,
    # Parameters of excitatory population’s frequency-current (f-I) function
    "a_e": 310.,
    "b_e": 125.,
    "d_e": 0.16,
    # Parameters of inhibitory population’s f-I function
    "a_i": 615.,
    "b_i": 177.,
    "d_i": 0.087,
    # Rate of saturation
    "gamma_e": 6.41e-4,
    "gamma_i": 1.e-3,
    # Time scales of synaptic activity
    "tau_e": 100.,
    "tau_i": 10.,
    # Noise scaling
    "sigma": 0.01}

sim_params = {
    # master seed for random number generators
    'rng_seed': 1,
    # simulation step (in ms)
    'dt': 1.,
    # simulated time (in ms)
    't_sim': 10.0,
    # no. of MPI processes:
    'num_processes': 1,
    # no. of threads per MPI process':
    'local_num_threads': 1,
    # Areas represented in the network
    'areas_simulated': "brain_nn",
}

network_params = {"sim_params": sim_params, "single_node_params": single_node_params}

def nested_update(d, customized_d):
    for key in customized_d:
        if isinstance(customized_d[key], dict) and key in d:
            nested_update(d[key], customized_d[key])
        else:
            d[key] = customized_d[key]


def check_custom_params(d, customized_d):
    for key, val in customized_d.items():
        if isinstance(val, dict):
            try:
                check_custom_params(d[key], customized_d[key])
            except KeyError:
                raise KeyError('Unused setup in custom parameter dictionary: {}'.format(key))
        else:
            try:
                def_val = d[key]
            except KeyError:
                raise KeyError('Unused key in custom parameter dictionary: {}'.format(key))

def flat_dict(nested_dict):
    for key in nested_dict:
        for nested_key in nested_dict[key]:
            yield nested_key, nested_dict[key][nested_key]