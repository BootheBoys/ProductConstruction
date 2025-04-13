# DFA Product Construction in Python

This project implements **Product Construction** of two Deterministic Finite Automata (DFAs). Given two DFAs, it generates a new DFA that represents either the **intersection** or **union** of their accepted languages.

---

## 📁 File Overview

- **`dfa_product.py`**  
  Main script to construct the product DFA. It reads two DFA definitions from JSON files, builds the product DFA, and outputs the result to a new JSON file.

- **`create_example_dfas.py`**  
  Utility script that generates a set of example DFAs and saves them as JSON files in the `example_dfas/` directory.

---

## ✅ Features

- Product construction using **intersection** (default) or **union** of two DFAs.
- Validates alphabet compatibility between input DFAs.
- JSON import/export for DFA structures.
- Clean CLI interface for building DFAs.

---

## 🧪 Example DFA Library

Run the following command to generate 10 sample DFA JSON files:

```bash
python create_example_dfas.py
```

These will be saved in the `example_dfas/` directory:
- `ends_with_a.json`
- `even_bs.json`
- `starts_with_a.json`
- `contains_ab.json`
- `odd_as.json`
- `length_div_by_3.json`
- `a_followed_by_b.json`
- `at_most_one_a.json`
- `a_mod2_b_mod3.json`
- `no_aa.json`

---

## 🚀 Usage

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

---

## 📄 DFA JSON Format

Each DFA is defined in the following structure:

```json
{
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
```

---

## 🔧 Requirements

- Python 3.6+
- No external libraries required

---

## 🧠 Notes

- The product DFA uses tuples of original states (e.g., `("q0", "p0")`) as its composite states.
- Make sure both DFAs use the exact same alphabet before attempting product construction.

---
