#markov chains:the future depends only on the resent state not on past history
import numpy as np
import matplotlib.pyplot as plt
transition_matrix=np.array([[0.6,0.3,0.1],[0.2,0.5,0.3],[0.1,0.3,0.6]])
states=['down','same','up']
def simulate_markov_chain(transition_matrix,initial_state=1,n_steps=50):
    state=initial_state
    chain=[state]
    for i in range(n_steps):
        state=np.random.choice([0,1,2],p=transition_matrix[state])
        chain.append(state)
    return chain
np.random.seed(42)
chain=simulate_markov_chain(transition_matrix,initial_state=1,n_steps=100)
plt.figure(figsize=(12,4))
plt.plot(chain,marker='o',linestyle='-',color='b')
plt.yticks([0,1,2],states)
plt.title('Working of Markov Chains')
plt.xlabel("Time Step")
plt.ylabel("State")
plt.grid(True)
plt.savefig("graph1.png")