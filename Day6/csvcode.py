import csv
with open("pandi.csv",'r') as k:
    csv_reader=csv.DictReader(k,delimiter='\t')
    with open("new_file.csv",'w',newline='') as p:
        fieldnames=['first_name','last_name']
        csv_writer=csv.DictWriter(p,fieldnames=fieldnames,delimiter='\t',extrasaction="ignore")
        csv_writer.writeheader()
        for l in csv_reader:
            del l['email']
            csv_writer.writerow(l)
    
    