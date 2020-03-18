n = int(input())
arr = list(map(int, input().split()))

maximum = max(arr)
print(maximum)


#----------rozwiazanie kogos z neta----------------
# i=0
# while(i<n):
    # if maximum == max(arr):
        # arr.remove(max(arr))
    # i+=1
# print(max(arr))

#-----------moje rozwiazanie-----------
def checkIfNotHighest(points):
    if points == maximum :
        return False
    else:
        return True
 
array=filter(checkIfNotHighest, arr)
print(max(array))
