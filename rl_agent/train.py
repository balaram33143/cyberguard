 
import gym
from gym import spaces
import numpy as np
from stable_baselines3 import DQN
import os

class CyberEnv(gym.Env):
    def __init__(self):
        super(CyberEnv, self).__init__()
        
        self.observation_space = spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)
        self.action_space = spaces.Discrete(4)
        self.state = self._next_observation()
        self.steps = 0

    def _next_observation(self):
        return np.random.rand(5)

    def reset(self):
        self.steps = 0
        self.state = self._next_observation()
        return self.state

    def step(self, action):
        self.steps += 1
        reputation_score = self.state[0]
        user_habit_score = self.state[4]
        risky = reputation_score < 0.3 and user_habit_score > 0.8

        if action == 2 and risky:
            reward = 10
        elif action == 1 and risky:
            reward = 5
        elif action == 0 and risky:
            reward = -10
        elif not risky and action in [1, 2]:
            reward = -5
        else:
            reward = 1

        done = self.steps >= 50
        self.state = self._next_observation()
        return self.state, reward, done, {}

env = CyberEnv()
model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

os.makedirs("rl_agent/model", exist_ok=True)
model.save("rl_agent/model/cyberguard_agent")
