import json
import sys
from dfa_input_parser import DFA

# Check command line arguments
if len(sys.argv) < 2:
    print("Usage: python dfa_product.py <dfa1_file>")
    sys.exit(1)

dfa1_file = sys.argv[1]
# Load DFA from JSON file
try:
    with open(dfa1_file, 'r') as f:
        dfa1_data = json.load(f)
    dfa1 = DFA.from_dict(dfa1_data)

except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON format - {e}")
    sys.exit(1)

        # Print summary of inputs and output file
print(f"\nDFA ({dfa1_file}):")
print(f"  States: {dfa1.states}")
print(f"  Alphabet: {dfa1.alphabet}")
print(f"  Start: {dfa1.start_state}")
print(f"  Accept States: {dfa1.accept_states}")
print(dfa1.transitions)
