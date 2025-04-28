from graphviz import Digraph
from dfa_input_parser import DFA
import json
import sys

def main():
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python visual.py <dfa1_file>")
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
    print(f"  States: {len(dfa1.states)}")
    print(f"  Alphabet: {dfa1.alphabet}")
    print(dfa1.transitions)

    graph = Digraph()
    graph.node('start', style="invisible")

    nodeList = []

    #i = 1
    for a in dfa1.states:
        if isinstance(a, list):
            elemenCount = 1
            temp = "("
            for b in a:
                temp += str(b)
                if elemenCount < len(a):
                    temp += ", "
                    elemenCount += 1
            temp += ")"
        else:
            temp = a
       
        if a not in dfa1.accept_states:
            graph.node(str(temp), temp, shape='circle')
            nodeList.append(str(temp))
        else:
            graph.node(str(temp), temp, shape='doublecircle')
            nodeList.append(str(temp))

        if a == dfa1.start_state:
            graph.edge('start', str(temp))
        
        for token in dfa1.alphabet:
            key = (str(a), token)
            value = str(dfa1.transitions[(str(a), str(token))])
            #graph.edge(str(temp), value)

    newnodeList = list(dict.fromkeys(nodeList))
    print(newnodeList)

    for a in newnodeList:
        if a.startswith('('):
            temp =(a.split())
            temp1 = temp[0].split("(")[1].split(",")[0]
            temp2 = temp[1].split(")")[0]
            for b in dfa1.alphabet:
                tempResult = (dfa1.transitions[(str([temp1, temp2]), b)])
                tempResult = ("(" + str((tempResult[0]))+ ", " + tempResult [1] + ")")
                graph.edge(a, tempResult,  " " + str(b))
        else:
            for b in dfa1.alphabet:
                tempResult = (dfa1.transitions[(a, b)])
                graph.edge(a, tempResult, " " + str(b))
        
        #i += 1
    


    # Save and render to a PDF
    graph.render('output/flowchart', format='pdf', view=True)

if __name__ == "__main__":
    main()