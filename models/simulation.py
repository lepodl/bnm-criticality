# -*- coding: utf-8 -*- 
# @Time : 2023/10/20 17:36 
# @Author : lepold
# @File : simulation.py
from configs.parameters import check_custom_params, nested_update

class Simulation:
    def __init__(self, network, **sim_spec):
        """
           Simulation class.
           An instance of the simulation class with the given parameters.
           Can be created as a member class of a multiarea_model instance
           or standalone.

           Parameters
           ----------
           network:
                a instance of Network
           sim_spec :
               detailed customized setting of simulation
        """
        sim_params = network.params["sim_params"]
        check_custom_params(sim_params, sim_spec)
        nested_update(sim_params, sim_spec)
        for key in sim_params:
            self.__setattr__(key, sim_spec[key])

        # assign parameters of single node
        for key in network.params["single_node_params"]:
            self.__setattr__(key, network.params["single_node_params"[key]])



