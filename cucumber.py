with open('c:\\mine\\No.txt') as noTxt:
    with open('c:\\mine\\number.txt','w') as numberTxt:
        for line in noTxt:
            nos = line.split(',')
            start,end = int(nos[0]), int(nos[1])
            for i in range(start, end):
                numberTxt.write(str(i) + '\n')