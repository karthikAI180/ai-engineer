#REVISE

def add(a, b=0):
    return a + b

def subtract(a, b=0):
    return a - b

def multiply(a, b=1):
    return a * b

def divide(a, b):
    if b==0:
        return None
    return a / b


def calculate(*args, op="add"):
    ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    result = args[0]        # start with first number
    for n in args[1:]:      # apply op with each remaining number
        result = ops[op](result, n)
    return result

    # e.g. calculate(10, 5, 3, op="add") → 18
    # e.g. calculate(100, 4, 5, op="divide") → 5.0
    

def calculate_verbose(**kwargs):
    op = kwargs["op"]
    numbers = [v for k, v in kwargs.items() if k != "op"]
    return calculate(*numbers, op=op)

    # Read a, b, op from kwargs
    # Call calculate(a, b, op=op) and return the result
    # e.g. calculate_verbose(a=10, b=3, op="multiply") → 30



# --- Test calls (do not change these) ---
print(add(3, 4))                                 # 7
print(subtract(10, 3))                           # 7
print(multiply(3, 4))                            # 12
print(divide(10, 2))                             # 5.0
print(divide(10, 0))                             # None

print(calculate(10, 5, 3, op="add"))             # 18
print(calculate(100, 4, 5, op="divide"))         # 5.0
print(calculate(2, 3, 4, op="multiply"))         # 24

print(calculate_verbose(a=10, b=3, op="multiply"))  # 30
print(calculate_verbose(a=20, b=4, op="divide"))    # 5.0