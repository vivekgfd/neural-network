# First four bytes should decide which operator to use
# Last two bytes is p and q

samples = [
    [[0], [0], [0], [0], [0], [0]], # p ∨ q    - logical disjunction
    [[0], [0], [0], [0], [0], [1]], # p ∨ q    - logical disjunction
    [[0], [0], [0], [0], [1], [0]], # p ∨ q    - logical disjunction
    [[0], [0], [0], [0], [1], [1]], # p ∨ q    - logical disjunction
    [[0], [0], [0], [1], [0], [0]], # p ∧ q    - logical conjunction
    [[0], [0], [0], [1], [0], [1]], # p ∧ q    - logical conjunction
    [[0], [0], [0], [1], [1], [0]], # p ∧ q    - logical conjunction
    [[0], [0], [0], [1], [1], [1]], # p ∧ q    - logical conjunction
    [[0], [0], [1], [0], [0], [0]], # p ↓ q    - logical NOR
    [[0], [0], [1], [0], [0], [1]], # p ↓ q    - logical NOR
    [[0], [0], [1], [0], [1], [0]], # p ↓ q    - logical NOR
    [[0], [0], [1], [0], [1], [1]], # p ↓ q    - logical NOR
    [[0], [0], [1], [1], [0], [0]], # p ⊕ q    - exclusive disjunction
    [[0], [0], [1], [1], [0], [1]], # p ⊕ q    - exclusive disjunction
    [[0], [0], [1], [1], [1], [0]], # p ⊕ q    - exclusive disjunction
    [[0], [0], [1], [1], [1], [1]], # p ⊕ q    - exclusive disjunction
    [[0], [1], [0], [0], [0], [0]], # p → q   - material implication
    [[0], [1], [0], [0], [0], [1]], # p → q   - material implication
    [[0], [1], [0], [0], [1], [0]], # p → q   - material implication
    [[0], [1], [0], [0], [1], [1]], # p → q   - material implication
    [[0], [1], [0], [1], [0], [0]], # p xnor q - logical biconditional
    [[0], [1], [0], [1], [0], [1]], # p xnor q - logical biconditional
    [[0], [1], [0], [1], [1], [0]], # p xnor q - logical biconditional
    [[0], [1], [0], [1], [1], [1]], # p xnor q - logical biconditional
    [[0], [1], [1], [0], [0], [0]], # ⊥        - contradiction
    [[0], [1], [1], [0], [0], [1]], # ⊥        - contradiction
    [[0], [1], [1], [0], [1], [0]], # ⊥        - contradiction
    [[0], [1], [1], [0], [1], [1]], # ⊥        - contradiction
    [[0], [1], [1], [1], [0], [0]], # ⊤        - tautology
    [[0], [1], [1], [1], [0], [1]], # ⊤        - tautology
    [[0], [1], [1], [1], [1], [0]], # ⊤        - tautology
    [[0], [1], [1], [1], [1], [1]], # ⊤        - tautology
    [[1], [0], [0], [0], [0], [0]], # p ↚ q   - converse nonimplication
    [[1], [0], [0], [0], [0], [1]], # p ↚ q   - converse nonimplication
    [[1], [0], [0], [0], [1], [0]], # p ↚ q   - converse nonimplication
    [[1], [0], [0], [0], [1], [1]], # p ↚ q   - converse nonimplication
    [[1], [0], [0], [1], [0], [0]], # p ↛ q   - nonimplication
    [[1], [0], [0], [1], [0], [1]], # p ↛ q   - nonimplication
    [[1], [0], [0], [1], [1], [0]], # p ↛ q   - nonimplication
    [[1], [0], [0], [1], [1], [1]], # p ↛ q   - nonimplication
    [[1], [0], [1], [0], [0], [0]], # p ← q   - converse implication
    [[1], [0], [1], [0], [0], [1]], # p ← q   - converse implication
    [[1], [0], [1], [0], [1], [0]], # p ← q   - converse implication
    [[1], [0], [1], [0], [1], [1]], # p ← q   - converse implication
    [[1], [0], [1], [1], [0], [0]], # p ↑ q    - logical NAND
    [[1], [0], [1], [1], [0], [1]], # p ↑ q    - logical NAND
    [[1], [0], [1], [1], [1], [0]], # p ↑ q    - logical NAND
    [[1], [0], [1], [1], [1], [1]], # p ↑ q    - logical NAND
    [[1], [1], [0], [0], [0], [0]], # p        - projection function
    [[1], [1], [0], [0], [0], [1]], # p        - projection function
    [[1], [1], [0], [0], [1], [0]], # p        - projection function
    [[1], [1], [0], [0], [1], [1]], # p        - projection function
    [[1], [1], [0], [1], [0], [0]], # ¬p       - negation
    [[1], [1], [0], [1], [0], [1]], # ¬p       - negation
    [[1], [1], [0], [1], [1], [0]], # ¬p       - negation
    [[1], [1], [0], [1], [1], [1]], # ¬p       - negation
    [[1], [1], [1], [0], [0], [0]], # q        - projection function
    [[1], [1], [1], [0], [0], [1]], # q        - projection function
    [[1], [1], [1], [0], [1], [0]], # q        - projection function
    [[1], [1], [1], [0], [1], [1]], # q        - projection function
    [[1], [1], [1], [1], [0], [0]], # ¬q       - negation
    [[1], [1], [1], [1], [0], [1]], # ¬q       - negation
    [[1], [1], [1], [1], [1], [0]], # ¬q       - negation
    [[1], [1], [1], [1], [1], [1]]  # ¬q       - negation
]

targets = [
    [[0]], [[1]], [[1]], [[1]],
    [[0]], [[0]], [[0]], [[1]],
    [[1]], [[0]], [[0]], [[0]],
    [[0]], [[1]], [[1]], [[0]],
    [[1]], [[1]], [[0]], [[1]],
    [[1]], [[0]], [[0]], [[1]],
    [[0]], [[0]], [[0]], [[0]],
    [[1]], [[1]], [[1]], [[1]],
    [[0]], [[1]], [[0]], [[0]],
    [[0]], [[0]], [[1]], [[0]],
    [[1]], [[0]], [[1]], [[1]],
    [[1]], [[1]], [[1]], [[0]],
    [[0]], [[0]], [[1]], [[1]],
    [[1]], [[1]], [[0]], [[0]],
    [[0]], [[1]], [[0]], [[1]],
    [[1]], [[0]], [[1]], [[0]]
]
