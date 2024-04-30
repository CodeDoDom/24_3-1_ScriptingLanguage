import csv

f = open('mydata.csv', 'w', newline='')
writer = csv.writer(f, delimiter=':', quoting=csv.QUOTE_ALL)
writer.writerow([100, 176, 81])
writer.writerow([101, 180, 90])
writer.writerow(['yoon, leehana', 180, 88])
writer.writerows([
    [1, 2, 3], [4, 5, 6]
])
f.close()
