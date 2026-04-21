import numpy as np

# States
states = [0, 1, 2, 3]

# Actions: 0=Open, 1=Close, 2=Wait
actions = [0, 1, 2]

# Discount factor
gamma = 0.9

# Transition probabilities P[s][a][s']
P = {
    0: {
        0: [(1.0, 0)],  # open when no one → still no one
        1: [(1.0, 0)],
        2: [(0.8, 0), (0.2, 1)]
    },
    1: {
        0: [(1.0, 3)],  # open → door open
        1: [(1.0, 2)],  # close → person waits
        2: [(0.5, 1), (0.5, 2)]
    },
    2: {
        0: [(1.0, 3)],
        1: [(1.0, 2)],
        2: [(1.0, 2)]
    },
    3: {
        0: [(1.0, 3)],
        1: [(1.0, 0)],
        2: [(1.0, 3)]
    }
}

# Rewards R[s][a]
R = {
    0: [ -5, 5, -1 ],
    1: [ 10, -2, -1 ],
    2: [ 10, -10, -1 ],
    3: [ 0, 5, -1 ]
}

# Initialize random policy
policy = np.random.choice(actions, size=len(states))

# Initialize value function
V = np.zeros(len(states))

def policy_evaluation(policy, V, theta=1e-4):
    while True:
        delta = 0
        for s in states:
            v = V[s]
            a = policy[s]
            V[s] = sum([prob * (R[s][a] + gamma * V[s_next])
                        for prob, s_next in P[s][a]])
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V

def policy_improvement(V):
    policy_stable = True
    new_policy = np.zeros(len(states), dtype=int)

    for s in states:
        action_values = []
        for a in actions:
            value = sum([prob * (R[s][a] + gamma * V[s_next])
                         for prob, s_next in P[s][a]])
            action_values.append(value)

        best_action = np.argmax(action_values)

        if best_action != policy[s]:
            policy_stable = False

        new_policy[s] = best_action

    return new_policy, policy_stable

# Policy Iteration
iteration = 0
while True:
    iteration += 1
    print(f"\nIteration {iteration}")

    V = policy_evaluation(policy, V)
    new_policy, stable = policy_improvement(V)

    print("Policy:", new_policy)
    print("Value Function:", V)

    if stable:
        break

    policy = new_policy

# Final Output
action_names = ["Open", "Close", "Wait"]

print("\nOptimal Policy:")
for s in states:
    print(f"State {s} → {action_names[policy[s]]}")