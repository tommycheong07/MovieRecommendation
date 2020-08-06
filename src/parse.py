import csv
import sys


with open(sys.argv[1]) as read_file:
    with open(sys.argv[2], 'w', newline='') as write_file:
        writer = csv.writer(write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        rd = csv.reader(read_file, delimiter="\t", quotechar='"')
        for row in rd:
            writer.writerow([row[0], row[1]])
