file = open('sample.txt', 'r')
data = file.readlines()
file.close()

words = []

for i in data:
    words.extend(i.lower().split())

print(words)
file = open('output.txt', 'w')
file.write(str(words))
file.close()