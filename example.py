n = int(input())
arr = map(int, input().split())
#print(arr)
#maximum = max(arr)
#for i in arr:
#    print(i)
#    if i == maximum:
#        arr.remove(i)

maximum = max(arr)
i=0
while(i<n):
    if maximum == max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))

#inne zadanko (HackerRank List Comprehension)
#without List Comprehension
python x = int ( raw_input())
y = int ( raw_input())
n = int ( raw_input())
ar = []
p = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
        if i+j != n:
            ar.append([])
            ar[p] = [ i , j ]
            p+=1
print ar

#using list comprehension
python x = int ( raw_input())
y = int ( raw_input())
n = int ( raw_input())
print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]