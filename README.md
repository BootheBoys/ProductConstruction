# DFA Product Construction in Python

This project implements **Product Construction** of two Deterministic Finite Automata (DFAs).

---

- **`dfa_product.py`**  
  Main script to construct the product DFA. It reads two DFA definitions from JSON files, builds the product DFA, and outputs the result to a new JSON file.

---

## Usage

```bash
python dfa_product.py <dfa1_file> <dfa2_file> <output_file> [operation]
```

- `dfa1_file`: Path to the first DFA JSON file.
- `dfa2_file`: Path to the second DFA JSON file.
- `output_file`: Path where the resulting product DFA will be saved.
- `operation`: *(Optional)* Either `intersection` (default) or `union`.

### Example:

```bash
python dfa_product.py example_dfas/ends_with_a.json example_dfas/even_bs.json product_output.json intersection
```
