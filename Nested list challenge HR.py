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
print("array", array)

newMinimum = findMin(array)
newArray = [lista for lista in array if lista[1] == newMinimum]
print("newArray", newArray)

#----------cudze rozwiązanie--------
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))