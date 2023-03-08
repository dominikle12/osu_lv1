with open('song.txt', 'r') as f:
   words = f.read().strip().split()

dict = {}

for word in words:
   dict[word] = words.count(word)

print(dict)