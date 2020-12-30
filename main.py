import gym
import numpy as np
from on_policy import on_policy_first_visit_control

if __name__ == "__main__":
    # setup gym environment
    env = gym.make('Blackjack-v0')
    env.reset()

    # get necessary environment variables
    # num_states = env.nS
    # num_actions = env.nA
    # state_transition = env.P
    #
    # print(num_states)
    # print(num_actions)
    # print(state_transition)
