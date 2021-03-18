import csv
file=open("C:/Users/student.MCALAB/Desktop/20MCA007/PYTHON 1/BOOK1.csv",'r')
reader = csv.reader(file)
for row in reader:
    print(row)