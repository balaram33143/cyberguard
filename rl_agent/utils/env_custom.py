# rl_agent/utils/env_custom.py

import gym
from gym import spaces
import numpy as np
from rl_agent.utils.reward_shaping import custom_reward

class CyberGuardEnv(gym.Env):
    def __init__(self):
        super(CyberGuardEnv, self).__init__()
        self.observation_space = spaces.Box(low=0, high=1, shape=(10,), dtype=np.float32)
        self.action_space = spaces.Discrete(2)  # 0 = allow, 1 = block

    def reset(self):
        self.state = np.random.rand(10)
        return self.state

    def step(self, action):
        phishing_detected = np.random.rand() < 0.2
        false_positive = (action == 1 and not phishing_detected)

        info = {
            "phishing_detected": phishing_detected and action == 1,
            "false_positive": false_positive
        }

        done = True  # Single-step episode for simplicity
        reward = custom_reward(self.state, action, done, info)

        return self.state, reward, done, info

    def render(self, mode='human'):
        pass
