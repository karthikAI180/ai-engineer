import csv
def read_and_filter(input_file,output_file):
    try:
        with open (input_file, 'r') as input_reader:
            k=csv.DictReader(input_reader,delimiter='\t')
            with open(output_file,'w',newline='') as output_writer:
                fieldnames=['first_name','last_name']
                l=csv.DictWriter(output_writer,fieldnames=fieldnames,delimiter='\t')
                l.writeheader()
                for i in k:
                    del(i['email'])
                    l.writerow(i)
    except FileNotFoundError:
        print("file not found")
    except Exception:
        print("something went wrong")
    finally:
        print("program finished")



