import csv

with open("./product.csv","r") as csv_file :
    if "pen" not in csv_file.read():
        print("doesnot exist")
        with open("./product.csv", "a") as csv_file_ :
            i = csv.writer(csv_file_).writerow([109,"pen",9999])
            
    else :
        print("exists")

    
