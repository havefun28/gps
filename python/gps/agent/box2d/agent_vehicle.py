""" This file defines an agent for the vehicle simulator. """
from copy import deepcopy
import numpy as np
from gps.agent.agent import Agent
from gps.agent.agent_utils import generate_noise, setup
from gps.agent.config import AGENT_VEH
# from gps.proto.gps_pb2 import ACTION
from gps.sample.sample import Sample


class AgentVeh(Agent):
	"""
    All communication between the algorithms and Vehicle is done through
    this class.
    """
    def __init__(self, hyperparams):
	    config = deepcopy(AGENT_VEH)
	    config.update(hyperparams)
	    Agent.__init__(self, config)

	    self._setup_conditions()
	    #TODO: customize world for veh
	    self._setup_world(self._hyperparams["world"],
	                      self._hyperparams["target_state"],
	                      self._hyperparams["render"])
	
	def _setup_conditions(self):
		"""
        Helper method for setting some hyperparameters that may vary by
        condition.
        """
		# TODO: specify the fields
		conds = self._hyperparams['conditions']
        for field in ('xxxx'):
        	self._hyperparams[field] = setup(self._hyperparams[field], conds)

	def _setup_world(self):
		"""
        Helper method for handling setup of the Box2D world.
        """
        self.x0 = self._hyperparams["x0"]  # initial state
        self._worlds = [world(self.x0[i], target, render)
                        for i in range(self._hyperparams['conditions'])]
    
    def sample(self, policy, condition, verbose=False, save=True, noisy=True):
        """
        Runs a trial and constructs a new sample containing information
        about the trial.

        Args:
            policy: Policy to to used in the trial.
            condition (int): Which condition setup to run.
            verbose (boolean): Whether or not to plot the trial (not used here).
            save (boolean): Whether or not to store the trial into the samples.
            noisy (boolean): Whether or not to use noise during sampling.
        """

        # reset the world and assign the initialized state to new_sample
        self._worlds[condition].run()
        self._worlds[condition].reset_world()
        b2d_X = self._worlds[condition].get_state()
        new_sample = self._init_sample(b2d_X)

        # initialize a dummy action sequence
        U = np.zeros([self.T, self.dU])
        if noisy:
            noise = generate_noise(self.T, self.dU, self._hyperparams)
        else:
            noise = np.zeros((self.T, self.dU))
        for t in range(self.T):
            X_t = new_sample.get_X(t=t)
            obs_t = new_sample.get_obs(t=t)
            U[t, :] = policy.act(X_t, obs_t, t, noise[t, :])
            if (t+1) < self.T:
                for _ in range(self._hyperparams['substeps']):
                    self._worlds[condition].run_next(U[t, :])
                b2d_X = self._worlds[condition].get_state()
                self._set_sample(new_sample, b2d_X, t)
        new_sample.set(ACTION, U)
        if save:
            self._samples[condition].append(new_sample)
        return new_sample

    def _init_sample(self, b2d_X):
        """
        Construct a new sample and fill in the first time step.
        """
        sample = Sample(self)
        self._set_sample(sample, b2d_X, -1)
        return sample

    def _set_sample(self, sample, b2d_X, t):
        for sensor in b2d_X.keys():
            sample.set(sensor, np.array(b2d_X[sensor]), t=t+1)
            