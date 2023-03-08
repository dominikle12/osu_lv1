import math
listaBrojeva = []
unos = ""
while unos != "Done":
    unos = str(input("Unesite broj: ")) 
    
    if unos.isnumeric() == True and unos != "Done":
        listaBrojeva.append(int(unos))
    else:
        print("Unesite isključivo brojeve!")
       

avg = math.fsum(listaBrojeva)/len(listaBrojeva)



print("Sredina: " + str(avg))
print("Minimalna vrijednost: " + str(min(listaBrojeva)))
print("Maksimalna vrijednost: " + str(max(listaBrojeva)))
listaBrojeva.sort
print(listaBrojeva)