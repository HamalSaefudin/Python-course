from tabulate import tabulate
file = open("biodata-table.txt","r")
teks = file.read()
lines = teks.split(',')
print(tabulate([lines], headers=['Name', 'Age', 'Address']))