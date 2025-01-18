# Reinforcement-Learning-Taxi-v3
This repository tackles the Taxi-v3 problem from OpenAI Gym, a classic gridworld challenge in Reinforcement Learning (RL). The project demonstrates:

* Training an RL agent using the Q-learning algorithm.
* Visualization of the environment with step-by-step agent actions.
* Insights into the reward system, exploration-exploitation strategies, and training hyperparameters.

Whether you're a student, researcher, or RL enthusiast, this repository provides an accessible starting point for learning RL concepts and applying them in simulated environments.

# 🚕 Classic Gym's Taxi Problem: A Reinforcement Learning Case Study

Here's an demonstration on how to solve the **Taxi-v3 problem** using **Reinforcement Learning (RL)**. The project explores Q-Learning, a model-free RL algorithm, and uses **OpenAI Gym** to simulate the Taxi environment. (Refer slides)

### Problem visualization:

![Video](./av/taxi_problem_gif.gif)


## 📂 Repository Contents
- **Code**: Python implementation for training and testing the taxi agent using Q-learning.
- **Presentation**: A detailed PowerPoint presentation explaining the problem, solution approach, and results.
- **Environment Setup**: Instructions to set up the environment for running the code.

---

## 🌟 Problem Overview
The Taxi problem involves navigating a taxi through a grid to:
1. **Pick up** a passenger from a designated location.
2. **Drop off** the passenger at the destination.
3. Optimize actions to maximize rewards.

### **Key Concepts**
- **State Space**: Taxi position, passenger location, and destination.
- **Action Space**: Move (North, South, East, West), Pick Up, Drop Off.
- **Rewards**: Positive for successful drops, negative for invalid actions, and step penalties.

---

## 🛠️ Getting Started

### Prerequisites
1. **Python** (>=3.7)
2. **OpenAI Gym** (tested with version 0.16.0)
3. **NumPy**

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MohanKrishnaGR/Reinforcement-Learning-Taxi-v3.git
   cd Reinforcement-Learning-Taxi-v3 
   ```

2. Install dependencies:
    ```bash
    pip install gym==0.16 numpy
    ```

---
## 🚀 Running the Code
1. Run the Python script:
    ```bash
    python taxi_problem.py
    ```
2. Watch the agent learn and test the trained model.
---
## 📊 Results

* **Training**: The agent learns the optimal policy over multiple episodes using the Q-learning algorithm.

* **Testing**: The trained agent successfully navigates the gridworld to maximize rewards.

* **Visualization**: The environment is rendered step-by-step to visualize the agent’s behavior after training.
---
## 📜 Presentation
The PowerPoint presentation provides:

* An introduction to Reinforcement Learning and the Taxi Problem.
* A walkthrough of Q-learning and its application to the problem.
* Results with key takeaways.
---
### End Note

Thank you for your interest in this project! We welcome any feedback. Feel free to reach out to us.