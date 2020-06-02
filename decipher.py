class decrypt:
    def __init__(self, file_path, key):
        import random
        key = key
        key = key.split(';')
        inputcol = len(key)
        firstdict = {}
        counter2 = 0
        inputcol2 = 0
        f = open(file_path, "r")
        word = f.read()
        for i in word:
            inputcol2 += 1
        lister = []
        finallist = []
        finallist.append([0])
        lister.append([])
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
                firstdict[int(i)] = lister[counter2]
                counter2 += 1
            except:
                break
        f.close()
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
        print('Plain Text: {}'.format(''.join(list2)))
        f = open("C:/Users/User/Downloads/{}".format('newtext.txt'), "w")
        writing = ''.join(list2)
        f.write(writing)
        f.close()





