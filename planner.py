#!/usr/bin/python
# coding=cp949
import random
import time
numDays = 31
arrayDays1 = [-1]*(numDays+1) #index out of bound removal
arrayDays2 = [-1]*(numDays+1) #index out of bound removal
arrayDays3 = [-1]*(numDays+1) #index out of bound removal
arrayDays4 = [-1]*(numDays+1) #index out of bound removal
matrixDays = []
matrixDays.append(arrayDays1) 
matrixDays.append(arrayDays2) 
matrixDays.append(arrayDays3) 
matrixDays.append(arrayDays4) 
notSet = -1
rest = 0
vacation = 1
night = 2
nightEnd = 3
day = 4
nightCounter1 = 10
nightCounter2 = 9
nightCounter3 = 3
nightCounter4 = 9
maxStreak = 2
setNight =2

#set manually the first day & other days for rest, vacation, night, and day (weekends)
#0 -dae hyun 1 - baek kyung ho 2 - me 3 - park jong min

#night putting

#group 1, 2 should exist, and for group 1, there should be 20, and for group 1, there should be 10.
#18 to 12 might be okay as well, and allocate some for dae hyun and so forth as well if needed.
#adjustable will be pretty nice. 31 total yas, and 11 for group 2 and 20 for group 1 will be nice.
iterate = 0
while True:
    groupCounter1 = 0.0 #adjust this for you know what (for 경호) -> 비번이나 휴일 미리 지정해주기
    groupResult1 = 20 #adjust this for balance! should match the numDay amount!
    groupCounter2 = 0.1 #adjust this if needed!
    groupResult2 = 11 #adjust this for balance!
    i = 0
    streakCount = [0,0,0,0]
    arrayDays1 = [-1]*(numDays+1) #index out of bound removal
    arrayDays2 = [-1]*(numDays+1) #index out of bound removal
    arrayDays3 = [-1]*(numDays+1) #index out of bound removal
    arrayDays4 = [-1]*(numDays+1) #index out of bound removal
    matrixDays = []
    matrixDays.append(arrayDays1) 
    matrixDays.append(arrayDays2) 
    matrixDays.append(arrayDays3) 
    matrixDays.append(arrayDays4) 
    #set manually ####################################################################################################################
    arrayDays1[9-1]=night
    arrayDays1[10-1]=nightEnd
    arrayDays1[26-1]=rest
    
    arrayDays2[1-1]=rest
    arrayDays2[2-1]=rest
    arrayDays2[8-1]=rest
    arrayDays2[9-1]=day
    arrayDays2[14-1]=night
    arrayDays2[15-1]=nightEnd
    arrayDays2[21-1]=night
    arrayDays2[22-1]=nightEnd
    arrayDays2[29-1]=rest

    arrayDays3[1-1]=nightEnd
    arrayDays3[9-1]=day
    arrayDays3[13-1]=day
    arrayDays3[14-1]=day
    arrayDays3[15-1]=day
    arrayDays3[23-1]=day
    arrayDays3[26-1]=day
    arrayDays3[29-1]=day

    arrayDays4[1-1]=day
    arrayDays4[2-1]=night
    arrayDays4[3-1]=nightEnd
    arrayDays4[4-1]=rest
    arrayDays4[5-1]=day
    arrayDays4[6-1]=rest
    arrayDays4[7-1]=rest
    arrayDays4[8-1]=night
    arrayDays4[9-1]=nightEnd
    arrayDays4[10-1]=rest
    arrayDays4[11-1]=night
    arrayDays4[12-1]=nightEnd
    arrayDays4[13-1]=night
    arrayDays4[14-1]=nightEnd
    arrayDays4[15-1]=rest
    arrayDays4[16-1]=rest
    arrayDays4[17-1]=rest
    arrayDays4[18-1]=night
    arrayDays4[19-1]=nightEnd
    arrayDays4[20-1]=rest
    arrayDays4[21-1]=rest
    arrayDays4[22-1]=rest
    arrayDays4[23-1]=night
    arrayDays4[24-1]=nightEnd
    arrayDays4[25-1]=night
    arrayDays4[26-1]=nightEnd
    arrayDays4[27-1]=rest
    arrayDays4[28-1]=night
    arrayDays4[29-1]=nightEnd
    arrayDays4[30-1]=night
    arrayDays4[31-1]=nightEnd
    ##################################################################################################################################
    #night putting
    while True:
        if i == numDays:
            break
    ##################################################################################################################################
        if i == 9-1:
            i+=1
            continue

        if i == 14-1 or i == 21-1:
            i+=1
            continue
        #

        if i == 2-1 or i == 8-1 or i == 11-1 or i == 13-1 or i == 18-1 or i == 23-1 or i == 25-1 or i == 28-1 or i == 30-1: #manually set
            i += 1
            continue
    ##################################################################################################################################
        randPlayerChooser = int(random.random()*10%4)
        #if groupCounter1/groupCounter2 < 20.0/11.0:
            #randPlayerChooser = int(random.random()*10%2)
        if matrixDays[randPlayerChooser][i] is notSet and matrixDays[randPlayerChooser][i+1] is notSet:
            if streakCount[randPlayerChooser] == 2: #streak amount
                continue
            else: #adding element
            #    for m in range(4):
             #       if(streakCount[m]!=0):
              #          streakCount[m] -=1
                streakCount[randPlayerChooser] +=3
                matrixDays[randPlayerChooser][i] = night
                matrixDays[randPlayerChooser][i+1] = nightEnd
                i = i+1
        else:
            continue
    print('test')
    #day putting
    i = 0

