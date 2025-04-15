import json
import sys
import os

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def __str__(self):
        result = "DFA:\n"
        result += f"  States: {self.states}\n"
        result += f"  Alphabet: {self.alphabet}\n"
        result += f"  Start State: {self.start_state}\n"
        result += f"  Accept States: {self.accept_states}\n"
        result += "  Transitions:\n"
        for (state, symbol), next_state in sorted(self.transitions.items()):
            result += f"    δ({state}, {symbol}) = {next_state}\n"
        return result

    def to_dict(self):
        """Convert DFA to dictionary for JSON serialization"""
        # Convert transitions from dict with tuple keys to list format
        transitions_list = []
        for (state, symbol), next_state in self.transitions.items():
            transitions_list.append({
                "from_state": state,
                "symbol": symbol,
                "to_state": next_state
            })

        return {
            "states": list(self.states),
            "alphabet": list(self.alphabet),
            "transitions": transitions_list,
            "start_state": self.start_state,
            "accept_states": list(self.accept_states)
        }

    @classmethod
    def from_dict(cls, data):
        """Create DFA from dictionary (loaded from JSON)"""
        states = set(data["states"])
        alphabet = set(data["alphabet"])

        # Convert transitions from list format to dict with tuple keys
        transitions = {}
        for t in data["transitions"]:
            transitions[(t["from_state"], t["symbol"])] = t["to_state"]

        start_state = data["start_state"]
        accept_states = set(data["accept_states"])

        return cls(states, alphabet, transitions, start_state, accept_states)

def product_construction(dfa1, dfa2, operation="intersection"):
    """
    Construct the product of two DFAs.

    Args:
        dfa1: First DFA
        dfa2: Second DFA
        operation: Either "intersection" or "union" to determine accept states

    Returns:
        A new DFA representing the product
    """
    # Verify that both DFAs have the same alphabet
    if dfa1.alphabet != dfa2.alphabet:
        raise ValueError("Both DFAs must have the same alphabet")

    # Create product states
    product_states = set()
    for q1 in dfa1.states:
        for q2 in dfa2.states:
            product_states.add((q1, q2))

    # The alphabet remains the same
    product_alphabet = set(dfa1.alphabet)

    # Create the start state
    product_start_state = (dfa1.start_state, dfa2.start_state)

    # Define accept states based on the operation
    product_accept_states = set()
    for q1 in dfa1.states:
        for q2 in dfa2.states:
            if operation == "intersection":
                if q1 in dfa1.accept_states and q2 in dfa2.accept_states:
                    product_accept_states.add((q1, q2))
            elif operation == "union":
                if q1 in dfa1.accept_states or q2 in dfa2.accept_states:
                    product_accept_states.add((q1, q2))

    # Define transitions for the product DFA
    product_transitions = {}
    for q1 in dfa1.states:
        for q2 in dfa2.states:
            for symbol in product_alphabet:
                if (q1, symbol) in dfa1.transitions and (q2, symbol) in dfa2.transitions:
                    next_q1 = dfa1.transitions[(q1, symbol)]
                    next_q2 = dfa2.transitions[(q2, symbol)]
                    product_transitions[((q1, q2), symbol)] = (next_q1, next_q2)

    # Create and return the product DFA
    return DFA(product_states, product_alphabet, product_transitions,
               product_start_state, product_accept_states)

def main():
    # Check command line arguments
    if len(sys.argv) < 4:
        print("Usage: python dfa_product.py <dfa1_file> <dfa2_file> <output_file> [operation]")
        print("  operation: 'intersection' (default) or 'union'")
        sys.exit(1)

    dfa1_file = sys.argv[1]
    dfa2_file = sys.argv[2]
    output_file = sys.argv[3]
    operation = sys.argv[4] if len(sys.argv) > 4 else "intersection"

    if operation not in ["intersection", "union"]:
        print("Error: operation must be either 'intersection' or 'union'")
        sys.exit(1)

    # Load DFAs from JSON files
    try:
        with open(dfa1_file, 'r') as f:
            dfa1_data = json.load(f)
        dfa1 = DFA.from_dict(dfa1_data)

        with open(dfa2_file, 'r') as f:
            dfa2_data = json.load(f)
        dfa2 = DFA.from_dict(dfa2_data)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        sys.exit(1)

    # Compute product DFA
    try:
        product_dfa = product_construction(dfa1, dfa2, operation)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Convert product DFA to dictionary for JSON serialization
    product_data = product_dfa.to_dict()

    # Save product DFA to JSON file 
    try:
        with open(output_file, 'w') as f:
            json.dump(product_data, f, indent=2)
        print(f"Product DFA saved to {output_file}")
    except IOError as e:
        print(f"Error: Failed to write output file - {e}")
        sys.exit(1)

    # Print summary of inputs and output file
    print(f"\nDFA 1 ({dfa1_file}):")
    print(f"  States: {len(dfa1.states)}")
    print(f"  Alphabet: {dfa1.alphabet}")

    print(f"\nDFA 2 ({dfa2_file}):")
    print(f"  States: {len(dfa2.states)}")
    print(f"  Alphabet: {dfa2.alphabet}")

    print(f"\nProduct DFA ({operation}):")
    print(f"  States: {len(product_dfa.states)}")
    print(f"  Alphabet: {product_dfa.alphabet}")
    print(f"  Accept States: {len(product_dfa.accept_states)}")

if __name__ == "__main__":
    main()
