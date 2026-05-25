def build_url(base, **params):
    # YOUR CODE HERE
    # Join the params as key=value pairs separated by &
    # Add a ? between the base and the params
    # Return the full URL string
    if len(params)==0:
        return base
    pairs=[]
    for k,v in params.items():
        pairs.append(str(k)+'='+str(v))
    s='&'.join(pairs)
    return base+'?'+s




# --- Test calls (do not change these) ---
print(build_url("https://api.example.com/search", q="python", page=2, limit=10))
print(build_url("https://api.example.com/users", id=42))
print(build_url("https://api.example.com/data"))

'''
https://api.example.com/search?q=python&page=2&limit=10
https://api.example.com/users?id=42
https://api.example.com/data
'''