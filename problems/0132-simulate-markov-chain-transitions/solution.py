import numpy as np
def simulate_markov_chain(transition_matrix, initial_state, num_steps):
    # Your code here
    states = [initial_state]
    current_state = initial_state

    num_states = transition_matrix.shape[0]
    all_states = np.arange(num_states)

    for _ in range(num_steps):
        next_state = np.random.choice(all_states, p= transition_matrix[current_state])
        states.append(next_state)
        current_state = next_state

    return np.array(states)
    
    
    


