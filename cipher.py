import random
inputcol = int(input("Number of columns: "))
word = str(input('Plain text'))
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
        key.append(i[0])
        i.remove(i[0])
    except:
        break
finalfinaltext = []
for i in ciphertext:
    finalfinaltext.append(''.join(i))
finalfinaltext = ''.join(finalfinaltext)
print(finalfinaltext)
print(key)
#end-----------------------
inputcol = int(input("colmn: "))
word = finalfinaltext
lister = []
finallist = []
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
print(lister)
firstdict = {}
counter2 = 0
for i in key:
    try:
        firstdict[i] = lister[counter2]
        counter2 += 1
    except:
        break
seconddict = {}
print(firstdict)
for i in sorted(firstdict):
    seconddict[i] = firstdict[i]
secondlist = []
for i in seconddict:
    secondlist.append(seconddict[i])
list2 =[]
countercolumn = 0
counterrow = 0
while True:
    try:
        if counterrow == inputcol - 1:
            list2.append(secondlist[counterrow][countercolumn])
            counterrow = 0
            countercolumn += 1
        else:
            list2.append(secondlist[counterrow][countercolumn])
            counterrow += 1
    except:
        break
print(''.join(list2))




