"""
Sample file for learning openai gym
"""

import logging
from rich.logging import RichHandler
import rich.traceback
import gym
import time

rich.traceback.install()

# create logger
logging.basicConfig(
    level=logging.INFO, format="%(message)s", handlers=[RichHandler()]
)
log = logging.getLogger("gym_logger")

env = gym.make("BreakoutNoFrameskip-v4", render_mode="human")
env.reset()

print("Observation Space ", env.observation_space)
print("Action Space ", env.action_space)

obs = env.reset()

for i in range(1000):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    time.sleep(0.01)
env.close()

# env = gym.make("MountainCar-v0", render_mode="human")
# # Observation and action space
# obs_space = env.observation_space
# action_space = env.action_space
# print("The observation space: {}".format(obs_space))
# print("The action space: {}".format(action_space))

# # # reset the environment and see the initial observation
# # obs = env.reset()
# # print("The initial observation is {}".format(obs))

# # # Sample a random action from the entire action space
# # random_action = env.action_space.sample()

# # # # Take the action and get the new observation space
# # new_obs, reward, done, info = env.step(random_action)
# # print("The new observation is {}".format(new_obs))
# # env_screen = env.render()
# # print(env_screen)
# # plt.imshow(env_screen[0])
# # plt.show()
# # env.close()

# logging.info(type(env.observation_space))
# logging.info(env.observation_space.high)

# # num_steps = 1500

# # obs = env.reset()

# # for step in range(num_steps):
# #     action = env.action_space.sample()
# #     obs, reward, done, info = env.step(action)
# #     env.render()
# #     time.sleep(0.001)
# #     if done:
# #         env.reset()

# # env.close()
