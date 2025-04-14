import json
import os

def save_dfa(dfa_dict, filename):
    """Save DFA dictionary to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(dfa_dict, f, indent=2)
    print(f"Created {filename}")

# Create a directory for example DFAs if it doesn't exist
os.makedirs("example_dfas", exist_ok=True)

# Example 1: DFA accepting strings ending with 'a'
dfa1 = {
    "states": ["q0", "q1"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q0", "symbol": "a", "to_state": "q1"},
        {"from_state": "q0", "symbol": "b", "to_state": "q0"},
        {"from_state": "q1", "symbol": "a", "to_state": "q1"},
        {"from_state": "q1", "symbol": "b", "to_state": "q0"}
    ],
    "start_state": "q0",
    "accept_states": ["q1"]
}
save_dfa(dfa1, "example_dfas/ends_with_a.json")

# Example 2: DFA accepting strings with an even number of 'b's
dfa2 = {
    "states": ["p0", "p1"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "p0", "symbol": "a", "to_state": "p0"},
        {"from_state": "p0", "symbol": "b", "to_state": "p1"},
        {"from_state": "p1", "symbol": "a", "to_state": "p1"},
        {"from_state": "p1", "symbol": "b", "to_state": "p0"}
    ],
    "start_state": "p0",
    "accept_states": ["p0"]
}
save_dfa(dfa2, "example_dfas/even_bs.json")

# Example 3: DFA accepting strings starting with 'a'
dfa3 = {
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q0", "symbol": "a", "to_state": "q1"},
        {"from_state": "q0", "symbol": "b", "to_state": "q2"},
        {"from_state": "q1", "symbol": "a", "to_state": "q1"},
        {"from_state": "q1", "symbol": "b", "to_state": "q1"},
        {"from_state": "q2", "symbol": "a", "to_state": "q2"},
        {"from_state": "q2", "symbol": "b", "to_state": "q2"}
    ],
    "start_state": "q0",
    "accept_states": ["q1"]
}
save_dfa(dfa3, "example_dfas/starts_with_a.json")

# Example 4: DFA accepting strings containing the substring 'ab'
dfa4 = {
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q0", "symbol": "a", "to_state": "q1"},
        {"from_state": "q0", "symbol": "b", "to_state": "q0"},
        {"from_state": "q1", "symbol": "a", "to_state": "q1"},
        {"from_state": "q1", "symbol": "b", "to_state": "q2"},
        {"from_state": "q2", "symbol": "a", "to_state": "q2"},
        {"from_state": "q2", "symbol": "b", "to_state": "q2"}
    ],
    "start_state": "q0",
    "accept_states": ["q2"]
}
save_dfa(dfa4, "example_dfas/contains_ab.json")

# Example 5: DFA accepting strings with an odd number of 'a's
dfa5 = {
    "states": ["q0", "q1"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q0", "symbol": "a", "to_state": "q1"},
        {"from_state": "q0", "symbol": "b", "to_state": "q0"},
        {"from_state": "q1", "symbol": "a", "to_state": "q0"},
        {"from_state": "q1", "symbol": "b", "to_state": "q1"}
    ],
    "start_state": "q0",
    "accept_states": ["q1"]
}
save_dfa(dfa5, "example_dfas/odd_as.json")

# Example 6: DFA accepting strings with length divisible by 3
dfa6 = {
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q0", "symbol": "a", "to_state": "q1"},
        {"from_state": "q0", "symbol": "b", "to_state": "q1"},
        {"from_state": "q1", "symbol": "a", "to_state": "q2"},
        {"from_state": "q1", "symbol": "b", "to_state": "q2"},
        {"from_state": "q2", "symbol": "a", "to_state": "q0"},
        {"from_state": "q2", "symbol": "b", "to_state": "q0"}
    ],
    "start_state": "q0",
    "accept_states": ["q0"]
}
save_dfa(dfa6, "example_dfas/length_div_by_3.json")

# Example 7: DFA accepting strings where every 'a' is followed by 'b'
dfa7 = {
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q0", "symbol": "a", "to_state": "q1"},
        {"from_state": "q0", "symbol": "b", "to_state": "q0"},
        {"from_state": "q1", "symbol": "a", "to_state": "q2"},
        {"from_state": "q1", "symbol": "b", "to_state": "q0"},
        {"from_state": "q2", "symbol": "a", "to_state": "q2"},
        {"from_state": "q2", "symbol": "b", "to_state": "q2"}
    ],
    "start_state": "q0",
    "accept_states": ["q0", "q1"]
}
save_dfa(dfa7, "example_dfas/a_followed_by_b.json")

# Example 8: DFA accepting strings with at most one 'a'
dfa8 = {
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q0", "symbol": "a", "to_state": "q1"},
        {"from_state": "q0", "symbol": "b", "to_state": "q0"},
        {"from_state": "q1", "symbol": "a", "to_state": "q2"},
        {"from_state": "q1", "symbol": "b", "to_state": "q1"},
        {"from_state": "q2", "symbol": "a", "to_state": "q2"},
        {"from_state": "q2", "symbol": "b", "to_state": "q2"}
    ],
    "start_state": "q0",
    "accept_states": ["q0", "q1"]
}
save_dfa(dfa8, "example_dfas/at_most_one_a.json")

# Example 9: DFA accepting strings where the number of 'a's is divisible by 2 and the number of 'b's is divisible by 3
dfa9 = {
    "states": ["q00", "q01", "q02", "q10", "q11", "q12"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q00", "symbol": "a", "to_state": "q10"},
        {"from_state": "q00", "symbol": "b", "to_state": "q01"},
        {"from_state": "q01", "symbol": "a", "to_state": "q11"},
        {"from_state": "q01", "symbol": "b", "to_state": "q02"},
        {"from_state": "q02", "symbol": "a", "to_state": "q12"},
        {"from_state": "q02", "symbol": "b", "to_state": "q00"},
        {"from_state": "q10", "symbol": "a", "to_state": "q00"},
        {"from_state": "q10", "symbol": "b", "to_state": "q11"},
        {"from_state": "q11", "symbol": "a", "to_state": "q01"},
        {"from_state": "q11", "symbol": "b", "to_state": "q12"},
        {"from_state": "q12", "symbol": "a", "to_state": "q02"},
        {"from_state": "q12", "symbol": "b", "to_state": "q10"}
    ],
    "start_state": "q00",
    "accept_states": ["q00"]
}
save_dfa(dfa9, "example_dfas/a_mod2_b_mod3.json")

# Example 10: DFA accepting strings that do not contain the substring 'aa'
dfa10 = {
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transitions": [
        {"from_state": "q0", "symbol": "a", "to_state": "q1"},
        {"from_state": "q0", "symbol": "b", "to_state": "q0"},
        {"from_state": "q1", "symbol": "a", "to_state": "q2"},
        {"from_state": "q1", "symbol": "b", "to_state": "q0"},
        {"from_state": "q2", "symbol": "a", "to_state": "q2"},
        {"from_state": "q2", "symbol": "b", "to_state": "q2"}
    ],
    "start_state": "q0",
    "accept_states": ["q0", "q1"]
}
save_dfa(dfa10, "example_dfas/no_aa.json")

print("\nAll example DFAs created successfully!")