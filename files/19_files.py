file = open('sample.txt', 'r')
data = file.readlines()

for i in data:
    print(i.strip()[::-1])

file.close()