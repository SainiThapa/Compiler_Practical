# Define the grammar production rules
grammar = {
    'S': ['aAB', 'bBC'],
    'A': ['a', ''],
    'B': ['b', 'c'],
    'C': ['c', '']
}

# Create a dictionary to store the FIRST sets
first_sets = {}

# Function to compute the FIRST set for a non-terminal symbol
def compute_first(symbol):
    # If the FIRST set is already computed, return it
    if symbol in first_sets:
        return first_sets[symbol]

    first_set = set()

    for production in grammar[symbol]:
        # Handle epsilon (empty) production
        if production == '':
            first_set.add('epsilon')
        else:
            # Find the FIRST set of the first symbol in the production
            first_of_first_symbol = compute_first(production[0])
            first_set.update(first_of_first_symbol)

            # Check if epsilon is in the FIRST set of the first symbol
            if 'epsilon' in first_of_first_symbol:
                # If epsilon is in the FIRST set, consider the rest of the symbols in the production
                first_set.update(compute_first(production[1:]))

    # Cache and return the computed FIRST set
    first_sets[symbol] = first_set
    return first_set

# Compute the FIRST sets for all non-terminals
for symbol in grammar.keys():
    compute_first(symbol)

# Print the FIRST sets
for symbol, first_set in first_sets.items():
    print(f'FIRST({symbol}) = {first_set}')
