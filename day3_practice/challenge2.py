def stats(*numbers):
    # YOUR CODE HERE
    # Return a dict with min, max, mean, count
    # Handle empty call — don't crash
    if len(numbers)==0:
        return {'min': None, 'max': None, 'mean': None, 'count': 0}

    d={}
    d['min']=min(numbers)
    d['max']=max(numbers)
    add=0
    for i in numbers:
        add+=i
    d['mean']=add/len(numbers)
    d['count']=len(numbers)
    return d

print(stats(4, 7, 2, 9, 1)) 
    


''' Test calls (do not change these) ---
print(stats(4, 7, 2, 9, 1))   # {'min': 1, 'max': 9, 'mean': 4.6, 'count': 5}
print(stats(10, 20, 30))       # {'min': 10, 'max': 30, 'mean': 20.0, 'count': 3}
print(stats(42))               # {'min': 42, 'max': 42, 'mean': 42.0, 'count': 1}
print(stats())                 # {'min': None, 'max': None, 'mean': None, 'count': 0}
# No imports allowed
# Compute mean manually (no sum() builtin — use a loop)
# Empty call stats() must not crash
'''