# Define the DFA transition table
transition_table = {
    0: {'a': 1, 'b': 0},
    1: {'a': 1, 'b': 1}
}

# Function to simulate the DFA
def is_accepted(input_string):
    current_state = 0  # Start in State 0 (initial state)

    for symbol in input_string:
        if symbol not in transition_table[current_state]:
            return False  # Invalid symbol, reject the input
        current_state = transition_table[current_state][symbol]

    return current_state == 1  # Check if the final state is State 1 (accepting state)

# Main function
if __name__ == "__main__":
    input_string = input("Enter a string (a's and b's): ")

    if is_accepted(input_string):
        print("Accepted")
    else:
        print("Rejected")
