import csv

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# This will read a CSV file and print each row

#Fun Facts
import csv

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
# This will write data to a CSV file