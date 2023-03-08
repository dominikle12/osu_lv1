
spamCount = 0
hamCount = 0
hamWords=0
spamWords=0
usklicnikCount=0
with open('SMSSpamCollection.txt', 'r') as f:
   for line in f:        
        if line.startswith("ham"):
            hamCount += 1
            hamWords += len(line.strip().split())
        elif line.startswith("spam"):
            spamCount += 1
            spamWords += len(line.strip().split())
            if line.strip().endswith("!"):
                usklicnikCount+=1

avgSpam = spamWords/spamCount
avgHam = hamWords/hamCount

print(avgHam)
print(avgSpam)
print(usklicnikCount)    

