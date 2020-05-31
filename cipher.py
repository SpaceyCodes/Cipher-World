import random
word = str(input('Plain text (please input "-" at random intervals):'))
inputcol = int(input("Number of columns: "))
lister = []
finallist = []
key = []
finallist.append([0])
lister.append([])
ciphertext = []
countercolumn = 1
counterrow = 0
for i in word:
    if countercolumn == inputcol:
        lister.append([])
        lister[counterrow].append(i)
        counterrow += 1
        countercolumn = 1
    else:
        lister[counterrow].append(i)
        countercolumn += 1
while True:
    if countercolumn != inputcol + 1:
        lister[counterrow].append('-')
        countercolumn += 1
    else:
        break
n = counterrow
countercolumn2 = 0
a = 0
while True:
    try:
        if a == len(lister):
            a = 0
            countercolumn2 += 1
            finallist.append([countercolumn2])
        else:
            finallist[countercolumn2].append(lister[a][countercolumn2])
            a += 1
    except:
        finallist.remove(finallist[-1])
        break
#------------------------------------------
while True:
    try:
        randomnum = random.randint(0,len(finallist)-1)
        ciphertext.append(finallist[randomnum])
        finallist.remove(finallist[randomnum])
    except:
        break
#forming key and final display of ciphertext-------------------
for i in ciphertext:
    try:
        key.append(str(i[0]))
        i.remove(i[0])
    except:
        break
finalfinaltext = []
for i in ciphertext:
    finalfinaltext.append(''.join(i))
finalfinaltext = ''.join(finalfinaltext)
print(finalfinaltext)
print(';'.join(key))
#end-----------------------
