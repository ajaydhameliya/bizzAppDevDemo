

Road = 100

cockroach1 = 1
cockroach2 = 100
crossed = False
for i in range(1, 500):
    if i%10 == 0:
        cockroach1 -= 2
    else:
        cockroach1 += 1
    if i%5 == 0:
        cockroach2 += 1
    else:
        cockroach2 -= 2
    if not crossed and (cockroach1 == cockroach2):
        print("First both cockroaches meet time is :", i)
        print("cockroach1 distance is :", cockroach1)
        print("cockroach2 distance is :", cockroach2)
        crossed = True

    if(cockroach1 >= 100 and cockroach2 <=0):
        #print("=====================================")
        #print(cockroach1)
        #print(cockroach2)
        print("total time :", i)
        break