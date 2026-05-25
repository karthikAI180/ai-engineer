people = [
    {"name": "Alice", "age": 28, "score": 88},
    {"name": "Bob",   "age": 17, "score": 52},
    {"name": "Eve",   "age": 34, "score": 95},
    {"name": "John",  "age": 15, "score": 73},
    {"name": "Sara",  "age": 25, "score": 61},
]

# --- Challenge: complete these 3 lines only ---
# Rules: no loops, no def — only lambda + map/filter

# 1. Extract just the names as a list

names = list(map(lambda x:x["name"], people))
print(names)
# ['Alice', 'Bob', 'Eve', 'John', 'Sara']

# 2. Keep only adults (age >= 18)
adults = list(filter(lambda x:x['age']>=18, people))
print(adults)
# [{'name': 'Alice', ...}, {'name': 'Eve', ...}, {'name': 'Sara', ...}]

# 3. Get scores curved by 1.1 — rounded to 1 decimal
curved = list(map(lambda x:round(x['score']*1.1,1), people))
print(curved)
# [96.8, 57.2, 104.5, 80.3, 67.1]
