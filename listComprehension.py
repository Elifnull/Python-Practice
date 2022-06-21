v = [2,-3,1]
scalarV = [x*4 for x in v]

print(scalarV)

listA = [1,2,3,4]
listB = [True,False,True,True]

cartesList = [(x,y) for x in listA for y in listB]

print(cartesList)