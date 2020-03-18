#--------------moje rozwiazanie------------
listOfScoresAndNames = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    listOfScoresAndNames.append([name,score])

def findMin(listOfNestedLists):
    scores = []
    for i in listOfNestedLists:
        scores.append(i[1])
    minimum = min(scores)
    return minimum

minimum = findMin(listOfScoresAndNames)
array = [lista for lista in listOfScoresAndNames if lista[1] != minimum]

newMinimum = findMin(array)
newArray = [lista for lista in array if lista[1] == newMinimum]

def sortByName(val):
    return val[0]
newArray.sort(key=sortByName)
for i in newArray:
    print(i[0])