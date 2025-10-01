#  Infix to Postfix Converter (Python)

This project implements an **Infix to Postfix (Reverse Polish Notation) converter** in Python using a **Stack**.  
It demonstrates how operator precedence and parentheses are handled in expression evaluation.

---

##  Features
- Converts infix expressions (e.g., `(1 + 2) * 3`) into postfix notation (`1 2 + 3 *`).
- Uses **stack-based algorithm** to respect operator precedence.
- Supports operators: `+`, `-`, `*`, `/`.
- Handles parentheses properly.



### Input Expressions
```python
expr1 = "5 + ( 6 - 2 ) * 9"
expr2 = "( 1 + 2 ) * ( 3 + 4 )"
output: 5 6 2 - 9 * +
        1 2 + 3 4 + *
