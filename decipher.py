import random
word = str(input('Plain text:'))
key = str(input("Key seperated using (;): "))
key = key.split(';')
inputcol = len(key)
firstdict = {}
counter2 = 0
inputcol2 = 0
for i in word:
    inputcol2 += 1
lister = []
finallist = []
finallist.append([0])
lister.append([])
ciphertext = []
countercolumn = 1
counterrow = 0
for i in word:
    if countercolumn == inputcol2/inputcol:
        lister.append([])
        lister[counterrow].append(i)
        counterrow += 1
        countercolumn = 1
    else:
        lister[counterrow].append(i)
        countercolumn += 1
for i in key:
    try:
        firstdict[i] = lister[counter2]
        counter2 += 1
    except:
        break
seconddict = {}
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




