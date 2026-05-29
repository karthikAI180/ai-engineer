try:
    f=open("ab_c.txt")
    print(f.read())
except Exception:
    print("This file is not avaialable")
else:
    print(f.read())
finally:
    print("Done with the execution")

