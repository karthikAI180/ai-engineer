import csv
from itertools import chain,combinations,product
def csv_batch_reader(filename,size):
    with open(filename,'r') as f:
        f=csv.reader(f)
        next(f)
        batch=[]
        for i in f:
            batch.append(i)
            if len(batch)==size:
                yield batch
                batch=[]
k=csv_batch_reader('C:/Users/kredd/AI_180/AI-portfolio/01-heart-disease-eda/data/heart.csv',10)
for i in range(10):
    print(next(k))
print(list(chain([1,2,3],[4,5,6])))
print(list(combinations(['a','b','c','d'],2)))
print(list(product([1,2],['x','y'])))










