import numpy as np
import gym
import random
import time

# create Taxi environment
env = gym.make('Taxi-v3')

# Display the environment's action space and observation space
print("Action space:", env.action_space)
print("Observation space:", env.observation_space)

def epsilon_greedy(q_table, state, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Explore: Random action
    else:
        return np.argmax(q_table[state])  # Exploit: Best action from Q-table

# Q-learning parameters
alpha = 0.1   # Learning rate
gamma = 0.99  # Discount factor
epsilon = 0.1 # Exploration factor
episodes = 1000
q_table = np.zeros([env.observation_space.n, env.action_space.n])

# Training the agent
for episode in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        action = epsilon_greedy(q_table, state, epsilon)
        next_state, reward, done, _ = env.step(action)
        q_table[state, action] = q_table[state, action] + alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state, action])
        state = next_state
        total_reward += reward
    # Optionally print progress
    if episode % 100 == 0:
        print(f"Episode {episode}/{episodes}, Total Reward: {total_reward}")

# Evaluating the trained agent with visualization
state = env.reset()
done = False
total_reward = 0

print("\nVisualizing the trained agent's behavior...\n")
time.sleep(1)  # Pause before visualization starts
while not done:
    env.render()  # Render the current state of the environment
    action = np.argmax(q_table[state])  # Use the best-known action
    next_state, reward, done, _ = env.step(action)
    state = next_state
    total_reward += reward
    time.sleep(1)  # Add a delay to see each step clearly

env.render()  # Render the final state
print("Total reward after training:", total_reward)

env.close()