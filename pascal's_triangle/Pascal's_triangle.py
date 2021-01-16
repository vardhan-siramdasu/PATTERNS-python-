arr=[]
print('enter noof rows')
rows=int(input())
if rows % 2 == 0:
    even_or_odd = 0
else:
    even_or_odd = 1
for i in range(rows):
    arr.append([])
    for j in range(i + rows):
        if ((i + j < rows - 1) or ((i + j) % 2 == even_or_odd)):
            arr[i].append('  ')
        elif(i + j == rows - 1 or len(arr[i]) == rows - 1 + i):
            arr[i].append(1)
        else:
            value=arr[i - 1][j - 1] + arr[i - 1][j + 1]
            arr[i].append(value)
print('Pascals triangle :')
for i in arr:
    for j in i:
        print(j ,end = '    ')
    print()
