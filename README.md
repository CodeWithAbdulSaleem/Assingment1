# 🚪 Automatic Door Control using Reinforcement Learning (Policy Iteration)

## 📌 Problem Statement

Design a Reinforcement Learning model for an automatic door system that decides whether to:

* Open the door
* Keep it closed
* Wait

The system should use **Policy Iteration** to learn the optimal behavior based on environmental conditions.

---

## 🧠 Concept Used

This project is based on **Markov Decision Process (MDP)** and solved using:

* States (S)
* Actions (A)
* Rewards (R)
* Transition Probabilities (P)
* Policy Iteration Algorithm

---

## 🏗️ Environment Design

### 🔹 States

| State | Description        |
| ----- | ------------------ |
| 0     | No person detected |
| 1     | Person approaching |
| 2     | Person waiting     |
| 3     | Door open          |

---

### 🔹 Actions

| Action | Description |
| ------ | ----------- |
| 0      | Open Door   |
| 1      | Close Door  |
| 2      | Wait        |

---

### 🔹 Rewards

| Scenario                        | Reward |
| ------------------------------- | ------ |
| Open when person present        | +10    |
| Open when no one present        | -5     |
| Keep closed when no one present | +5     |
| Wait unnecessarily              | -1     |
| Keep closed when person waiting | -10    |

---

## 🔄 Policy Iteration Steps

1. Initialize random policy
2. Perform **Policy Evaluation**
3. Perform **Policy Improvement**
4. Repeat until policy converges

---

## ⚙️ Requirements

* Python 3.x
* NumPy

Install using:

```bash
pip install numpy
```

---

## ▶️ How to Run

```bash
python automatic_door_rl.py
```

---

## 📊 Output

* Optimal policy for each state
* State value function

---

## 🧪 Example Output

```
Optimal Policy:
State 0 → Close
State 1 → Open
State 2 → Open
State 3 → Wait

Value Function:
[5.0, 9.5, 10.2, 8.7]
```

---

## 📚 Learning Outcome

* Understanding MDP formulation
* Implementing Policy Iteration
* Applying RL to real-world automation systems

---

## 👨‍💻 Author

Abdul Saleem
