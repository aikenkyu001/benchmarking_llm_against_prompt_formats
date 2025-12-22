You are a world-class logical reasoner. Solve the "Einstein's Puzzle" logic puzzle defined below by reasoning step-by-step.

**Puzzle Rules:**

1.  There are five houses in a row.
2.  Each house is painted a different color.
3.  The person living in each house has a different nationality.
4.  Each person drinks a different beverage.
5.  Each person smokes a different brand of cigarette.
6.  Each person keeps a different pet.

**Constraints:**

1.  The Brit lives in the red house.
2.  The Swede keeps dogs as pets.
3.  The Dane drinks tea.
4.  The green house is on the left of the white house.
5.  The person who lives in the green house drinks coffee.
6.  The person who smokes Pall Mall rears birds.
7.  The owner of the yellow house smokes Dunhill.
8.  The person living in the center house drinks milk.
9.  The Norwegian lives in the first house.
10. The person who smokes Blends lives next to the one who keeps cats.
11. The person who keeps a horse lives next to the person who smokes Dunhill.
12. The owner who smokes Bluemaster drinks beer.
13. The German smokes Prince.
14. The Norwegian lives next to the blue house.
15. The person who smokes Blends has a neighbor who drinks water.

**Final Question:**
Who owns the fish? Answer with the person's nationality.

**Reasoning Process:**
To arrive at the final answer, please think step-by-step using the following procedure:

1.  First, identify the position of each house (from 1st to 5th).
2.  Write down the information that can be directly identified from each constraint (e.g., the Norwegian lives in the first house).
3.  Infer information that can be derived indirectly by combining the constraints.
4.  Repeat this process until all attributes (color, nationality, beverage, cigarette, pet) are assigned to each house.
5.  Finally, identify the person who owns the fish and state their nationality.

**Output Format:**
Your answer must be output as a Python code block in the following format. The script should contain only one function called `solve_puzzle()`. When executed, this function must print the single word answer (the nationality) to the final question to standard output. Do not include any explanations or comments other than the code.

**Example Output:**
```python
def solve_puzzle():
    # It was concluded through reasoning that the owner of the fish is German.
    print("German")
```

**Instruction for Self-Consistency:**
Solve this puzzle multiple times (e.g., 3 times) and output the final answer that you obtained most frequently as your confident answer. If multiple answers appear with the same frequency, choose the answer derived from the most detailed reasoning process.