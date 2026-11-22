"""Simple command-line calculator (UCS745 Lab Q1)."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot take modulo by zero")
    return a % b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide, "%": modulo}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")
    return OPERATIONS[op](a, b)


if __name__ == "__main__":
    a = float(input("First number: "))
    op = input("Operator: ").strip()
    b = float(input("Second number: "))
    print("Result:", calculate(a, op, b))