#    while True:
#        if i == numDays:
#            break
#        randPlayerChooser = int(random.random()*10%2)+2
#        if matrixDays[randPlayerChooser][i] is notSet:
#            matrixDays[randPlayerChooser][i] = day
#            i = i+1
#        elif matrixDays[randPlayerChooser][i] is night:
#            i = i+1
#        elif matrixDays[randPlayerChooser][i] is nightEnd:
#            i = i+1
#        else:
#            continue
#    
    #rest putting
#    i = 0
#    while True:
#        if i == numDays:
#            break
#        randPlayerChooser = int(random.random()*10%2)
#        if matrixDays[randPlayerChooser][i] is notSet:
#            matrixDays[randPlayerChooser][i] = rest
#            i = i+1
#        elif matrixDays[randPlayerChooser][i] is night:
#            i = i+1
#        elif matrixDays[randPlayerChooser][i] is nightEnd:
#            i = i+1
#        else:
#            continue
#    #rest putting (for day)

#    i = 0
#    while True:
#        if i == numDays:
#            break
#        randPlayerChooser = int(random.random()*10%2)+2
#        if matrixDays[randPlayerChooser][i] is day:
#            randomRest = int(random.random()*10%2)
#            if randomRest ==1:
#                matrixDays[randPlayerChooser][i] = rest
#                i = i+1
#            else:
#                i = i+1
#        elif matrixDays[randPlayerChooser][i] is night:
#            i = i+1
#        elif matrixDays[randPlayerChooser][i] is nightEnd:
#            i = i+1
#        else:
#            continue
#
    arrayDaysLetter1 = []
    arrayDaysLetter2 = []
    arrayDaysLetter3 = []
    arrayDaysLetter4 = []
    restCount1 = 0
    restCount2 = 0
    restCount3 = 0
    restCount4 = 0
    nonCount1 = 0
    nonCount2 = 0
    nonCount3 = 0
    nonCount4 = 0
    nightCount1 = 0
    nightCount2 = 0
    nightCount3 = 0
    nightCount4 = 0

    for i in arrayDays1:
        if 4 == i:
            arrayDaysLetter1.append("주")
        elif 2 == i:
            arrayDaysLetter1.append("야")
            nightCount1 +=1
        elif 3 == i:
            arrayDaysLetter1.append("비")
        elif 0 == i:
            arrayDaysLetter1.append("휴")
            restCount1 += 1
        elif -1 == i:
            arrayDaysLetter1.append("미")
            nonCount1 += 1

    for i in arrayDays2:
        if 4 == i:
            arrayDaysLetter2.append("주")
        elif 2 == i:
            arrayDaysLetter2.append("야")
            nightCount2 +=1
        elif 3 == i:
            arrayDaysLetter2.append("비")
        elif 0 == i:
            arrayDaysLetter2.append("휴")
            restCount2 += 1
        elif -1 == i:
            arrayDaysLetter2.append("미")
            nonCount2 += 1

    for i in arrayDays3:
        if 4 == i:
            arrayDaysLetter3.append("미") #주
            nonCount3 += 1
        elif 2 == i:
            arrayDaysLetter3.append("야")
            nightCount3 +=1
        elif 3 == i:
            arrayDaysLetter3.append("비")
        elif 0 == i:
            arrayDaysLetter3.append("휴")
            restCount3 += 1
        elif -1 == i:
            arrayDaysLetter3.append("미")
            nonCount3 += 1

    for i in arrayDays4:
        if 4 == i:
            arrayDaysLetter4.append("미") #주
            nonCount4 += 1
        elif 2 == i:
            arrayDaysLetter4.append("야")
            nightCount4 +=1
        elif 3 == i:
            arrayDaysLetter4.append("비")
        elif 0 == i:
            arrayDaysLetter4.append("휴")
            restCount4 += 1
        elif -1 == i:
            arrayDaysLetter4.append("미")
            nonCount4 += 1
    print(nightCount1, nightCount2, nightCount3, nightCount4)

    streakLevel = 0
    coolDown = 0
    repeat = 0
    if(nightCount1 ==nightCounter1):
        if(nightCount2 ==nightCounter2):
            if(nightCount3 == nightCounter3):
                if(nightCount4 == nightCounter4):
                    break
                    for i in range(30):
                        if coolDown == 4:
                            repeat = 1
                            continue
                        if night == arrayDays2[i]:
                            streakLevel +=1
                            coolDown +=2
                        else:
                            if coolDown > 0:
                                coolDown -= 1
                    if repeat == 0:
                        break
    iterate += 1
    print(iterate)
arraydays = []
for i in range(1,32):
    if(i<10):
        label = str(i)+' '
    else:
        label = str(i)
    arraydays.append(label)
print(arraydays)
print(arrayDaysLetter1, nightCount1, restCount1, nonCount1)
print(arrayDaysLetter2, nightCount2, restCount2, nonCount2)
print(arrayDaysLetter3, nightCount3, restCount3, nonCount3)
print(arrayDaysLetter4, nightCount4, restCount4, nonCount4)
  
