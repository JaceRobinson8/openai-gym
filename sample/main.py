"""
Sample file for learning openai gym
"""

import logging
from rich.logging import RichHandler

import gym
import matplotlib.pyplot as plt

# create logger
logging.basicConfig(
    level=logging.INFO, format="%(message)s", handlers=[RichHandler()]
)
logger = logging.getLogger("gym_logger")

env = gym.make('MountainCar-v0', new_step_api=False)
obs_space = env.observation_space
action_space = env.action_space
logger.info("The observation space: %s", obs_space)
logger.info("The action space: %s", action_space)
 
obs = env.reset()
logger.info("The initial observation is %s", obs)
random_action = env.action_space.sample()
new_obs, reward, done, info = env.step(random_action) # type: ignore
logger.info("The new observation is %s", new_obs)

env.render(mode = "human")
env.close()
