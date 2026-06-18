import csv
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







