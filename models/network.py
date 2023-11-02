# -*- coding: utf-8 -*- 
# @Time : 2023/10/20 15:18 
# @Author : lepold
# @File : network.py


from configs.parameters import network_params, nested_update, check_custom_params, flat_dict
import torch
from copy import deepcopy
import os
from config import data_path
import json
import time
import pprint
from .simulation import Simulation

class Network:

    def __init__(self, network_spec, simulation=False,
                 analysis=False):
        """
        network model class.
        An instance of the network model with the given parameters.

        Parameters
        ----------
        network_spec : dict or str
            Specify the network. If it is of type dict, the parameters defined
            in the dictionary overwrite the default parameters defined in
            default_params.py.
            If it is of type str, the string defines the time and label of a previously
            initialized model instance that is now loaded, e.g., "2023-10-20|29"
        simulation : bool
            whether to create an instance of the simulation class as member.
        analysis : bool
            whether to create an instance of the analysis class as member.

        """
        self.params = deepcopy(network_params)
        if isinstance(network_spec, dict):
            print("Initializing network from dictionary.")
            check_custom_params(self.params, network_spec)
            custom_params = network_spec
            current_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            rand_data_label = torch.randint(1000, (1, )).item()
            current_working_dir = os.path.join(data_path, current_time)
            os.makedirs(current_working_dir, exist_ok=True)
            tmp_parameter_fn = os.path.join(current_working_dir,
                                            'custom_{}_parameter_dict.json'.format(rand_data_label))
            nested_update(self.params, custom_params)
            with open(tmp_parameter_fn, 'w') as f:
                json.dump(self.params, f)
            # identification of this class
            self.label = current_time + "|{}".format(rand_data_label)
        else:
            print("Initializing network from label.")
            self.label = network_spec
            data, label = network_spec.split("|")
            parameter_fn = os.path.join(data_path,
                                        data,
                                        '{}_config'.format(label))
            with open(parameter_fn, 'r') as f:
                self.params = json.load(f)
        # for key, value in flat_dict(self.params):
        #     self.__setattr__(key, value)
        if simulation:
            self.simulation = Simulation(self)
        if analysis:
            raise NotImplementedError

    def __str__(self):
        s = "brain network {} with custom parameters: \n".format(self.label)
        s += pprint.pformat(self.params, width=1)
        return s

    def __eq__(self, other):
        return self.label == other.label





